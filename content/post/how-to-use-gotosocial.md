---
title: "搭建自己的节点之 Gotosocial 篇"
slug: "how-to-use-gotosocial"
author: "Bin Hua"
lastmod: 2022-12-18T05:55:03Z
date: 2022-12-18T05:55:03Z
tags: ["mastodon", "twitter", "gotosocial", "elonmusk"]
---

基于三个原因，我还是决定将自己的吃饭游玩日常打卡和叨逼叨的内容转移到自己的服务器

- 我一直想把这些内容放在自己的服务器，之前自己也基于 hugo 写了个 hugo buzz(在 [GitHub](https://github.com/tourcoder/hugobuzz) 上开源了)，并和自己的博客集成，玩了一段段时间，但有些东西不是很方便，后面就没有继续做下去。

- 自从马斯克购买了推特后，推特变得越来越莫名其妙，我觉得我的推特迟早会被封号，毕竟以前也被封过一个号。

- 我还是想再次折腾下分布式社交网络的，其实之前我有折腾股一段时间的 mastodon，但对我一个个人用户来说，mastodon 实在太吃资源太重了，没有必要。碰巧又发现了轻量级的 gotosocial，索性重新折腾。

今天的主角就是 gotosocial 这个东西，关于它的介绍，可以去看其官网或者其在 GitHub 上的项目库，本文后我将附上这两个地址。

### 准备工作

- VSP: 512M / 40G / Debian 11，因为 GoToSocial 占用资源很少，这个配置足够。

- Docker: 本次我是用 Docker 的安装方式，所以，需要在服务器上安装好 Docker，一键安装 Docker 和 Docker Compose 可以用我的脚本 [Dockerman](https://github.com/tourcoder/dockerman)。

- Caddy: 我是将 GotoSocial 放在代理后面的，我用 Caddy 来对端口进行反代，当然也可以用 nginx 等。

### 安装过程

官方有相关的英文教程，具体可以看[这里](https://docs.gotosocial.org/en/latest/)，我这里用中文说下我折腾的过程

- 创建文件夹

    ```
    mkdir -p your_folder/data
    ```

- 将官方制作好的 docker-compose.yaml 文件下载下来，这是 demo 文件，可以直接在上面修改

    ```
    cd your_folder
    wget https://raw.githubusercontent.com/superseriousbusiness/gotosocial/main/example/docker-compose/docker-compose.yaml
    ```

- 修改 docker-compose.yaml 文件，我修改后的文件是这样的

    ```
    version: "3.3"

    services:
    gotosocial:
        image: superseriousbusiness/gotosocial:latest
        container_name: your_containner_name
        user: 1000:1000
        networks:
        - gotosocial
        environment:
        GTS_HOST: your_domain_name
        GTS_DB_TYPE: sqlite
        GTS_DB_ADDRESS: /gotosocial/storage/sqlite.db
        GTS_LETSENCRYPT_ENABLED: "false"
        GTS_LETSENCRYPT_EMAIL_ADDRESS: ""
        ## For reverse proxy setups:
        # GTS_TRUSTED_PROXIES: "172.x.x.x"
        ports:
        - "8080:8080"
        ## For letsencrypt:
        #- "80:80"
        ## For reverse proxy setups:
        #- "127.0.0.1:8080:8080"
        volumes:
        - ~/your_folder/data:/gotosocial/storage
        restart: "always"

    networks:
    gotosocial:
        ipam:
        driver: default
    ```

    我修改了 `container_name`，`GTS_HOST`， `ports` 和 `volumes` 的内容，跟着说明酌情修改即可。这里有个重点，`user` 的内容应该是通过 `cat /etc/passwd` 获取到的。然后用命令 `docker-compose up -d` 拉起容器。

- 配置反向代理的内容，这里将 8080 端口反代即可。

- 访问域名，这时候就会出现成功的页面。

### 用户设置

现在阶段的 gotosocial 还没有完善的网页版管理界面，需要通过命令行来进行用户的设置。

**增加用户**

```
docker exec -it your_container_name /gotosocial/gotosocial admin account create --username your_username --email your_email --password '123456'
```

当增加完用户后，即可访问前面设置的域名地址 `your_domain_name/admin` 来登录到账户里，登录的用户名是 email，密码是上面增加用户时的密码。如果想将某一个用户设置为管理员，则执行

**将用户提升为管理员**

```
docker exec -it your_container_name /gotosocial/gotosocial admin account promote --username your_username
```

### 如何使用

现在阶段的 gotosocial 同样也没有一个网页来发内容等，可以用 mastodon 支持的一些应用，比如我在 iOS 上用的是 mastodon，更多能用的应用可以查看 [https://joinmastodon.org/apps](https://joinmastodon.org/apps)。更多关于它的玩法，可以多看看 mastodon。

### 一些问题

- 上面 `docker-compose.yaml` 文件中说到的 `user` 问题，可能会导致 sqlite 文件无法生成而出错，严格说，官方还没有解决好这个问题，具体看[这里](https://github.com/superseriousbusiness/gotosocial/issues/476)，这里也提供了解决办法，简单粗暴的方式是将 user 设置成 `root:root`。我有个解决办法
 
     - 通过 `cat /etc/passwd` 获取当前用户的`用户标识号`和`组标识号`
     
     - 将 `docker-compose.yaml` 文件中 `user` 内容改成所获取到的`用户标识号`和`组标识号`
     
     - `docker-compose.yaml` 文件中的 `volumes` 不应该用 `~`，而使用绝对目录 `/home/username/***` 这样的形式。需要注意的是，如果用户是 `admin`，可能没有作用，建议新建个用户。

- 数据都是保存在容器所映射的本地目录中，及时备份。

- 修改 `docker-compose.yaml` 文件后，需要先 `docker compose down`，然后再拉起容器。

### 相关资源

- GoToSocial 官网: [gotosocial.org](https://gotosocial.org)

- GoToSocial 项目地址: [superseriousbusiness/gotosocial@GitHub](https://github.com/superseriousbusiness/gotosocial)