#!/bin/bash
# 在 LingShu 目录下运行此脚本来设置环境变量

export NO_PROXY="localhost,127.0.0.1,localaddress,.local,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,api.stepfun.com"
export no_proxy="$NO_PROXY"

echo "✅ 环境变量已设置"
echo "NO_PROXY=$NO_PROXY"
