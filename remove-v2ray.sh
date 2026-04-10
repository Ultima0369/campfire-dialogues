#!/bin/bash
# v2ray 完全卸载脚本
# 执行此脚本需要 sudo 密码: 789260
# 用法: bash ~/LingShu/remove-v2ray.sh

set -e

echo "========================================="
echo "   v2ray 卸载脚本"
echo "========================================="
echo ""

# 1. 停止 v2ray 服务
echo "[1/5] 停止 v2ray 服务..."
sudo systemctl stop v2ray 2>/dev/null || echo "  (服务可能未运行)"

# 2. 禁用 v2ray 开机启动
echo "[2/5] 禁用 v2ray 开机启动..."
sudo systemctl disable v2ray 2>/dev/null || echo "  (服务可能未启用)"

# 3. 删除 systemd 服务文件
echo "[3/5] 删除 systemd 服务文件..."
sudo rm -f /etc/systemd/system/v2ray.service
sudo rm -f /usr/lib/systemd/system/v2ray.service
sudo systemctl daemon-reload 2>/dev/null || true

# 4. 删除 v2ray 文件
echo "[4/5] 删除 v2ray 文件..."
sudo rm -rf /etc/v2ray 2>/dev/null || echo "  (目录可能不存在)"
sudo rm -f /usr/bin/v2ray 2>/dev/null || echo "  (文件可能不存在)"
sudo rm -f /usr/local/bin/v2ray 2>/dev/null || echo "  (文件可能不存在)"
sudo rm -rf /var/lib/v2ray 2>/dev/null || echo "  (目录可能不存在)"

# 5. 验证删除结果
echo "[5/5] 验证删除结果..."
echo ""
echo "--- 验证结果 ---"
if systemctl list-unit-files 2>/dev/null | grep -q v2ray; then
    echo "  ✗ v2ray systemd 单元仍然存在"
else
    echo "  ✓ v2ray systemd 单元已清理"
fi

if ps aux | grep -v grep | grep -q v2ray; then
    echo "  ✗ v2ray 进程仍在运行"
else
    echo "  ✓ v2ray 进程已停止"
fi

if [ -d /etc/v2ray ]; then
    echo "  ✗ /etc/v2ray 目录仍然存在"
else
    echo "  ✓ /etc/v2ray 目录已删除"
fi

if command -v v2ray &>/dev/null; then
    echo "  ✗ v2ray 命令仍然可用"
else
    echo "  ✓ v2ray 命令已移除"
fi

echo ""
echo "========================================="
echo "   卸载完成"
echo "========================================="
echo ""
echo "当前系统代理状态:"
echo "  - Clash Verge: $(ps aux | grep -v grep | grep -c 'clash-verge\|verge-mihomo') 个进程"
echo "  - 开机启动: systemd用户服务($(systemctl --user is-enabled clash-verge.service 2>/dev/null || echo unknown)), 桌面自启($([ -f ~/.config/autostart/clash-verge.desktop ] && echo yes || echo no))"
echo ""
