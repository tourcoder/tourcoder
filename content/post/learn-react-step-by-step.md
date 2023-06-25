---
title: "React 学习笔记"
slug: "learn-react-step-by-step"
author: "Bin Hua"
date: 2023-06-25T06:18:06Z
tags: ["react", "前端"]
draft: true
---

一直以来，我在学习一个新的框架或语言的时有个特别的习惯，用这个框架或语言写一个博客系统，这几乎成了我用新技术写东西的 “hello world”，这次学习 react 也不例外。至于 react 是什么，可以看其[官网](https://react.dev/)介绍。

### 学习内容和目的

学习 react 的内容，并用它写一个博客系统。博客的主要内容有：

**前台**

- 文章列表页（首页）

- 文章详情页面

- 访客评论

**后台**

- 登录

- 文章列表

- 文章编辑

- 文章删除

- 登出

### 准备工作

安装好对应的环境，比如 node，npm（yarn），npx，mongodb（本项目所用的数据库）

### 具体步骤

**初始化 blog 应用**

通过 `npx create-react-app blog` 命令初始化创建一个名叫 blog 的 react 应用，执行该命令后，在 loading 一段时间后就会创建这个 blog 应用。其结构如下

![](/imgs/learn-react-step-by-step-001.png)

在 `public` 文件夹下的文件中

- favicon 是个性化图标

- index.html 是应用的主 html 文件

这两个是最主要的，logo192.png logo51.png 和 maifest.json 是 PWA 的文件，robots.txt 是 seo 用到的文件，这几个文件是非必须的。

在 `src` 文件夹下，

- app.js 主组件文件

- index.js 入口文件

- index.css 和 app.css 样式文件，非必须

- logo.svg logo 图片，非必须

- app.test.js 测试文件，非必须

- reportWebVitals.js 性能上报文件，非必须

- setupTests.js 测试文件，非必须

剩下的就是 package.json 和 readme 文件了。



