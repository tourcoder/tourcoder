---
title: "修复 OpenSSH 的安全漏洞"
slug: "fixed-openssh-security-problems"
author: "Bin Hua"
date: 2024-07-02T06:20:14Z
tags: ["OpenSSH", "Debian", "Ubuntu"]
draft: false
---

OpenSSH 爆了一个远程代码执行漏洞，编号是 CVE-2024-6387，具体看[这里]()。一早更新了几台服务器，记录下过程。

### 受影响的 OpenSSH 版本

受影响的版本是：从 v8.5p1 到 v9.8

### 解决方案

升级到 v9.8p1 即可

### 环境

我的这些服务器（或 VPS）安装的都是 Debian 系统，所以下面的内容都是基于 Debian 的，Ubuntu 也可以这样解决。也因为我使用的是编译方式解决，在 CentOS 也可以用下面方法解决，大差不离。

### 过程

进入到服务器，下载对应的文件，所需的文件在[这里](https://www.openssh.com/releasenotes.html)

```
# 从上面链接中，下载 OpenSSH 官网提供的源码并解压
wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.8p1.tar.gz
tar -xzf openssh-9.8p1.tar.gz
cd openssh-9.8p1

# 安装构建所需要的依赖项，一般这步省略（基本这些内容服务器都早已经安装）
sudo apt update -y
sudo apt install build-essential libssl-dev zlib1g-dev -y

# 先备份配置文件
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
sudo cp /etc/ssh/ssh_config /etc/ssh/ssh_config.bak

# 配置编译和安装
./configure --prefix=/usr --sysconfdir=/etc/ssh
make
sudo make install

# 重启 SSH 服务
sudo systemctl restart ssh

# 验证安装，看是否是最新版
ssh -V
```