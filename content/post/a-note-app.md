---
title: "一个笔记应用"
slug: "a-note-app"
author: Bin Hua
date: 2023-04-30T00:59:55Z
tags: ["笔记", "note", "notion", "evernote"]
draft: false
---

我一直喜欢三类应用，Twitter 的信息流类，Email 类和笔记类，这个我在[推特](https://twitter.com/tourcoder/status/1582641919909253120)上说过，打不开链接可以看[截图](https://storage.tourcoder.com/tcblog/a-note-app-01.png)。

### 我所理解的笔记

笔记犹如人生，开启的时候白纸一张，使用简单，记录下内容就会被保存在那里。整个过程就三个点

{{<mermaid>}}
graph LR
A(记录/收集)-->B(整理/学习)-->C(保存/回顾)
{{</mermaid>}}

市面上有很多非常优秀的笔记应用，但在使用它们的时候，我或多或少的感觉到有点别扭，要么使用复杂，要么不轻便。

现在是时候写一个笔记类的应用了。

### 方向选择

我有两个方向来做这个笔记应用

- 服务器主导

    一切以服务器为主，服务器端提供 API 接口，客户端服务于服务器端。

- 客户端主导

    以客户端为主，数据存储同步等借用第三方，比如 iCloud，Google Drive 等。

这两种方式各有各的特色，也各有个的优劣势。比如第一种方式要注意多个客户端和服务端的同步的问题等，我选择服务器主导这种方式。

### 技术栈

鉴于目前的技术能力以及我想学习一些知识，我会用下面的技术栈来实现这个笔记应用。

- Database：mongoDB

- API：Koa.js + Node.js(javascript)

- Web client：React

- iOS：Swift

- Android：待定

- Browser Extension：Plasmo
    
### 产品特点

之前自己想了很多，觉得产品有不少特点，但现在真的做的时候发现这个产品没有什么特点。

### 是否开源

我会将它通过 MIT 协议开源在 GitHub 上。地址是 [https://github.com/binge](https://github.com/binge)。

PS. 这篇日志也会随着这个笔记应用的更新不断更新。