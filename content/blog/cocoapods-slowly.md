---
title: "CocoaPods 慢"
slug: "cocoapods-slowly"
author: "Bin Hua"
date: 2017-03-22 07:00:43
tags: ["cocoapods", "iOS", "macOS"]
draft: false
---

CocoaPods 在 iOS/macOS 应用开发中经常用到，但因为墙等因素，会经常遇到问题，慢显得特别严重，这里提供一些解决办法，至于如何安装使用等基本问题，请去[官网](https://cocoapods.org/)查看

**方法一：更换源**

```
pod repo remove master
pod repo add master 新源库地址
pod repo update
pod setup
```

网上有很多镜像源，你可以搜索看看。

**方法二：手工添加索引库**

```
cd ~/cocoapods/repos/
```

将 CocoaPods 的库内容添加到这里即可。