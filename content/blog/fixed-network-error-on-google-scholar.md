---
title: "修复 Google Scholar 无法访问的问题"
slug: "fixed-network-error-on-google-scholar"
author: "Bin Hua"
date: 2021-10-02T13:02:21Z
tags: ["Google", "scholar", "IPv6"]
draft: false
---

想必频繁访问 [Google Scholar](https://scholar.google.com/) 网站时或多或少遇到过下面的这个问题 

```
We're sorry...

... but your computer or network may be sending automated queries. To protect our users, we can't process your request right now.
See Google Help for more information.
```

造成这个原因的是科学上网的 IP 被 Google 拉黑了。解决这个问题的办法主要有三种

1. 找一个没有被 Google 拉黑的 IP

2. 用[谷歌上网助手](https://chrome.google.com/webstore/detail/%E8%B0%B7%E6%AD%8C%E4%B8%8A%E7%BD%91%E5%8A%A9%E6%89%8B-%E5%BC%80%E5%8F%91%E7%89%88/cieikaeocafmceoapfogpffaalkncpkc?hl=zh-CN)这个浏览器插件。

3. 修改 Hosts 用 IPv6 访问，Google Scholar 拉黑的基本是 IPv4，本文介绍的是通过 IPv6 开启对 Google Scholar 的访问，具体步骤如下

先开启服务器的 IPv6 服务，获取 IPv6，然后 SSH 到服务器，在 root 权限下执行下面的内容

```
echo '2404:6800:4008:c06::be scholar.google.com
2404:6800:4008:c06::be scholar.google.com.hk
2404:6800:4008:c06::be scholar.google.com.tw
2404:6800:4005:805::200e scholar.google.cn' >> /etc/hosts
```

即可。
