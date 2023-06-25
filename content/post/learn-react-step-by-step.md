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

文章列表页（首页）

文章详情页面

**后台**

登录

文章列表

文章编辑

文章删除

登出

### 准备工作

安装好对应的环境，比如 node，npm（yarn），npx，mongodb（本项目所用的数据库）

### 具体步骤

**创建 blog 应用**

通过 `npx create-react-app blog` 命令创建一个名叫 blog 的 react 应用，执行该命令后，会 loading 一段时间就会创建一个应用。其结构如下


