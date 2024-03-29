---
title: "Apple App Review 的双刃剑"
slug: "to-be-or-not-be-is-a-question-for-apple-appreview"
author: "Bin Hua"
date: 2018-03-16 07:36:06
tags: ["Apple", "App"]
draft: false
---

两个 App 又被拒绝了，拒绝的理由依旧是很奇葩，习惯就好。App Review 这件事是一把双刃剑，做得好了，能提升 AppStore 平台，做得差了，也能毁掉平台。很可惜，现在 App Review 正在向差的方向大踏步，而导致这个现象的主要原因是专业性和态度。

**专业性**

现在 Apple 的 App Reviewer 并不专业，他们的业余体现在对规则的不合理使用，给人一种死背教条的感觉。很多内容都不能够准确的描述，甚至发生拒绝的理由和产品本身没有相关性的事情。

**态度**

态度往往和专业性在一起的，态度端正才能够提升自己的专业性，但 App Review 团队里的不少人的态度是非常敷衍的，比如我之前吐槽过的文章。

**我的观点**

由上面的两点引发的一系列问题非常严重，对一个开发者来说简直是灾难性的。

就拿我来说吧，我现在越来越不喜欢开发 iOS 上的应用，其中很重要的一个原因是成本太高，而且这些成本完全是由 App Reviewer 带来额外成本。

比如我想到一个点子，然后我会论证是否符合苹果官方文档标准，一旦符合，会经过几个月的开发测试，然后提交，但这时候 App Reviewer 给了一个莫名其妙的理由拒绝上线，然后我按他的要求更改再次提交，然后他又会给出另外一个同样莫名其妙的理由，让我继续修改，就这样来来回回反反复复，等最后真能上线的应用已经和当初自己最初的想法不一样了，更要命的是时间已经花掉了很多很多。
这只是其中的一个情况，如果是个人，损失还好；但如果是一个团队，那损失是灾难性的。这已经完全违背了 AppStore 快速上线，快速迭代，小步快跑的模式。

让 App Reviewer 有权利干预 App 的内容是件非常扯蛋的事情，如果是违背开发者指南的内容需要修改是必须的，但现在的情况是这些 App Reviewer 让开发者改的不只是违背开发者指南的内容。

举个简单列子，我的一款应用需要读取相册，在读取相册的时候需要提醒用户，我写了如下内容

```
为了插入图片和保存图片的操作，本应用需要相册权限
```

但这被 App Review 拒绝了，说让我重新修改这段文字。怎么改？没说。类似的情况多的举不胜举。
怎么说呢，这类情况发生太多，让我逐步丧失了在 iOS 平台创作的欲望。

另外，App Review 团队是我见过最怂的团队，他都不敢把拒绝的内容呈现在邮件中，每次的邮件都是说你有问题了，需要去后台看，呵呵。

最后我想说，做这方面开发的技术人员，不妨关注下 PWA，如果 Google 好好弄，不用多久，会是一个更好的趋势。

一早思路有点乱，写得有点乱～