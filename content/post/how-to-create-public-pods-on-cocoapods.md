---
title: "创建公有的 Cocoapods 库"
slug: how-to-create-public-pods-on-cocoapods
author: "Bin Hua"
lastmod: 2020-07-18 05:59:35
date: 2019-03-26 02:10:00
tags: ["iOS", "macOS", "cocoapods", "github", "terminal"]
---

Cocoapods 是一个很棒的开发管理库，有时候为了方便，自己也会制作一些库上传到上面，这里分享下过程。

- 首先注册 cocoapods

    在终端中执行如下命令

    ```
    pod trunk register hello@tourcoder.com 'tourcoder' --verbose
    ```
    
    这里的 hello@tourcoder.com 和 tourcoder 换成自己的，输入命令后，hello@tourcoder.com 会收到一封邮件，点击邮件里面的确认链接，即可得到下图
    
    ![](/imgs/cocoapods_ss01.png)
    
    注册成功，提醒你回到终端。
    
- 查看信息

    可以随时通过命令 `pod trunk me` 查看自己的信息以及发布的 pods
    
- pods 库文件的操作

    因为这个库是要通过代码共享的方式出去的，所以需要一个共享代码的地方，Github 自然是首选，在 Github 中新建一个仓库，并克隆到本地。比如这里的仓库是 notifylabel
    
    进入到本地仓库文件夹中，创建几个文件（夹），下面的文件（夹）都是必需的，这是一种精简的做法，如果不知道该怎么弄，也可以通过命令 `pod lib create 项目名` 来初始化一个。
    
    - 文件夹 notifylabel: 里面包含了 notifylabel 这个 pod 的所有代码
    
    - LICENSE 文件

    - README.md 文件

    - notifylabel.podspec 文件：可以通过 `pod spec create 文件名` 来创建，创建完成后格式大致如下

        ```
        Pod::Spec.new do |s|
        s.name         = "notifylabel"
        s.version      = "0.0.1"
        s.summary      = "A simple pop-ups label"
        s.homepage     = "https://github.com/tourcoder/notifylabel"
        s.license      = "MIT"
        s.author             = { "tourcoder" => "hello@tourcoder.com" }
        s.platform     = :ios
        s.source       = { :git => "https://github.com/tourcoder/notifylabel.git", :tag => "#{s.version}" }
        s.source_files  = "notifylabel/*.{h,m}"
        s.exclude_files = "Classes/Exclude"
        end
        ```
        
- 验证 podspec 文件

    进入到 podspec 文件所在的目录下，执行命令
    
    ```
    pod lib lint
    ```
        
    在等待一段时间后，会出现相关的内容，如果有错误，就根据错误来修正即可，正确的应该是出现绿色的 passed 字样，如下图
    
    ![](/imgs/cocoapods_ss02.png)
    
- 发布 pods

    在发布之前，应该将当前稳定版本的仓库打 tag，标签号和 podspec 文件中 `s.version` 保持一致，这里就是 0.0.1
    
    ```
    git tag -a 0.0.1 -m 'tag 0.0.1'
    git push origin --tags
    ```
    
    然后在终端中执行命令 `pod trunk push notifylabel.podspec`，在一段时间的等待后，会出现下图的成功提示
    
    ![](/imgs/cocoapods_ss03.png)
    
    上面的命令执行了一套流程
    
    - 更新本地 pods库，所需时间较长
    
    - 验证 podspec 格式是否正确
    
    - 将 podspec 文件转成 JSON 格式
    
    - 对 master 仓库进行合并并提交

    到这里基本一个 pod 的创建发布流程就完成了。

#### 测试

在终端中输入 `pod search notifylabel` 命令，在一段时间等待后，会出现

![](/imgs/cocoapods_ss04.png)

表示已经发布成功，如果使用，即执行命令 `pod install notifylabel`。

#### 后续更新

每次更新，主要更新 notifylabel 文件夹中的代码，更新 podspec 文件的版本号，将新版本的内容 push 到 GitHub 并打上最新的 tag（和 podspec 文件中的版本号对应），最后执行命令

```
pod trunk push notifylabel.podspec
```

即可。

#### 本地项目地址
    
[https://github.com/tourcoder/notifylabel](https://github.com/tourcoder/notifylabel)