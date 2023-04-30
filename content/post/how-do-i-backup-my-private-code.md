---
title: "我如何备份私有代码"
slug: "how-do-i-backup-my-private-code"
author: "Bin Hua"
lastmod: 2022-03-05T12:17:34Z
date: 2022-03-05T12:17:34Z
tags: ["GitHub", "Chaos"]
---

我一直用 GitHub 作为代码存储的主力工具，不用 GitLab 的原因是之前 GitLab 出了个针对中国和俄罗斯的政策，这里就不细说了，具体可以搜索下。GitHub 同样也做过类似的事情，比如无任何征兆的封禁了一些国家地区的账号。甚至有些项目中因为有伊朗的开发者贡献过代码，整个项目都被封掉了。比如 Aurelia 这个项目。

随着这次乌克兰俄罗斯的战争，这个势头越来越猛，让这些平台中立已经不可能的事情，很有可能下一个就会沦落到我的头上。

#### 以前的做法

如上面所说，我一直用 GitHub 作为代码存储的主力工具，GitHub 上有一份，本地有一份。

#### 现在的做法

考虑了下，我最后决定用 Google Cloud 的 Source Repositories 做备份。实现原理，通过镜像的方式保存到 Google Cloud 中。当 GitHub 这边有更新时，Google Cloud 这边会自动获取并更新。具体操作

进入 Source Repositories 后新增一个 repo，进入下面界面

![](/imgs/how-do-i-backup-my-private-code-001.jpg)

选择 `Connect external repository`

![](/imgs/how-do-i-backup-my-private-code-002.jpg)

选择要同步的 repo 来源，我这里自然选择 GitHub，然后完成即可。如标题下面的一段话所言

```
Select the Cloud project and hosted service that you want to connect. After you make this connection, commits pushed to the hosted service will be automatically synced to Cloud Source Repositories. 
```

每当 GitHub 那边的 repo 有更新会自动同步到这里。

#### 其他方案

不只是 Google Cloud 有这个方案，还有其他的服务也有这个方面，比如上面说到的 GitLab，还有 bitbucket，甚至一些开源的工具也可以，比如能自建的 gogs。

我选择 Google Cloud 的原因纯粹是因为它方便而已。
