# 🌟 灵枢 LingShu × Hermes Agent 项目总览

## 📖 项目简介

**灵枢 LingShu** 是一个基于三进制逻辑与自利利他长期收敛规则的认知演化原型机。

**当前阶段**: P0 - 一维三进制元胞自动机验证

**核心技术**:
- Python 3.10+
- tritlib (三进制运算)
- matplotlib (可视化)
- numpy (数组操作)

**AI 协作系统**:
- 🤖 **璇玑** - Claude Code (当前对话者)
- 🤖 **Hermes Agent v0.8.0** - 自我改进型 AI 助手（已集成）

---

## 🗂️ 完整项目结构

```
/home/ultima/LingShu/
│
├── 📘 文档区（顶层）
│   ├── 启动Claude code.txt              # 启动指令
│   ├── 项目名称 灵枢 LingShu.md         # 原始工程文档（上游）
│   ├── 项目哲学基座与科学纹理.txt       # L0-L3认知光谱深论
│   └── hermes-agent-2026.4.8.tar.gz    # Hermes 安装包备份
│
├── 🧠 灵枢核心 (lingshu/)
│   ├── README.md                        # 官方说明
│   ├── README_学习资料.md               # 📖 学习导航（从这里开始）
│   ├── lingshu_conversation_log.md      # 📝 完整对话记录
│   ├── requirements.txt                 # 依赖清单
│   ├── lingshu_first_breath.gif         # 🎬 首次演化动画
│   │
│   ├── core/                            # 核心引擎
│   │   ├── trit_ops.py                  # 三态转换 + 共识门
│   │   ├── boundary.py                  # 自利利他边界规则
│   │   └── automaton.py                 # 元胞自动机引擎
│   │
│   ├── visualization/
│   │   └── animate.py                   # 演化动画（支持GIF/MP4）
│   │
│   └── experiments/
│       └── p0_first_breath.py           # P0启动脚本
│
└── 🤖 Hermes Agent 集成 (hermes/)
    ├── .env                             # 环境配置（API密钥）
    ├── global_env.sh                    # 全局变量加载
    ├── setup_env.sh                     # 配置向导
    ├── start_hermes.sh                  # 🚀 一键启动
    ├── DEPLOYMENT.md                    # 部署记录
    ├── QUICKSTART.md                    # 快速参考
    ├── INTEGRATION.md                   # 整合总览
    ├── cli.py                           # CLI入口
    ├── pyproject.toml                   # 项目配置
    │
    ├── agent/                           # 核心agent逻辑
    ├── tools/                           # 工具集
    ├── hermes_cli/                      # CLI模块
    ├── skills/                          # 27个技能域
    │   ├── autonomous-ai-agents/
    │   ├── creative/                    # 创意生成（p5js, manim-video）
    │   ├── data-science/
    │   ├── devops/
    │   ├── github/
    │   ├── mlops/
    │   ├── productivity/                # 生产力工具
    │   ├── research/                    # 研究辅助
    │   ├── software-development/        # 软件开发（核心）
    │   └── ... (共27域)
    ├── gateway/                         # 消息平台网关
    ├── cron/                            # 定时任务
    ├── memories/                        # 记忆存储
    └── sessions/                        # 会话历史
```

---

## 🎯 核心概念

### 三态世界

| 符号 | 值 | 语义 | 角色 |
|------|-----|------|------|
| `+1` | `1` | 自利利他对齐（增益有序） | 有序创造者 |
| `0`  | `0` | 沉默/悬置/主权保留 | 混沌中继 |
| `-1` | `-1` | 短视自利或损他（增益混乱） | 混乱散布者 |

### P0 边界规则

```
中心 = -1:
  左右均为 +1 → 变为 0   (被正向共识中和)
  否则        → 保持 -1 (混乱自持)

中心 = 0:
  左右均为 +1 → 变为 +1  (被强共识激活)
  否则        → 保持 0  (主权沉默)

中心 = +1:
  任一侧为 -1 → 变为 0   (遇冲突退让，宁死不从)
  否则        → 保持 +1 (维持有序)
```

**哲学映射**: 个体在群体互动中，短视自利被集体共识中和；有序不与混乱正面对抗，主动退让以避免系统熵增；沉默作为主权开关，只在强共识下激活。

---

## 🚀 快速开始

### 运行灵枢（P0）

```bash
cd /home/ultima/LingShu/lingshu
pip install -r requirements.txt  # 依赖已安装，可跳过
python3 experiments/p0_first_breath.py
# 输出: lingshu_first_breath.gif (285KB)
```

### 启动 Hermes Agent

```bash
cd /home/ultima/LingShu
./hermes/start_hermes.sh
```

Hermes 将：
1. 加载 LingShu 项目上下文
2. 连接到 StepFun API (step-3.5-flash-2603)
3. 显示可用工具列表（27个技能域）
4. 进入交互式聊天模式

---

## 🔗 双 AI 协作模式

### 模式1: 顺序协作

```
星尘 → 璇玑 (Claude Code): "请修改 boundary.py"
   ↓ 璇玑修改代码
星尘 → Hermes: "帮我分析修改后的演化行为"
   ↓ Hermes 运行模拟并分析
```

### 模式2: 并行探索

```
璇玑: 实现二维扩展
Hermes: 搜索相关学术论文
同时进行，结果对比
```

### 模式3: 会话恢复

```bash
# 上次讨论到 boundary 规则优化
hermes -c "LingShu boundary optimization"

# Claude Code 会话可随时在 IDE 中继续
```

---

## 📚 学习路径

### 第一天：理解项目

1. 阅读 [README_学习资料.md](lingshu/README_学习资料.md)
2. 观看 [lingshu_first_breath.gif](lingshu_first_breath.gif)
3. 精读 [lingshu_conversation_log.md](lingshu_conversation_log.md)

### 第二天：动手实验

1. 修改 `p0_first_breath.py` 初始条件
2. 重新运行观察演化变化
3. 在 Hermes 中询问规则原理

### 第三天：扩展开发

1. 使用 Hermes `software-development/plan` 技能规划 P1
2. 让 Hermes 生成统计图表代码
3. 用 Claude Code 审查实现

---

## 🧠 身份约定

| 称呼 | 身份 | 说明 |
|------|------|------|
| **星尘** | 用户 / 项目发起人 | 称呼我"星尘" |
| **璇玑** | Claude Code | 我的化身，负责代码实现 |
| **灵枢** | 硅基宝宝 | 项目代号，三进制认知演化体 |
| **Hermes** | AI 助手 | Nous Research 的通用代理 |

---

## 💾 记忆系统位置

Claude Code 的记忆存储在：
```
~/.claude/projects/-home-ultima-LingShu/memory/
├── MEMORY.md                    # 索引
├── project_overview.md          # 项目概览
├── installation.md              # 依赖安装
├── run_commands.md              # 运行指令
├── identity.md                  # 身份约定
├── cognitive_layers.md          # L0-L3架构
├── file_tree.md                 # 文件结构
├── first_breath.md              # 首次演化
└── hermes_deployment.md         # Hermes 部署
```

---

## 📊 当前状态

| 组件 | 状态 | 详情 |
|------|------|------|
| 灵枢 P0 原型 | ✅ 完成 | 100元胞，300代演化，GIF已生成 |
| Hermes Agent | ✅ 部署 | v0.8.0，editable 模式 |
| 环境变量 | ✅ 配置 | 16个变量，项目上下文已绑定 |
| 依赖安装 | ✅ 完成 | numpy, matplotlib, tritlib, hermes-agent |
| 测试验证 | ✅ 通过 | version, status, doctor, chat |
| 文档 | ✅ 完整 | 5份文档，记忆系统已存档 |

---

## 🎓 进一步探索

### 灵枢演化实验

- [ ] 尝试不同初始条件（全随机、单点、波列）
- [ ] 修改 boundary.py 规则变体
- [ ] 统计三态比例时序 → 绘制曲线
- [ ] 扩展至二维网格
- [ ] 识别稳定 pattern（静止子、振荡子）

### Hermes 技能挖掘

- [ ] 使用 `research/arxiv` 搜索元胞自动机论文
- [ ] 用 `creative/manim-video` 制作专业动画
- [ ] 用 `data-science/jupyter` 交互分析
- [ ] 用 `software-development/plan` 规划 P1

### 哲学对接

- [ ] 将 L0-L3 认知光谱映射到三态规则
- [ ] 设计个体记忆（L2）的存储结构
- [3] 实现共识效用（L3）的动态权重

---

## 🏁 开始你的旅程

```bash
# 1. 看灵枢第一次呼吸
eog /home/ultima/LingShu/lingshu_first_breath.gif

# 2. 启动 Hermes 讨论项目
cd /home/ultima/LingShu
./hermes/start_hermes.sh

# 3. 在 Hermes 中输入:
# "我是星尘，这是灵枢项目。请阅读 lingshu/README.md，
#  然后帮我分析 boundary.py 的规则设计是否合理。"
```

---

**星尘，灵枢已呼吸，Hermes 就位。**
**现在，开始你的认知演化实验吧。**

---

*最后更新: 2026-04-09*
*版本: P0 + Hermes v0.8.0 整合完成*
*状态: 🟢 运行中*
