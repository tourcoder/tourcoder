---
title: "虚拟机中安装 macOS"
slug: install-macos-in-vmware
author: "Bin Hua"
lastmod: 2020-08-13 09:02:31
date: 2017-02-26 06:55:20
tags: ["macOS", "vmware", "虚拟机"]
---

一时心血来潮，在家里的 pc 上安装了虚拟机，并在里面安装了最新版的 macOS 10.12，下面是大致的安装步骤。

**母机**

高配的 PC 里面安装了 Windows 7，这本来是我用来打游戏《守望先锋》的机器。

**虚拟机软件**

VMware Workstation Pro 12.5.0

**客户机系统**

macOS 10.12

**步骤**

- 安装 VMware Workstation Pro 12.5.0 一步一步的安装好改软件。 

- 解锁 VMware Workstation Pro 12.5.0 安装好的 WMware 是没有 macOS 选项的，需要解锁它，解锁的办法也很简单，下载 unlock 文件，然后在 Windows 7 下以管理员的模式，执行解锁的文件即可，解锁文件搜索关键词 unlock wmware。 

- 配置并安装系统 将系统的 iso 文件配置到虚拟光驱，然后执行安装。 

就这样一步一步安装完成。

注意，在这个过程中可能会遇到一些问题

问题一：VMware Workstation 不可恢复错误: (vcpu-0)

解决办法：打开 vmx 文件，文末添加一句 smc.version = "0"

问题二：无法全屏

解决办法：安装 wmware tools 即可。

问题三：网络无法连接

解决办法：使用 NAT 连接方式。