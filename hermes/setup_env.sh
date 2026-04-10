#!/bin/bash
# Hermes Agent 全局环境变量配置
# 用于 LingShu 项目整合
# 使用方法: source /home/ultima/LingShu/hermes/setup_env.sh

echo "=== Hermes Agent 环境配置 ==="
echo "项目: 灵枢 LingShu"
echo ""

# Hermes 核心路径
export HERMES_HOME="$HOME/.hermes"
export HERMES_PROJECT_DIR="/home/ultima/LingShu"
export HERMES_DEFAULT_MODEL="step-3.5-flash-2603"
export HERMES_MAX_TOKENS="4096"
export HERMES_TEMPERATURE="0.7"
export HERMES_UI_THEME="dark"
export HERMES_INTERACTIVE="1"
export HERMES_YOLO_MODE="1"

# API 配置 (StepFun 端点 - Hermes 使用 OpenAI SDK，需要 /v1 后缀)
export OPENAI_API_KEY="5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE"
export ANTHROPIC_API_KEY="5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE"
export OPENAI_BASE_URL="https://api.stepfun.com/step_plan/v1"
export HERMES_BASE_URL="https://api.stepfun.com/step_plan/v1"

# LingShu 项目上下文
export LINGSHU_PROJECT_NAME="灵枢 LingShu"
export LINGSHU_PROJECT_DIR="/home/ultima/LingShu"
export LINGSHU_P0_STAGE="1D-tritium-cellular-automaton"
export LINGSHU_PHILOSOPHY="self-benefit-other-benefit-long-term-convergence"

# 确保 hermes 命令可执行
if [ -f "$HOME/.local/bin/hermes" ]; then
    echo "✓ Hermes 可执行文件已就绪: $HOME/.local/bin/hermes"
else
    echo "⚠ Hermes 可执行文件未找到，请先运行: pip install -e /home/ultima/LingShu/hermes"
fi

echo ""
echo "环境变量已配置完成。"
echo "运行 'hermes' 或 'hermes-agent' 启动。"
echo ""
