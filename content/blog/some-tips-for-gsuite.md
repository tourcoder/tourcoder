---
title: "G Suite 的设置贴士"
slug: "some-tips-for-gsuite"
author: "Bin Hua"
lastmod: 2019-04-11 13:38:14
date: 2019-04-11 13:38:14
tags: ["Gmail", "Google", "gsuite", "googlecloud", "oracle", "甲骨文"]
---

Thomas Kurian 不愧是从 Oracle 过来的，没多久就给 Google Cloud 来了一波骚操作，作为一个资深用户，我对他的这波操作还是有异议的，比如 G Suite 取消了年度支付的折扣。

废话少说，本博文的重点是 G Suite 的一些设置贴士

1. 在注册的过程中，发现无法进入该怎么办？

    这里的无法进入有多个原因，其中有个很直接的解决办法，直接访问 `https://admin.google.com/setup/u/0/apps/verification`，这个链接也可以做一些不太好的事情，这就不展开说了。
    
2. DKIM 要不要设置，如何设置？

    DKIM 一定要设置，设置的方式是进入 G Suite 后台，在菜单 `Apps - G Suite - Gmail - Authenticate email`，在选择你的域名，然后创建一个记录，建议这里选择 1024，创建完成后，去域名处进行相关的解析即可。同样，SPF 也应该是设置的。