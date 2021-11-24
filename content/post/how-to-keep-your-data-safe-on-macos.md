---
title: "macOS 的安全设置"
slug: how-to-keep-your-data-safe-on-macos
author: Bin Hua
lastmod: 2020-08-04 02:02:44
date: 2020-07-12 14:26:20
tags: ["Apple", "macOS", "数据安全"]
---

我日常用的 MacBook Air 出了一点问题，让我想到了保护上面的数据。搜索了一圈后，我发现我该做的保护都做到了，特分享下。

#### 安全保护

应用场景是，当我的电脑被偷了，该如何保护我电脑上的数据。

1. 设置开机登录密码

这是安全最基本的一步，给你的账号设置一个比较“强壮”的密码，数字+字母+符号，别单一用 `123456`。

2. 设置固件密码

即便有开机密码了，别人还是很容易，绕过它，我的博客里就能找到相关的文章。那么设置一个固件密码，就是第二步加强了安全。操作步骤是：

(1) 开机，按下 Command 和 R 键来启动恢复模式，选择`工具-固件密码实用工具`

(2) 在固件工具窗口中，选择`打开固件密码`，输入两次密码，然后确定。

(3) 退出固件工具，重启电脑即可。

3. 设置 FileVault

FileVault 在 macOS 上对整个磁盘加密，别人通过物理方式偷数据或修改数据变得困难。开启步骤，打开`系统设置`，进入到`安全和隐私`，选择 `FileVault`，如下图

![](/imgs/keep_your_data_safe_on_macos_0011.png)

点击打开 `FileVault`，会进入下一步

![](/imgs/keep_your_data_safe_on_macos_0021.png)

因为我并不相信 iCloud 的技术，所以，我选择了下一项，记录本地的恢复码，注意选择这项的一定要保存好这个恢复码。

![](/imgs/keep_your_data_safe_on_macos_0031.png)

点下一步后，它就开始加密整个磁盘，时间也会比较长，完成后重启电脑即可。

4. USB 接口的安全

[usbkill](https://github.com/hephaest0s/usbkill) 这个工具可以帮你处理 USB 接口的安全问题，它是一旦发现 USB 接口异常，就会关机。具体怎么安装，点上面的链接。

#### 数据备份

我会不定期的用 Time Machine 备份下系统，但随着我的开发环境迁往云端，本地我的数据变少了。重要的数据，比如密码之类的，我都是记忆在大脑里。

#### macOS 中关于用户的隐藏问题

可查看官方的文档 [https://support.apple.com/zh-cn/HT203998](https://support.apple.com/zh-cn/HT203998)