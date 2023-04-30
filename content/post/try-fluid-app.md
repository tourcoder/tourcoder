---
title: "Fluid App 初步使用"
slug: try-fluid-app
author: "Bin Hua"
lastmod: 2020-08-13 09:09:52
date: 2017-10-12 07:11:58
tags: ["Gmail", "electron", "fluid"]
---

昨天有朋友看了我博文后，问了我几个问题

- 怎么封包 Gmail 的，性能如何？

    Gmail 本身的 Webapp 已经做的非常好，秉着原生就是最好的原则，加上我实在没动力继续开发之前写的邮件客户端了，我产生封包 Gmail 的念头，主要由三个部分组成

    - Webview：载入 Gmail 页面，对 Gmail 的操作
    
    - Gmail API：用 swift 做了一些定制性的东西，比如通知
    
    - 科学性：内置无 wall

    性能还行，对我来说很好用了，而且比我之前写的邮件客户端要轻便。

- fluid 用过吗？能不能帮忙做点修改？

    fluid 听说过但没有用过，随即下载研究了下，朋友付钱买了软件，挺有意思的软件。这个软件的作用就是帮你把任何一个网页打包成一个 macOS 下的 APP，其实我更喜欢叫快捷方式，不过它自带了一些接口，可以通过 userscripts 进行一些修改。

    朋友让我帮忙修改的网页是他客户的东西，不方便透露，下面我用 Gmail 来做示例。

    打开软件，并参考下图填入相关信息

    ![](/imgs/try-fluid-app-01.png)
    
    点击 Create，稍等一会，你的 Gmail 应用已经诞生了，很方便是不是？

    运行刚才创建的 Gmail App，你可以点击顶部菜单 Gmail-Preferences，还可以设置

    ![](/imgs/try-fluid-app-02.png)

    其它更多的设置自行研究，我重点说下它的 userscripts，点菜单栏中的 `Window->userscripts`

    ![](/imgs/try-fluid-app-03.png)

    点左下角的 +，创建一个 Gmail，在右上部填写 Gmail 的几个地址，右下面就是你的 js 工作区。fluid 官方也提供了一些接口，[Fluid API](http://fluidapp.com/developer)。

    比如我给 Gmail 增加个通知提醒功能，macOS 应用提醒有三个方面，图标的 badge，声音和通知中心。

    ```
    window.fluid.dockBadge = '';
    setInterval(unRead, 1000);
    var currentBadge = 0;
    function unRead() {
        var inboxcontent = document.querySelector('a[title^="Inbox"]');
        var regex = /\s*Inbox\s*\((\d+)\)[^\d]*/;
        var result = inboxcontent.title.match(regex);
        if (result && result.length > 1) {
            var newBadge = result[1];
            window.fluid.dockBadge = newBadge;
            if(newBadge > currentBadge) {
                window.fluid.playSound("Hero");
            }
            currentBadge = newBadge;
        } else {
            window.fluid.dockBadge = '';
        }
    }
    ```
    
    这段代码完成的工作是当有邮件来了，会有声音提醒，同时 Dock 中图标的 badge 也会显示
    
    ```
    var inboxcontent = document.querySelector('a[title^="Inbox"]');
    var regex = /\s*Inbox\s*\((\d+)\)[^\d]*/;
    ```
    
    因为时间关系，这段代码的正值部分，我用了网上的代码，据说有 bug，会因为语言版本的不一样出错。

    ```
    function notifycenter() {
        window.fluid.showGrowlNotification({
          title: "Gmail",
          description: "You have a mail",
          priority: 1,
          sticky: true,
          onclick: function(){},
          identifier: "Gmail Notifier",
          icon: "url/gmail.png"
        });
    }
    ```

    而官方通知接口中，并没有成功运行

    ```
    function notifyPermission() {
      if (!("Notification" in window)) {
        console.log("Not support desktop notification");
      }
      else if (Notification.permission === "granted") {
        console.log("The permission has already been granted");
      }
      else if (Notification.permission === "denied") {
        console.log("Do nothing");
      }
      else if (Notification.permission === "default") {
        Notification.requestPermission(function (permission) {
          switch(permission) {
            case granted:
                console.log("user accepts the permision");
                break;
            case denied:
                console.log("user denies the permision");
                break;
            default:
                break;
          }
        });
      }
    }
    ```
    
    检查了通知的权限，是 granted 状态，Gmail 本身也开启了桌面提醒，目测和 macOS 自身的通知 API 有关系，有待深入研究。

    需要注意的是，fluid 创建的 App 可以自由选择 userAgent，但是似乎有个 bug，当选择 userAgent 为 Chrome 的时候，Gmail 是打不开的，卡在 Loading 界面，换成其他的 userAgent 工作正常。

至于性能等方面，没有做研究测试，以上代码没有做优化，有兴趣的人可以自己去下载一个玩玩，有什么研究成果，记得分享。