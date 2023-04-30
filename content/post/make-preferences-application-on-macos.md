---
title: "开发 macOS 中 Preferences Application"
slug: make-preferences-application-on-macos
author: "Bin Hua"
lastmod: 2020-07-18 05:57:43
date: 2019-07-13 12:02:29
tags: ["macOS", "App", "swift", "objc", "Productivity"]
---

想必有很多和我一样喜欢拿着 mac 在外面写点东西的人都遇到过一个问题，当专心写东西往往没有注意 mac 没电，直到没电关机，要是有一个 app 能想 iPhone 上那样低电量提醒就好了。

所以，我就写了个这样的应用 **BatteryBird**，不过并不是安装在 `Application` 这个文件夹下的应用，而是出现在 `System Preferences` 中的应用，其实它本身就是一个独立的应用。

### 准备条件

系统环境：macOS Version 10.14.5 (18F132)

开发工具：XCode Version 10.2.1 (10E1001)

知识点：Preferences Pane

测试环境：同系统环境

### 开发

在 XCode 中新建一个项目

![](/imgs/make-preferences-application-on-macos-01.png)

这里选择对应的模板：`Prefernce Pane`

![](/imgs/make-preferences-application-on-macos-02.png)

输入项目名等信息，点击`下一步`直到创建完成。

![](/imgs/make-preferences-application-on-macos-03.png)

创建好后的项目左侧文件，整个文件挺少，是我喜欢的方式，需要注意的是这里自动生成的文件 `BatteryBird.tiff` 是一个空文件，然后就是编码过程，等代码写完，测试通过后，按 `command + B` 对代码进行编译。

PS. 从上面的文件结构可以看出，它默认支持的是 Objc，而不是 Swift，如果需要用 Swift 来写，[这里](https://stackoverflow.com/questions/32041677/using-swift-with-an-os-x-preference-pane-plugin)的一个问答很有帮助。

![](/imgs/make-preferences-application-on-macos-04.png)

编译通过，在 `Products` 文件夹下的文件 `BatteryBird.prefPane` 点右键，选择 `Open with External Editor`，此时会自动打开，需要安装

![](/imgs/make-preferences-application-on-macos-05.png)

点击安装，在安装完成后，即可在 `System Preferences` 中看到相关的 icon 了。

![](/imgs/make-preferences-application-on-macos-06.png)

这基本就是 `Preferences Application` 的开发过程。