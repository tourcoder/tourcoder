---
title: "在 Debian 10 上安装 Trojan 和 bbr plus"
slug: "how-to-install-trojan-bbr-plus-on-debian-10"
author: "Bin Hua"
date: 2022-03-05T09:17:22Z
tags: ["trojan", "bbr", "Debian", "trojan go"]
draft: false
---

Trojan 协议出来很久了，一直没有尝试过，借此机会尝试下，也尝试下 BBR PLUS。

#### 基础信息

系统：Debian 10

#### 准备工作

先将系统升级到最新版本，`apt update -y && apt upgrade -y`

申请一个证书，至于如何申请，可以查看之前我写的博文，[给网站加 ssl](https://tourcoder.com/ssl-for-website/) 或者 [CentOS 7 下签发 Let's Encrypt https 证书](https://tourcoder.com/get-lets-encrypt-on-centos-7/)，前面一篇是 Debian 系下，后面一篇是 centOS 下。

#### 安装 BBR

Debian 10 自带了 BBR，我使用的是网上的一个开源脚本，脚本看[这里](https://github.com/chiakge/Linux-NetSpeed/raw/master/tcp.sh)。直接安装，需要在 root 权限下执行。

```
wget https://github.com/chiakge/Linux-NetSpeed/raw/master/tcp.sh
chmod +x tcp.sh
./tcp.sh
```

根据里面的选项，先安装后使用即可。其中在选择安装的时会弹窗提示 `Abort kernel removal?` 选择 `no`。

#### 安装和配置 Trojan

在 Debian 下可以直接通过 `apt install trojan` 安装，进入 `/etc/trojan`，编辑里面的 `config.json` 文件

```
{
    "run_type": "server",
    "local_addr": "0.0.0.0",
    "local_port": 443,
    "remote_addr": "127.0.0.1",
    "remote_port": 80,
    "password": [
        "password1",
        "password2"
    ],
    "log_level": 1,
    "ssl": {
        "cert": "/path/to/certificate.crt",
        "key": "/path/to/private.key",
        "key_password": "",
        "cipher": "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256",
        "prefer_server_cipher": true,
        "alpn": [
            "http/1.1"
        ],
        "reuse_session": true,
        "session_ticket": false,
        "session_timeout": 600,
        "plain_http_response": "",
        "curves": "",
        "dhparam": ""
    },
    "tcp": {
        "prefer_ipv4": false,
        "no_delay": true,
        "keep_alive": true,
        "fast_open": false,
        "fast_open_qlen": 20
    },
    "mysql": {
        "enabled": false,
        "server_addr": "127.0.0.1",
        "server_port": 3306,
        "database": "trojan",
        "username": "trojan",
        "password": ""
    }
}
``` 

修改上面的密码和 ssl 证书的位置，然后重启 `serivce trojan restart`，也可以通过 `service trojan status` 或者 `ss -lp | grep trojan` 查看状态。如果需要增加 ws + tls 则在该配置里增加如下内容

```
"websocket": {
    "enabled": true,
    "path": "/你的路径/",
    "host": "你的域名"
  },
  "mux": {
    "enabled": true,
    "concurrency": 8,
    "idle_timeout": 60
  }
```

以及在 ssl 代码块中增加 `"sni": "你的域名"`

#### 一键安装 Trojan 和 Trojan Go

Trojan Go 这个项目可以理解为是升级版的 Trojan，网上有大神搞了带多用户管理的程序，地址是：[https://github.com/Jrohy/trojan](https://github.com/Jrohy/trojan) ，安装方式里面写的也很清楚，非常方便。通过它安装的配置文件位置是 `/usr/local/etc/trojan/config.json`

发现很多人是直接用了这个仓库里的 docker 安装方式，什么都没有修改，这个很危险！！！至少要把数据库的 docker 配置改一下，可以改成

```
docker run --name trojan-mariadb \
--restart=always \
-p 127.0.0.1:3306:3306 \
-v /home/admin/mariadb:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=你的 root 用户密码 \
-e MYSQL_DATABASE=你的数据表名 \
-d mariadb:10.2
```

如上，至少把端口限制成宿主使用，修改下 root 密码和数据表名，这是最基本的！

#### 客户端

至于在客户端如何配置，自行查看网上的其它教程。
