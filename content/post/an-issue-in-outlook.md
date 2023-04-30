---
title: "MS OFFICE OUTLOOK中的问题"
slug: an-issue-in-outlook
author: "Bin Hua"
lastmod: 2020-07-18 06:14:55
date: 2009-01-21 05:08:00
tags: ["bug", "outlook"]
---

今天同事使用了新的邮件刊模板，然后生成的邮件刊，在写的过程中他使用了

```
.Title_English{background:url(images/title_English.gif) no-repeat left top;}
```

这样的样式，来进行一个背景的定义，得到的反馈是，在outlook中，该图片无法显示，这里说明下，具体的原因是因为outlook不支持的原因导致的。outlook还可能不支持的属性如下

```
Forms
Background images
Animated GIFs
Flash
Float or position commands
Alt tags in images
```

做页面，写前端的朋友要注意哦。更多的知道，请查看这里

#### 解决方法：
 
- 尝试TABLE的形式 

- 尝试用插入图片不用背景，这里有一个关于图片重复的问题，详细稍后送上 