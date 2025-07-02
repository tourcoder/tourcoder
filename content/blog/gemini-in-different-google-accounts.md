---
title: "Gemini in Different Google Accounts"
slug: "gemini-in-different-google-accounts"
author: "Bin Hua"
date: 2025-07-02T02:58:07Z
tags: ["Gemini", "Google", "AI"]
draft: false
---

我很早前写过 Google 要做好 AI 先要把它混乱的账号体系给整理下，和那时候比，现在算是不那么乱了。这里分享下这几个账号的情况。

### gemini.google.com (Gemini app on iOS/Android)

这是 Gemini 官方的访问地址，因为账户不同基本被分成了三类，看图

![](https://storage.tourcoder.com/tcblog/gemini-in-different-google-accounts-001.png)

![](https://storage.tourcoder.com/tcblog/gemini-in-different-google-accounts-001.png)

![](https://storage.tourcoder.com/tcblog/gemini-in-different-google-accounts-001.png)

具体说明如下：

- Google Workspace Standard/Plus: 都会有 PRO/ULTRA 的标识，几乎畅用 Gemini。同时聊天内容有盾牌，获得企业级数据保护，数据不会被用于训练。单人订阅使用。

- Google Workspace Business Starter or G Suite: 无 PRO，有限使用 Gemini。同时聊天内容有盾牌，企业级数据保护，数据不会被 用于训练。单人订阅使用。

- Google Personal Account: 订阅版有 PRO/ULTRA 标识，几乎畅用 Gemini；未订阅的无标识。同时聊天部分无盾牌，没有企业级数据保护，对话可能会人工审核，并被拿去做训练。订阅版可家庭共享，最高 6 个人使用。

### Google Code Assist (VSCode/Gemini CLI)

- Google Workspace Account: 有限制的行为，所使用的 model 不是最新的，我目前用下来是 2.0，连 2.5 flash 都不是。

- Google Personal Account: 有限制的使用，但能用最新的 model。

需要注意的是，**Google Code Assist 并不需要账户拥有任何的订阅**，只要你有个账户即可使用，和 Google One/Google AI Pro(Ultra) 没有任何关系。唯一有关系的是，当你授权 Google Code Assist 后，会在你的 Google Cloud 自动创建一个受限的项目，这个项目你几乎没有任何的控制权。这里有个 bug，如果你的 Google Cloud 里本身有其它项目，VSCode 授权成功后会卡在登录视图。解决这个问题的办法：1. 换个账号登录；2. 删掉你现在有的项目。

### Google One / Google AI Pro(Ultra)

这是 Google Personal Account 的两个订阅，它们不是同一个东西。

Google One 的订阅主要作用体现在存储容量的大小，在 Gemini 的使用上是未订阅的受限版本；Google AI Pro(Ultra) 的订阅主要体现在 Gemini 使用上，几乎畅用。同时还赠送了存储容量。
