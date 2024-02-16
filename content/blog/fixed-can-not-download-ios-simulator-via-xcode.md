---
title: "解决无法通过 xcode 下载 iOS 模拟器的 bug"
slug: "fixed-can-not-download-ios-simulator-via-xcode"
author: "Bin Hua"
date: 2024-02-16T12:47:15+08:00
tags: ["xcode", "ios", "Apple"]
draft: false
---

在 xcode 中下载 iOS 的模拟器总会出错，明明磁盘空间足够，但它总是提示错误。可以直接下载模拟器文件的方式解决这个问题。

### 下载模拟器文件

进入页面 `https://developer.apple.com/download/all/` 下载对应的模拟器文件，比如我这里下载的是 iOS 17.2，格式是 dmg 的。

### 安装模拟器文件

执行下面的三个命令即可解决问题。

```
sudo xcode-select -s /Applications/Xcode.app
xcodebuild -runFirstLaunch
xcrun simctl runtime add "your_path/iOS_17.2_Simulator_Runtime.dmg"
```

需要注意的是安装完成后，这个文件不能删除，如果删除了，xcode 会提示错误。