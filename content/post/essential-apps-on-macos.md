---
title: "macOS 上必装的应用"
slug: essential-apps-on-macos
author: Bin Hua
lastmod: 2023-01-26 21:07:04
date: 2019-08-14 04:25:36
tags: ["macOS", "alfred", "slowquitapps", "lulu", "micro snitch", "dozer", "flux", "spectacle", "ntfs"]
---

因为工作需要，我在 macOS 上安装了很多应用，除了和工作相关的应用之外，我在 macOS 有几款必装的应用。

#### Homebrew

在 macOS 下非常好用的东西，很多开源免费的软件可以通过它来安装。官网 [https://brew.sh/](https://brew.sh/)。

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

在终端中输入上面的命令即可安装完成。

因为 `raw.githubusercontent.com` 这个域名被污染，所以，在安装时会遇到 `Connection refused` 的问题，解决办法，编辑 `hosts` 文件

```
sudo vi /etc/hosts
```

在里面增加 `199.232.28.133 raw.githubusercontent.com` 即可。也可以通过代理终端的方式解决。

#### Raycast

这是一款效率工具，[官网](https://www.raycast.com/)

我用它取代了之前一直用的 alfred

#### Slowquitapps

macOS 的人经常会遇到一个问题，就是一不小心就会按错，按到 `command+q` 键导致当前界面退出，使用了这款应用就不怕了。这是一款开源免费的应用，开源在 [GitHub](https://github.com/dteoh/SlowQuitApps)，可以下载源代码，通过 xcode 编译安装，也可以用 Homebrew 安装。这里翻译下它在 GitHub 上的安装方式等

在 macOS 下打开终端，执行命令

```
brew tap dteoh/sqa
brew install slowquitapps --cask
```

这样就安装完成了，打开这个应用给它一定的权限，完事，当每次再出现手残情况时就会出现如下界面

![](/imgs/sqa_01.png)

会有一个倒计时的进度条，当进度条跑满后，应用就可以退出了。

**设置时间**

```
defaults write com.dteoh.SlowQuitApps delay -int 1000 //1 秒
```

**白名单**

白名单就是直接调用系统自带的退出快捷键，不走 Slowquitapps 的规则

```
defaults read com.dteoh.SlowQuitApps whitelist // 查看白名单列表
defaults write com.dteoh.SlowQuitApps whitelist -array-add com.tourcoder.appname // 将某应用加入白名单，需要使用应用的 bundle ID
osascript -e 'id of app "appname"' // 获取某个应用的 bundle ID
defaults delete com.dteoh.SlowQuitApps whitelist // 清空白名单
```

**黑名单**

有白名单自然就有黑名单，其意义是和白名单相反，默认情况下每个应用都是黑名单里面的应用

```
defaults write com.dteoh.SlowQuitApps invertList -bool YES // 开启黑名单
defaults delete com.dteoh.SlowQuitApps invertList // 关闭黑名单
```

**查看配置**

```
defaults read com.dteoh.SlowQuitApps
```

#### Lulu

Lulu 算是一款保护你隐私的应用，它检测网络链接的请求，并及时地通知。

![](/imgs/lulu_01.png)

它也是一款开源的应用，可以从[这里](https://github.com/objective-see/LuLu/releases)下载。

#### Micro Snitch

同样也是一款隐私保护的应用，它能检测那些应用在使用摄像头和麦克风，它是一款收费的应用。

官网地址：[https://obdev.at/products/microsnitch/](https://obdev.at/products/microsnitch/)

#### Flux

作为一个长期对着电脑工作的人，眼睛的保护显得非常重要，Flux 就是这么一款保护眼睛的应用

![](/imgs/flux_01.png)

它会根据时间来降低屏幕的光度等，这也是一款免费的应用，从[官网](https://justgetflux.com/)下载即可。

#### Spectacle

这也是一个开源的应用，它的作用就是一个，通过键盘控制各应用窗口的位置，可以在[这里](https://www.spectacleapp.com/)下载到，它的源码在 [GitHub](https://github.com/eczarny/spectacle)。

#### Dock

Dock 是 macOS 自带的，它有个问题就是关闭了的应用很多时候会还显示在 Dock 上，这点非常讨厌，可以通过命令行来解决

```
defaults write com.apple.dock static-only -boolean true
killall Dock
```

这样就只能显示打开的应用了，如果不喜欢这样，也可以通过命令恢复到之前的状态

```
defaults delete com.apple.dock static-only
killall Dock
```

#### The Unarchiver

The Unarchiver 是一个解压软件，我用了很多年，非常棒，直接在 Mac AppStore 搜索下载即可。

以上是我在 macOS 必装的，但和工作娱乐基本没有什么太大关系的应用。

#### Paragon NTFS for Mac

让用户方便的在 macOS 上进行 NTFS 的读写，这是一款收费软件，官网点[这里](https://www.paragon-software.com/home/ntfs-mac/#)。

上面是必装的，至于其他的应用，可以参考我博客的其他文章。
