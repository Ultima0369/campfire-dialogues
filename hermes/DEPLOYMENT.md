# Hermes Agent 部署记录

## 📦 安装来源

- **源码包**: `/home/ultima/LingShu/hermes-agent-2026.4.8.tar.gz` (8.4 MB)
- **版本**: Hermes Agent v0.8.0 (2026.4.8)
- **来源**: Nous Research
- **安装方式**: Editable mode (`pip install -e .[cli]`)

## 📁 项目结构

```
/home/ultima/LingShu/
├── hermes/                      # Hermes Agent 源码（整合后）
│   ├── .env                     # 环境变量配置（API密钥、端点）
│   ├── .env.example             # 环境变量模板
│   ├── global_env.sh            # 全局环境变量加载脚本
│   ├── setup_env.sh             # 交互式环境配置脚本
│   ├── start_hermes.sh          # Hermes 启动脚本（集成 LingShu 上下文）
│   ├── cli.py                   # Hermes CLI 入口（390KB）
│   ├── pyproject.toml           # 项目配置与依赖声明
│   ├── requirements.txt         # 依赖清单（便利版）
│   ├── agent/                   # 核心 agent 逻辑
│   ├── tools/                   # 工具集（terminal, browser, file...）
│   ├── hermes_cli/              # CLI 模块
│   ├── skills/                  # 技能库（27个技能域）
│   │   ├── autonomous-ai-agents/  # AI代理协作技能
│   │   ├── creative/              # 创意生成（p5js, manim-video）
│   │   ├── data-science/          # 数据科学
│   │   ├── devops/                # 运维部署
│   │   ├── github/                # GitHub集成
│   │   ├── mlops/                 # 机器学习运维
│   │   ├── productivity/          # 生产力工具（Google Workspace, Linear, Notion）
│   │   ├── research/              # 研究辅助（ArXiv, 大集合探索）
│   │   ├── software-development/  # 软件开发（plan, code-review）
│   │   └── ... (共27个技能域)
│   ├── gateway/                 # 消息平台网关
│   ├── cron/                    # 定时任务
│   ├── memories/                # 记忆存储
│   └── sessions/                # 会话历史
├── lingshu/                     # 灵枢项目（三进制认知演化）
│   └── ...
└── hermes-agent-2026.4.8.tar.gz # 原始安装包备份
```

## 🔧 环境变量配置

### 核心变量

| 变量名 | 值 | 说明 |
|--------|-----|------|
| `HERMES_HOME` | `/home/ultima/.hermes` | Hermes 数据目录 |
| `HERMES_PROJECT_DIR` | `/home/ultima/LingShu` | 当前项目根目录 |
| `HERMES_DEFAULT_MODEL` | `step-3.5-flash-2603` | 默认模型 |
| `OPENAI_API_KEY` | `5cFLQ...o8RE` | StepFun API 密钥 |
| `OPENAI_BASE_URL` | `https://api.stepfun.com/step_plan/v1` | API 端点 |

### LingShu 项目上下文

这些变量让 Hermes 知道它在灵枢项目中工作：

| 变量名 | 值 |
|--------|-----|
| `LINGSHU_PROJECT_NAME` | 灵枢 LingShu |
| `LINGSHU_PROJECT_DIR` | `/home/ultima/LingShu/lingshu` |
| `LINGSHU_P0_STAGE` | 1D-tritium-cellular-automaton |
| `LINGSHU_PHILOSOPHY` | self-benefit-other-benefit-long-term-convergence |

## 🚀 启动方式

### 方式1：直接命令（已配置环境变量）

```bash
# 加载环境变量
source /home/ultima/LingShu/hermes/global_env.sh

# 启动 Hermes 交互模式
hermes

# 单次查询
hermes chat -q "你的问题"
```

### 方式2：使用启动脚本（推荐）

```bash
cd /home/ultima/LingShu
./hermes/start_hermes.sh
```

脚本会自动：
- 检查环境配置文件
- 加载环境变量
- 显示项目上下文
- 启动 Hermes Agent

### 方式3：集成到 LingShu 工作流

在 `lingshu/` 目录下创建便捷脚本：

```bash
# lingshu/run_with_hermes.sh
#!/bin/bash
source ../hermes/global_env.sh
hermes chat -q "$@"
```

## ✅ 测试验证结果

### 版本检查

```bash
$ hermes --version
Hermes Agent v0.8.0 (2026.4.8)
Project: /home/ultima/LingShu/hermes
Python: 3.13.7
OpenAI SDK: 2.30.0
```

### 状态检查 (`hermes status`)

```
◆ Environment
  Project:      /home/ultima/LingShu/hermes
  Python:       3.13.7
  .env file:    ✓ exists
  Model:        step-3.5-flash-2603
  Provider:     Custom endpoint

◆ API Keys
  OpenAI        ✓ configured
  Anthropic     ✓ configured
```

### 诊断检查 (`hermes doctor`)

```
◆ Required Packages
  ✓ OpenAI SDK
  ✓ Rich (terminal UI)
  ✓ python-dotenv
  ✓ PyYAML
  ✓ HTTPX

◆ Directory Structure
  ✓ ~/.hermes directory exists
  ✓ sessions/ exists (18个历史会话)
  ✓ skills/ exists (27个技能域)
  ✓ MEMORY.md exists

◆ Tools Available
  ✓ terminal, file, browser, code_execution, ...
```

### 聊天测试

```bash
$ hermes chat -q "你好"
# 成功启动并显示可用工具列表
```

## 🔐 安全说明

1. **API 密钥**: 存储在 `/home/ultima/LingShu/hermes/.env`，此文件应保密
2. **网络连接**: 直连模式（无代理配置），直接访问 StepFun API
3. **YOLO 模式**: `HERMES_YOLO_MODE=1` 已启用，绕过危险命令确认（谨慎使用）
4. **Sudo**: 当前禁用，Hermes 无法执行需要sudo的命令

## 🧠 与 LingShu 的集成点

### 1. 项目上下文感知

Hermes 通过环境变量感知：
- 所在项目为"灵枢 LingShu"
- 当前阶段为 P0 三进制元胞自动机
- 核心哲学是"自利利他长期收敛"

### 2. 技能映射

Hermes 技能可协助 LingShu 开发：

| Hermes 技能 | 对 LingShu 的用途 |
|-------------|------------------|
| `software-development/plan` | 架构规划 |
| `software-development/code-review` | 代码审查 |
| `software-development/debug` | 调试 |
| `creative/manim-video` | 生成演化动画（替代 matplotlib） |
| `research/arxiv` | 搜索元胞自动机相关论文 |
| `data-science/jupyter` | 交互式数据分析 |
| `productivity/notion` | 记录实验笔记 |
| `github/codebase-inspection` | 分析 LingShu 代码库 |

### 3. 会话持久化

所有与 Hermes 关于 LingShu 的对话都保存在：
```
~/.hermes/sessions/
```

可随时恢复：
```bash
hermes -r "session_name_or_id"
```

## 📊 当前状态

- ✅ Hermes Agent v0.8.0 已安装（editable mode）
- ✅ 环境变量已配置
- ✅ API 连接验证通过
- ✅ 27个技能域已加载
- ✅ 18个历史会话已迁移
- ✅ 与 LingShu 项目上下文已绑定

## ⚠️ 已知限制

1. **无虚拟环境**: Python 3.13 系统环境直接运行（建议后续创建 venv）
2. **部分技能需额外配置**:
   - `web` 工具需 EXA/FIRECRAWL API 密钥
   - `image_gen` 需 FAL 或其它图像生成 API
   - `messaging` 需 Telegram/Discord/Slack 机器人令牌
3. **Git submodule**: `tinker-atropos` 未初始化（RL 技能依赖）
4. **图形界面**: 当前为纯终端环境，Hermes 的 TUI 可工作但无色彩（SSH 限制）

## 📚 后续建议

1. **创建项目专用 Profile**:
   ```bash
   hermes profile create lingshu
   ```

2. **初始化技能子模块**:
   ```bash
   cd /home/ultima/LingShu/hermes
   git submodule update --init --recursive
   ```

3. **安装可选依赖**:
   ```bash
   pip install -e ".[all]"  # 安装所有可选技能依赖
   ```

4. **配置外部 API** (按需):
   - Exa (web search): `EXA_API_KEY`
   - Firecrawl: `FIRECRAWL_API_KEY`
   - Tavily: `TAVILY_API_KEY`

5. **LingShu 专用技能**: 考虑为"自利利他边界规则"创建自定义 Hermes 技能

---

**部署时间**: 2026-04-09 23:15 UTC
**部署者**: 璇玑 (Claude Code)
**状态**: ✅ 已就绪，可投入使用

## 🔍 系统范围搜索补充

后台全系统搜索（`find / -type f -iname "*hermes*"`）还发现了以下相关文件：

### 用户目录文件

| 路径 | 用途 |
|------|------|
| `/home/ultima/test-hermes-auto.sh` | Hermes auto 模式测试脚本（用户自定义） |
| `/home/ultima/.local/bin/hermes-auto` | 非交互模式启动器（已链接） |

### 桌面文档

| 路径 | 用途 |
|------|------|
| `/home/ultima/桌面/HERMES-AUTO-SETUP.md` | Hermes 自动设置指南 |
| `/home/ultima/桌面/everything-claude-code/docs/HERMES-SETUP.md` | Claude 集成文档 |
| `/home/ultima/桌面/everything-claude-code/docs/HERMES-OPENCLAW-MIGRATION.md` | OpenClaw 迁移指南 |

### Claude 插件文档

| 路径 | 用途 |
|------|------|
| `~/.claude/plugins/marketplaces/ecc/docs/HERMES-SETUP.md` | ECC 市场插件设置 |
| `~/.claude/plugins/marketplaces/ecc/docs/HERMES-OPENCLAW-MIGRATION.md` | OpenClaw 迁移 |

### 临时提取文件

| 路径 | 用途 |
|------|------|
| `/tmp/hermes-agent-2026.4.8/setup-hermes.sh` | 原始安装脚本 |
| `/tmp/hermes-agent-2026.4.8/website/` | 官方网站资源 |
| `/tmp/hermes-agent-2026.4.8/tests/` | 测试套件 |

**注**：以上文件为系统搜索发现的补充信息，主要部署文件已在 `/home/ultima/LingShu/hermes/` 目录完整保存。

