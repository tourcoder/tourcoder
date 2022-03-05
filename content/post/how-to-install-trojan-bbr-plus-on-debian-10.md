---
title: "在 Debian 10 上安装 Trojan 和 bbr plus"
slug: "how-to-install-trojan-bbr-plus-on-debian-10"
author: Bin Hua
lastmod: 2022-03-05T09:17:22+08:00
date: 2022-03-05T09:17:22+08:00
tags: ["trojan", "bbr", "debian"]
draft: true
---

Trojan 协议出来很久了，一直没有尝试过，借此机会尝试下，也尝试下 BBR PLUS。

#### 基础信息

系统：Debian 10


#### 安装 BBR

Debian 10 自带了 BBR，我使用的是网上的一个开源脚本，脚本看[这里](https://github.com/chiakge/Linux-NetSpeed/raw/master/tcp.sh)。直接安装，需要在 root 权限下执行。

```
wget https://github.com/chiakge/Linux-NetSpeed/raw/master/tcp.sh
chmod +x tcp.sh
./tcp.sh
```

根据里面的选项，先安装后使用即可。其中在选择安装的时会弹窗提示 `Abort kernel removal?` 选择 `no`。

#### 安装和配置 Trojan

在 Debian 下可以直接通过 `apt install trojan` 安装，