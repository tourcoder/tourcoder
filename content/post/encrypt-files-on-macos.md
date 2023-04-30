---
title: "macOS 下加密压缩"
slug: encrypt-files-on-macos
author: "Bin Hua"
lastmod: 2020-08-13 09:27:16
date: 2019-03-12 15:41:59
tags: ["macOS", "加密", "encrypt"]
---

我买了商业版的 G Suite，有无限空间，正好我可以用它来存储照片，但我不想把自己照片放在 Google Photo 里面，只想压缩后放在 Google Drive 中，而单纯的压缩，还是容易被查看到的，所以在 macOS 下做一下加密压缩，就显得特别重要。

#### 压缩过程

在终端中输入下面命令

```
zip -e zippedname.zip sourcefile.txt
```

执行该命令后，会要求输入密码，输入密码即可，注意是要输入两次密码的。如果是要压缩一个文件夹，则输入命令

```
zip -er zippedname.zip sourcefolder
```

后面是一样要求输入两次密码。

![](/imgs/encrypt-files-on-macos-encrypt.png)

#### 解压过程

双击压缩后的文件，会要求输入密码，输入正确的密码即可解压成功。

![](/imgs/encrypt-files-on-macos-decrypt.png)
