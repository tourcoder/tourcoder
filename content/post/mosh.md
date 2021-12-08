---
title: "Mosh 试用"
slug: "mosh"
author: Bin Hua
lastmod: 2021-12-08T12:42:55Z
date: 2021-12-08T12:42:55Z
tags: ["mosh", "shell", "iterm", "terminal"]
---

Mosh 全称 mobile shell，其官网是 [https://mosh.org/](https://mosh.org/)，特点很多，其中一个很重要的特点是比起 ssh 在一般网络状态下的稳定。因为我日常开发是在 macOS 上通过 ssh 到一台开发机上，因为网络导致的问题还是挺多的，所以这次试试 mosh。虽然早就知道这个，但还是第一次正式使用。

### 安装

在 macOS 上直接通过 homebrew 安装即可 `brew install mosh`

### 使用

和使用 ssh 一样方式

```
mosh username@server
```

即可。更多内容可以看其官网或者使用 `mosh -h` 查看。
