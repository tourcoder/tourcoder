---
title: "比较几个 vscode 的网页版"
slug: "compare-some-vscode-web-services"
author: Bin Hua
lastmod: 2022-09-27T05:34:43Z
date: 2022-09-27T05:34:43Z
tags: ["vscode", "GitHub", "Microsoft", "Copilot"]
---

我之前一直有一个开发机，近小半年，我开始使用了下几个在线的 VS Code 的服务，下面做一个比较。主要功能的比对，需要注意的是，这里没有比较自建的，也仅限使用率高的。

|产品|供应商|形式|是否有终端|是否有 Copilot|其他插件|进入方式|
|---|---|---|---|---|---|---|
|GitHub 开发页|GitHub|github.dev|无，提示网页不支持|无，提示网页不支持|大部分支持|浏览器打开 GitHub 上仓库地址，点击 . 进入，或者将 https://github.com/username/reponame 中的 `github.com` 改成 `github.dev` 即可|
|GitHub Codespaces|GitHub|它有两种形式，调用本地 VSCode 和打开浏览器|都有|都有|都有|在所创建的项目的 codespace 后点 `...` 选择调用本地 VSCode 还是在浏览器里打开|
|VSCode 开发页|微软|vscode.dev|无，提示网页不支持|无，提示网页不支持|大部分支持|浏览器上打开 vscode.dev 直接使用即可|

**几点注意**

- GitHub Codespaces 其实就是一个开发机，可以通过浏览器打开，也可以调用本地 VSCode 进行远程连接。但它的这个开发机围绕一个项目（repo）创建，至于其他的事情，虽然应该可以，但强烈不建议。
