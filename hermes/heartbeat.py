#!/usr/bin/env python3
"""
Hermes 本地心跳机制
监控 LingShu 项目关键服务健康状态，完全本地运行
"""

import os
import sys
import json
import time
import socket
import subprocess
import signal
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
import threading
import atexit

# ========== 配置 ==========
CONFIG = {
    "heartbeat_interval": 5,          # 心跳间隔（秒）
    "full_check_interval": 30,        # 深度检查间隔（秒）
    "snapshot_interval": 300,         # 完整快照间隔（秒，5分钟）
    "log_retention_days": 7,          # 日志保留天数
    "alert_disk_threshold": 80,       # 磁盘使用告警阈值（%）
    "services": {
    "p0_automaton": {
        "name": "P0 自动机",
        "command": ["python3", "/home/ultima/LingShu/lingshu/experiments/p0_first_breath.py", "--test"],
        "timeout": 15,
        "priority": "P0",
        "auto_recover": False
    },
        "hermes_service": {
            "name": "Hermes Agent",
            "systemd_unit": "hermes",
            "priority": "P0",
            "auto_recover": True
        },
        "bitnet_service": {
            "name": "BitNet 服务",
            "http_url": "http://localhost:8080/v1/models",
            "http_timeout": 3,
            "priority": "P1",
            "auto_recover": True,
            "start_script": "/home/ultima/LingShu/start_bitnet.sh"
        },
        "postgresql": {
            "name": "PostgreSQL",
            "pg_isready": True,
            "host": "localhost",
            "port": 5432,
            "priority": "P1",
            "auto_recover": True
        }
    }
}

# ========== 路径 ==========
HERMES_DIR = Path.home() / ".hermes"
HEARTBEAT_LOG = HERMES_DIR / "heartbeat.log"
SNAPSHOT_FILE = HERMES_DIR / "status_latest.json"
HISTORY_DIR = HERMES_DIR / "history"
ALERT_LOG = HERMES_DIR / "alerts.log"

HERMES_DIR.mkdir(parents=True, exist_ok=True)
HISTORY_DIR.mkdir(parents=True, exist_ok=True)

# ========== 全局状态 ==========
running = True
loop_counter = 0
last_full_check = 0
alert_count = 0

# ========== 工具函数 ==========
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def log_heartbeat(status: Dict[str, Any]):
    """记录心跳日志（JSONL）"""
    log_entry = {
        "timestamp": now_iso(),
        "status": status
    }
    with open(HEARTBEAT_LOG, "a") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def log_alert(level: str, service: str, msg: str):
    """记录告警"""
    global alert_count
    alert_count += 1
    entry = f"[{now_iso()}] [{level}] {service}: {msg}"
    with open(ALERT_LOG, "a") as f:
        f.write(entry + "\n")
    print(f"🚨 {entry}", file=sys.stderr)

def check_disk(path: str = "/") -> Tuple[bool, float]:
    """检查磁盘空间，返回 (充足, 使用率%)"""
    stat = shutil.disk_usage(path)
    percent_used = (stat.used / stat.total) * 100
    return (percent_used < CONFIG["alert_disk_threshold"], percent_used)

def check_systemd_service(unit: str) -> Tuple[str, str]:
    """检查 systemd 用户服务状态
    返回: (状态, 简要信息)
    """
    try:
        result = subprocess.run(
            ["systemctl", "--user", "is-active", unit],
            capture_output=True, text=True, timeout=5
        )
        status = result.stdout.strip() or result.returncode == 0 and "active" or "inactive"
        if result.returncode == 0:
            return ("✅", status)
        else:
            return ("❌", status or "failed")
    except Exception as e:
        return ("❌", f"error: {e}")

def run_p0_smoke_test() -> Tuple[str, str]:
    """P0 自动机冒烟测试"""
    try:
        result = subprocess.run(
            CONFIG["services"]["p0_automaton"]["command"],
            capture_output=True, text=True, timeout=CONFIG["services"]["p0_automaton"]["timeout"]
        )
        if result.returncode == 0:
            return ("✅", "running")
        else:
            return ("❌", f"exit={result.returncode}")
    except subprocess.TimeoutExpired:
        return ("❌", "timeout")
    except Exception as e:
        return ("❌", str(e))

def check_bitnet_http() -> Tuple[str, str]:
    """检查 BitNet HTTP 服务"""
    import json as _json
    import urllib.request
    url = CONFIG["services"]["bitnet_service"]["http_url"]
    timeout = CONFIG["services"]["bitnet_service"]["http_timeout"]
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Hermes-Heartbeat"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                data = _json.loads(resp.read().decode())
                models = [m.get('id', 'unknown') for m in data.get('data', [])]
                return ("✅", f"HTTP 200, models: {models}")
            else:
                return ("⚠️", f"HTTP {resp.status}")
    except Exception as e:
        return ("❌", str(e)[:50])

def check_postgres() -> Tuple[str, str]:
    """检查 PostgreSQL 服务"""
    try:
        result = subprocess.run(
            ["pg_isready", "-h", "localhost", "-p", "5432"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return ("✅", "accepting connections")
        else:
            return ("❌", "not ready")
    except FileNotFoundError:
        return ("⚠️", "pg_isready not found")
    except Exception as e:
        return ("❌", str(e))

def attempt_recovery(service_id: str):
    """尝试自动恢复服务"""
    svc = CONFIG["services"][service_id]
    if not svc.get("auto_recover"):
        log_alert("WARN", service_id, "异常但禁用自动恢复")
        return False

    log_alert("INFO", service_id, "尝试自动恢复...")

    if service_id == "hermes_service":
        try:
            subprocess.run(["systemctl", "--user", "restart", svc["systemd_unit"]],
                          capture_output=True, timeout=10)
            time.sleep(3)  # 等待重启
            new_status, _ = check_systemd_service(svc["systemd_unit"])
            if new_status == "✅":
                log_alert("INFO", service_id, "恢复成功 ✅")
                return True
        except Exception as e:
            log_alert("ERROR", service_id, f"恢复失败: {e}")

    elif service_id == "bitnet_service":
        script = svc.get("start_script")
        if script and Path(script).exists():
            try:
                subprocess.run(["pkill", "-f", "llama-server"], capture_output=True)
                time.sleep(2)
                subprocess.Popen([script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(5)
                new_status, _ = check_bitnet_http()
                if new_status == "✅":
                    log_alert("INFO", service_id, "恢复成功 ✅")
                    return True
            except Exception as e:
                log_alert("ERROR", service_id, f"恢复失败: {e}")

    elif service_id == "postgresql":
        try:
            subprocess.run(["sudo", "-n", "systemctl", "start", "postgresql"],
                          capture_output=True, timeout=10)
            time.sleep(3)
            new_status, _ = check_postgres()
            if new_status == "✅":
                log_alert("INFO", service_id, "恢复成功 ✅")
                return True
        except Exception as e:
            log_alert("ERROR", service_id, f"恢复失败: {e}")

    return False

# ========== 心跳核心 ==========
def heartbeat_once(force_full: bool = False) -> Dict[str, Any]:
    """执行一次心跳检查"""
    global loop_counter, last_full_check

    status = {
        "timestamp": now_iso(),
        "uptime_sec": int(time.time() - start_time),
        "loop": loop_counter,
        "services": {},
        "system": {},
        "alerts": []
    }

    # 1. 自检
    status["services"]["heartbeat"] = {"icon": "💓", "state": "alive"}

    # 2. 磁盘检查（每次）
    disk_ok, disk_pct = check_disk("/")
    status["system"]["disk_root_pct"] = round(disk_pct, 1)
    status["system"]["disk_ok"] = disk_ok
    if not disk_ok:
        status["alerts"].append(f"磁盘使用率 {disk_pct:.1f}% >= {CONFIG['alert_disk_threshold']}%")

    # 3. 深度检查（定时）
    now = time.time()
    do_full = force_full or (now - last_full_check >= CONFIG["full_check_interval"])

    if do_full:
        last_full_check = now

        # P0 自动机
        p0_icon, p0_msg = run_p0_smoke_test()
        status["services"]["p0_automaton"] = {"icon": p0_icon, "state": p0_msg}
        if p0_icon == "❌":
            status["alerts"].append("P0 自动机异常")
            attempt_recovery("p0_automaton")

        # Hermes 服务
        h_icon, h_msg = check_systemd_service("hermes")
        status["services"]["hermes_service"] = {"icon": h_icon, "state": h_msg}
        if h_icon == "❌":
            status["alerts"].append("Hermes 服务异常")
            attempt_recovery("hermes_service")

    # 4. 完整巡检（定时）
    if do_full and (loop_counter % (CONFIG["snapshot_interval"] // CONFIG["heartbeat_interval"]) == 0):
        # BitNet
        b_icon, b_msg = check_bitnet_http()
        status["services"]["bitnet_service"] = {"icon": b_icon, "state": b_msg}
        if b_icon == "❌":
            status["alerts"].append("BitNet 服务异常")
            attempt_recovery("bitnet_service")

        # PostgreSQL
        p_icon, p_msg = check_postgres()
        status["services"]["postgresql"] = {"icon": p_icon, "state": p_msg}
        if p_icon == "❌":
            status["alerts"].append("PostgreSQL 异常")
            attempt_recovery("postgresql")

        # 写快照
        with open(SNAPSHOT_FILE, "w") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)

        # 写历史（按日期）
        history_file = HISTORY_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        with open(history_file, "a") as f:
            f.write(json.dumps(status, ensure_ascii=False) + "\n")

    # 5. 告警汇总
    if status["alerts"]:
        for alert in status["alerts"]:
            log_alert("ALERT", "Heartbeat", alert)

    return status

def render_console(status: Dict[str, Any]):
    """在终端渲染实时状态面板"""
    os.system("clear" if os.name == "posix" else "cls")
    print(f"\033[1;36m[Hermes Heartbeat] {status['timestamp']}\033[0m")
    print("┌" + "─" * 60 + "┐")

    services = status["services"]
    for key in ["p0_automaton", "hermes_service", "bitnet_service", "postgresql"]:
        if key in services:
            svc = services[key]
            name = CONFIG["services"][key]["name"].ljust(15)
            icon = svc["icon"].ljust(3)
            state = svc["state"].ljust(30)
            print(f"│ {name} │ {icon} {state} │")

    # 系统信息
    disk_pct = status["system"].get("disk_root_pct", 0)
    disk_color = "\033[1;32m" if disk_pct < 80 else "\033[1;33m" if disk_pct < 90 else "\033[1;31m"
    disk_str = f"{disk_color}{disk_pct:.1f}%\033[0m".ljust(12)
    print("│ " + "磁盘 /".ljust(15) + " │ " + disk_str + " │")

    print("└" + "─" * 60 + "┘")
    print(f"Next full check: {max(0, CONFIG['full_check_interval'] - (time.time() - last_full_check)):.0f}s  |  Alerts: {alert_count}  |  Uptime: {status['uptime_sec']}s")
    sys.stdout.flush()

# ========== 主循环 ==========
start_time = time.time()
shutdown_event = threading.Event()

def signal_handler(signum, frame):
    global running
    print("\n\033[1;33m[Heartbeat] 收到停止信号，正在优雅退出...\033[0m")
    running = False
    shutdown_event.set()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def main():
    global loop_counter

    print("\033[1;32m[Heartbeat] Hermes 本地心跳机制启动\033[0m")
    print(f"  日志: {HEARTBEAT_LOG}")
    print(f"  快照: {SNAPSHOT_FILE}")
    print(f"  历史: {HISTORY_DIR}/")
    print("  按 Ctrl+C 停止\n")
    time.sleep(2)

    while running:
        loop_counter += 1

        try:
            status = heartbeat_once()
            log_heartbeat(status)

            # 每轮都渲染（快速检查）
            if loop_counter % (CONFIG["full_check_interval"] // CONFIG["heartbeat_interval"]) == 0:
                render_console(status)

        except Exception as e:
            log_alert("ERROR", "Heartbeat", f"主循环异常: {e}")

        # 等待
        shutdown_event.wait(CONFIG["heartbeat_interval"])

    print("\033[1;32m[Heartbeat] 已停止，最终状态已保存\033[0m")

if __name__ == "__main__":
    main()
