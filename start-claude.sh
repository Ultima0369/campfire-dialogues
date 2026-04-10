#!/bin/bash
# Claude Code 启动脚本 - 统一代理配置

echo "=== 启动 Claude Code（统一代理配置）==="

# 代理设置 - 使用 Clash Verge（混合端口 25841，支持 HTTP 和 SOCKS5）
export HTTP_PROXY=http://127.0.0.1:25841
export HTTPS_PROXY=http://127.0.0.1:25841
# SOCKS5 备用：export ALL_PROXY=socks5://127.0.0.1:7898
# 直连白名单（不走代理的地址）
export NO_PROXY=localhost,127.0.0.1,localaddress,.local,\
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,\
api.stepfun.com,.stepfun.com,stepfun.com
export no_proxy="$NO_PROXY"

echo "环境变量已设置："
echo "  HTTP_PROXY=$HTTP_PROXY"
echo "  HTTPS_PROXY=$HTTPS_PROXY"
echo "  NO_PROXY=$NO_PROXY"
echo ""
echo "启动 Claude Code..."

cd /home/ultima/LingShu
claude --dangerously-skip-permissions
