---
title: "Unable to boot device because it cannot be located on disk."
slug: "unable-to-boot-device-because-it-cannot-be-located-on-disk"
author: "Bin Hua"
lastmod: 2020-08-13 09:38:04
date: 2019-09-29 05:27:42
tags: ["iOS", "cocoapods", "swift"]
---

昨天做了下磁盘清理，导致今天在用 xcode 编译一个应用时出现了两个问题

**问题一**

错误提示如下

```
Multiple commands produce '/Users/TOURCODER/Library/Developer/Xcode/DerivedData/ProjectName-fuzydagfygwvdbaaesbqgyxhuvgh/Build/Products/Debug-iphonesimulator/ProjectName.app/Assets.car':
1) Target 'ProjectName' (project 'ProjectName') has compile command with input '/Users/TOURCODER/workspace/ProjectName/Assets.xcassets'
2) That command depends on command in Target 'ProjectName' (project 'ProjectName'): script phase “[CP] Copy Pods Resources”
```

解决的办法：

xcode 中选择 `File->Workspace settings` 会弹出如下图片

![](/imgs/unable-to-boot-device-because-it-cannot-be-located-on-disk001.png)

选择其中的 `Legacy Build System` 即可解决问题。


**问题二**

错误提示如下

```
Unable to boot device because it cannot be located on disk.
```

解决办法：

在终端中输入 `xcrun simctl erase all` 完成该命令即可。