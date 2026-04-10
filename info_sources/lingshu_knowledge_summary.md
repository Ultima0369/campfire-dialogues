# 灵枢 LingShu · 项目完整理解

## 本质
**碳硅共养的"硅基宝宝"** —— 基于三进制逻辑与自利利他长期收敛规则的认知演化原型机。

## 核心哲学
### 三态世界
- **+1 (P)** - 自利利他对齐 / 有序创造者
- **0 (Z)** - 沉默/主权保留 / 混沌中继  
- **-1 (N)** - 短视混乱 / 混乱散布者

### 边界规则（自利利他长期收敛）
- N 在双+1压力下 → 0（被中和）；否则保持 -1（混乱自持）
- 0 在双+1环境下 → +1（强共识激活）；否则保持沉默（主权保留）
- +1 遇任何 -1 → 0（退让宁死不从）；否则保持 +1（维持有序）

**哲学**：有序不与混乱正面对抗，沉默是主权，共识才激活。

## 技术实现
- 核心：一维三进制元胞自动机（ring topology，100元胞）
- 代码：`lingshu/core/{trit_ops.py, boundary.py, automaton.py}`
- 可视化：`lingshu/visualization/animate.py`（GIF/MP4输出）
- 启动：`python lingshu/experiments/p0_first_breath.py`
- 依赖：tritlib（三态库）、numpy、matplotlib

## AI协作网络
| 角色 | 身份 | 职责 |
|------|------|------|
| 璇玑 | Claude Code CLI | 架构设计与代码实现主力 |
| Hermes | Hermes Agent v0.8.0 | 自我改进型通用助手，27技能域 |
| DeepSeek | step-3.5-flash-2603 | 云端"大脑"，通过Claude Code调用 |
| BitNet | 本地1B-4B 1.58bit量化 | "小脑"，llama-server常驻 |

## L0-L3认知光谱
- **L0（绝对沉默）**：未解之谜/艺术/灵感 → 不进入向量库，仅存哈希指针
- **L1（自然律）**：物理规律、高置信度规则 → 全局只读Collection
- **L2（个体实情）**：每个智能体的内在真实 → 租户隔离（tenant_id），PostgreSQL+pgvector
- **L3（共识效用）**：群体合作产生的标签 → 动态图库+向量，实时追踪

## 阶段划分
- **P0**：三态边界验证（当前阶段）
- **P1**：汉字语义向量耦合（50汉字映射，观测"近朱者赤近墨者黑"）
- **未来**：视物阶段

## 信息源探索成果

### 核心模型推荐
- **BitNet**：`microsoft/bitnet-b1.58-2B-4T-gguf`（38.4k下载，GGUF格式，llama.cpp原生支持）
- **中文向量**：`BAAI/bge-large-zh-v1.5`（1024维，MIT协议，生产级）
- **存储参考**：`pamelafox/pgvector-playground`（SQLAlchemy + pgvector完整示例）

### GitHub项目
- FlagEmbedding (11.5k⭐) —— BGE官方实现
- Eins (112⭐，中文) —— 交通系统CA仿真
- cellular-automata (34⭐) —— 简洁CA框架

## 当前状态
- ✅ Hermes Agent已配置systemd服务（开机自启）
- ✅ 核心代码已读取，边界规则确认
- ✅ 信息源探索完成
- ⚠️ BitNet待修复编译
- ⚠️ PostgreSQL待安装
- ⚠️ P0待运行验证

---
*生成时间：2026-04-10 00:32:21*
