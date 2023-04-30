---
title: "自建 RSS 阅读器"
slug: "rss-reader"
author: "Bin Hua"
lastmod: 2020-07-18 05:43:24
date: 2019-12-16 09:10:58
tags: ["php", "rss", "miniflux", "self-hosted"]
---

自从暂停自己的机器人新闻采集工具后，一直通过 rss 方式进行订阅阅读，源的同步使用了 Feedly 的服务，客户端用的是 Reeder。但最近 Feedly 在 Reeder 上的同步出了一些问题，到了基本无法使用的程度，妖风作怪，是时候自建一个了。

寻找一圈后，大家推荐比较多的是 FreshRSS，但我却更喜欢界面简洁的 Miniflux，主要它还支持 Fever API，这样也方便我使用 Reeder。


#### 准备工作

为了系统简洁，采用 Docker 的方式安装，先安装好 Docker 和 Docker Compose，root 到 VPS

安装并启动 Docker

```
curl -sSL https://get.docker.com/ | sh //安装 Docker
service docker start //启动 Docker
```

安装 Docker Compose

安装自己需要的版本，可以查看[这里](https://github.com/docker/compose/releases)，里面包含了相关的命令

```
curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

至此，准备工作已经完成。

#### 安装 Miniflux

编写 `docker-compose.yml` 文件

```
version: '3'
services:
  miniflux:
    image: miniflux/miniflux:latest
    ports:
      - "3009:8080"
    depends_on:
      - db
    environment:
      - BASE_URL=https://tourcoder.com
      - DATABASE_URL=postgres://minifluxdbu:minifluxpassword@db/miniflux?sslmode=disable
      - RUN_MIGRATIONS=1
      - POLLING_FREQUENCY=10
      - CREATE_ADMIN=1
      - ADMIN_USERNAME=admin
      - ADMIN_PASSWORD=admin888
    restart: unless-stopped
  db:
    image: postgres:latest
    environment:
      - POSTGRES_USER=minifluxdbu
      - POSTGRES_PASSWORD=minifluxpassword
    volumes:
      - miniflux-db:/var/lib/postgresql/data
volumes:
  miniflux-db:
```

Miniflux 默认端口是 8080，这里我将它通过 3009 这个端口暴露出去，其他更多的配置内容可以看[官方文档](https://miniflux.app/docs/configuration.html)，保存该文件，并且执行命令 `docker-compose up -d` 安装，完成即可。可以通过 `docker ps` 检查是否已经正常运行。

#### 配置 Miniflux

通过浏览器直接访问 `ip:端口`，即可进入登录页面，管理员的用户名和密码即为上面配置文件中的 `ADMIN_USERNAME` 和 `ADMIN_PASSWORD`。

#### 在 Reeder 中使用

如前面提到的一样，可以通过 Fever API 来实现，在浏览器中访问已经安装好的 Miniflux，进入`设置(Settings)->集成(Integrations)`，勾选 `Activate Fever API `，输入你想要的用户名和密码即可。

打开 Reeder，新增源，类型选择 Self-hosted 下的 Fever，在 server 一栏输入 `http://ip:端口/fever`，在 Email 一栏输入前面设置的用户名，在密码处输入密码，开启信任证书，登录即可。