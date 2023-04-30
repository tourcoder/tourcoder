---
title: "一些压力测试工具"
slug: testing-tools
author: "Bin Hua"
lastmod: 2020-08-13 09:13:12
date: 2018-03-07 07:31:56
tags: ["工具", "abtest"]
---

压力测试是一个 web 应用必须要做的，不只是为了测试程序的强壮性。压力测试的服务和工具很多，比如网上就很专业的压力测试的服务，也有 ab，webbench，siege，tcpcoy 等这样的测试工具。

**ab 测试**

ab 是 apache bench，从名字就可以看出是 apache 附带的一个工具，下载地址在[这里](http://httpd.apache.org/)。

因为它在 macOS 下多少有点问题，就拿 windows 简单说明，在终端中进入到 apache 所在的安装路径，比如 `d:\apache`， 执行命令

```
ab -n 请求数 -c 并发数 http://tourcoder.com/
```

运行后的结果就是你的测试报告。如果遇到需要登录的页面，使用开发者工具，比如 Chrome Dev Tools 找到登录会话的 Cookies，然后执行命令

```
ab －n 请求数 －C key＝value http://tourcoder.com/
```

如果 Cookies 较多，则设置头部

```
ab -n 请求数 -H "Cookie: Key1=Value1; Key2=Value2" http://tourcoder.com/
```

更多的用法，请去官网查阅资料。

**webbench**

webbench 也是一款不错的压力测试工具，用法和 ab 差不多，终端中执行命令

```
webbench -c 并发数 -t 运行测试的时间 http://tourcoder.com
```

即可。

**siege**

siege 也是一款不错的压力测试工具，用法和上面一样，在终端中输入命令

```
siege -c 并发数 -t 运行测试的时间 http://tourcoder.com
```

需要注意的是，这里的运行测试的时间是可以有单位的，如果没有写单位表示的是分钟，如果带单位，比如 s 表示秒。

**tcpcopy**

这是国人开发的一款很好的测试工具，说它好是因为它能够导入线上流量进行测试，上面的基本都是在非生产力环境下的测试，这个是可以实时的将线上流量导入到测试环境中。目前开源在 [GitHub](https://github.com/wangbin579/tcpcopy)，具体的用法请自行查看。

**一些概念**

特别注明：这些概念来之网络上的整理。

- 吞吐率（Requests per second）

    概念：服务器并发处理能力的量化描述，单位是 reqs/s，指的是某个并发用户数下单位时间内处理的请求数。某个并发用户数下单位时间内能处理的最大请求数，称之为最大吞吐率。

    计算公式：总请求数 / 处理完成这些请求数所花费的时间，即 `Request per second = Complete requests / Time taken for tests`

- 并发连接数（The number of concurrent connections）

    概念：某个时刻服务器所接受的请求数目，简单的讲，就是一个会话。

- 并发用户数（The number of concurrent users，Concurrency Level）

    概念：要注意区分这个概念和并发连接数之间的区别，一个用户可能同时会产生多个会话，也即连接数。

- 用户平均请求等待时间（Time per request）

    计算公式：处理完成所有请求数所花费的时间/ （总请求数 / 并发用户数），即 `Time per request = Time taken for tests / (Complete requests / Concurrency Level)`

- 服务器平均请求等待时间（Time per request: across all concurrent requests）

    计算公式：处理完成所有请求数所花费的时间 / 总请求数，即 `Time taken for / testsComplete requests` 可以看到，它是吞吐率的倒数。同时，它也=用户平均请求等待时间/并发用户数，即 `Time per request / Concurrency Level`。
