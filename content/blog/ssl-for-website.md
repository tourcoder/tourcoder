---
title: "给网站加 SSL"
slug: "ssl-for-website"
author: "Bin Hua"
date: 2017-03-05 06:56:35
tags: ["ssl", "https"]
draft: false
---

信息安全无容置疑，现在好多网站还是 http 的方式在跑着，应该早点转到 https。

ssl 就是一道护盾，虽然以前买个 ssl 证书很贵，但现在便宜了很多，而且还有免费好用的，比如 Let's Encrypt 就是一家。

**预备条件**

服务器 ubuntu 16.04

证书 Let's Encrypt 的 ssl

**安装**

先更新系统

```
apt update && apt upgrade -y
```

![](https://storage.tourcoder.com/tcblog/ssl-for-website-01.png)

安装需要到的工具

```
apt install -y zip build-essential
```

![](https://storage.tourcoder.com/tcblog/ssl-for-website-02.png)

安装 Let's Encrypt client:

```
apt install -y letsencrypt
```

![](https://storage.tourcoder.com/tcblog/ssl-for-website-03.png)

查看版本

```
letsencrypt --version
```

![](https://storage.tourcoder.com/tcblog/ssl-for-website-04.png)

获取证书

```
letsencrypt certonly -d yourdomain.com -d www.yourdomain.com --email username@gmail.com --agree-tos --standalone
```

执行完成后，在 `/etc/letsencrypt/live/yourdomain.com` 目录下就会有你刚申请好的证书和私钥。

这里记得把域名指向该服务器的 IP

最后直接在 Nginx 或 Apache 上配置下，你的网站就跑在了 ssl 下咯。

**update@20180604 : 给 GitHub Pages 设置 ssl**

博客移动到了 Github，主要是每次写博客的时候，只要写一个 Markdown 的文件就行了，简单方便。

- 在 GitHub 上创建一个库，然后设置部分如下图设置  如果你使用 GitHub 的网址，可以设置 https，但如果你使用自己的域名，就需要借用到第三方服务。

- cloudflare 如上面所说，你需要借用到第三方服务，比如 cloudflare，这是一个非常棒的服务，只是有时候会出现抽风的现象。 注册 cloudflare 后添加域名，进入管理界面，点顶部菜单 crypto，在下面 SSL 中选择 Flexible  选择 Page Rules，创建一条 Rule，设置 HTTP 总是用 HTTPS 方式访问  

就这样，完成了。