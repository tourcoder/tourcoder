---
title: "如何在应用中集成 Admob"
slug: "admob-in-app"
author: "Bin Hua"
date: 2016-06-11 06:45:09
tags: ["iOS", "App", "admob"]
draft: false
---

如何让免费的应用有额外的收入？Admob是个不错的选择。

**什么是 Admob?**

Admob 是 Google 于 2009 年底收购的广告平台，国内外类似的广告平台有很多，但实际测试下来，Admob 是我觉得最稳定和安心的。

**什么样的应用集成 Admob?**

理论上说所有的应用都可以集成 Admob，但我建议集成 Admob 应该有所考量，比如，你的应用是一个游戏，那么在游戏的间隙（暂停），你可以弹窗广告等。

**如何在应用中集成？**

简单的三步就可以完成 Admob 的集成

第一步、在 Admob 网站添加新应用

登录 Admob 的网站，登录后，选择创建一个新的应用，然后按步骤来

![](https://storage.tourcoder.com/tcblog/admob_01.jpeg)

输入应用名字，选择所在的平台，因为我这个是 iOS 上的应用，所以平台是 iOS。

![](https://storage.tourcoder.com/tcblog/admob_02.jpeg)

选择广告类型，自定义 UI，我选择了顶部的 Banner 形式。

![](https://storage.tourcoder.com/tcblog/admob_03.jpeg)

链接 Firebase 的统计分析，我不需要，选择跳过。

![](https://storage.tourcoder.com/tcblog/admob_04.jpeg)

选择完成，那么在 Admob 网站，你的创建就完成了，记录下这里的 App ID 和 Ad unit ID，后面我们将用用到，就这样我们第一步完成了。

第二步、将 Google Mobile Ads 添加到应用中

去 Admob 网站下载 SDK，当前 SDK 版本是 7.8.1,

![](https://storage.tourcoder.com/tcblog/admob_05.jpeg)

可以选择手工的添加方式，也可以选择用 CocoaPods，图方便，我采用了 CocaPods

![](https://storage.tourcoder.com/tcblog/admob_06.jpeg)

需要注意的是因为某些“不可抗力”的因素，你在使用 CocoaPods 安装时需要挂 VPN，至于 CocoaPods 这个利器怎么用等，在以后我兴许会写一篇文章。

第三步、在显示 Admob 的界面显示相关内容

这一步就是写代码了，在 iOS 中，你可以把它看成是一个 View 的子类，直接添加即可，部分代码如下

```
- (void)callAD {
  _bannerView = [[GADBannerView alloc] initWithFrame:CGRectMake(0, 0, self.view.frame.size.width, 70)];  // 创建
  _bannerView.adUnitID = ADMOB_UNIT_ID; // 之前在 Admob 增加应用时获取到的。
  _bannerView.rootViewController = self;
  GADRequest *request = [GADRequest request]; // 创建请求
  request.testDevices = @[@""]; // 测试的设备，如果是在模拟器中运行，则会自动出现
  [self.view addSubview:_bannerView]; // 增加
  [_bannerView loadRequest:request]; //请求
}
```

记得导入库，在新版本的 SDK 中，导入库用 @import GoogleMobileAds;

显示的效果如下

![](https://storage.tourcoder.com/tcblog/admob_07.jpeg)

怎么样，是不是很简单？！

Admob 更多的用法说明？

去 Admob 官网看文档，不会的 Google 一下，你就知道。

update@20190317: Google 更新了文档，也推出了中文文档，看[这里](https://developers.google.com/admob/ios/quick-start)。