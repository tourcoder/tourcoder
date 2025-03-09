---
title: "基于 Radicale 搭建一个自用的 CalDev 服务"
slug: "how-to-build-a-caldav-server-based-on-radicale"
author: "Bin Hua"
date: 2025-03-09T09:43:33Z
tags: ["selfhosting", "radicale", "caldav"]
draft: false
---

最近日常用的 Google Calendar 的同步总是莫名其妙的出现问题，又不想用 iCloud 的，索性自建一个玩玩。在和 AI 聊了一会后，决定试试 Radicale 这个 Debian 自带的。

### 安装

Debian 上安装非常简单，直接执行 `sudo apt install radicale -y` 即可。执行命令 `radicale` 即运行了这个服务。

### 配置

配置文件在 `/etc/radicale/config`，基础配置是

```
[server]
# 监听所有 IP
hosts = 0.0.0.0:5232

[auth]
# 启用用户名/密码认证
type = htpasswd
htpasswd_filename = /etc/radicale/users
htpasswd_encryption = bcrypt

[rights]
type = owner_only
```

在 auth 这一块，创建用户

```
sudo apt install apache2-utils  # 安装 htpasswd 工具
htpasswd -B -c /etc/radicale/users user1
htpasswd -B /etc/radicale/users user2
```

这里的参数 `-c` 表示是创建新文件，如果这个文件存在的话，则不用增加该参数。

在 rights 这一块， type 类型不同，权限不同，owner_only 是每个人只能访问自己的日历。如果需要更为详细的配置，可以查看 [Radicale 官网](https://radicale.org/v3.html)

到此，一个 Caldav 服务就搭建完成了。当然现在是通过 ip 和 port 访问的，可以用 caddy，nginx 等反代。

### 注意点

- `/.Radicale.lock` 文件无法访问的问题

执行 `ls -lah /var/lib/radicale/collections/` 查看文件权限，执行 `ps aux | grep radicale` 查看 Radicale 的权限，两个的运行用户是否一致。不一致则改一下

```
sudo chown -R the_user:the_user /var/lib/radicale/collections
sudo chmod -R 750 /var/lib/radicale/collections
```