---
title: "iOS 中使用图标字体"
slug: how-to-use-icon-font-in-ios
author: "Bin Hua"
lastmod: 2020-11-23 23:57:03
date: 2019-09-06 06:45:31
tags: ["iOS", "swift", "font"]
---

之前写过一篇在 iOS 中自定义字体的「[博文](/ios-dev-tips/)」，随着现在字体的图形化，在 iOS 开发中也可以通过使用这些图形字体来替代图片，也能减少应用的体积。

#### 准备工作：找字体

现在这些图标字体很多，比如 [FontAwesome](https://fontawesome.com/)，再比如阿里的 [IconFont](https://www.iconfont.cn/)，我这里使用的是 [IcoMoon](https://icomoon.io/)

访问 IcoMoon 的网站，选择需要用到的字体，比如这里选择耳机

![](/imgs/how-to-use-icon-font-in-ios-01.png)

选中后，点击下面的 `Generate Font` 生成字体，在下一个界面下载字体，同时记录下这个字体的编码

![](/imgs/how-to-use-icon-font-in-ios-00.png)

#### 开发

- 创建项目，并将刚才下载的字体添加到项目中

    ![](/imgs/how-to-use-icon-font-in-ios-02.png)

- 编辑 `Info.plist` 文件，引入字体

    打开 `Info.plist` 文件，增加 `Fonts provided by application`，值为刚才字体文件的名字 `iconmoon.ttf`
    
    **这里字体文件的名字可以随意修改**
    
- 编写代码

    这里用 `UILabel` 来显示内容
   
    ```
    let label = UILabel(frame: CGRect(x:30, y:30, width: 100, height: 100))
    label.font =  UIFont.init(name: "icomoon", size: 96)
	label.text = "\u{e910}"
    ```
    
    先初始化字体，然后输入字体的编码即可，运行后的效果如下
    
    ![](/imgs/how-to-use-icon-font-in-ios-04.png)
    
#### 源码

本次教程源码查看：[GitHub](https://github.com/tourcoder/IconFontExample)