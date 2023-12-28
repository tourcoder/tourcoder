---
title: "IRC 快速入门"
slug: "new-to-irc"
author: "Bin Hua"
date: 2021-05-30T10:33:28Z
tags: ["irc", "freenode", "libera"]
draft: false
---

最近 freenode 的收购方做了一些谜一样的操作导致大家都开始逃离 freenode 这个长达十多年的 IRC 服务。IRC 是一种网络聊天协议，freenode 根据该协议组成了聊天网络，其实也有其他的聊天网络，只不过 freenode 更为出名，基本是“古老”开源的标配了。

有人逃离，就需要有地方接受，一些人就搞了 libera.chat，借用这次迁移介绍下一些简单的 IRC 操作.

- 大致流程

    有很多客户端可以选择，这里我以 libera.chat 的 web 客户端为例，[https://web.libera.chat/](https://web.libera.chat/)，打开页面，在 Nick 处输入用户名，默认是没有密码的，然后进入。比如我以 tourcoder 这个昵称进入了聊天室

    ![](https://storage.tourcoder.com/tcblog/new-to-irc-001.png)

    这样即可在里面聊天了。左侧 # 是不同的频道/主题，可以搜索相关的频道/主题，然后加入

    ![](https://storage.tourcoder.com/tcblog/new-to-irc-002.png)

    频道/主题之间的切换点击即可，有些频道/主题是邀请机制的，也有些需要用户验证身份，比如 python 在 libera.chat 上的频道/主题

    ![](https://storage.tourcoder.com/tcblog/new-to-irc-003.png)

    将当前使用的昵称注册即可，在输入框输入命令 `/msg nickserv register 密码 email地址` 并回车执行

    ![](https://storage.tourcoder.com/tcblog/new-to-irc-004.png) 

    打开自己的邮箱，按邮件中说明的方式验证即可，这时再进入之前的 python 频道/主题即可发现已经可以访问了

    ![](https://storage.tourcoder.com/tcblog/new-to-irc-005.png)

- 其它操作命令

    更改昵称 `/nick 新昵称`

    加入某个频道/主题 `/join #频道名`，命令行版本的加入频道/主题的方式

    加入其它的聊天网络 `/server 其它聊天网络地址`，不是所有的频道/主题都会建立在 libera.chat 或者 freenode 上

最后推荐一款终端版本的客户端 [https://github.com/irssi/irssi](https://github.com/irssi/irssi)
