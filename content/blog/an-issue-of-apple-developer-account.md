---
title: "Apple 开发者帐号的问题"
slug: "an-issue-of-apple-developer-account"
author: "Bin Hua"
lastmod: 2019-09-15 04:48:01
date: 2019-09-15 04:48:01
tags: ["Apple", "apple developer", "苹果开发者账户", "appstore"]
---

昨天深夜上传了个新应用，没几个小时，也就今天早上五点多的时候，收到 Apple 发来的邮件，随即登录开发者后台查看。

```
Hello,

Upon further review of the activity associated with your Apple Developer Program membership, we have determined that your membership, or a membership associated with your account, has been used for dishonest or fraudulent activity. Therefore, your Apple Developer Program account has been flagged for removal. 
```

原文很长，就不全贴了，看完我一脸懵逼。他们说他们非常确定我的开发者账户涉嫌欺诈，并把我的开发者账户给悬挂并标注成即将被删除。他们给我 14 天时间申诉，不是 14 个工作日，只是 14 天，14 天后会删除我的账户，好强势的有没有。

我仔细会想一下，我没有做过什么事情，这个账户是我第二个 Apple 开发者账户，注册于 2012 年，里面一共就五个应用，每个应用第一个版本的提交时间至少是几年前，怎么我账户就欺诈了？

想到这封邮件是来自昨天我提交的某个应用的反馈，我去查看了下更为详细的内容，其中有段话引起了我的注意

```
"You will not, directly or indirectly, commit any act intended to interfere with the Apple Software or Services, the intent of this Agreement, or Apple’s business practices including, but not limited to, taking actions that may hinder the performance or intended use of the App Store, Custom App Distribution, or the Program (e.g., submitting fraudulent reviews of Your own Application or any third party application, choosing a name for Your Application that is substantially similar to the name of a third party application in order to create consumer confusion, or squatting on application names to prevent legitimate third party use)."
```

我想到莫非是我应用的名字？随即在应用商店搜索了下相关的名字，应该也没有什么问题。而且但凡做过 AppStore 的人都知道，同名的应用，在开发者后台系统中，只能够存在一个，这话的意思就是别人占用了这个名字，你是没有办法再用这个名字的，除非你有这个名字的商标之类的东西，找 Apple 进行维权。

说回我的应用名字，这个名字是我很早就在手上的，之前我用这个名字上架过一款应用，但后来我下线并删除了这款应用，但名字保留在我手上。这次拿出来，提交一款新的应用，就遇到了这个问题。

现在我按 Apple 的要求提交了申诉，在具体等发生了什么，关于这件事，会有后续更新。

另外说一句，Apple 这几年对开发人员的态度越来越恶劣，网上有很多这类的报道，去年 2 月份，我也遇到过其他的奇葩事情，看「[记录一次 App 审核](/appreviewer-of-apple-sucks/)」。

**2019.09.17 20:40**

已经过去两天，还未收到来自 Apple 的任何消息，只能再次提交申诉，有件奇怪的事情是，一般情况下提交 case 都会产生一个 case number 自动发送到对应的邮箱，但这两次申诉都没有收到对应的 case number。

**2019.09.19 20:00**

又过去了两天，还是未收到来自 Apple 的任何消息，看这样子，他们是铁了心地响删除我的账户了。晚点我会给 Tim Cook 发一封邮件，说明这个情况。

**2019.09.20 22:00**

依旧未得到任何回复消息，给 Tim Cook 发了一封邮件。

**2019.09.21 03:00**

在给 Tim Cook 发邮件后的四个半小时不到的时间，我收到了来自 Apple 应用审核团队的回复，他们说我的开发者账户不会被删除，我所提交的这个应用没问题，他们只是觉得功能太少了，建议我多增加点功能。

不过到此刻，该开发账户下面的几个应用还是不能够操作，比如转移。只好给他们再提交一个 case 询问原因，和前两次不一样的是这次在我提交了 case 后，立刻收到了对应的 case number。

**2019.09.23 12:30**

账户里面的应用依旧无法转移到其它账户，怀疑还是账户并没有完全解除禁止。考虑到现在美国时间还是周日的夜间，会在几个小时后，再次联系他们。

**2019.09.24 17:20**

刚才接到了 Apple 开发者支持的电话，在线核查了我的账户，说我账户没有问题，但是就是解决不了这个问题。她告知我已经将该案例提交到高级的技术支持，期待有好的结果。

**2019.09.27 09:20**

昨天我发现前一天我重点说到的一个应用可以转移了，更加证明是我的账户出了问题。但其他问题还是没有解决，但在我和该客服邮件联系时，她坚信我的问题已经解决，没有办法，我再次提供了详细的不能再详细的信息给了她，详细的文字描述和截图，同时她也表示这个问题一旦解决会第一时间告诉我。

今天早上五点多收到邮件通知，已经拖了十多天的应用状态改变，直接从状态 `Wait for Review` 变成了 `Ready for Sale`，连中间状态 `In Review` 的邮件通知都没有，应用就这么上架了，但是现在过去了四个多小时，AppStore 上还是没有更新，以前这种更新基本是一两个小时的事情。

另外还发现一个问题，昨天转移的那个应用在 AppStore 上并没有进入到新的帐号下面，还是在旧的账号下面。这种转移以前也是一两个小时就会变更的事情，现在过去了十几个小时，还是没有变化。

给他们技术支持又发了一封邮件，并详细描述了问题，说真的，现在 Apple 自身软件的质量是一次又一次的刷新了我对他们要求的下限。