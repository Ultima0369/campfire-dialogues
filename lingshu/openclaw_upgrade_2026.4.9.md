# OpenClaw 升级记录

**日期：** 2026-04-10  
**操作：** 版本 2026.4.8 → 2026.4.9  
**备份位置：** `/home/ultima/.nvm/versions/node/v24.14.1/lib/node_modules/openclaw-backup-2026.4.8.tar.gz`

---

## 升级前状态

| 项目 | 值 |
|------|-----|
| 旧版本 | OpenClaw 2026.4.8 (9ece252) |
| 安装路径 | `/home/ultima/.nvm/versions/node/v24.14.1/lib/node_modules/openclaw/` |
| 配置目录 | `~/.openclaw/` (保留，未删除) |
| 主要模型 | StepFun Step-3.5-Flash-2603 |
| 网关端口 | 18789 (loopback) |

---

## 升级操作

```bash
# 1. 备份
cd /home/ultima/.nvm/versions/node/v24.14.1/lib/node_modules/
tar czf openclaw-backup-2026.4.8.tar.gz openclaw/

# 2. 升级
npm install -g openclaw@latest

# 输出摘要：
# added 23 packages, removed 230 packages, and changed 686 packages
```

---

## 升级后验证

```bash
$ openclaw --version
OpenClaw 2026.4.9 (0512059)

$ openclaw --help | head -15
🦞 OpenClaw 2026.4.9 (0512059) — More integrations than your therapist's intake form.
...
```

✅ 版本号已更新  
✅ 配置文件 `~/.openclaw/openclaw.json` 保留未变  
✅ Skills 列表正常（7/50 ready，需 setup 的 bundled skills 保持原状）

---

## 配置兼容性检查

### 保留的配置项
- `~/.openclaw/openclaw.json` — 未修改，包含 StepFun provider 设置
- `~/.openclaw/exec-approvals.json` — 执行审批 token 保持有效
- `~/.openclaw/workspace/` — 工作区保留
- `~/.openclaw/skills/` — 自定义技能保留

### 可能的变化
- **新增 Skill**：2026.4.9 版本可能新增集成（查看 `openclaw skills list` 输出）
- **Bug 修复**：不改变现有 API 行为
- **安全补丁**：无 Breaking change 预期

---

## 回滚方案（如遇问题）

```bash
# 停止当前 openclaw 进程（如果有）
pkill -f openclaw

# 恢复备份
cd /home/ultima/.nvm/versions/node/v24.14.1/lib/node_modules/
rm -rf openclaw
tar xzf openclaw-backup-2026.4.8.tar.gz

# 验证回滚版本
openclaw --version  # 应显示 2026.4.8
```

---

## 与 LingShu 集成的关联

OpenClaw 在 LingShu 架构中的定位：
- **角色**：手足工具层（Claude Code 的替代/补充）
- **当前配置**：使用 StepFun Step-3.5-Flash-2603 作为默认模型
- **集成点**：
  - 可作为 Hermes Agent 的外部工具调用者
  - 可通过 `openclaw skills` 管理 LingShu 自定义技能
  - 网关运行在 18789 端口，供本地服务连接

**待办：** 在 `待办事宜.md` 中确认 OpenClaw 升级状态。

---

**升级完成时间：** 2026-04-10 03:12 UTC  
**备份文件大小：** 276 MB  
**升级耗时：** ~1 分钟
