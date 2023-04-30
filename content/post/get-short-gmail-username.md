---
title: "获取 6 个字符的 Gmail 用户名"
slug: get-short-gmail-username
author: "Bin Hua"
lastmod: 2019-09-20 15:43:34
date: 2019-05-27 04:16:35
tags: ["Gmail", "github", "centos", "python"]
---

Gmail 的用户名最少是 6 位，随着其用户越来越多，能够得到一个较短的用户名也比较麻烦了，恰好在 GitHub 上发现了一个比较好玩的库，用来查找 Gmail 中还剩下的 6 位字符的用户名。

#### 实验环境

-  CentOS 7

-  Python 3

-  Git

-  GitHub 项目地址：[https://github.com/xyou365/gmail-username-available](https://github.com/xyou365/gmail-username-available)

#### 操作步骤

-  配置 python 3 的环境

    系统中默认的是 python 2.7，本实验项目需要 python 3 的环境，故需要进行环境的更新
    
    **源码安装方式**
    
    ```
    sudo yum install yum-utils -y
    sudo yum-builddep python -y
    curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
    tar xf Python-3.5.0.tgz
    cd Python-3.5.0
    ./configure
    make
    sudo make install
    python3 -V
    ```
    
    **EPEL 仓库安装方式**
    
    ```
    sudo yum install epel-release -y
    sudo yum install python34 -y
    ```
    
- 安装 Git

    直接通过命令 `yum install git -y` 安装。
    
- 专属链接的获取

    访问页面 `https://accounts.google.com/SignUpMobile?loc=CN&hl=en`，输入相关信息
    
    ![](/imgs/get-short-gmail-username-01.png)
    
    输入手机号码
    
    ![](/imgs/get-short-gmail-username-02.png)
    
    提交后，会有一个提示，等待一段时间。然后根据提示获取到`专属链接`，记得是 `Copy as cURL`。
    
- 执行脚本

    执行脚本 `python3 gmail_username_try.py`，然后输入专属链接，就可以一个一个的检查六字符的用户名了。
    
    
最后，根据你喜欢的注册吧。
    
    
    