#!/bin/bash
# Hermes Agent 启动脚本 - 集成到 LingShu 项目
# 使用方法: ./start_hermes.sh [交互模式|自动模式]

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}╔════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║       Hermes Agent · 灵枢 LingShu 集成启动         ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════╝${NC}"
echo ""

# 检查环境
if [ ! -f "/home/ultima/LingShu/hermes/.env" ]; then
    echo -e "${RED}✗ 未找到 Hermes 环境配置文件${NC}"
    echo "请先运行: cp /home/ultima/LingShu/hermes/.env.example /home/ultima/LingShu/hermes/.env"
    echo "并编辑填入必要的 API 密钥"
    exit 1
fi

# 加载环境变量
if [ -f "/home/ultima/LingShu/hermes/setup_env.sh" ]; then
    source /home/ultima/LingShu/hermes/setup_env.sh
fi

# 检查 hermes 命令
if ! command -v hermes &> /dev/null; then
    echo -e "${RED}✗ Hermes 未安装或不在 PATH 中${NC}"
    echo "请运行: pip install -e /home/ultima/LingShu/hermes"
    exit 1
fi

echo -e "${GREEN}✓ Hermes Agent 已就绪${NC}"
echo ""
echo "项目上下文:"
echo "  - 项目: 灵枢 LingShu (认知演化原型机)"
echo "  - 阶段: P0 一维三进制元胞自动机"
echo "  - 核心规则: 自利利他长期收敛"
echo ""
echo "模型配置:"
echo "  - 提供商: StepFun (step-3.5-flash-2603)"
echo "  - 上下文: 4096 tokens"
echo "  - 温度: 0.7"
echo ""
echo -e "${YELLOW}正在启动 Hermes Agent...${NC}"
echo ""

# 启动模式
MODE="${1:-interactive}"

case "$MODE" in
    auto|--auto|-a)
        echo "模式: 自动模式 (非交互)"
        HERMES_YOLO_MODE=1 hermes
        ;;
    *)
        echo "模式: 交互模式"
        hermes "$@"
        ;;
esac
