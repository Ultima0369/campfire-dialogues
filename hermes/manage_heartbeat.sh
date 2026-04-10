#!/bin/bash
# Hermes 心跳守护进程控制脚本

set -e

SERVICE_NAME="hermes-heartbeat"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$HOME/.hermes/heartbeat.log"

show_status() {
    echo "=== Hermes Heartbeat 状态 ==="
    echo "服务单元: $SERVICE_NAME"
    echo "脚本位置: $SCRIPT_DIR/heartbeat.py"
    echo "日志文件: $LOG_FILE"
    echo ""

    if systemctl --user is-active --quiet "$SERVICE_NAME"; then
        echo "状态: ✅ 运行中"
        echo "主进程: $(systemctl --user show -p MainPID "$SERVICE_NAME" | cut -d= -f2)"
        echo "启动时间: $(systemctl --user show -p ActiveEnterTimestamp "$SERVICE_NAME" | cut -d= -f2)"
        echo ""
        echo "最新心跳 (tail -5):"
        tail -5 "$LOG_FILE" 2>/dev/null | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        data = json.loads(line.strip())
        ts = data['timestamp']
        services = data.get('status', data).get('services', {})
        alerts = data.get('status', data).get('alerts', [])
        print(f\"  {ts} | services: {len(services)} | alerts: {len(alerts)}\")
    except: pass
" 2>/dev/null || echo "  (无日志或解析失败)"
    else
        echo "状态: ❌ 未运行"
        if systemctl --user is-enabled --quiet "$SERVICE_NAME" 2>/dev/null; then
            echo "启用状态: ✅ 已启用（开机自启）"
        else
            echo "启用状态: ❌ 未启用"
        fi
    fi
}

start_service() {
    echo "启动 Hermes Heartbeat..."
    systemctl --user daemon-reload
    systemctl --user start "$SERVICE_NAME"
    sleep 1
    if systemctl --user is-active --quiet "$SERVICE_NAME"; then
        echo "✅ 服务已启动"
    else
        echo "❌ 启动失败，查看日志: journalctl --user -u $SERVICE_NAME -n 20"
    fi
}

stop_service() {
    echo "停止 Hermes Heartbeat..."
    systemctl --user stop "$SERVICE_NAME"
    echo "✅ 服务已停止"
}

restart_service() {
    echo "重启 Hermes Heartbeat..."
    systemctl --user restart "$SERVICE_NAME"
    sleep 1
    if systemctl --user is-active --quiet "$SERVICE_NAME"; then
        echo "✅ 服务已重启"
    else
        echo "❌ 重启失败"
    fi
}

enable_autostart() {
    echo "启用开机自启..."
    systemctl --user enable "$SERVICE_NAME"
    echo "✅ 已启用"
}

disable_autostart() {
    echo "禁用开机自启..."
    systemctl --user disable "$SERVICE_NAME"
    echo "✅ 已禁用"
}

tail_log() {
    echo "=== 实时心跳日志 (Ctrl+C 退出) ==="
    journalctl --user -u "$SERVICE_NAME" -f 2>/dev/null || \
    tail -f "$LOG_FILE"
}

case "${1:-status}" in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        restart_service
        ;;
    enable)
        enable_autostart
        ;;
    disable)
        disable_autostart
        ;;
    status)
        show_status
        ;;
    log|logs)
        tail_log
        ;;
    *)
        echo "用法: $0 {start|stop|restart|enable|disable|status|log}"
        echo ""
        echo "命令:"
        echo "  start     启动心跳守护进程"
        echo "  stop      停止心跳守护进程"
        echo "  restart   重启服务"
        echo "  enable    启用开机自启"
        echo "  disable   禁用开机自启"
        echo "  status    查看运行状态"
        echo "  log       实时查看日志"
        exit 1
        ;;
esac
