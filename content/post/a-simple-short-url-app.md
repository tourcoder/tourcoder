---
title: "一个简单的短网址系统"
slug: a-simple-short-url-app
author: Bin Hua
lastmod: 2020-08-13T09:31:40Z
date: 2019-07-15T03:42:19Z
tags: ["App", "Productivity", "shorturl"]
---

厌烦了现在博客的 url 长地址，虽然在 SEO 上是有一定的帮助，但分享起来，还是比较麻烦，索性就给本博客增加了一个外部的短网址系统。当前博客程序用的是 ghost，它本身提供了一套 API，只是因为懒得去读它的文档，索性就是写了个外部的。

### 基本信息

- 开发语言: NodeJS (koa2)

- 运行环境: Debian 8

### 主要问题

- 路由问题

    根据 koa-router 的路由资料来操作即可
    
- 外部调用

    说是外部调用，其实有两个功能，生成和展示。
    
    - 展示部分代码
    
        ```
        <script type="text/javascript">
        var hoho = "domainname/links?link="+window.location.href;
        $.ajax({
                type: "GET",
                url: hoho, 
                success: function(data) {
                        $("p#shorturlforthispost").html("本文短网址: <a href='domainname/" + data + "'>domainname/" + data + "</a>")
                },
                error: function(jqXHR, error, errorThrown) {
                        //console.log(jqXHR.status);
                }
         });
         </script>
         ```
    
    通过 `jQuery` 的 `$.ajax` 远程获取返回的内容即可。
    
    - 生成部分的方式
    
        这个博客有两百来篇文章，我懒，不想再逐条去设置，索性就让用户在访问的过程中帮我生成。当访客访问某一篇文章，会自动的为这篇文章生成一个短网址。
        
### 总结

因为代码比较简单，总共就 80 行代码，就不开源了，核心的内容在上面也讲过。

更新：现在每天能产生几百个垃圾链接，而我没有足够的时间去维护清理，只能关闭对外公共方式，只作为本博客的附属服务。其实如果你能看懂我上面的代码，你知道该如何生成自己的短网址 :)

更新：本站短网址功能已经取消。