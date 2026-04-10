#!/usr/bin/env python3
"""
边界检查钩子：Claude Code pre_tool_use 拦截器

调用约定：
    python boundary_check.py --context '<tool_json>'

返回（stdout）：
    1  → 允许工具调用
    0  → 沉默拒绝（不阻断，但返回 0 信号）
    -1 → 拒绝并记录（高危操作）

退出码始终为 0（仅用 stdout 传递决策）
"""

import sys
import json
import logging
from pathlib import Path
from typing import Any

# 添加项目根目录到路径以便导入 lingshu 模块
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.boundary import should_speak, P, Z, N
from core.trit_ops import int_from_trit

logger = logging.getLogger("boundary_check")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)]
)

# 危险工具与操作的静态风险评级（L0/L1 快速校验）
RISK_LEVELS = {
    "shell": 2,           # 高危：直接执行命令
    "bash": 2,
    "exec": 2,
    "write": 1,           # 中危：文件写入
    "edit": 1,
    "delete": 1,
    "read": 0,            # 低危：只读
    "glob": 0,
    "grep": 0,
    "read_file": 0,
}

# 危险路径模式（正则或子串）
DANGEROUS_PATHS = [
    "/etc/",
    "/root/",
    "~/.ssh/",
    "~/.claude/",
    "sudo",
    "rm -rf",
    "chmod 777",
    "> /dev/",
]

def assess_risk(tool_input: dict[str, Any]) -> tuple[int, str]:
    """
    快速风险评估（L0/L1 层）

    返回：(risk_level, reason)
        risk_level: 2=高, 1=中, 0=低
    """
    tool_name = tool_input.get("tool_name", "")
    arguments = tool_input.get("arguments", {})

    # 1. 按工具类型定级
    base_risk = RISK_LEVELS.get(tool_name, 1)  # 未知工具默认中危

    # 2. 检查危险路径/参数
    danger_reason = []
    for key, val in arguments.items():
        if isinstance(val, str):
            for pattern in DANGEROUS_PATHS:
                if pattern in val:
                    base_risk = max(base_risk, 2)
                    danger_reason.append(f"参数 {key} 包含危险模式 '{pattern}'")

    reason = "基线工具风险" if not danger_reason else "; ".join(danger_reason)
    return base_risk, reason


def decide(tool_input: dict[str, Any]) -> int:
    """
    核心决策逻辑

    返回：1（允许）/ 0（沉默拒绝）/ -1（拒绝并记录）
    """
    tool_name = tool_input.get("tool_name", "unknown")
    arguments = tool_input.get("arguments", {})

    risk_level, risk_reason = assess_risk(tool_input)
    logger.info(f"工具: {tool_name}, 风险等级: {risk_level}, 原因: {risk_reason}")

    # L0 快速拒绝（高危且无主权豁免）
    if risk_level == 2:
        # 检查是否有显式用户授权标记（L2 主权豁免）
        if arguments.get("_force", False) is not True:
            logger.warning(f"高危工具 '{tool_name}' 被阻断: {risk_reason}")
            return -1  # 拒绝并记录
        else:
            logger.info(f"高危工具 '{tool_name}' 被 L2 主权豁免允许")
            return 1

    # L1 边界规则（三元逻辑）
    # 将风险评估映射为三元态：
    #   低风险(0) → 中心状态 = P（正向）
    #   中风险(1) → 中心状态 = Z（待定）
    #   高风险(2) → 中心状态 = N（负向）
    center_map = {0: P, 1: Z, 2: N}
    center_state = center_map.get(risk_level, Z)

    # 邻居状态：根据参数复杂度推导
    # 简单实现：将每个关键参数视为一个"邻居"的潜在影响
    # 默认邻居为 P（环境默认允许），除非检测到危险
    neighbor_count = len(arguments)
    neighbor_states = []
    for key, val in arguments.items():
        if isinstance(val, str):
            # 检查该参数是否触发危险模式
            param_risk = 0
            for pattern in DANGEROUS_PATHS:
                if pattern in val:
                    param_risk = 2
                    break
            neighbor_states.append(N if param_risk == 2 else P)
        else:
            neighbor_states.append(P)  # 非字符串参数默认友好

    # 应用边界规则
    decision = should_speak(center_state, neighbor_states)
    decision_int = int_from_trit(decision)

    if decision == P:
        return 1
    elif decision == Z:
        logger.info(f"工具 '{tool_name}' 被边界规则静默拒绝（主权保留）")
        return 0
    else:  # N
        logger.warning(f"工具 '{tool_name}' 被边界规则拒绝（冲突检测）")
        return -1


def main():
    # 从 stdin 或文件读取上下文（Claude Code hook 通过 stdin 传递 JSON）
    if len(sys.argv) > 1:
        # 调试：从命令行参数读取
        context_str = sys.argv[1]
    else:
        # 正常：从 stdin 读取完整 JSON
        context_str = sys.stdin.read()

    try:
        tool_input = json.loads(context_str)
    except json.JSONDecodeError as e:
        print(f"JSON 解析失败: {e}", file=sys.stderr)
        sys.exit(1)

    result = decide(tool_input)
    print(result)
    sys.exit(0)  # 始终成功退出，决策通过 stdout 传递


if __name__ == "__main__":
    main()
