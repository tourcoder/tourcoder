---
title: "GitHub Down"
slug: "github-down"
author: "Bin Hua"
lastmod: 2018-10-25 07:47:50
date: 2018-10-25 07:47:50
tags: ["bug", "git", "GitHub"]
---

对全世界的程序员来说，几天前比较大的一个新闻应该就是 GitHub Down，GitHub 在毫无征兆的情况下突然挂了整整一天的时间。

到目前为止，GitHub 官方在其博客发了两篇文章 1 和 2。

从他们的两篇文章上来看，本次当机事件不是受黑客攻击导致，而仅是因为网络分区以及后续数据库的故障导致，GitHub 团队出于谨慎考虑，主动的采取一些措施，比如暂停 webhook events。

但我认为早在发生当机事件之前，GitHub 的部分功能已经出了问题，而且很长时间没有得到修复（没有发现？）

比如，我一直用的 chrome 插件 Octotree，它在读取私有库的时候，是需要 Personal access tokens 的，在发生当机事件前的很长一段时间，在读取私有库的时候，Octotree 总是无法正常工作，但当这次当机事件处理完成后，Octotree 自动的又好了，这期间我没有做过任何的操作。

同样，另外一个需要 Personal access tokens 的插件也发生一样的情况。

**想的多**

可能是我想得有点多，从这次当机事件，GitHub 给我的感觉是他们一直在暗箱操作一些事情。不知道是不是和被微软收购后有关系，难道是所有的服务要全部都迁移到 Azure？

当然经过这次事情，还是应该吸取个教训，商业团队工作流的东西，还是应该多点其他的选择。

另外，不知道是否有人统计过这次 GitHub 当机造成了多少钱的损失，期待 GitHub 后续给我们带来详细的报告说明。