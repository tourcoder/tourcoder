---
title: "批量取消 twitter following"
slug: "bulk-unfollow-in-twitter"
author: "Bin Hua"
lastmod: 2020-07-18 06:07:35
date: 2017-03-21 06:59:54
tags: ["twitter"]
---

要在 twitter 上宣传产品，使用很久前注册的 twitter 账号，因为很久没有登录，莫名其妙的 follow（关注） 了很多人，如图

![](/imgs/twitterunfollowing_01.png)

1411 人基本都是一些莫名其妙的账户，尤其是里面很多是阿拉伯文的账号，只能取消关注，但如果一个一个点取消，那是一项相当大的工程，在研究了下 unfollow（取消关注） 这个按钮的执行机制后，得到下面的方式可以批量取消关注。

登录你的账号后，访问 following（关注） 页面，即 [https://twitter.com/following](https://twitter.com/following) 然后在控制台执行如下命令

```
$(".following .js-follow-btn").click()
```

输入命令后，等待一段时间，即可出现下图执行效果

![](/imgs/twitterunfollowing_02.png)

刚才批量取消关注了 576 人。

![](/imgs/twitterunfollowing_03.png)

效果还不错吧？

需要注意的是，该命令作用于显示出来的关注的人员，在取消的过程中可能会出现错误，比如 rate limit，你可以等一会时间再执行或每次取消关注的数量少一点

当然网上也有一些第三方的服务可以帮你一样实现这些，但出于安全考虑，我没有测试。

题外话，晚上几个人闲聊《守望先锋》，都有差不多的感受

在国服打《守望先锋》，只要掉到鱼塘区（2000分以下），单排上分就非常难，即便你操作厉害，也难一打六，上分的方法就是找个好车队，2-3 个人的车队最好，3 个人以上的车队容易翻车。

话说我的号被我老婆坑到 600 分后，我单排好不容易才打到 1200 分，打的都要吐了。