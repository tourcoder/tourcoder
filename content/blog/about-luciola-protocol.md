---
title: "关于‘萤火虫协议’一点想说的"
slug: "about-luciola-protocol"
author: "Bin Hua"
date: 2026-10-06T06:32:24Z
tags: ["luciola", "protocol", "twitter", "x", "mastodon"]
draft: false
---

自从 Twitter 变 X，产品本身是越做越好了，但对我这类用户来说，体验越来越糟糕。泛滥的垃圾信息，失控的算法，被操控的舆论导向等等，它的核心 DNA 也有所改变，从一个信息流通的广场，变成了一台垃圾信息制造机。

今年 1 月份的那一次“比基尼”风波后，我因厌烦 X，索性开发了个基于 ActivityPub 协议的网站 [xcoder.org](https://xcoder.org)，从此，基本就在那边更新自己的动态。

但在维护这个网站的过程中，有个强烈的感觉：ActivityPub 协议已经被 Mastodon “裹挟”了，或者说围绕 ActivityPub 做这类产品的人渐渐丢掉了自己的理想和坚持，因为功能的实现，表现形式，API 等等很多东西都被 Mastodon 给“定义”了。

最直观的感受有二：

- 有用户发邮件来，希望我给 xcoder 加 Mastodon 上的一个功能
- 要与其他节点互通，基本都得按 Mastodon 设计的那套 API 来

我极度反感！ 

10 月 2 日睡不着，对着 iPad 发呆时来了点灵感，随手写下了“萤火虫协议”的草稿，10 月 3 日和 AI 聊了聊，完善后在 GitHub 发布了初稿。

### 为什么叫 Luciola

我一直怀念 Google Buzz，所以最初我想用的名字是 buzz/buzzr，但无奈这个名字被各种协议项目等占得七七八八。

就改成了 AIN，取之于本协议最核心的三个概念：**A**ction（行为）、**I**dentity（身份）、**N**ode（节点），但也遇到了同样的问题。

最后我想：这是一个面向个人和 AI agent 的协议，参与者都是独立的个体，独立的节点，一闪一闪，有点像萤火虫，最后就定下来拉丁语中的萤火虫 -- Luciola。

### 资源

协议的初稿已经在 GitHub 上开源，AI Agent 也正在努力的开发基于协议的演示产品，我审核后🤭，也会开源出来

- 组织地址：[https://github.com/luciolaprotocol](https://github.com/luciolaprotocol)

- 协议地址：[https://github.com/luciolaprotocol/luciola](https://github.com/luciolaprotocol/luciola)