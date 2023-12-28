---
title: "将博客程序换回了 Ghost"
slug: "back-to-ghost-and-find-a-bug"
author: "Bin Hua"
date: 2018-11-26 14:12:23
tags: ["bug", "ghost", "GitHub Pages"]
draft: false
---

如前面所说，我的博客在 Github Pages 上架设了一段时间，随着我在 Github 的私有库到期，我不计划续费，架设在 Github Pages 上的博客自然要迁出。其实不用迁出用公开库也行的，只是我不愿意让自己的博客在公开库中。

图省事，直接买了 aws，用 Ghost，之前我的文章中也介绍过如何安装，有兴趣的可以去翻翻，不过不喜欢折腾的人，我建议用官方最新的方式，具体的查看他们的官方账户 [Ghost](https://github.com/tryghost/ghost)，按照一贯的作风，我还是会折腾一下，将 PWA 功能增加进去。

另外刚使用，就发现了他们的 bug，具体看这里的视频 [bug in ghost](http://https://www.dropbox.com/s/6hf8zrdd1zvxeat/Screen%20Recording%202018-11-26%20at%209.54.33%20PM.mov?dl=0)

#### Reproduce

OS: macOS Mojave 10.14.2 Beta (18C48a)

Browser: Firefox 63.0.3 (64) / Safari 12.0.2 (14606.3.4)

Ghost-CLI version: 1.9.8

Ghost version: development

Server OS: centOS 7

Installed ghost with command `ghost install local`, and `new story`, and you will get this bug.
