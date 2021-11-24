---
title: "本博客升级到 PWA，附升级教程"
slug: upgrade-to-pwa
author: Bin Hua
lastmod: 2020-08-13 09:18:05
date: 2018-11-20 07:50:32
tags: ["GitHub", "jekyll", "pwa"]
---

昨晚将本博客升级到了 PWA，现在用安卓手机访问本博客，都会有「添加到桌面」的提示，按提示操作，你会得到一个本博客的 webapp 安装在你的手机里。

**PWA 是什么？**

PWA 全称 Progressive Web Apps，是 Google 几年前提出的技术，我在之前的文章中也有说明，关于更多的 PWA 说明，可以查看[官网](https://developers.google.com/web/progressive-web-apps/)

**本博客所用技术**

```
本博客搭建在 GitHub Pages 上，博客生成器是 Jekyll，主题是基于 hyde 二次开发而成，因为 hyde 在最新的 Jekyll 上有问题。
```

**升级过程**

整个过程比较简单，主要是处理几个地方

- 头文件 增加相关的 meta 和 link，你可以右键看我博客的源码，对比下就知道需要增加哪些内容了。 读取 `ServiceWorker` 文件 

```
<script type="text/javascript">   
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register("/sw.js");   
    } 
</script>
```

- Service Worker Serviceworker 文件是 PWA 的核心，使用 Hyde 主题的可以看[这里](https://github.com/jonpitch/progressive-hyde)， Jon 提供了一个很不错的 DEMO。 

**Lighthouse 测试**

下载 Chrome 上一个插件 Lighthouse，然后对它测试，我的测试结果如下

![](/imgs/upgrade-to-pwa-001.png)

然后根据每项进行优化即可，下图是我优化后的结果

![](/imgs/upgrade-to-pwa-003.png)

**部分问题的解决**

![](/imgs/upgrade-to-pwa-002.png)

[Text elements must have sufficient color contrast against the background](https://dequeuniversity.com/rules/axe/2.2/color-contrast?application=lighthouse)

最后，期待 iOS 早点全面支持 PWA。