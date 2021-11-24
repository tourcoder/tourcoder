---
title: "IPTraf 安装与使用"
slug: iptraf
author: Bin Hua
lastmod: 2020-08-13 09:02:24
date: 2017-01-18 06:54:38
tags: [iptraf", "centos"]
---

最近在做一个采集程序的时候遇到一个问题，自己感觉跑的流量和服务器供应商给出来的统计相差很大，想多方面检测下具体的情况，就使用了 IPTraf。

**先决条件**

服务器： centOS 7

**安装**

可以去下载源码安装，去官网下载源码，需要注意的是官网应该是被封了，[官网地址](http://iptraf.seul.org/)

我是直接执行命令 `yum install iptraf -y`，很快就可以安装完成。

**运行**

![](/imgs/iptraf-01.png)

提示错误，因为在 centOS 中，当安装 iptraf 的时候，已经自动的安装了 `iptraf-ng`，所以这里应该执行命令 `iptraf-ng`。

注意，你要调整你的终端尺寸，否则也会报错，一切正常后，进入

![](/imgs/iptraf-02.png)

至于怎么用，都是图文化的界面，很容易。
