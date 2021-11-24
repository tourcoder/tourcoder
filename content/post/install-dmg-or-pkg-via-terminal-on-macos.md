---
title: "在 macOS 的终端里安装 dmg 或 pkg 文件"
slug: "install-dmg-or-pkg-via-terminal-on-macos"
author: Bin Hua
lastmod: 2021-05-31T09:54:38+08:00
date: 2021-05-31T09:54:38+08:00
tags: ["macos", "terminal", "iterm2"]
---

痴迷终端，想什么都通过它来解决，即便是安装 macOS 上的应用，命令如下

**DMG 文件**

比如该文件名是 downloadedFileName

```
hdiutil attach path/downloadedFileName.dmg
```

执行该命令后，将在 `/Voumes` 下挂载该 dmg 文件，进入到该文件夹（比如是 mountedPackage）

```
cd /Volumes/mountedPackage
```

执行命令将里面 `.app` 后缀的文件包复制到 `/Applications` 中，即

```
cp -rf .app /Applications
```

因为这里的 `.app` 不是单个文件，而是一个包，复制时需要参数 `-r`。最后退出挂载。

```
hdiutil detach mountedPackage
```

**PKG 文件**

执行命令

```
sudo installer -pkg downloadedFile.pkg -target /Applications
```
