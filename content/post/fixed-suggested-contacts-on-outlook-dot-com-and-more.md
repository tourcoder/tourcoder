---
title: "微软 hotmail.com 中 bug 及解决办法"
slug: fixed-suggested-contacts-on-outlook-dot-com-and-more
author: Bin Hua
lastmod: 2020-08-13 09:40:43
date: 2019-11-11 15:08:33
tags: ["bug", "outlook", "微软", "hotmail", "代码", "microsoft todo", "task", "live.com"]
---

因为 hotmail 邮箱中的一个问题，发现了一连串的问题，而且挺严重的，也许是微软的设计缺陷，也许是其他因素。

- Suggested Contacts 问题

    当写一封邮件，在收件人地方输入任何一个字母，就会弹出窗口，如下图
    
    ![](/imgs/fixed-suggested-contacts-on-outlook-dot-com-and-more-00.png)
    
    比如，当我输入一个字母 a 时候，这时候弹出以前联系过的 Email 中包含 a 的人的 Email 地址，即便你删除了你的通讯录中所有人，删除了所有的邮件，这些人依旧被**微软记录并保存了下来**，在你每次输入的时候，会弹出提示。在这些 Email 旁边有个叉号，可以删除掉，但是！这里的删除是假的，下次登录，还是会出现。搜索下后发现，不只是我有这个问题，很多人都有这个问题，最近一次反馈这个问题的人，在这个月 5 日说他总是在这里看到曾经恐吓他，威胁要杀死他的狗的人 email 地址出现，他都要崩溃了，可以去[这里](https://outlook.uservoice.com/forums/601444-the-new-outlook-com/suggestions/31179604-cannot-delete-the-suggested-contacts)看。
    
    解决办法：返回到 hotmail.com 的旧版本，在旧版本里面删除，如果回到 hotmail.com 的旧版本？后面附上答案。
    
- Tasks 和 Microsoft To-Do

    Microsoft To-Do 是微软重金收购 wunderlist 后，wunderlist 团队打造的一款用来取代 wunderlist 的应用，微软对其非常重视，重视到他们已经将 Microsoft To-Do 设定为  hotmail 邮箱中本身自带的 Tasks 的新版，并且自动将 Tasks 中的内容同步过去，这思路没有错，但问题在于，你从 Microsoft To-Do 中删除任何内容，而在 Tasks 中依旧存在。直白点说，同一个账户的数据，在新版中说删除了，但在旧版中还能显示，说明这被删除的数据只是在新版中被隐藏了，而在旧版中没有被隐藏，符合微软的一贯作风。
    
    解决办法：在新版和旧版中都删除这些数据，当然这里可能是用隐藏好一点。
    
#### 新旧版切换

上面的两个问题都需要进入到旧版

- Tasks 

    Tasks 如果你没有开启试用新版的话，点击 Tasks 进入的就是旧版。如果已经开启了试用，则在新界面的右上角关闭试用新版的按钮即可。
    
- Mail

    默认情况下 Mail 的界面已经被新版替代，暂时找不到进入旧版的入口，但可以通过一些技巧来进入到旧版。
    
    在旧版的 Tasks 界面下，点击左上角的九宫格，在弹出的窗口中右键点击 Mail 的图标，选择新窗口或者新标签打开，这时候你就进入到旧版的 Mail 中了，如下图。
    
    ![](/imgs/fixed-suggested-contacts-on-outlook-dot-com-and-more-01.png)
    
    此时，可以新建一封邮件，点收件人那边，在弹出的 Suggested Contacts 中，点击每个人后面的叉号，下次新建邮件就不会再出现这些人了。
    
#### 最后

还是我很早前的一句话，在外面微软又是拥抱开源，又是这样，又是那样，但依旧改变不了它做东西越来越不靠谱。