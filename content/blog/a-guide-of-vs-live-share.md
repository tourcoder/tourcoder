---
title: "VS Code 中的 Live Share"
slug: "a-guide-of-vscode-live-share"
author: "Bin Hua"
date: 2019-01-28T02:33:31Z
tags: ["GitHub", "微软", "VSCode", "plus", "workflow"]
draft: false
---

如果团队的程序员不在一个场所工作，分享编码的屏幕进行协同工作，就比较重要。VS Live Share 就是一个很不错的方案，这里用 VS Code 做演示。

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_01.png)

打开 VS Code，并安装对应的插件 VS Live Share

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_02.png)

安装完成后，重启 VS Code，然后点击 Live Share 的按钮，可以看到有几个选项

- 加入一个合作 

- 开始一个合作

- 开始一个只读的合作

点开始合作，会弹出窗口要求输入帐号密码，有微软的账户和 GitHub 两个账户体系的选择，我这里使用了 GitHub 的帐号，输入后即可看到下面的界面

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_03.png)

记得在开始之前先打开你的工作目录，如果没有打开，VS Code 会提示你选择一个工作目录

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_04.png)

完成后复制上面的邀请链接可以邀请一位协作者加入，将邀请链接发送给协作者，他打开链接会看到如下的内容，会自动弹窗选择打开方式，这里需要协作者也安装了 VS Code 和 Live Share 的插件。

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_05.png)

当被邀请的协作者加入后，你会看到提醒，对方已经加入，如下图右下角

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_06.png)

而他会看到你整个 VS Code 的内容，并且会看到你的 VS Code 的所有操作，如下图

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_07.png)

当协作结束后，可以点击下图中的退出

![](https://storage.tourcoder.com/tcblog/vscodeliveshare_08.png)

这就是整个 VS Live Share 的流程。