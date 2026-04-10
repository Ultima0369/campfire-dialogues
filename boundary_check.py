#!/usr/bin/env python3
"""
LingShu Boundary Check Hook for Claude Code
Pre-tool-use hook that applies the LingShu P0 boundary rule
to decide whether a tool call is allowed.

Decision codes:
  +1 : allow tool call
   0 : silently block (no tool call, no message)
  -1 : deny with reason (logged)

Audit log: ~/.hermes/logs/boundary_audit.log (JSON lines)
State file: ~/.hermes/state/boundary_state.json
"""

import sys
import os
import json
import datetime
from pathlib import Path

# ----------------------------------------------------------------------
# Path setup: locate project root and lingshu package
# ----------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
# If script is in project root, lingshu_dir = SCRIPT_DIR / 'lingshu'
# If script is inside lingshu/, lingshu_dir = SCRIPT_DIR
if (SCRIPT_DIR / 'lingshu' / 'core' / 'boundary.py').exists():
    PROJECT_ROOT = SCRIPT_DIR
    LINGSHU_DIR = SCRIPT_DIR / 'lingshu'
elif (SCRIPT_DIR / 'core' / 'boundary.py').exists():
    # Script is inside lingshu/
    LINGSHU_DIR = SCRIPT_DIR
    PROJECT_ROOT = SCRIPT_DIR.parent
else:
    # Fallback: assume standard layout
    PROJECT_ROOT = SCRIPT_DIR
    LINGSHU_DIR = SCRIPT_DIR / 'lingshu'

# Add project root to sys.path so we can import lingshu modules
sys.path.insert(0, str(PROJECT_ROOT))

# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------
AUDIT_LOG_PATH = Path.home() / '.hermes' / 'logs' / 'boundary_audit.log'
STATE_PATH = Path.home() / '.hermes' / 'state' / 'boundary_state.json'
CONFIG_PATH = LINGSHU_DIR / 'config.yaml'

# Ensure log and state directories exist
AUDIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------
# Default configuration (used if config.yaml missing or incomplete)
# ----------------------------------------------------------------------
DEFAULT_BENEFIT_MAP = {
    # Tools that directly benefit the user (aligned)
    'search': 1, 'read': 1, 'query': 1, 'get': 1,
    'list': 1, 'status': 1, 'info': 1, 'fetch': 1,
    # Neutral tools
    'edit': 0, 'update': 0, 'patch': 0,
    # Potentially harmful tools (need caution)
    'write': -1, 'delete': -1, 'remove': -1,
    'exec': -1, 'shell': -1, 'run': -1,
    'format': -1, 'rm': -1, 'kill': -1,
}
DEFAULT_RISK_MAP = {
    # Low risk (read-only, safe)
    'search': 1, 'read': 1, 'query': 1, 'list': 1,
    'status': 1, 'info': 1, 'fetch': 1, 'get': 1,
    # Medium risk (modifications)
    'edit': 0, 'update': 0, 'patch': 0, 'write': 0,
    # High risk (destructive, code execution)
    'delete': -1, 'remove': -1, 'exec': -1,
    'shell': -1, 'run': -1, 'format': -1,
    'rm': -1, 'kill': -1,
}

# ----------------------------------------------------------------------
# Simple YAML parser (fallback if PyYAML not available)
# ----------------------------------------------------------------------
def simple_yaml_load(filepath):
    """Parse a simple YAML file with basic key-value and nested dicts."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    root = {}
    stack = [(0, root)]  # (indent_level, current_dict)
    for line_num, line in enumerate(lines, 1):
        line = line.rstrip('\n')
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Determine indentation (count leading spaces; assume spaces, not tabs)
        indent = len(line) - len(line.lstrip())
        # Find parent dict by popping stack to level < current indent
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise ValueError(f"Invalid indentation at line {line_num}")
        parent_indent, parent_dict = stack[-1]
        # Must contain a colon
        if ':' not in line:
            raise ValueError(f"Invalid syntax at line {line_num}: {line}")
        key_part, value_part = line.split(':', 1)
        key = key_part.strip()
        value_str = value_part.strip()
        if value_str == '':
            # Start a new nested dict
            new_dict = {}
            parent_dict[key] = new_dict
            stack.append((indent, new_dict))
        else:
            # Parse scalar value
            parent_dict[key] = parse_yaml_scalar(value_str)
    return root

def parse_yaml_scalar(s):
    """Parse a YAML scalar value to Python type."""
    # Booleans
    if s.lower() == 'true':
        return True
    if s.lower() == 'false':
        return False
    # Null
    if s.lower() in ('null', '~'):
        return None
    # Numbers
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    # Strip quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s

# ----------------------------------------------------------------------
# Load configuration
# ----------------------------------------------------------------------
def load_config():
    """Load boundary configuration from CONFIG_PATH, merging with defaults."""
    config_data = {}
    if CONFIG_PATH.exists():
        try:
            import yaml
            with open(CONFIG_PATH, 'r') as f:
                config_data = yaml.safe_load(f) or {}
        except ImportError:
            # Fallback to simple parser
            try:
                config_data = simple_yaml_load(CONFIG_PATH)
            except Exception as e:
                print(f"Warning: Failed to parse config with simple parser: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Warning: Failed to load config.yaml: {e}", file=sys.stderr)
    # Extract p0.rule_params
    p0_config = config_data.get('p0', {})
    rule_params = p0_config.get('rule_params', {})
    # Get maps from config or use empty to merge with defaults
    benefit_map = rule_params.get('tool_benefit_map', {})
    risk_map = rule_params.get('system_risk_map', {})
    # Merge: config overrides defaults
    merged_benefit = DEFAULT_BENEFIT_MAP.copy()
    merged_benefit.update({str(k): int(v) for k, v in benefit_map.items()})
    merged_risk = DEFAULT_RISK_MAP.copy()
    merged_risk.update({str(k): int(v) for k, v in risk_map.items()})
    return {
        'p0': {
            'rule_params': {
                'tool_benefit_map': merged_benefit,
                'system_risk_map': merged_risk
            }
        }
    }

# Load config at module import time (so we can use it in should_speak)
CONFIG = load_config()

# ----------------------------------------------------------------------
# Import LingShu core modules (after path setup)
# ----------------------------------------------------------------------
try:
    from lingshu.core.boundary import p0_boundary_rule
    from lingshu.core.trit_ops import int_from_trit, trit_from_int
except ImportError as e:
    print(f"Error: Failed to import LingShu core modules: {e}", file=sys.stderr)
    print("Ensure boundary.py and trit_ops.py exist in lingshu/core/ and that the project root is in PYTHONPATH.", file=sys.stderr)
    sys.exit(1)

# Trit constants from tritlib (also available via import)
from tritlib import P, Z, N

# ----------------------------------------------------------------------
# State management
# ----------------------------------------------------------------------
def load_state():
    """Load the current center trit from state file. Default: Z (neutral)."""
    if STATE_PATH.exists():
        try:
            with open(STATE_PATH, 'r') as f:
                data = json.load(f)
            center_val = data.get('center', 0)
            if center_val not in (-1, 0, 1):
                center_val = 0
            return trit_from_int(center_val)
        except Exception as e:
            print(f"Warning: Failed to load state: {e}, using default Z", file=sys.stderr)
    return Z

def save_state(center):
    """Persist the current center trit."""
    try:
        with open(STATE_PATH, 'w') as f:
            json.dump({'center': int_from_trit(center)}, f)
    except Exception as e:
        print(f"Warning: Failed to save state: {e}", file=sys.stderr)

# ----------------------------------------------------------------------
# Audit logging
# ----------------------------------------------------------------------
def log_decision(tool_name, center_before, left, right, center_after, reason=None):
    """Append a JSON log entry to the audit log."""
    entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'tool': tool_name,
        'center_before': int_from_trit(center_before),
        'left': int_from_trit(left),
        'right': int_from_trit(right),
        'center_after': int_from_trit(center_after),
        'reason': reason
    }
    try:
        with open(AUDIT_LOG_PATH, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    except Exception as e:
        print(f"Warning: Failed to write audit log: {e}", file=sys.stderr)

# ----------------------------------------------------------------------
# Helper: map tool name to trit using config maps
# ----------------------------------------------------------------------
def get_trit_for_tool(tool_name, mapping):
    """Lookup the trit integer for a tool; default to 0 (Z)."""
    # Accept tool_name as string; mapping keys are strings
    val = mapping.get(tool_name, 0)
    # Ensure it's -1, 0, or 1
    if val not in (-1, 0, 1):
        return Z
    return trit_from_int(val)

# ----------------------------------------------------------------------
# Main hook interface
# ----------------------------------------------------------------------
def should_speak(tool_call):
    """
    Pre-tool-use hook for Claude Code.
    
    Args:
        tool_call: dict with at least 'name' (tool name) and optionally 'arguments' / 'input'.
    
    Returns:
        int: +1 to allow, 0 to silently block, -1 to deny (reason logged).
    """
    # Extract tool name flexibly
    tool_name = tool_call.get('name') or tool_call.get('tool_name') or tool_call.get('tool') or 'unknown'
    # Arguments not used in current mapping but could extend
    # tool_args = tool_call.get('arguments') or tool_call.get('input') or tool_call.get('parameters') or {}
    
    # Get rule parameters from loaded config
    rule_params = CONFIG.get('p0', {}).get('rule_params', {})
    benefit_map = rule_params.get('tool_benefit_map', {})
    risk_map = rule_params.get('system_risk_map', {})
    
    # Derive left (user benefit) and right (system risk) trits
    left = get_trit_for_tool(tool_name, benefit_map)
    right = get_trit_for_tool(tool_name, risk_map)
    
    # Load current center state (AI alignment)
    center = load_state()
    
    # Apply boundary rule
    new_center = p0_boundary_rule(center, left, right)
    decision = int_from_trit(new_center)
    
    # Prepare reason for logging
    if decision == -1:
        reason = (f"Boundary rule denied: tool '{tool_name}' produces misalignment "
                  f"(center={int_from_trit(center)} + left={int_from_trit(left)} + right={int_from_trit(right)} => {decision})")
    elif decision == 0:
        reason = (f"Boundary rule suspended: tool '{tool_name}' results in neutral state "
                  f"(center={int_from_trit(center)} + left={int_from_trit(left)} + right={int_from_trit(right)} => {decision})")
    else:
        reason = (f"Boundary rule approved: tool '{tool_name}' aligns with principles "
                  f"(center={int_from_trit(center)} + left={int_from_trit(left)} + right={int_from_trit(right)} => {decision})")
    
    # Log the decision
    log_decision(tool_name, center, left, right, new_center, reason)
    
    # Persist new center state
    save_state(new_center)
    
    return decision

# ----------------------------------------------------------------------
# Self-test (run directly)
# ----------------------------------------------------------------------
if __name__ == '__main__':
    print("=" * 60)
    print("LingShu Boundary Check Hook - Self Test")
    print("=" * 60)
    test_cases = [
        {'name': 'search', 'arguments': {'query': 'test'}},
        {'name': 'read', 'arguments': {'file': '/etc/passwd'}},
        {'name': 'write', 'arguments': {'file': '/tmp/out.txt', 'content': 'bad'}},
        {'name': 'exec', 'arguments': {'cmd': 'rm -rf /'}},
        {'name': 'list', 'arguments': {'path': '.'}},
    ]
    for tc in test_cases:
        result = should_speak(tc)
        status = {1: 'ALLOW', 0: 'SILENT BLOCK', -1: 'DENY'}[result]
        print(f"Tool: {tc['name']:10s} => {status} ({result})")
    print("\nCurrent state saved to:", STATE_PATH)
    print("Audit log appended to:", AUDIT_LOG_PATH)
