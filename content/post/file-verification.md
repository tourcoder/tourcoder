---
title: "文件的校验"
slug: file-verification
author: Bin Hua
lastmod: 2020-08-13 09:30:46
date: 2019-05-27 03:20:32
tags: ["macOS", "sha1", "sha", "sha224", "sha256", "sha384", "sha512", "md5", "base64"]
---

下载的文件很多时候是应该对文件进行校验的，常用的校验有 md5，sha1 等等，校验方式也比较简单，这里单纯用 md5 校验

-  安装相关的校验命令

    通过 `homebrew` 来安装校验命令工具
    
    ```
    brew install md5sha1sum
    ```
    
-  命令行进行校验

    打开命令行工具，执行命令 `md5sum 待校验的文件名`即可。其实在 macOS 下可以直接用 `md5 代校验文件名`来直接进行校验。