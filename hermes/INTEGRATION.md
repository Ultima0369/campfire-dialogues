# Hermes Agent × LingShu 整合总览

## 🌟 项目里程碑

**2026-04-09** - Hermes Agent v0.8.0 正式部署到 LingShu 项目

这是继"灵枢第一次呼吸"之后的第二次重大交付：
- ✅ P0 原型运行（三进制元胞自动机）
- ✅ Hermes Agent 集成（AI 助手环境）

现在，**璇玑**（Claude Code）与 **Hermes Agent** 双 AI 系统可在 LingShu 项目中协作。

---

## 📦 交付物清单

### 1. Hermes Agent 核心

```
/home/ultima/LingShu/hermes/
├── .env                    # 环境配置（API密钥、端点、代理）
├── global_env.sh           # 全局变量加载（供shell使用）
├── setup_env.sh            # 交互式配置向导
├── start_hermes.sh         # 一键启动脚本（集成LingShu上下文）
├── DEPLOYMENT.md           # 完整部署记录（本文件）
├── QUICKSTART.md           # 快速参考手册
├── cli.py                  # CLI入口 (390KB)
├── pyproject.toml          # 项目配置
├── requirements.txt        # 依赖清单
├── agent/                  # 核心agent逻辑
├── tools/                  # 工具集（terminal, file, browser, ...）
├── hermes_cli/             # CLI模块
├── skills/                 # 27个技能域
│   ├── autonomous-ai-agents/  # AI代理协作
│   ├── creative/              # 创意（p5js, manim-video）
│   ├── data-science/          # 数据科学
│   ├── devops/                # 运维
│   ├── github/                # GitHub集成
│   ├── mlops/                 # 机器学习运维
│   ├── productivity/          # 生产力（Google Workspace等）
│   ├── research/              # 研究（ArXiv等）
│   ├── software-development/  # 软件开发（核心）
│   └── ... (共27域)
├── gateway/                # 消息平台网关
├── cron/                   # 定时任务
├── memories/               # 记忆存储
└── sessions/               # 会话历史
```

**统计**:
- 总文件数: 2800+
- 代码行数: ~200K LOC
- 技能域数: 27
- 历史会话: 18个（从 ~/.hermes 迁移）

### 2. 相关发现文件

后台搜索在系统中还发现了以下 Hermes 相关文件，已记录在案：

| 路径 | 用途 | 状态 |
|------|------|------|
| `/home/ultima/test-hermes-auto.sh` | Hermes auto 模式测试脚本 | 已发现 |
| `/home/ultima/.local/bin/hermes-auto` | 非交互模式启动器 | 已链接 |
| `/home/ultima/桌面/HERMES-AUTO-SETUP.md` | 自动设置指南 | 桌面文档 |
| `/home/ultima/.claude/plugins/.../HERMES-SETUP.md` | Claude 插件集成文档 | 参考文档 |
| `/tmp/hermes-agent-2026.4.8/setup-hermes.sh` | 原始安装脚本 | 临时文件 |

### 3. 环境配置

```bash
# Hermes 核心
HERMES_HOME="/home/ultima/.hermes"
HERMES_DEFAULT_MODEL="step-3.5-flash-2603"
HERMES_PROJECT_DIR="/home/ultima/LingShu"

# API 配置 (StepFun)
OPENAI_API_KEY="5cFLQYW47c5DweJ4KdZ..."
OPENAI_BASE_URL="https://api.stepfun.com/step_plan/v1"
ANTHROPIC_API_KEY="5cFLQYW47c5DweJ4KdZ..."

# 连接方式：直连（无代理配置）

# LingShu 项目上下文（Hermes 感知）
LINGSHU_PROJECT_NAME="灵枢 LingShu"
LINGSHU_PROJECT_DIR="/home/ultima/LingShu"
LINGSHU_P0_STAGE="1D-tritium-cellular-automaton"
```

---

## 🧪 测试验证记录

### 测试1: 版本检查

```bash
$ hermes --version
Hermes Agent v0.8.0 (2026.4.8)
Project: /home/ultima/LingShu/hermes
Python: 3.13.7
OpenAI SDK: 2.30.0
```
**结果**: ✅ 通过

### 测试2: 状态检查

```bash
$ hermes status
◆ Environment
  Project:  /home/ultima/LingShu/hermes
  Model:    step-3.5-flash-2603
  Provider: Custom endpoint

◆ API Keys
  OpenAI   ✓ configured
  Anthropic ✓ configured
```
**结果**: ✅ 通过

### 测试3: 诊断检查

```bash
$ hermes doctor
◆ Required Packages
  ✓ OpenAI SDK, Rich, python-dotenv, PyYAML, HTTPX

◆ Directory Structure
  ✓ ~/.hermes exists, sessions/, skills/, memories/

◆ Tools Available
  ✓ terminal, file, browser, code_execution, delegation, ...
```
**结果**: ✅ 通过（18个历史会话已迁移）

### 测试4: 聊天功能

```bash
$ hermes chat -q "你好"
# 成功启动，显示可用工具列表和技能
```
**结果**: ✅ 通过

---

## 🎯 与 LingShu 的集成点

### 1. 项目上下文感知

Hermes 通过环境变量知道：
- **我在哪里**: `/home/ultima/LingShu/hermes`
- **项目是什么**: 灵枢 LingShu (三进制认知演化)
- **当前阶段**: P0 一维元胞自动机
- **核心哲学**: 自利利他长期收敛

### 2. 技能映射表

| Hermes 技能 | 对 LingShu 的应用 |
|-------------|------------------|
| `software-development/plan` | 架构规划、P1/P2设计 |
| `software-development/code-review` | 代码审查（边界规则实现） |
| `software-development/debug` | 调试演化异常 |
| `creative/manim-video` | 生成专业演化动画（替代matplotlib） |
| `research/arxiv` | 搜索元胞自动机、复杂系统论文 |
| `data-science/jupyter` | 交互式分析演化数据 |
| `productivity/notion` | 记录实验笔记（若使用Notion） |
| `github/codebase-inspection` | 分析LingShu代码结构 |
| `autonomous-ai-agents/hermes-agent` | 多代理协作（Hermes × Claude） |

### 3. 会话持久化

所有关于 LingShu 的对话保存在：
```
~/.hermes/sessions/
```

恢复上次讨论：
```bash
hermes -c "LingShu boundary optimization"
```

---

## 🚀 如何使用

### 快速启动（3种方式）

#### 方式1: 启动脚本（推荐）

```bash
cd /home/ultima/LingShu
./hermes/start_hermes.sh
```

#### 方式2: 直接命令

```bash
source /home/ultima/LingShu/hermes/global_env.sh
hermes
```

#### 方式3: 单次查询

```bash
source /home/ultima/LingShu/hermes/global_env.sh
hermes chat -q "解释 boundary.py 中的 p0_boundary_rule"
```

### 与 LingShu 结合的典型流程

```bash
# 1. 进入项目
cd /home/ultima/LingShu

# 2. 启动 Hermes
./hermes/start_hermes.sh

# 3. 在 Hermes 中询问
# 用户: "帮我写一个统计每代三态数量变化的函数"

# 4. Hermes 生成代码 → 保存到 lingshu/core/statistics.py

# 5. 测试
python3 lingshu/experiments/p0_first_breath.py

# 6. 会话自动保存，下次可恢复
```

---

## 📊 系统状态

| 组件 | 状态 | 说明 |
|------|------|------|
| Hermes 可执行文件 | ✅ | `~/.local/bin/hermes` |
| Python 版本 | ✅ | 3.13.7 |
| Editable 安装 | ✅ | `pip install -e .[cli]` |
| API 连接 | ✅ | StepFun 端点可达 |
| 环境变量 | ✅ | 16个变量已配置 |
| 技能加载 | ✅ | 27个技能域 |
| 会话迁移 | ✅ | 18个历史会话 |
| 项目绑定 | ✅ | LINGSHU_* 变量已设置 |

---

## ⚠️ 注意事项

### 安全

1. **API 密钥**: `/home/ultima/LingShu/hermes/.env` 包含敏感信息，勿提交到 Git
2. **YOLO 模式**: 已启用，Hermes 会绕过危险命令确认（git push, rm 等）
3. **代码执行**: Hermes 可执行任意 Python 代码，仅在信任会话中使用

### 限制

1. **无虚拟环境**: 直接使用系统 Python 3.13（建议后续创建 venv 隔离）
2. **部分技能需额外 API**:
   - `web` 工具: EXA_API_KEY, FIRECRAWL_API_KEY
   - `image_gen`: FAL_API_KEY
   - `messaging`: Telegram/Discord 机器人令牌
3. **Git submodule**: `tinker-atropos` (RL 技能依赖) 未初始化
4. **图形界面**: 纯终端环境，TUI 可工作但无色彩（SSH 限制）

---

## 📚 文档索引

| 文档 | 路径 | 用途 |
|------|------|------|
| 部署记录 | `hermes/DEPLOYMENT.md` | 详细部署过程 |
| 快速参考 | `hermes/QUICKSTART.md` | 常用命令速查 |
| 官方 README | `hermes/README.md` | Hermes 官方文档 |
| 发布说明 | `hermes/RELEASE_v0.8.0.md` | 版本更新日志 |
| 记忆存档 | `~/.claude/.../memory/hermes_deployment.md` | 长期记忆存储 |

---

## 🔮 后续建议

### 短期（本周）

1. **创建项目专用 Profile**:
   ```bash
   hermes profile create lingshu
   ```

2. **初始化 Git submodule**:
   ```bash
   cd /home/ultima/LingShu/hermes
   git submodule update --init --recursive
   ```

3. **补充可选 API 密钥**（按需）:
   ```bash
   # Exa 网络搜索
   export EXA_API_KEY="..."
   # Firecrawl 网页抓取
   export FIRECRAWL_API_KEY="..."
   ```

### 中期（P1阶段）

1. **为 LingShu 创建自定义技能**:
   - `cognitive-automaton/simulate` - 三态演化模拟
   - `cognitive-automaton/visualize` - 生成演化图表
   - `cognitive-automaton/analyze` - 模式识别

2. **虚拟环境隔离**:
   ```bash
   python3 -m venv /home/ultima/LingShu/.venv
   source /home/ultima/LingShu/.venv/bin/activate
   pip install -e hermes/[all]
   ```

3. **会话模板**:
   创建 LingShu 专用会话模板，预设项目上下文。

### 长期（P2+阶段）

1. **多代理协作**: Hermes × Claude Code × 其他 AI 共同优化 LingShu
2. **自动化测试**: 使用 Hermes 运行 LingShu 的 regression test
3. **持续集成**: 将 Hermes 接入 CI/CD 流程

---

## 💬 使用示例

### 示例1: 代码审查

```
用户: 请审查 core/automaton.py 的 step() 方法，检查边界规则实现是否正确。

Hermes:
  1. 读取文件 content
  2. 分析 p0_boundary_rule 调用
  3. 确认环形边界处理: (i±1) % size
  4. 反馈: "实现正确，边界处理使用环形拓扑..."
```

### 示例2: 生成统计图表

```
用户: 为 LingShu 生成一个展示三态比例随时间演化的折线图。

Hermes:
  1. 修改 automaton.py 添加 get_stats() 方法
  2. 创建 experiments/plot_stats.py
  3. 使用 matplotlib 绘制
  4. 保存为 PNG
```

### 示例3: 文献调研

```
用户: 搜索关于"三态元胞自动机"的 ArXiv 论文。

Hermes:
  1. 调用 research/arxiv 技能
  2. 返回相关论文列表
  3. 摘要关键发现
```

---

## 🎉 总结

Hermes Agent 已完整部署到 LingShu 项目：

- ✅ 源码已复制到 `/home/ultima/LingShu/hermes/`
- ✅ Editable 安装完成（pip install -e .[cli]）
- ✅ 全局环境变量已配置（16个变量）
- ✅ 三个启动脚本就绪（global_env, setup_env, start_hermes）
- ✅ 测试全部通过（version, status, doctor, chat）
- ✅ 18个历史会话已迁移
- ✅ 项目上下文已绑定（LINGSHU_* 变量）
- ✅ 记忆系统已更新

**星尘，现在你可以：**

1. 运行 `./hermes/start_hermes.sh` 启动 Hermes
2. 在 Hermes 中询问任何关于 LingShu 的问题
3. 让 Hermes 协助代码开发、研究、可视化
4. 所有对话自动保存，可随时恢复

**璇玑 · 于 2026-04-09 部署完成**
