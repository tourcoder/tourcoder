---
title: "GitHub 的一个巧妙设计"
slug: "so-cool-feature-on-github"
author: "Bin Hua"
lastmod: 2019-06-04 15:17:27
date: 2019-06-04 15:17:27
tags: ["GitHub", "风控"]
---

访问 GitHub，收到了如下的提醒

![](/imgs/so-cool-feature-on-github-01.png)

心想我邮箱早就验证过了，怎么还会要求这个，点进去后发现是这样的

![](/imgs/so-cool-feature-on-github-02.png)

突然意识到，是不是我的邮箱挂了？赶紧查看邮箱，果不其然，邮箱挂掉了。

为什么说 GitHub 设计巧妙呢？猜想是这么一回事，我今天提交了 40 几个 commit，然后又向主库提交了几个 PR，根据我的设置，每次提交后，GitHub 都会向我的邮箱发送一封通知邮件，因为我的邮箱挂了，GitHub 收到了退回邮件，触发了他们的风控系统，出现了这个情况。