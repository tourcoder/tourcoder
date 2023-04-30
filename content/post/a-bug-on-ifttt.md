---
title: "IFTTT 中的 bug"
slug: a-bug-on-ifttt
author: "Bin Hua"
lastmod: 2020-08-13T09:28:56Z
date: 2019-03-25T04:37:15Z
tags: ["bug", "ifttt"]
---

严格上说，这不是一个 bug，是一个功能缺失，具体复现步骤如下

- 创建账户

    登录 ifttt.com，注册一个账户，这里输入的 email 地址是 hello@tourcoder.com
    
- 创建一个 Applet

    按照下面截图的步骤创建一个 Applet，这里便于测试，this 部分用时间

    ![](/imgs/iftttbug_01.png)
    
    第一步

    ![](/imgs/iftttbug_02.png)
    
    第二步

    ![](/imgs/iftttbug_03.png)
    
    第三步

    ![](/imgs/iftttbug_04.png)
    
    第四步

    ![](/imgs/iftttbug_05.png)
    
    第五步

    ![](/imgs/iftttbug_06.png)
    
    第六步

    ![](/imgs/iftttbug_07.png)
    
    第七步

    ![](/imgs/iftttbug_08.png)
    
    第八步

    ![](/imgs/iftttbug_09.png)
    
    第九步

    ![](/imgs/iftttbug_10.png)
    
    第十步
    
    当时间到时，hello@tourcoder.com 这个邮箱会收到该 applet 的邮件。
    
- 更改 Applet

    进入到之前创建的 Applet，然后更改该 Applet 的 email 地址为 opensource@tourcoder.com，

    ![](/imgs/iftttbug_11.png)

    ![](/imgs/iftttbug_12.png)
    
    等待时间到后，会发现邮件还是会发送到 hello@tourcoder.com 这个邮箱，而非更改后的邮箱 opensource@tourcoder.com
    
#### 更为严重的问题

如果更改了账户中的 email，如下图

![](/imgs/iftttbug_13.png)

但当你再次创建新的 applet 的时候，email 地址还是 hello@tourcoder.com，这个问题就非常严重了

![](/imgs/iftttbug_14.png)

关于这些问题，我提交过多次 issue 给 ifttt，但他们一直没有回复过，也罢。

**解决方案**：我猜 IFTTT 在这里的设计思路是预防 spam，只能够发送到注册账户的 email 地址里面，不可以修改。其实 IFTTT 可以考虑发送到验证完成的邮箱里面。