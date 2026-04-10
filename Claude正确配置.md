# Claude Code 正确配置文档
**生成时间**: 2026-04-10  
**Claude Code 版本**: 2.1.98  
**项目**: LingShu 三进制认知演化原型机  
**状态**: ✅ 已通过 Clash Verge 香港代理测试

---

## 📋 目录

1. [版本信息](#1-版本信息)
2. [核心 API 配置](#2-核心-api-配置)
3. [主配置文件](#3-主配置文件-settingsjson)
4. [本地覆盖配置](#4-本地覆盖配置-settingslocaljson)
5. [启动脚本](#5-启动脚本-start-claudesh)
6. [项目环境变量](#6-项目环境变量-env)
7. [当前生效配置](#7-当前生效配置总结)
8. [权限配置](#8-权限配置)
9. [代理配置说明](#9-代理配置说明)
10. [快速验证](#10-快速验证命令)

---

## 1. 版本信息

| 项目 | 值 |
|------|-----|
| Claude Code CLI | 2.1.98 |
| 模型 | step-3.5-flash-2603 |
| API 提供商 | StepFun (stepfun.com) |
| 工作目录 | /home/ultima/LingShu |

---

## 2. 核心 API 配置

### 2.1 API 密钥

```json
{
  "ANTHROPIC_AUTH_TOKEN": "5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE"
}
```

⚠️ **安全提示**: 此令牌已暴露在文档中，生产环境应使用环境变量或密钥管理器。

### 2.2 API 端点

| 配置项 | settings.json | settings.local.json | 说明 |
|--------|--------------|---------------------|------|
| `ANTHROPIC_BASE_URL` | `https://api.stepfun.com/step_plan` | `https://api.stepfun.com/step_plan/v1` | ✅ 使用 `/step_plan` (无 `/v1` 后缀) |
| `ANTHROPIC_MODEL` | `step-3.5-flash-2603` | `step-3.5-flash-2603` | StepFun 定制模型 |

**正确配置**: `settings.json` 的 `ANTHROPIC_BASE_URL` 应为 `https://api.stepfun.com/step_plan`（无 `/v1` 后缀）。

---

## 3. 主配置文件 (`~/.claude/settings.json`)

**文件路径**: `/home/ultima/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE",
    "ANTHROPIC_BASE_URL": "https://api.stepfun.com/step_plan",
    "ANTHROPIC_MODEL": "step-3.5-flash-2603"
  },
  "skipDangerousModePermissionPrompt": true
}
```

**说明**:
- 这是 Claude Code 的主配置文件
- 环境变量优先于项目 `.env` 文件
- 当前**未配置代理**（代理通过启动脚本注入）
- `skipDangerousModePermissionPrompt`: 跳过危险模式确认

---

## 4. 本地覆盖配置 (`~/.claude/settings.local.json`)

**文件路径**: `/home/ultima/.claude/settings.local.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE",
    "ANTHROPIC_BASE_URL": "https://api.stepfun.com/step_plan/v1",
    "ANTHROPIC_MODEL": "step-3.5-flash-2603",
    "HTTP_PROXY": "http://127.0.0.1:7890",
    "HTTPS_PROXY": "http://127.0.0.1:7890",
    "ALL_PROXY": "http://127.0.0.1:7890",
    "NO_PROXY": "localhost,127.0.0.1,localaddress,.local,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,api.stepfun.com,.stepfun.com,stepfun.com",
    "no_proxy": "localhost,127.0.0.1,localaddress,.local,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,api.stepfun.com,.stepfun.com,stepfun.com",
    "PROXY_MODE": "smart"
  },
  "skipAutoPermissionPrompt": true,
  "permissions": {
    "defaultMode": "auto",
    "autoMode": {
      "allow": [
        "Bash", "Glob", "Grep", "Read", "Write", "Edit", "MultiEdit",
        "TaskCreate", "TaskUpdate", "TaskGet", "TaskList", "Agent",
        "WebFetch", "WebSearch", "Skill", "AskUserQuestion",
        "ExitPlanMode", "EnterPlanMode", "ExitWorktree", "EnterWorktree"
      ],
      "soft_deny": [],
      "environment": []
    }
  }
}
```

**⚠️ 注意**:
- `HTTP_PROXY` 端口为 `7890`（这是**旧配置**，当前 v2ray 已移除，此端口不可用）
- **实际使用中**代理配置由 `start-claude.sh` 注入（端口 `25841`）
- 此文件中的代理配置**不会自动生效**，因为启动脚本会覆盖环境变量

---

## 5. 启动脚本 (`start-claude.sh`)

**文件路径**: `/home/ultima/LingShu/start-claude.sh`

```bash
#!/bin/bash
# Claude Code 启动脚本 - 统一代理配置

echo "=== 启动 Claude Code（统一代理配置）==="

# 代理设置 - 使用 Clash Verge（混合端口 25841，支持 HTTP 和 SOCKS5）
export HTTP_PROXY=http://127.0.0.1:25841
export HTTPS_PROXY=http://127.0.0.1:25841
# SOCKS5 备用：export ALL_PROXY=socks5://127.0.0.1:7898

# 直连白名单（不走代理的地址）
export NO_PROXY=localhost,127.0.0.1,localaddress,.local,\
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,\
api.stepfun.com,.stepfun.com,stepfun.com
export no_proxy="$NO_PROXY"

echo "环境变量已设置："
echo "  HTTP_PROXY=$HTTP_PROXY"
echo "  HTTPS_PROXY=$HTTPS_PROXY"
echo "  NO_PROXY=$NO_PROXY"
echo ""

echo "启动 Claude Code..."
cd /home/ultima/LingShu
claude --dangerously-skip-permissions
```

**✅ 这是当前生效的正确配置**。

**关键点**:
- 使用 Clash Verge **mixed-port 25841**（HTTP 代理）
- 备用 SOCKS5: `127.0.0.1:7898`
- NO_PROXY 白名单包含 `api.stepfun.com`（不走代理，直连）
- 工作目录切换到项目根目录 `/home/ultima/LingShu`

---

## 6. 项目环境变量 (`.env`)

**文件路径**: `/home/ultima/LingShu/.env`

```bash
# LingShu 项目环境配置
# 统一的代理配置

HTTP_PROXY=http://127.0.0.1:7890      # ⚠️ 旧端口，已废弃
HTTPS_PROXY=http://127.0.0.1:7890     # ⚠️ 旧端口，已废弃
ALL_PROXY=http://127.0.0.1:7890       # ⚠️ 旧端口，已废弃

NO_PROXY=localhost,127.0.0.1,localaddress,.local,\
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,\
api.stepfun.com,.stepfun.com,stepfun.com

no_proxy=$NO_PROXY
PROXY_MODE=smart

# StepFun API 配置
ANTHROPIC_AUTH_TOKEN=5cFLQYW47c5DweJ4KdZxtRCYcI5TORg95BtnRPKTmuxgrzNKARKCt5PZ3zyGMo8RE
ANTHROPIC_BASE_URL=https://api.stepfun.com/step_plan/v1  # ⚠️ 含 /v1 后缀
ANTHROPIC_MODEL=step-3.5-flash-2603
```

**⚠️ 此文件已过时**:
- 代理端口 `7890` 已不可用（v2ray 已移除，Clash Verge 使用 `25841`）
- `ANTHROPIC_BASE_URL` 包含 `/v1` 后缀（应为 `/step_plan`）

**当前实际使用**: `start-claude.sh` 中的配置优先于 `.env` 文件。

---

## 7. 当前生效配置总结

| 配置项 | 实际值 | 来源 |
|--------|--------|------|
| `ANTHROPIC_AUTH_TOKEN` | `5cFLQYW47c...` | settings.json |
| `ANTHROPIC_BASE_URL` | `https://api.stepfun.com/step_plan` | settings.json ✅ |
| `ANTHROPIC_MODEL` | `step-3.5-flash-2603` | settings.json |
| `HTTP_PROXY` | `http://127.0.0.1:25841` | start-claude.sh ✅ |
| `HTTPS_PROXY` | `http://127.0.0.1:25841` | start-claude.sh ✅ |
| `NO_PROXY` | `localhost,127.0.0.1,...,api.stepfun.com` | start-claude.sh |
| `no_proxy` | `$NO_PROXY` | start-claude.sh |

**配置优先级**（从高到低）:
1. **启动脚本环境变量** (`start-claude.sh`) → **当前生效**
2. `settings.local.json` → 部分被覆盖
3. `settings.json` → 仅 API 配置生效
4. 项目 `.env` → 未使用（被启动脚本覆盖）

---

## 8. 权限配置

### 8.1 自动权限模式

```json
{
  "defaultMode": "auto",
  "autoMode": {
    "allow": [
      "Bash", "Glob", "Grep", "Read", "Write", "Edit", "MultiEdit",
      "TaskCreate", "TaskUpdate", "TaskGet", "TaskList", "Agent",
      "WebFetch", "WebSearch", "Skill", "AskUserQuestion",
      "ExitPlanMode", "EnterPlanMode", "ExitWorktree", "EnterWorktree"
    ],
    "soft_deny": [],
    "environment": []
  }
}
```

### 8.2 跳过确认

- `skipDangerousModePermissionPrompt`: `true` → 跳过危险模式确认
- `skipAutoPermissionPrompt`: `true` → 自动批准工具调用

---

## 9. 代理配置说明

### 9.1 当前代理架构

```
Clash Verge (PID 7092, 7229)
    ↓ mixed-port: 25841 (HTTP 代理)
    ↓
香港 Trojan 节点 (xg.xgacc.top:43001-43007)
    ↓
出口 IP: 45.39.198.14 (香港)
```

### 9.2 代理端口映射

| 端口 | 协议 | 用途 | 状态 |
|------|------|------|------|
| 25841 | HTTP | Claude Code 主代理 | ✅ 使用中 |
| 7898 | SOCKS5 | 备用代理 | ✅ 可用 |
| 7895 | redir | 透明代理 | ✅ 可用 |
| 7890 | HTTP | **旧配置（已废弃）** | ❌ 不可用 |

### 9.3 香港节点列表

| 节点 | 服务器 | 端口 | 类型 |
|------|--------|------|------|
| HK-01 | xg.xgacc.top | 43001 | Trojan |
| HK-02 | xg.xgacc.top | 43002 | Trojan |
| HK-03 | xg.xgacc.top | 43003 | Trojan |
| HK-04 | xg.xgacc.top | 43004 | Trojan |
| HK-07 | xg.xgacc.top | 43007 | Trojan |

### 9.4 代理路由规则

- **国内直连**: `api.stepfun.com` 在白名单中，但实测走代理也能通
- **海外代理**: GitHub、Google、AI 服务等走香港节点
- **NO_PROXY**: 本地地址、内网、StepFun API 域名

---

## 10. 快速验证命令

```bash
# 1. 检查 Claude Code 版本
claude --version
# 输出: 2.1.98 (Claude Code)

# 2. 验证当前生效的代理配置
env | grep -i proxy
# 应显示:
# HTTP_PROXY=http://127.0.0.1:25841
# HTTPS_PROXY=http://127.0.0.1:25841

# 3. 测试 Claude Code 连接（通过代理）
echo "test" | claude
# 应正常响应，无连接错误

# 4. 测试代理出口 IP
curl -x http://127.0.0.1:25841 https://httpbin.org/ip
# 应返回: {"origin": "45.39.198.14"} (香港)

# 5. 验证香港节点状态
curl --unix-socket /tmp/verge/verge-mihomo.sock http://localhost/proxies \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('HK-01:', d['proxies']['HK-01']['alive'])"
# 应返回: HK-01: True

# 6. 查看 Clash Verge 状态
systemctl --user status clash-verge.service
# 或
ps aux | grep -E "clash-verge|verge-mihomo" | grep -v grep

# 7. 重载 Clash Verge 配置（修改配置后）
echo 'reload' | socat - /tmp/verge/verge-mihomo.sock
```

---

## 11. 启动方式

```bash
# 方式1: 使用启动脚本（推荐，自动配置代理）
cd /home/ultima/LingShu
./start-claude.sh

# 方式2: 直接运行（需手动设置环境变量）
export HTTP_PROXY=http://127.0.0.1:25841
export HTTPS_PROXY=http://127.0.0.1:25841
claude

# 方式3: 临时使用（不修改任何文件）
HTTP_PROXY=http://127.0.0.1:25841 claude --print "hello"
```

---

## 12. 配置文件位置索引

| 文件 | 路径 | 说明 |
|------|------|------|
| 主配置 | `~/.claude/settings.json` | Claude Code 主配置（无代理） |
| 本地覆盖 | `~/.claude/settings.local.json` | 本地配置（含旧代理设置） |
| 启动脚本 | `/home/ultima/LingShu/start-claude.sh` | **当前生效配置** |
| 项目环境 | `/home/ultima/LingShu/.env` | 项目环境变量（已过时） |
| Clash 配置 | `~/.local/share/.../clash-verge.yaml` | Clash Verge 代理配置 |
| 香港节点源 | `~/桌面/OpenHarness/clash-config/config.yaml` | 原始香港节点配置 |
| 逆向报告 | `~/桌面/XIGUA_PROXY_EXTRACTION_REPORT.md` | 节点提取报告 |
| 代理文档 | `/home/ultima/代理.txt` | 完整代理配置文档 |

---

## 13. 待清理项

以下配置已过时，建议清理或更新：

| 文件 | 问题 | 建议 |
|------|------|------|
| `~/.claude/settings.local.json` | 代理端口 `7890` 已失效 | 更新为 `25841` 或删除代理配置 |
| `/home/ultima/LingShu/.env` | 代理端口 `7890`，API URL 含 `/v1` | 同步 `start-claude.sh` 配置 |
| `start-claude.sh` 注释的 SOCKS5 | 备用方案未启用 | 保留注释即可 |

---

## 14. 更新记录

| 日期 | 操作 | 说明 |
|------|------|------|
| 2026-04-10 11:20 | 应用 Clash Verge 代理 | 端口 25841，香港节点 |
| 2026-04-10 11:25 | 香港节点加载验证 | 5个 Trojan 节点全部 alive |
| 2026-04-10 11:29 | 创建开机启动 | systemd 用户服务 + 桌面自启 |
| 2026-04-10 11:35 | v2ray 完全移除 | 仅保留 Clash Verge |
| 2026-04-10 11:40 | 文档化当前配置 | 本文档生成 |

---

## 15. 故障排查

### 问题1: Claude Code 连接失败

```bash
# 检查代理是否运行
ps aux | grep -E "clash-verge|verge-mihomo" | grep -v grep

# 检查端口
ss -tlnp | grep 25841

# 测试代理
curl -x http://127.0.0.1:25841 https://api.stepfun.com -I

# 查看 Clash 节点状态
curl --unix-socket /tmp/verge/verge-mihomo.sock http://localhost/proxies \
  | python3 -m json.tool | grep -E '"alive"|"name"'
```

### 问题2: 环境变量未生效

```bash
# 确保通过 start-claude.sh 启动
source /home/ultima/LingShu/start-claude.sh
env | grep proxy
```

### 问题3: 香港节点不可用

```bash
# 检查节点延迟
curl --unix-socket /tmp/verge/verge-mihomo.sock http://localhost/proxies \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(k, v.get('delay','N/A')) for k,v in d['proxies'].items() if 'HK' in k]"

# 手动切换节点
curl -X PUT -d '{"name":"HK-02"}' http://127.0.0.1:9097/proxies/PROXY
```

---

**文档维护**: 每次修改 Claude Code 配置后，请更新此文档。  
**最新检查**: 2026-04-10 11:40 CST  
**验证状态**: ✅ 所有配置已测试通过
