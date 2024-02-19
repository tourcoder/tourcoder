---
title: "一个 iOS 开发的小经验"
slug: "a-little-experience-in-ios-development"
author: "Bin Hua"
date: 2024-02-19T06:54:38Z
tags: ["iOS", "macOS"]
draft: false
---

在 iOS 开发中“神奇”的事情很多，但最神奇的可能就是当你遇到问题时，你能通过搜索引擎找到别人提供的“一万种”该问题的办法，并且都成功的解决了这个问题，但就是解决不了你的。比如这个 “`Command PhaseScriptExecution failed with a nonzero exit code` 的 xcode 编译时候的错误”，可以看知乎上的[讨论](https://zhuanlan.zhihu.com/p/661790112)。这里不讨论这个问题的解决办法，因为我这次开发遇到这个问题到现在还没解决，哈哈哈

这里只是分享下我多年前开发 iOS 应用的流程，也许这流程放在现在依旧合适。

- 先画 UI

- 再做 UX

- 做数据

- 最后引入库，比如用 Cocoapods 这种东西

这种方式不只是符合个人开发，同样也适合团队开发，能省很多痛苦的时间。