---
title: "CSS3 中自定义字体"
slug: "custom-font-in-css3"
author: "Bin Hua"
lastmod: 2020-08-13 09:14:46
date: 2018-05-07 07:38:42
tags: ["web前端", "webfont", "fontawesome"]
---

虽然现在有 Google web font 这么一个好用的字体库，但有时网页中需要用到自定义的字体，在 css3 中就能很好的解决这个问题。

**使用**

用 `font-face` 引入这个字体

```
@font-face {
  font-family: 'fontname';
  src: url('../fontname.eot');
  src: url('../fontname.eot?#iefix') format('embedded-opentype'),
       url('../fontname.woff') format('woff'),
   url('../fontname.ttf') format('truetype'),
   url('../fontname.svg#SingleMaltaRegular') format('svg');
}
```

然后在需要用到的地方直接使用即可

```
font-family: fontname;
```

**浏览器支持情况**

一、TureTpe(.ttf)格式：

.ttf 字体是 Windows 和 Mac 的最常见的字体

支持这种字体的浏览器有 IE9+, Firefox3.5+, Chrome4+, Safari3+, Opera10+, iOS Mobile Safari4.2+

二、OpenType(.otf)格式：

.otf 字体被认为是一种原始的字体格式，其内置在TureType的基础上

支持这种字体的浏览器有 Firefox3.5+, Chrome4.0+, Safari3.1+, Opera10.0+, iOS Mobile Safari4.2+

三、Web Open Font Format(.woff)格式：

.woff 字体是 Web 字体中最佳格式，他是一个开放的 TrueType/OpenType 的压缩版本，同时也支持元数据包的分离

支持这种字体的浏览器有 IE9+, Firefox3.5+, Chrome6+, Safari3.6+, Opera11.1+

四、Embedded Open Type(.eot)格式：

.eot 字体是 IE 专用字体，可以从 TrueType 创建此格式字体

支持这种字体的浏览器有 IE4+

五、SVG(.svg)格式：

.svg 字体是基于 SVG 字体渲染的一种格式

支持这种字体的浏览器有 Chrome4+, Safari3.1+, Opera10.0+, iOS Mobile Safari3.2+
由此可见在 @font-face 中至少需要 .woff 和 .eot 两种格式字体，至于支持更多的浏览器，可以根据上面的情况来调整。

**字体生成器**

去 [Font Squirrel](https://www.fontsquirrel.com/tools/webfont-generator) 可以轻松的在线生成一些格式的字体。