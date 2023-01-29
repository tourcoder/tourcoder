---
title: "获取 Nginx Cloudflare 架构中客户端真实的 IP"
slug: "get-client-realip-in-the-nginx-cloudflare-architecture"
author: Bin Hua
lastmod: 2021-12-23T12:34:42Z
date: 2021-12-23T12:34:42Z
tags: ["Cloudflare", "nginx"]
---

在 nginx+cloudflare 的架构中，如果不做设置，获取到的客户端 IP 地址是 cloudflare 的地址，而非真实的客户端 IP，需要做如下的设置。

在编译安装 nginx 的时候，增加参数 `--with-http_realip_module`，即

```
./configure --with-http_realip_module
```

同时在 `nginx.conf` 的 http 块中增加

```
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 104.16.0.0/12;
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 131.0.72.0/22;
set_real_ip_from 141.101.64.0/18;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 2400:cb00::/32;
set_real_ip_from 2606:4700::/32;
set_real_ip_from 2803:f800::/32;
set_real_ip_from 2405:b500::/32;
set_real_ip_from 2405:8100::/32;
set_real_ip_from 2c0f:f248::/32;
set_real_ip_from 2a06:98c0::/29;
real_ip_header CF-Connecting-IP;
```

最后在程序中直接获取就可以，比如 koa 的 nodejs 程序中获取 `ctx.request.ip`。
