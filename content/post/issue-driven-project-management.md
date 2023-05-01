---
title: "Issue 驱动的项目管理"
slug: "issue-driven-project-management"
author: "Bin Hua"
lastmod: 2018-12-26 15:43:13
date: 2018-12-26 15:43:13
tags: ["git", "GitHub", "项目管理", "issue"]
---

今天基本耗了一天时间在安装系统，主要是安装过程中遇到了一个安全问题，然后就在那边研究这个问题，具体我的 twitter 上有说明，这里就不展开说了。

言归正传，在安装系统的等待中，我整理了下以前做项目管理中开发部分的资料，觉得可以分享下。这种方法将它称为：Issue 驱动。

- **什么是 Issue**

    Issue 是 GitHub 代码仓库中的一个功能，方便大家提交错误信息等
    
- **怎么用 Issue**

    所有的项目相关的内容都会在 Issue 中，结合 GTD 思想将 Issue 分为六个标签，分别为 feature, bug, processing, done, pass, abnormail
    
    ![](/imgs/issue-driven-project-management.PNG)

    - feature

        所有的需求内容都应该打上 feature 这个标签
  
    - bug

        发现 bug，提交 Issue 必须打上 bug 这个标签
    
    - processing

        当某一 Issue 有人负责处理时，处理人员应该将该 Issue 打上 processing 标签
    
    - done

        当某一 Issue 处理完成时，处理人员应该将该 Issue 打上 done 标签。需要注意的是，该 Issue 必须要严格测试通过后才可以被打上该标签
  
    - pass

        针对已经打上 done 标签的 Issue 进行二度测试，确认没有问题后，负责二度测试的人员将该 Issue 打上 pass 标签，并且关闭该 Issue
    
    - abnormail

        针对已经打上 done 标签的 Issue 进行二度测试，测试未通过则打上 abnormal 标签
        
    - 备注：配色参数

        ```
        Bug #FF0000
        Feature #0033CC
        Processing #D1D100
        Pass #5CB85C
        Abnormal #F0AD4E
        Done #7F8C8D
        ```
        
- **优点**

    这样做，细化到功能点，结合了 log 和 milestone，可以实时的追踪到每个功能点的情况，而且每一个环节都会被清楚的放大
    
- **缺点**

    早期需要一个或多个有经验的人将功能合理的拆分
    
- **实际应用及扩展**

    我们实际使用情况下的标签要比这多，主要是我们每一位都需要会使用 git，这其中包含设计师。