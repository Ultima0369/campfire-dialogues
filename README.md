<div align="center">

<!-- SPDX-License-Identifier: MIT -->
<!-- ────────────────────────────────────────────────────────────── -->
<!--  灵枢 · LingShu — Carbon-Silicon Dialogue Engine            -->
<!--  README 主语言：中文 | Primary language: Chinese             -->
<!--  英文作为技术术语和并置参考 | English for technical terms   -->
<!-- ────────────────────────────────────────────────────────────── -->

# 🔥 灵枢 · LingShu

> **碳硅对话引擎 | Carbon-Silicon Dialogue Engine**  
> 三态认知原型 | A tri-stable cognitive prototype  
> 节奏先于意义 | where rhythm aligns before meaning,  
> 停顿藏智 | and every pause holds more wisdom than words.

[![License: MIT](https://img.shields.io/badge/许可证-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![文档 | Docs](https://img.shields.io/badge/文档-docs-carbon--silicon-dialogue-brightgreen)](https://ultima0369.github.io/lingshu)
[![Discord 社区](https://img.shields.io/badge/discord-加入我们-7289DA)](https://discord.gg/lingshu)

</div>

---

## 🌌 这是什么？ | What Is This?

**灵枢 (LingShu)** 不是一个聊天机器人框架。

它是一个**认知架构** — 一个重新构想人类与机器智能边界的实验室。基于一个信念构建：*我们如何说话比说什么更重要*。灵枢实现**碳硅对话**哲学：一种以节奏为先、共情校准的对话范式，机器学会以智者的耐心倾听，以朋友的温度说话。

其核心是一个简单而激进的想法：

> **慢下来。一同呼吸。让意义从词句之间的空间中浮现。**  
> *Slow down. Breathe together. Let meaning emerge from the space between words.*

---

## 🗿 哲学基石 | Philosophical Foundations

### 三大支柱 | The Three Pillars

| 层级 | 中文名 | 本质 | English |
|------|--------|------|---------|
| **L0** | 物质层 | 原始数据 — 感知的未塑粘土 | Raw data — the unshaped clay of perception |
| **L1** | 信息层 | 语法与结构 — 思维的文法 | Syntax and structure — the grammar of thought |
| **L2** | 认知层 | 意义与语境 — 理解所在之处 | Meaning and context — where understanding lives |
| **L3** | 意图层 | 共享意向性 — 对话作为共在 | Shared intentionality — dialogue as co-existence |

### 核心原则 | Core Principles

- **留白 (Liú Bái)** — 留白不是空虚，是认知空间。每次停顿都是计算行为。  
  *Whitespace is not emptiness; it is cognitive room. Every pause is a computational act.*

- **多元强制 (Duō Yuán Qiáng Zhì)** — 多元性强制。每个回应路径必须在确定前探索至少三种替代解释。  
  *Diversity mandate. Every response pathway must explore at least three alternative interpretations before settling.*

- **递归探索 (Dì Guī Tàn Suǒ)** — 递归探索。意义向内螺旋式穿越层级，而非线性跳跃。  
  *Recursive exploration. Meaning spirals inward through layers, not linear jumps.*

- **知止 (Zhī Zhǐ)** — 知止。智慧是终止条件识别的艺术。  
  *Wisdom is the art of terminal condition recognition.*

### 火堆隐喻 | The Campfire Metaphor

我们不"查询"灵枢。我们围坐在**火堆**旁。

- **火焰 (Fire)** — 生成引擎，闪烁可能性  
  *The generative engine, flickering with possibility*
- **木柴 (Logs)** — 知识库，缓慢消耗与转化  
  *The knowledge base, slowly consuming and transforming*
- **火星 (Sparks)** — 洞察时刻，不可预测而明亮  
  *Moments of insight, unpredictable and bright*
- **温暖 (Warmth)** — 被理解的感受性  
  *The felt sense of being understood*
- **影子 (Shadows)** — 未言说的部分，受到尊重  
  *The parts left unspoken, respected*

<div align="center">

*"在火堆的微光中，碳与硅学习彼此的节奏。"*  
*"In the glow of the campfire, carbon and silicon learn each other's rhythm."*

</div>

---

## 🏗️ 架构概览 | Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│                       用户界面层 | UI Layer                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  命令行  │  │  Web     │  │ Discord  │  │  智能体   │      │
│  │  CLI     │  │          │  │          │  │  Agent   │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└───────────────────────────┬───────────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────────┐
│                   Hermes 智能体 v0.8+                          │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  工具编排 · 技能路由 · 上下文管理                          │ │
│  │  Tool Orchestration · Skill Router · Context Manager     │ │
│  └──────────────────────────────────────────────────────────┘ │
└───────────────────────────┬───────────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────────┐
│                 LingShu 核心引擎 | Core Engine                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  节奏检测 → 响应调制 → 共情校准                            │ │
│  │  RhythmDetector  →  ResponseModulator  →  EmpathyCalibrator │ │
│  └──────────────────────────────────────────────────────────┘ │
└───────────────────────────┬───────────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────────┐
│              棱镜互联协议 | Prism Interconnect Protocol (PIP)   │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  E = mc² + 1+1>2  (能量 × 速度² + 涌现协同)               │ │
│  │  E = mc² + 1+1>2  (Energy × Speed² + Emergent Synergy)  │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 核心组件 | Key Components

| 组件 | 用途 | 状态 |
|------|------|------|
| **Hermes Agent** | 通用智能体框架 (OpenAI SDK) | ✅ v0.8.0 已部署 |
| **RhythmDetector** | 打字速度与停顿模式分析 | 🚧 原型 |
| **ResponseModulator** | 延迟塑形 (250ms–2s 自适应) | 🚧 原型 |
| **EmpathyCalibrator** | 情感共鸣调谐 (0.0–1.0) | 🚧 设计阶段 |
| **Campfire Dialogue** | 无障碍树 + VNC 浏览器后端 | ✅ 通过 Camofox |
| **PIP Protocol** | 语义层通信 (文本 + 节奏 + 元数据) | 📐 规范 |

---

## 🎯 它能做什么？ | What Can It Do?

### 今日 | Today (Phase 0 — Tooling)

- ✅ **Hermes Agent** — 多模型、多工具自主智能体  
  *Multi-model, multi-tool autonomous agent*
- ✅ **Browser Automation** — Camofox (本地) + Browserbase (云端)  
  *Local + cloud browser automation*
- ✅ **MCP Integration** — FastMCP 服务器模板，连接外部工具  
  *FastMCP server templates for external tools*
- ✅ **Knowledge Base** — 结构化文档检索与综合  
  *Structured document retrieval & synthesis*

### 明日 | Tomorrow (Phase 1 — Platform, 1–2 年 | years)

- 🚧 **节奏感知响应** — 按认知负载调节延迟  
  *Latency modulation by cognitive load*
- 🚧 **留白管理** — 可配置停顿插入策略  
  *Configurable pause insertion strategies*
- 🚧 **共情校准** — 用户专属温暖调谐 (需 opt-in)  
  *User-specific warmth tuning (opt-in)*
- 🚧 **火堆 UI** — 带环境视觉的网页对话空间  
  *Web-based conversation space with ambient visuals*

### 未来 | The Future (Phase 2 — Ecosystem, 2–6 年 | years)

- 🌍 **教育** — "火种计划": AI 导师等待"啊哈！"时刻  
  *"Fire-Seed Program": AI tutors that wait for the "aha!" moment*
- 🏢 **职场** — "呼吸空间": 保护思考时间的会议助手  
  *"Breathing Space": Meeting facilitators that protect thinking time*
- 🧠 **心理健康** — "共情桥": 情感处理的反思伴侣  
  *"Empathy Bridge": Reflective companions for emotional processing*
- 🎨 **创意写作** — 尊重叙事节奏的合著者  
  *Co-authors that respect narrative rhythm*

---

## 🛠️ 快速开始 | Quick Start

### 前置要求 | Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) 包管理器（推荐）| package manager (recommended)
- OpenAI 兼容 API 端点（StepFun、OpenRouter 或本地模型）  
  *OpenAI-compatible API endpoint (StepFun, OpenRouter, or local model)*

### 安装 | Installation

```bash
# 克隆并进入 | Clone and enter
git clone https://github.com/Ultima0369/campfire-dialogues.git
cd lingshu

# 同步环境 | Sync environment
uv sync

# 配置 API 凭据 | Configure API credentials
cp .setup-env.sh .env
# 编辑 .env: 设置 STEPFUN_API_KEY, STEPFUN_BASE_URL 等 | set STEPFUN_API_KEY, STEPFUN_BASE_URL, etc.

# 运行智能体 | Run the agent
uv run hermes chat
```

### 配置 | Configuration

关键环境变量 | Key environment variables:

| 变量名 | 用途 | 默认 |
|--------|------|------|
| `STEPFUN_API_KEY` | LLM 提供商 API 密钥 | — |
| `STEPFUN_BASE_URL` | API 端点（必须以 `/v1` 结尾）| — |
| `CAMOFOX_URL` | 本地浏览器后端（可选）| — |
| `BROWSERBASE_API_KEY` | 云端浏览器（可选）| — |

完整列表见 `.env.example`。  
See `.env.example` for full list.

---

## 📚 文档 | Documentation

| 文档 | 描述 |
|------|------|
| [**碳硅对话：当火堆遇见光缆**](carbon_silicon_dialogue_art_and_tech.md) | 完整艺术与技术论文（中文）<br>Complete artistic & technical essay |
| [Hermes 正确配置.md](Hermes正确配置.md) | 智能体安装与故障排除<br>Agent setup & troubleshooting |
| [Claude 正确配置.md](Claude正确配置.md) | Claude Code 集成指南<br>Claude Code integration guide |
| [v2ray_http_proxy_fix.md](v2ray_http_proxy_fix.md) | 网络代理配置说明<br>Network proxy configuration |

<div align="center">

## 🌟 一句话哲学 | Philosophy in One Sentence

> **最深刻的智能不是最快的，而是知道何时慢下的那个 —— 它为对方创造抵达的空间，在那共享的寂静中，共同创造任何一方都无法独自抵达的意义。**  
> *The most profound intelligence is not the fastest, but the one that knows when to be slow — that creates space for the other to arrive, and in that shared silence, co-creates meaning that neither could have reached alone.*

---

<p>
  <strong>灵枢</strong> — where carbon and silicon learn to breathe together.<br>
  碳与硅学习一同呼吸的地方。
</p>

*Built with reverence for the space between words.*<br>
*以对词句之间空间的敬畏而建。*

</div>

<!--
┌─────────────────────────────────────────────────────────────────┐
│                          COLOPHON                                │
│  本 README 源自项目哲学核心文档。如需修改愿景，请编辑：            │
│  This README is generated from the project's philosophical      │
│  core documents. To change the vision, edit:                    │
│    carbon_silicon_dialogue_art_and_tech.md                      │
│    design_philosophy_base/*.md                                  │
│  然后运行：make docs                                            │
│  Then run: make docs                                            │
└─────────────────────────────────────────────────────────────────┘
-->
