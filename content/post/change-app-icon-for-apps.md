---
title: "iOS 应用动态更改图标"
slug: change-app-icon-for-apps
author: "Bin Hua"
lastmod: 2020-11-23 23:55:46
date: 2019-02-21 04:23:16
tags: ["Apple", "iOS", "SDK", "代码示例", "GitHub"]
---

Apple 很早就已经将 iOS 应用动态更改图标的接口放了出来，只是信息比较零碎，文档看这里 [https://developer.apple.com/documentation/uikit/uiapplication/2806818-setalternateiconname](https://developer.apple.com/documentation/uikit/uiapplication/2806818-setalternateiconname), 它对 SDK 的要求是 iOS 10.3+ / tvOS 10.2+。

恰好这次的项目的一个需求是要求动态更改图标，看了下文档，试着写了个 DEMO。

**基本信息**

- 开发语言 objc

- SDK 版本 iOS SDK 12.1

- 项目名称 ChangeIcon

- 目标设备 iPhone（模拟器）

新建项目，命名为  ChangeIcon，通过 Assets 中的 AppIcon 可以看出本次测试设备 iPhone 需要四个基础尺寸的 Icon，20 / 29 / 40 / 60 及其倍数。制作两套分别为 A / B。

![](/imgs/change-app-icon-for-apps-01.png)

增加默认的 Icon，这里是 A。运行后的效果如下

![](/imgs/change-app-icon-for-apps-02.png)

写代码，这里的布局就是两个按钮，分别切换，具体代码比较简单

![](/imgs/change-app-icon-for-apps-03.png)

上面代码执行后，得到的如下的布局

![](/imgs/change-app-icon-for-apps-04.png)

**编辑 Info.plist 文件**

Info.plist 文件增加 Icon files (iOS 5)，而不是 Icon files，这里比较重要，增加的内容如下

![](/imgs/change-app-icon-for-apps-05.png)

这样就完成了该功能，测试一下

![](/imgs/change-app-icon-for-apps-06.png)

当点击 Set 2 A 时，会弹出窗口显示相关的内容，同样点击 Set 2 B 时，也会弹出相关的内容，这时 Icon 就发生了改变。

![](/imgs/change-app-icon-for-apps-07.png)

![](/imgs/change-app-icon-for-apps-08.png)

本次 Demo 的代码：[GitHub](https://github.com/tourcoder/ChangeIcon)