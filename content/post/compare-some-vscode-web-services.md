---
title: "比较几个 vscode 的网页版"
slug: "compare-some-vscode-web-services"
author: Bin Hua
lastmod: 2022-09-27T05:34:43Z
date: 2022-09-27T05:34:43Z
tags: ["vscode", "GitHub", "Microsoft", "Copilot", "Apple", "iPad Pro"]
---

我之前一直有一个开发机，近小半年，我开始使用了下几个在线的 VS Code 的服务，下面做一个比较。主要功能的比对，需要注意的是，这里没有比较自建的，也仅限使用率高的。

|产品|供应商|形式|是否有终端|是否有 Copilot|其他插件|进入方式|
|---|---|---|---|---|---|---|
|GitHub 开发页|GitHub|github.dev|无，提示网页不支持|无，提示网页不支持|大部分支持|浏览器打开 GitHub 上仓库地址，点击 . 进入，或者将 https://github.com/username/reponame 中的 `github.com` 改成 `github.dev` 即可|
|GitHub Codespaces|GitHub|它有两种形式，调用本地 VSCode 和打开浏览器|都有|都有|都有|在所创建的项目的 codespace 后点 `...` 选择调用本地 VSCode 还是在浏览器里打开|
|VSCode 开发页|微软|vscode.dev|无，提示网页不支持|无，提示网页不支持|大部分支持|浏览器上打开 vscode.dev 直接使用即可|

**几点注意**

- GitHub Codespaces 其实就是一个开发机，可以通过浏览器打开，也可以调用本地 VSCode 进行远程连接。但它的这个开发机围绕一个项目（repo）创建，至于其他的事情，虽然应该可以，但强烈不建议。除了编辑仓库文件之外，还能通过它打开本地电脑上的单个文件，并将该文件保存到开发机上，也可以将该文件下载到本地电脑。同时也可以通过外部链接访问该项目，可作调试使用。需要注意的是，只能通过它打开本地电脑的单个文件，无法打开整个文件夹。

- GitHub 开发页，即 github.dev，在浏览器里打开。因为也是基于项目创建，所以默认打开的是项目本身目录的内容。和 GitHub Codespaces 一样，也能打开本地电脑的单个文件，并选择保存位置。需要注意因为本身不是开发机，所以文件不是保存在本地电脑的，应该通过插件 `Source Control` 提交到仓库，否则浏览器关闭后，该内容将会丢失。

- VSCode 开发页，即 vscode.dev，在浏览器里打开。本地电脑文件打开和保存的情况和上面 GitHub Codespaces 一样，因为它本身也是一台开发机。但不同的是，未登录 vscode.dev 的账户下，只能打开编辑保存本地电脑的文件，而登录 vscode.dev 的账号后，可以打开远程的仓库，其它操作和 GitHub Codespaces 基本一致。无外部调试功能。

- GitHub Codespaces 可以修改 commit 的信息，GitHub.dev 和 VSCode.dev 目前无法修改 commit 信息。

**iPad 体验**

我用的是一台 iPad Pro，这三个体验下来都挺好的，但我使用 Codespaces 较多点。

之前写过一篇关于 GitHub Codespaces 的文章，可以参考下，[试用 Github Codespaces](https://tourcoder.com/try-github-codespaces/)
