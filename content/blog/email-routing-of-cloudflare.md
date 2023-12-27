---
title: "试用 Cloudflare 的电子邮箱路由"
slug: "email-routing-of-cloudflare"
author: "Bin Hua"
lastmod: 2021-12-21T20:07:07Z
date: 2021-12-21T20:07:07Z
tags: ["Cloudflare", "email", "routing"]
---

今天收到了 Cloudflare Email Routing 的试用的通知邮件

![](https://storage.tourcoder.com/tcblog/email-routing-of-cloudflare-001.jpg)

立刻做了下测试。

Cloudflare Email Routing 中文翻译电子邮件路由，Cloudflare 给它的定义是`为您的域创建自定义电子邮件地址并将传入电子邮件路由到您的首选邮箱`。直白点说，把发到该域名的电子邮件转发到自己指定的邮箱。

配置完如下图，我的域名是 `tourcoder.com`

![](https://storage.tourcoder.com/tcblog/email-routing-of-cloudflare-002.jpg)

自定义地址：可以设定一个基于域名的邮箱地址，可以将发到该设定邮箱的邮件转发到指定的邮箱，比如我使用了 `code@tourcoder.com`，可以添加多个。

Catch-all 地址：如果不想设定邮箱地址，可以开启这个。只要发到后缀为 `@tourcoder.com` 的邮件都会被转发到指定的邮箱。

通过电子邮件发送 DNS 记录：设置 DNS，让该服务启动，点击一键配置，Cloudflare 会配置 DNS。需要注意的是，如果已经有默认的 MX 记录，需要手动先删除，因为 Cloudflare 的自动配置目前还不能自动覆盖，会出错。

目标地址：就是接收邮件的地址，也可以添加多个，同时该地址需要认证。

#### 使用感受

邮件转发的速度挺快。

#### 期待

希望后期能够增加发邮件的路由功能。
