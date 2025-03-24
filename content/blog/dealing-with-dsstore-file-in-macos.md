---
title: "处理 macOS 中的 DS Store 文件"
slug: "dealing-with-dsstore-file-in-macos"
author: "Bin Hua"
date: 2025-03-24T11:16:22Z
tags: ["macOS", "trick"]
draft: false
---

macOS 下 DS Store 文件是一个烦人的东西，关于它的介绍说明，可以看[维基百科](https://zh.wikipedia.org/wiki/.DS_Store)上的解释。在维基百科的解释上也有几个禁止 DS Store 文件生成的办法，我来多分享几个处理技巧

1. 在 `/usr/sbin` 下有一个脚本文件 `dot_clean`，可用它来做这个事情。比如我要禁止我的工作目录下产生这个文件，即 `/usr/sbin/dot_clean -m ~/Workspace` 即可，在禁止产生的同时还会自动删除掉已经有的 .DS_Store 文件，但在新 macOS 下似乎没有效果了。 

2. 通过命令定期删除 `.DS_Store` 文件，执行命令 `find /path/to/directory -name ".DS_Store" -type f -delete` 即可。这里可以扩展为写成一个脚本，定期删除即可。

3. 避免使用 Finder 操作文件夹，用命令行或者第三方工具来操作复制粘贴。