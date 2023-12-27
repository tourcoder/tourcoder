---
title: "CentOS 网络设置和桌面"
slug: "set-network-and-desktop-for-centos"
author: "Bin Hua"
lastmod: 2019-02-20 12:27:52
date: 2019-02-20 12:27:52
tags: ["centos", "desktop", "gnome"]
---

如前一篇「Windows 10 安装 U 盘的制作」中说到，我制作了 CentOS 的安装 U 盘，制作过程如前面说的一样，不同的是把 Windows 10 的映像文件换成 CentOS 的文件，可以去 CentOS 的官方下载，下载地址：[https://www.centos.org/download/](https://www.centos.org/download/)

**网络设置**

在安装完 CentOS 后，发现无法上网，那是因为网络还没有设置

输入 `nmcli d` 即可看到网络是 disconnected 的状态，此时输入 `nmtui` 选择 `Edit connection`，然后再选择 `Edit`，让 `IPv4 CONFIGURATION` 设置为 `Automatic`，同时将 `Automatically connect` 勾选，然后确定。

最后重启网络 `service network restart`，在一会的等待后，CentOS 就可以上网了。

**Gnome 桌面**

![](https://storage.tourcoder.com/tcblog/set-network-and-desktop-for-centos.png)

因为这台电脑是需要一个桌面的，所以我选择了个人觉得比较好的 [Gnome](http://gnome.org)

安装也很简单，输入 `yum groupinstall "GNOME Desktop"` 即可安装，然后输入 `startx` 即可启动桌面。