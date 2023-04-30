---
title: "NPM 中 Module 安装后无法找到"
slug: command-not-found-in-nodejs-npm
author: "Bin Hua"
lastmod: 2020-08-13 09:28:47
date: 2019-03-25 03:51:38
tags: ["bug", "nodejs", "npm"]
---

在全局安装一些 npm 中的 module 文件后，执行该 module 会经常会出现 Command not found 的问题。

一般全局安装是安装在 `/usr/local/lib/node_modules` 这样的目录下的，可以通过 `npm root` 或者 `npm root -g` 查看当前返回目录是什么，如果返回的不是上面的目录，则运行 `npm config set prefix /usr/local` 来将目录设置成该地址，然后再次全局安装该 module 即可。

**注意**：在设置完后，建议再次用 `npm root -g` 命令查看下返回的目录地址是否正确。

    