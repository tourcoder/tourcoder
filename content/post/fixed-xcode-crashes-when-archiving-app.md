---
title: "Fixed Xcode Crashes When Archiving App"
slug: "fixed-xcode-crashes-when-archiving-app"
author: Bin Hua
lastmod: 2021-07-01T12:46:23+08:00
date: 2021-07-01T12:46:23+08:00
tags: ["xcode", "apple"]
---

在用 Xcode 打包应用时总是会导致 Xcode 闪退，检查其 log 后发现是因为 Source Control 引起的。

**解决方法**

进入 Xcode 的 `Preferences`，选择 `Source Control` 选项卡，然后将 `Enable Source Control` 的勾选取消。

![](/imgs/fixed-xcode-crashes-when-archiving-app.png)

即将上图的 Source Control 取消勾选即可。
