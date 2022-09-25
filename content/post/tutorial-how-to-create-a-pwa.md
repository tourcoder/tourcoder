---
title: "创建一个 PWA"
slug: "tutorial-how-to-create-a-pwa"
author: Bin Hua
lastmod: 2022-09-25T04:51:32Z
date: 2022-09-25T04:51:32Z
tags: ["pwa", "Google", "教程"]
---

PWA 是 Progressive Web Apps 的简称，翻译过来就是渐进式 Web 应用。由 Google 提出来的 web 技术，我第一次知道它是在 2017 年的 Google 开发者大会上。我那时希望它能越来越强大，能直接干掉原生的应用。2018 年也做过一个简单的尝试，将自己的博客换成了 PWA，具体看[这篇](https://tourcoder.com/upgrade-to-pwa/)，但几年下来，回头看看，似乎这阵风并没有吹很大。

下面写一个简单的 PWA，它和写网站差不多，但在网站上增加了一些东西。

先写一个 HTML 页面，代码如下

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PWA demo</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div>
    <p><img src="icon.png"></p>
    <p>This is a demo</p>
  </div>
</body>
</html>
```

以及里面引用的 `style.css` 和一个图片 `icon.png`

```
body {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 16px;
	font-family: Arial;
}
```

到这里，网站就写完了，将它放到服务器上，可以通过浏览器来访问，但它还不是一个 PWA，比如当没有网络的时候，我们就无法使用它，而且现在还不能像原生的应用一样，被安装到手机里，必须要依赖浏览器，才能被访问到。PWA 通过 `Service Worker` 解决了离线的问题，`Service Worker` 的作用不只是如此，将上面的代码更新为

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PWA demo</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div>
    <p><img src="icon.png"></p>
    <p>This is a demo</p>
  </div>
  <script>
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("sw.js")
      .then(reg_status => {
        console.log(reg_status);
      })
    }
  </script>
</body>
</html>
```

`Service Worker` 的注册也可以是在指定的域下面，但如果指定域了，它就只能作用于该域下面的所有页面。

```
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js", {
        scope: "/sub_path/sub_domain"
    })
    .then(reg_status => {
        console.log(reg_status);
    })
}
```

再说 sw.js 这个文件，先看代码

```
self.addEventListener('install', () => {
  // 安装回调
  console.log('安装')
})

self.addEventListener('activate', () => {
  // 激活回调
  console.log('激活')
})

self.addEventListener('fetch', event => {
  console.log('抓取' + event.request.url)
})
```

一个 `Service Worker` 的生命周期是这样的

先注册，然后安装，然后激活，最后是结束，所以上面的代码就很好理解了。

最后引入 `manifest.json` 文件，代码如下

```
{
  "name": "PWA Demo",
  "short_name": "PWA Demo",
  "display": "standalone",
  "start_url": "/",
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "icon-144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "icon.png",
      "sizes": "256x256",
      "type": "image/png"
    }
  ]
}
```

`Manifest.json` 文件是 Web 应用的配置文件，用于指定应用的显示名称、图标、应用入口文件地址及需要使用的设备权限等信息。也是扩展的配置文件，指明扩展的各种信息。

最后将代码上传到服务器，通过网址访问，然后在浏览器中，将该页面增加到桌面即可。

测试地址： [https://pwa.demo.tourcoder.com](https://pwa.demo.tourcoder.com)

### 参考教程

[渐进式 Web 应用（PWA）](https://developer.mozilla.org/zh-CN/docs/Web/Progressive_web_apps)
