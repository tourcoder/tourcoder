---
title: "Git 服务器架设"
slug: "how-to-set-up-a-git-server"
author: "Bin Hua"
lastmod: 2019-03-24 12:15:13
date: 2019-03-24 12:15:13
tags: ["git", "GitHub"]
---

Git 现在基本都是开发团队的标配，网上也有大量的相关服务，比如 GitHub，但也可以自己架设一个简单实用的 Git 服务器。

#### 准备

- centOS 7.0

#### 部署过程

- 更新系统

    ```
    yum update -y && yum upgrade -y
    ```
    
- 安装 git

    ```
    yum install git -y
    ```
    
    可以通过 `git --version` 查看安装后的版本，如果版本过低，可以升级，也可以源码方式安装
    
- 创建管理 git 服务的用户

    ```
    adduser git
    ```
    
    增加一个用户 git
    
- 初始化仓库

    新建一个地址，并初始化一个仓库
    
    ```
    cd ~
    mkdir gitc
    cd gitc
    git init --bare demo.git
    ```
    
    此时会有一个裸仓库，更改 owner 改成 git
    
    ```
    chown -R git:git demo.git
    ```
    
- 禁用 shell 登录

    因为安全因素，不应该让 git 用户登录 shell
    
    ```
    vi /etc/passwd
    ```
    
    找到 `git:x:1001:100:/home/git:/bin/bash`，将其后面改成 `:/home/git:/usr/bin/git-shell`。
    
- 克隆仓库

    ```
    git clone git@serveraddress:~/gitc/demo.git
    ```
    
    可以直接使用了。
    
#### 公钥及管理

用户登录是需要公钥的，把每个用户登录用的公钥导入到 `/home/git/.ssh/authorized_keys` 中，一行一个公钥。

还有一个工具 Gitosis 可以更好的管理公钥。

这里顺便介绍下在 macOS 下生成公钥

```
cd ~/.ssh
```

进入到 `~/.ssh` 下面查看是否有 `id_dsa` 和 `id_rsa.pub` 文件，其中 `.pub` 文件是公钥，另外一个是私钥。如果都不存在，甚至连 `~/.ssh` 文件夹也不存在，就创建

```
mkdir ~/.ssh
cd ~/.ssh
```

创建并进入 `~/.ssh` 文件夹

```
ssh-keygen
```

此时它会要求你确认保存公钥的位置 `~/.ssh/id_rsa`，直接回车确认，此时会要求你输入密码，可以留空，回车后即可创建完成，通过 `ls` 可以看到，已经存在上面说到的两个文件

![](/imgs/id_rsa_github.png)

运行命令 `cat ~/.ssh/id_rsa.pub` 将显示的内容放入到 git 服务器的密钥管理中即可。

#### 权限问题

Git 本身的权限是开放式的，但可以通过 Hook 来解决，推荐一个工具 Gitolite。
