# Hermes Agent 快速参考

## 📖 什么是 Hermes Agent？

Hermes Agent 是由 Nous Research 开发的自我改进型 AI 助手，具备工具调用能力，可创建和改进技能，支持多平台（终端、Telegram、Discord 等）。

**版本**: v0.8.0 (2026.4.8)
**模型**: step-3.5-flash-2603 (StepFun 云端)
**位置**: `/home/ultima/LingShu/hermes/`

## 🚀 快速启动

### 方法1：启动脚本（推荐）

```bash
cd /home/ultima/LingShu
./hermes/start_hermes.sh
```

### 方法2：直接命令

```bash
# 加载环境变量
source /home/ultima/LingShu/hermes/global_env.sh

# 启动交互模式
hermes

# 单次查询模式
hermes chat -q "你的问题"
```

### 方法3：恢复会话

```bash
# 恢复最近会话
hermes -c

# 恢复指定会话
hermes -r "session_name_or_id"
```

## 🛠️ 常用命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `hermes` | 启动交互式聊天 | `hermes` |
| `hermes chat -q "问题"` | 单次查询（非交互） | `hermes chat -q "解释三进制"` |
| `hermes status` | 查看状态 | `hermes status` |
| `hermes doctor` | 运行诊断 | `hermes doctor` |
| `hermes version` | 显示版本 | `hermes -V` |
| `hermes config` | 查看/编辑配置 | `hermes config` |
| `hermes skills` | 管理技能 | `hermes skills list` |
| `hermes sessions` | 管理会话 | `hermes sessions list` |
| `hermes -c` | 继续上次会话 | `hermes -c` |

## 🔧 配置管理

### 环境变量文件

```
/home/ultima/LingShu/hermes/
├── .env              # 主配置（API密钥、模型）
├── global_env.sh     # Shell加载脚本
├── setup_env.sh      # 交互式配置向导
└── start_hermes.sh   # 启动包装器
```

### 查看当前配置

```bash
source hermes/global_env.sh
hermes config
```

### 修改配置

```bash
# 编辑.env文件
nano /home/ultima/LingShu/hermes/.env

# 或使用hermes config交互编辑器
hermes config
```

## 🧠 可用技能（27个技能域）

Hermes 已加载以下技能，可直接在对话中调用：

| 技能域 | 说明 | 对 LingShu 的价值 |
|--------|------|-------------------|
| `autonomous-ai-agents` | AI代理协作 | 多代理系统设计 |
| `creative` | 创意生成 (p5js, manim-video) | 可视化、动画制作 |
| `data-science` | 数据科学 (Jupyter) | 演化数据分析 |
| `devops` | 运维部署 | 项目部署、监控 |
| `github` | GitHub集成 | 代码管理 |
| `mlops` | 机器学习运维 | 模型训练 |
| `productivity` | 生产力工具 | 笔记、文档 |
| `research` | 研究辅助 (ArXiv) | 文献调研 |
| `software-development` | 软件开发 | **核心：plan, code-review, debug** |
| `...` | 共27个 | ... |

查看完整技能列表：
```bash
hermes skills list
```

## 💬 对话示例

### 询问 LingShu 项目相关问题

```
用户: 请 review 一下 core/boundary.py 的边界规则实现是否符合自利利他长期收敛原则。

Hermes: [读取文件] → [分析规则] → [反馈意见]
```

### 请求代码协助

```
用户: 帮我写一个函数，统计每代三态(+1/0/-1)的数量变化。

Hermes: [生成代码] → [插入 automaton.py] → [验证逻辑]
```

### 研究辅助

```
用户: 搜索关于一维三进制元胞自动机的相关论文。

Hermes: [使用 research/arxiv 技能] → [返回文献列表]
```

## 📂 文件位置

### Hermes 自身文件

| 路径 | 用途 |
|------|------|
| `/home/ultima/LingShu/hermes/` | Hermes 源码与配置 |
| `~/.hermes/` | Hermes 数据目录（会话、记忆、日志） |
| `~/.hermes/sessions/` | 会话历史 JSON |
| `~/.hermes/memories/` | 长期记忆 |
| `~/.hermes/logs/` | 运行日志 |
| `~/.hermes/skills/` | 已安装技能（27个域） |

### LingShu 项目文件

| 路径 | 用途 |
|------|------|
| `/home/ultima/LingShu/lingshu/` | 灵枢核心代码 |
| `/home/ultima/LingShu/lingshu_first_breath.gif` | 首次演化动画 |

## 🔐 安全与权限

### 当前配置

- ✅ API 密钥已配置（StepFun）
- ✅ 直连模式（无代理配置）
- ⚠️ YOLO 模式启用（绕过危险命令确认）
- ❌ Sudo 禁用（无法执行特权操作）

### 重要警告

1. **API 密钥保密**: `.env` 文件包含敏感信息，勿提交到版本控制
2. **YOLO 模式**: `HERMES_YOLO_MODE=1` 已设置，Hermes 会直接执行危险操作（git push, rm 等），使用需谨慎
3. **代码执行**: Hermes 可执行任意代码，仅信任的会话中启用

## 🐛 故障排除

### Hermes 命令未找到

```bash
# 确保环境变量已加载
source /home/ultima/LingShu/hermes/global_env.sh

# 或使用完整路径
~/.local/bin/hermes --version
```

### API 连接失败

检查：
```bash
# 1. 验证 API 密钥
cat /home/ultima/LingShu/hermes/.env | grep API_KEY

# 2. 测试网络连接
curl -I https://api.stepfun.com/step_plan/v1/models
```

### 技能不可用

某些技能需额外 API 密钥：
```bash
# 查看缺失的配置
hermes doctor | grep "missing"

# 补充配置（按需）
export EXA_API_KEY="..."
export FIRECRAWL_API_KEY="..."
```

## 📚 文档资源

| 文档 | 路径 |
|------|------|
| Hermes 部署记录 | `/home/ultima/LingShu/hermes/DEPLOYMENT.md` |
| Hermes 官方 README | `/home/ultima/LingShu/hermes/README.md` |
| Hermes 发布说明 | `/home/ultima/LingShu/hermes/RELEASE_v0.8.0.md` |
| 技能列表 | `hermes skills list` |
| 配置文档 | `hermes config --help` |

## 🔄 与灵枢项目的协作

### 典型工作流

1. **启动 Hermes**（在 LingShu 项目上下文）
   ```bash
   cd /home/ultima/LingShu
   ./hermes/start_hermes.sh
   ```

2. **询问项目相关问题**
   ```
   用户: 帮我优化 boundary.py 的规则，使收敛更快。
   ```

3. **Hermes 分析并修改代码**
   - 读取文件
   - 提出修改建议
   - 直接编辑文件（需确认）

4. **验证修改**
   ```bash
   python3 lingshu/experiments/p0_first_breath.py
   ```

5. **记录会话**（自动保存在 `~/.hermes/sessions/`）

### 会话恢复

下次继续工作时：
```bash
hermes -c "LingShu boundary rule optimization"
```

---

**最后更新**: 2026-04-09
**维护者**: 璇玑
**状态**: ✅ 已部署，可随时调用
