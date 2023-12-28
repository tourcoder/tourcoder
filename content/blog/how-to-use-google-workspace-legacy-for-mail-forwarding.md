---
title: "如何使用 Google Workspace legacy 进行邮件转发"
slug: "how-to-use-google-workspace-legacy-for-mail-forwarding"
author: "Bin Hua"
date: 2022-04-09T08:12:53Z
tags: ["GSuite", "Google", "Google Workspace", "Email"]
draft: false
---

Google 终于给 GSuite legacy 后续进展下了一个定论，要么付费升级使用，要么使用 no-cost 方案，no-cost 方案缺少了一些核心的功能，比如 Gmail。具体说明看[这里](https://support.google.com/a/answer/60217#nocost)。


正好在 Twitter 上刷到一个推友说到的问题，子域名邮箱转发的问题，他使用了 Google Domains 和 Cloudflare，可惜它们不支持子域名，推友 hack 了下，还有点小问题，讨论看[这里](https://twitter.com/oasisfeng/status/1512275422045929472)。

其实关于域名的邮件转发，不管是子域名，还是主域名，基于 GSuite（现在叫 Google Workspace） 就有很好的解决方案，我已经使用几年了，特分享下，下面统一称呼 `GSuite` 为 `Google Workspace`，建议看完整篇内容后再进行操作。

第一步：

进入到 Google Workspace 的管理后台，`https://admin.google.com`，登录后去添加需要的二级域名，比如 `subdomain.mydomain.com`，如果已经添加了，忽略。

第二步：（最关键的一步）

升级你的套餐到一个收费套餐，升级完成后，等其他操作完成后，可以取消，这个过程应该只要花几美分。

为什么要升级呢？

在 Google Workspace 中 Gmail 里有一个路由功能，不升级的时候，该路由功能叫 `Routing`，只能将邮件转发到主域名的邮箱，看下图

![](https://storage.tourcoder.com/tcblog/how-to-use-google-workspace-legacy-for-mail-forwarding-01.jpg)

![](https://storage.tourcoder.com/tcblog/how-to-use-google-workspace-legacy-for-mail-forwarding-03.jpg)

而升级后，该路由功能叫 `Default routing`，可以将邮件转发到任意邮箱，如下图

![](https://storage.tourcoder.com/tcblog/how-to-use-google-workspace-legacy-for-mail-forwarding-02.jpg)

第三步：

增加一个或多个 `Default routing`，第一项选择 `All recipients`，也可以根据自己的需要填写，后面也可以自己修改的。在 `Envelope recipient` 处写转发到的邮箱，比如将所有邮件转发到了 `code@tourcoder.com`，如下图

![](https://storage.tourcoder.com/tcblog/how-to-use-google-workspace-legacy-for-mail-forwarding-04.jpg)

第四步：

降级，其实所谓的降级就是取消购买 License。

特别注意点：

我是差不多七年前，我在升级公司用的 `Google Workspace Legacy` 时，误操作将自己个人的账号升级了，然后发现了这个差别。

这句话也就意味着我是七年前做的操作，我不清楚这操作是否还适用于当前时间。

这七年来，所有邮件转发都非常稳。

#### 补充

在推特上一个傻几把屌说我不了解政策，说我会把大家带沟里去，他特码的自己不去花几美分试试，就特码的信口开河的猜。看了他的话，我买了个账号试试，本文写的办法依旧可以，完全没有问题。
