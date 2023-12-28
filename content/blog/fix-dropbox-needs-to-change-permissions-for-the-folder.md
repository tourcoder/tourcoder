---
title: "修复 macOS 下 Dropbox Needs to Change Permissions for the Folder 的问题"
slug: "fix-dropbox-needs-to-change-permissions-for-the-folder"
author: "Bin Hua"
date: 2022-02-02T15:52:21Z
tags: ["Dropbox", "macOS"]
draft: false
---

我最近修改了 macOS 的用户名及其文件夹，导致 Dropbox 无法正常启动了，总是提示

```
Dropbox Needs to Change Permissions for the Folder
```

看提示，Dropbox 一直定位到旧的用户名所在的文件夹， 做了以下几个尝试。

1. 尝试了重新安装 Dropbox，不行。

2. 尝试新建一个和旧用户名一样的用户，不行。

继续在当前用户下寻找发现，在该用户目录下有一个 `.dropbox` 的文件夹，应该是它的配置文件，尝试删除

```
sudo mv ~/.dropbox ~/.dropbox-old
```

这里没删除，是备份，预防后面有用。然后重新安装 Dropbox，问题解决了。
