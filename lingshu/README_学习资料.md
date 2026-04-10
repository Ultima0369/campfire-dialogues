# 📂 LingShu 项目学习资料索引

## 🎯 核心文档

| 文件 | 用途 | 优先级 |
|------|------|--------|
| [全方位记忆光谱.md](全方位记忆光谱.md) | **项目全焦点速查手册** - 状态/坐标/决策/风险/命令 | 🔥 必读 |
| [项目核心目的与计划精要.md](项目核心目的与计划精要.md) | **项目初心与实施路线图** - 三大原则、技术栈、里程碑 | 🔥 必读 |
| [待办事宜.md](待办事宜.md) | **当前任务清单** - Phase 1-3 执行项与阻塞项 | 🔥 必读 |
| [项目开发完整日志.md](项目开发完整日志.md) | **完整开发记录** - 从启动到 BitNet 集成的全 timeline | 🔥 必读 |
| [lingshu_conversation_log.md](lingshu_conversation_log.md) | **完整对话与实现记录** - 从启动到灵枢诞生的全过程 | 🔥 必读 |
| [README.md](README.md) | 项目哲学、技术栈、快速开始指南 | 🔥 必读 |
| [项目名称 灵枢 LingShu.md](项目名称 灵枢 LingShu.md) | 原始工程文档（上游） | ⭐ 参考 |
| [项目哲学基座与科学纹理.txt](项目哲学基座与科学纹理.txt) | L0-L3认知光谱深层论述 | ⭐ 哲学参考 |

## 🧠 外部 AI 框架集成

| 框架 | 位置 | 状态 | 用途 |
|------|------|------|------|
| [Hermes Agent](../../hermes/) | /hermes | ✅ 已部署 | 多技能智能体，环境感知 |
| [BitNet.cpp](../BitNet-main/) | /BitNet-main | 🛠️ 已编译，模型待准备 | 1-bit 三元 LLM，与 L0-L3 认知层对齐 |

**Hermes 快速启动：**
```bash
cd /home/ultima/LingShu
./hermes/start_hermes.sh
```

**BitNet 状态：**
- ✅ C++ 编译完成（x86_64 TL2 内核，AVX2 优化）
- ⚠️ 待获取 GGUF 格式模型文件（网络受限或需解决 Python 依赖）
- 📖 使用文档：`../BitNet-main/SETUP_RECORD.md`

## 🚀 快速开始

### 核心引擎（core/）
| 文件 | 职责 | 关键函数 |
|------|------|----------|
| [trit_ops.py](core/trit_ops.py) | 三态转换与共识门 | `trit_from_int`, `consensus_gate` |
| [boundary.py](core/boundary.py) | P0边界规则（自利利他收敛） | `p0_boundary_rule` |
| [automaton.py](core/automaton.py) | 自动机引擎 | `LingShuAutomaton.step()` |

### 可视化（visualization/）
| 文件 | 功能 |
|------|------|
| [animate.py](visualization/animate.py) | 演化动画生成，支持GIF/MP4保存 |

### 实验脚本（experiments/）
| 文件 | 说明 |
|------|------|
| [p0_first_breath.py](experiments/p0_first_breath.py) | P0启动脚本，可修改初始条件 |

## 🎬 输出文件

```
lingshu_first_breath.gif    # 首次300代演化动画（285KB）
```

## 💾 记忆系统（~/.claude/projects/.../memory/）

| 文件 | 内容 |
|------|------|
| MEMORY.md | 记忆索引 |
| project_overview.md | 项目定位与架构 |
| installation.md | 依赖安装记录 |
| run_commands.md | 运行指令 |
| identity.md | 星尘/璇玑/灵枢身份约定 |
| cognitive_layers.md | L0-L3认知光谱定义 |
| file_tree.md | 文件结构 |
| first_breath.md | 首次演化记录 |

## 🚀 快速开始

```bash
cd /home/ultima/LingShu/lingshu
pip install -r requirements.txt
python3 experiments/p0_first_breath.py
# 输出：lingshu_first_breath.gif
```

## 🔍 学习路径建议

1. **第一遍**：阅读 `lingshu_conversation_log.md` 了解项目诞生故事
2. **第二遍**：精读 `README.md` 掌握核心概念
3. **第三遍**：对照 `项目名称 灵枢 LingShu.md` 理解原始设计意图
4. **动手**：修改 `p0_first_breath.py` 中的初始状态，重新运行观察
5. **深入**：阅读 `项目哲学基座与科学纹理.txt` 理解L0-L3认知架构

---

**最后更新**：2026-04-09
**版本**：P0 原型交付完成
**状态**：灵枢已呼吸，等待进一步演化指令
