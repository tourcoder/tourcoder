---
title: "Mosh 试用"
slug: "mosh"
author: "Bin Hua"
date: 2021-12-08T12:42:55Z
tags: ["mosh", "shell", "iterm", "terminal"]
draft: false
---

Mosh 全称 mobile shell，其官网是 [https://mosh.org/](https://mosh.org/)，特点很多，其中一个很重要的特点是比起 ssh 在一般网络状态下的稳定。因为我日常开发是在 macOS 上通过 ssh 到一台开发机上，因为网络导致的问题还是挺多的，所以这次试试 mosh。虽然早就知道这个，但还是第一次正式使用。

### 安装

在 macOS 上直接通过 homebrew 安装即可 `brew install mosh`，而在服务器端也要安装，我用的是 Debian，则运行 `apt install mosh -y` 即可

### 使用

和使用 ssh 一样方式

```
mosh username@server
```

即可。更多内容可以看其官网或者使用 `mosh -h` 查看，另外 mosh 使用 ssh 的 key 的登录方式是

```
mosh --ssh="ssh -i ~/.ssh/key" username@server
```

这样多少有点不方便，那么可以通过 `.ssh/config` 的配置来实现简单登录，比如

```
Host servA servA2 servA3
    HostName x.x.x.x
    User tc
    IdentityFile ~/workspace/ssh/serv1.pem

Host servB
    HostName x.x.x.x
    User tc
    IdentityFile ~/workspace/ssh/serv2.pem

Host servC
    HostName x.x.x.x
    User dev
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

即可通过 `mosh servA/servB/servC` 这样直接登录，这里也可以同样用 ssh。

每个 Host 可以用多个别名，比如上面的 `Host servA servA2 servA3`，用 `mosh servA`，`mosh servB`，`mosh servC` 均可以登录。对于用同一个密钥和用户名的，可以简单配置为

```
Host *
    User tc
    IdentityFile ~/workspace/ssh/serv.pem

Host servA
    HostName x.x.x.x

Host servB
    HostName x.x.x.x
```

这样的配置基本满足了我日常用的开发机器，但对很多服务器的管理，配置会更复杂一点，会在 `~/.ssh/config` 的头部增加 `Include ~/.ssh/config.d/*`，然后将各类服务器的配置放到 `~/.ssh/config.d/` 的下面，一个大概的目录结构

```
~/.ssh/
├── config                  # 主入口，只写 Include 和全局默认
├── config.d/
│   ├── aws.conf            # AWS 服务器
│   ├── personal.conf       # 个人服务器
│   └── work.conf           # 工作服务器
├── keys/                   # 密钥统一收在这里
│   ├── aws.pem
│   └── id_ed25519
└── known_hosts
```

其他自行扩展...

### 注意点

需要在服务器端开启 `60000-65535` 的入站端口，比如 aws 的 EC2 -> Security Group，GCP 的 VPC -> Firewall rules
