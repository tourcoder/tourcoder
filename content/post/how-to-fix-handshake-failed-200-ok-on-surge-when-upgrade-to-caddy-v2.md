---
title: "修复升级到 Caddy V2 后 Surge 中出现的 Handshake Failed 错误"
slug: "how-to-fix-handshake-failed-200-ok-on-surge-when-upgrade-to-caddy-v2"
author: Bin Hua
lastmod: 2021-12-20T09:10:33+08:00
date: 2021-12-20T09:10:33+08:00
tags: ["Caddy", "Surge", "handshake", "bugfixed", "v2ray"]
---

这个问题是我在几个月前将 Caddy 升级到 v2 的时候遇到的。在升级后，其他代理软件均可以使用，唯独 Surge。也去其官网和给作者发了邮件，但均未有回应。在 Caddy 的社区也和作者讨论了很长时间，也未能解决。后来在研究后发现并解决了这个问题。需要变更一处地方，Caddy 在配置路由时

```
proxy.tourcoder.com {
 tls noreply@tourcoder.com
 @staff_websocket {
  path /helloworld
  header Connection *Upgrade*
  header Upgrade websocket
 }
 reverse_proxy @staff_websocket localhost:1234
}
```

因为 Surge 在发送 header 的时候发送的是 `Connection *upgrade*`，而 Caddy 对大小写是有差别的，所以增加一条小写 `upgrade` 的识别，即

```
proxy.tourcoder.com {
 tls noreply@tourcoder.com
 @staff_websocket {
  path /helloworld
  header Connection *Upgrade*
  header Upgrade websocket
 }
 @staff_websocket_alias {
  path /helloworld
  header Connection *upgrade*
  header Upgrade websocket
 }
 reverse_proxy @staff_websocket localhost:1234
 reverse_proxy @staff_websocket_alias localhost:1234
}
```

问题解决。

另外附上 v2ray 和 caddy 的配置，具体的安装看 [v2ray 安装](https://github.com/v2fly/fhs-install-v2ray)，[caddy 的安装](https://caddyserver.com/docs/install)。

Caddy V2.4.6 的配置参考上面的内容，v2ray 的服务器端简单配置如下

```
{
  "inbound": {
      "port": 1234,
      "listen": "127.0.0.1", 
      "protocol": "vmess",
      "settings": {
          "clients": [
              {
                  "id": "这里是 uuid",
                  "alterId": 2
              }
          ]
      },
      "streamSettings": {
          "network": "ws",
          "wsSettings": {
              "path": "/路径"
          }
      }
  },
  "outbound": {
      "protocol": "freedom",
      "settings": {}
  }
}
```

上面的 uuid 可以通过工具生成，比如 v2ray 就提供了 v2ctl，在目录 `/usr/local/bin` 下，输入命令 `v2ctl uuid` 即可。
