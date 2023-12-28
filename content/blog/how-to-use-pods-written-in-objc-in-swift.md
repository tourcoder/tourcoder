---
title: "在 Swift 项目中使用 Objc 的第三方库"
slug: "how-to-use-pods-written-in-objc-in-swift"
author: "Bin Hua"
date: 2019-04-16 15:04:29
tags: ["Apple", "iOS", "cocoapods", "swift", "objc"]
draft: false
---

最近在用 Swift 写项目，发现其中用到的一些第三方库还是用 Objc 来写的，还好 Swift 中提供了很方便的引用 Objc 第三方库的办法。

#### 安装第三方库

通过 cocoapods 直接安装，这个不用多说，可以看[这篇文章](/some-cocoapods-i-use/)

#### 创建连接文件并让它生效

Apple 官方推荐通过 `header file` 进行桥连接，操作如下

- 新建一个头文件 `Bridging-Header.h`

    ![](https://storage.tourcoder.com/tcblog/how-to-use-pods-written-in-objc-in-swift-01.png)
    
- 在生成的头文件中引入第三方库

    ```
    #ifndef Bridging_Header_h
    #define Bridging_Header_h
    #import "第三方类库.h"
    #endif /* Bridging_Header_h */
    ```
    
- 设置

    进入 `Xcode－>Target-->build settings`，搜索 `Objective-C Bridging-Header` 选项卡，将前面增加的头文件 `Bridging-Header.h` 连同路径一起填入
    
    ![](https://storage.tourcoder.com/tcblog/how-to-use-pods-written-in-objc-in-swift-02.png)
    
这样就完成了，不需要引入任何文件，直接在需要使用到该第三方库的地方直接使用即可。

#### 其他情况

如果 Podfile 文件中使用了 `use_frameworks!`，则不需要创建连接，在需要使用该第三方库的文件的头部直接引入该类库 `import 第三方类库`，直接使用即可。