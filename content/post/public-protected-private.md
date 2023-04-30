---
title: "基本功要扎实：概述public、protected、private"
slug: public-protected-private
author: "Bin Hua"
lastmod: 2020-07-18 06:16:45
date: 2009-08-31 05:48:27
tags: ["dotnet"]
---

事实上public、protected、private就是水平访问和垂直访问的区别。水平访问就是能被类
的对象访问，垂直访问就是能被子类访问。public是即可水平访问又可垂直访问；private
是既不可水平访问也不可垂直访问；而protected是可以垂直访问，不可水平访问。

子类的对象也不可访问父类的protected成员

类的成员函数可以访问本类及子类对象的private、protected成员
