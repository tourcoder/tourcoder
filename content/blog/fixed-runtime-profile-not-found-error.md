---
title: "解决 Runtime Profile Not Found 的错误"
slug: "fixed-runtime-profile-not-found-error"
author: "Bin Hua"
date: 2024-04-02T14:18:26Z
tags: ["iOS", "Xcode", "macOS"]
draft: false
---

新版的 xcode 总会有一个问题，当下载一个新的模拟器后，当再次项目时，总会弹出错误，比如我今天下载 iOS 17.4 的模拟器后，就出现了下面的错误

```
The com.apple.CoreSimulator.SimRuntime.iOS-17-4 Simulator runime is not available.
runtime profile not found using "System" match policy Download the com.apple.CoreSimulator.SimRuntime.iOS-17-4 simulator runtime from the Xcode Settinas.
```

最简单的解决办法是打开 xcode，进入到模拟器管理界面，删除掉里面的设备模拟器，然后重新增加即可。