---
title: "我常用的一些 iOS 插件"
slug: some-cocoapods-i-use
author: "Bin Hua"
lastmod: 2020-08-13 08:58:57
date: 2015-10-03 06:44:15
tags: ["插件", "iOS"]
---

在 iOS/OSX 应用开发中，我会用到一些插件，其中比较常规的有几个，我的 Podfile 文件内容如下

```
source 'https://github.com/CocoaPods/Specs.git'
platform :iOS, '8.0 #platform :osx, '10.12'
target 'project-name' do
	pod 'AFNetworking'
	pod 'PSUpdateApp'
	pod 'Appirater'
	pod 'Firebase/Core'
	pod 'Firebase/Crash'
	pod 'Firebase/AdMob'
end
```

**AFNetworking**

这是一个网络请求的，比较好用，我也用的比较多

**PSUpdateApp**

用于版本更新的提醒，我用的是自己写的，未开源，这个插件和我自己写的差不多，访问[这里](https://github.com/danielebogo/PSUpdateApp)

**Appirater**

用于提醒用户给应用评论，我用的也是自己写的，未开源，这个插件和我写的差不多，访问[这里](https://github.com/arashpayan/appirater)

**Firebase (Analytics, Crash Reporting, Admob)**

Firebase 可以查看官网的说明，[官网地址](https://firebase.google.com/)

在 `Delegate` 文件中

```
import Firebase; // SWIFT
@import Firebase; // OBJECTIVE-C
```

在头文件里的 `application:didFinishLaunchingWithOptions:` 中

```
FIRApp.configure() // SWIFT
[FIRApp configure] // OBJECTIVE-C
```

即可完成配置。

**Admob**

Admob 的设置

```
#import "AppDelegate.h"
@import GoogleMobileAds;

@interface ViewController ()
@property (nonatomic, strong) GADInterstitial *interstitial;
@property (nonatomic, retain) UIButton *btnClick;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    [self createAndLoadInterstitial];
    [self createButton];
}

- (void)createButton {
    _btnClick = [[UIButton alloc] initWithFrame:CGRectMake(10, 100, 300, 60)];
    [_btnClick addTarget:self action:@selector(clickThis) forControlEvents:UIControlEventTouchUpInside];
    [_btnClick setTitle:@"click" forState:UIControlStateNormal];
    _btnClick.titleLabel.font = [UIFont systemFontOfSize: 20.0f];
    [_btnClick setTitleColor:[UIColor blackColor] forState:UIControlStateNormal];
    [self.view addSubview:_btnClick];
}

- (void)clickThis {
    if (self.interstitial.isReady) {
        [self.interstitial presentFromRootViewController:self];
    }
    else {
        NSLog(@"Ad wasn't ready");
    }
}

- (void)createAndLoadInterstitial {
    self.interstitial =
    [[GADInterstitial alloc] initWithAdUnitID:ADMOB_INTERSTITIAL_ID];
    GADRequest *request = [GADRequest request];
    // Request test ads on devices you specify. Your test device ID is printed to the console when
    // an ad request is made.
    request.testDevices = @[kGADSimulatorID, @"2077ef9a63d2b398840261c8221a0c9b" ];
    [self.interstitial loadRequest:request];
}
```

基本上完成了 Admob 的简单设置。