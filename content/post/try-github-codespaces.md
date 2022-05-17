---
title: "试用 Github Codespaces"
slug: "try-github-codespaces"
author: Bin Hua
lastmod: 2022-05-17T06:28:01Z
date: 2022-05-17T06:28:01Z
tags: ["GitHub", "Codespaces", "试用"]
---

刚在玩「炉石」，突然来了一封邮件，是 Github Codespaces 开放通知，我能试用 GitHub Codespaces 了，先简单的试用一下。

![](/imgs/try-github-codespaces-001.jpg)

### GitHub Codespaces 是什么？

可以将它理解为是一个开发机，关于它的更多信息，可以查看[这里](https://docs.github.com/en/codespaces)。

### 它解决了我的什么问题？

可以在浏览器上编写代码，并能同时能提交到 GitHub 上的仓库里。其实这个方式目前在 GitHub 上是有一个隐藏技巧的，打开某一个仓库，比如地址是 `https://github.com/tourcoder/tourcoder`，按 `.` 号键或者将地址改成 `https://github.dev/tourcoder/tourcoder`，即把 `github.com` 部分改成 `github.dev`，即可打开一个 VS Code 的编辑器。

我比较看重的是，用 VS Code 连接它时，相对较稳定。要知道我之前用 VS Code 连接自己的开发机，总是过一段时间开发机就会处于假死状态。

### 基本流程

进入到 [Codespaces](https://github.com/codespaces) 的主界面，点击 `New codespace`

![](/imgs/try-github-codespaces-002.jpg)

选择相关的参数，比如仓库，分支等，然后点击创建即可。

![](/imgs/try-github-codespaces-003.jpg)

点击创建后，即开始自动配置，这个过程会花费一些时间，但是会自动完成。完成后，两种选择

![](/imgs/try-github-codespaces-004.jpg)

选择一，等待，然后会自动在当前浏览器中打开

![](/imgs/try-github-codespaces-005.jpg)

选择二，点击下面的`在 VS Code Desktop 中打开`，它会自动打开 VS Code，询问是否安装相关的插件

![](/imgs/try-github-codespaces-006.jpg)

![](/imgs/try-github-codespaces-007.jpg)

选择安装即可。到此，基本上就可以使用了。

### 一点小尝试

我尝试在浏览器端打开的 Codespace 增加了点内容，然后关闭该页面，结果显示，这些内容是保存在 Codespace 中的，没有提交到 GitHub 上。

![](/imgs/try-github-codespaces-008.jpg)

我尝试用 iPad pro 上的 Chrome 打开它，一切正常。

### 其他

进入到 [Codespaces](https://github.com/codespaces) 的主界面，可以看到刚才创建的 Codespaces，可以对它进行相关的操作。

![](/imgs/try-github-codespaces-009.jpg)

比如可以将当前的修改后的内容保存成一个新的分支，或者停用，甚至删除这个 Codespace。

### 注意点

1. 似乎不能同时打开同一个 Codespace，当我同时打开同一个 Codespace 时，连接都断开了。

2. 在浏览器打开 VS Code 的编辑器时地址是不一样的，前面说到的 `github.dev`，只是将 `github.com` 改成 `github.dev`，其他没变，但 Codespace 的地址是 `https://githubusername-orgname[option]-projectname.xxx.github.dev` 这样的格式。

### 说明

在使用过程中，我发现一些信息

1. 当一个仓库是空的时候，是不能创建 codespace 的。

2. Codespace 中的配置文件可以参考[这里](https://docs.github.com/cn/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers)，比较有意思的是 `git` 中的 `user.name` 默认来自 github 上主账户设置名称。

3. 每个 codespace 都有一个可以预览的链接，格式和 codespace 的地址差不多，只是改了域名，格式为 `https://githubusername-orgname[option]-projectname.xxx.githubpreview.dev`，预览需要登录 GitHub 账号，且只有自己能够预览。

4. 基本可以将 Codespaces 理解成是一个配置好一大半，并且和 GitHub 高度结合的开发机。

