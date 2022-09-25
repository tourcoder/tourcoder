---
title: "创建一个 PWA"
slug: "tutorial-how-to-create-a-pwa"
author: Bin Hua
lastmod: 2022-09-25T04:51:32Z
date: 2022-09-25T04:51:32Z
tags: ["pwa", "Google", "教程"]
draft: true
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

到这里，网站就写完了，将它放到服务器上，可以通过浏览器来访问，但它还不是一个 PWA，比如当没有网络的时候，我们就无法使用它，而且现在还不能像原生的应用一样，被安装到手机里，必须要依赖浏览器，才能被访问到。PWA 通过 `service worker` 解决了离线的问题。


### 参考教程

[渐进式 Web 应用（PWA）](https://developer.mozilla.org/zh-CN/docs/Web/Progressive_web_apps)
