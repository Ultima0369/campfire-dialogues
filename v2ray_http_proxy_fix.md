# ⚠️ 已过时 - V2Ray 修复方案（历史文档）

**状态**: v2ray 已完全移除（2026-04-10），Clash Verge 取代其功能。

当前系统使用 **Clash Verge** 作为唯一代理软件，混合端口 `25841`（HTTP）。本文件内容仅作历史参考，**请勿使用**。

## 修改后的配置文件

```json
{
  "inbounds": [
    {
      "port": 10086,
      "protocol": "vmess",
      "settings": {
        "clients": [
          {
            "id": "155b2a00-9f3c-4e64-9d84-c6498104332d",
            "level": 1,
            "alterId": 64
          }
        ]
      }
    },
    {
      "port": 7890,
      "protocol": "http",
      "settings": {
        "timeout": 360
      }
    },
    {
      "port": 1080,
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": true,
        "ip": "127.0.0.1"
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {}
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ]
}
```

## 操作步骤

1. 备份原配置：
```bash
sudo cp /etc/v2ray/config.json /etc/v2ray/config.json.bak
```

2. 用 sudo 编辑配置文件：
```bash
sudo nano /etc/v2ray/config.json
```
或使用 visudo 配置的无密码编辑方式。

3. 替换为上面的配置，保存。

4. 重启 v2ray 服务：
```bash
sudo systemctl restart v2ray
```

5. 验证端口：
```bash
ss -tlnp | grep -E "7890|1080"
```

6. 测试代理：
```bash
curl -x http://127.0.0.1:7890 https://api.stepfun.com
```

7. Claude Code 将自动使用 7890 HTTP 代理。

---

## 如果你没有 sudo 密码

**替代方案：使用 simple-tproxy 或 tinyproxy 在用户空间运行代理**

```bash
# 安装 tinyproxy（可能需要 sudo）
sudo apt install tinyproxy

# 或使用 Python 启动本地代理
pip install tinyproxy
```

或者，我可以帮你修改 `start-claude.sh` 直接连接（不经过代理），如果网络环境允许直连的话。
