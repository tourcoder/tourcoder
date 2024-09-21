---
title: "解决 macOS 无法连接星巴克等公共网络的问题"
slug: "how-to-fix-public-wifi-connection-issue-on-macos-15"
author: "Bin Hua"
date: 2024-09-21T02:13:36Z
tags: ["macos", "sequoia", "starbucks", "mstand"]
draft: false
---

最近升级到 macOS 15 sequoia 这个系统，在连接公共网络的时候总是连接不上。

### 问题描述

星巴克无法弹出认证窗口

MStand 在认证 192.168.100.2 处出错

手机热点连接 10 分钟左右就会自动掉线

### 解决办法

1. 关闭代理软件（代理设置），基本能解决类似 MStand 的问题

2. 访问 `captive.apple.com` 能解决类似星巴克无法弹出认证界面的问题

3. 在终端中进入到 `~/Library/LaunchAgents`，然后新建一个文件，比如 `apple.captivenetworkassistant.plist`，内容如下

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" \
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    <key>Label</key>
    <string>apple.captivenetworkassistant</string>
    <key>LowPriorityIO</key>
    <true/>
    <key>ProgramArguments</key>
    <array>
    <string>open</string>
    <string>/System/Library/CoreServices/Captive Network Assistant.app</string>
    </array>
    <key>WatchPaths</key>
    <array>
    <string>/Library/Preferences/SystemConfiguration</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    </dict>
    </plist>
    ```

    然后加载并执行这个文件

    ```
    launchctl load apple.captivenetworkassistant.plist
    launchctl start apple.captivenetworkassistant
    ```

    也可以修复网络问题。如果要删除这个

    ```
    launchctl stop apple.captivenetworkassistant
    launchctl unload apple.captivenetworkassistant.plist
    rm apple.captivenetworkassistant.plist
    ```

以上是从网络里整理出来的办法，欢迎有更好的解决方案的补充。

### Refer

- [macOS Catalina WiFi issue — captive portal broken](https://poweruser.blog/macos-catalina-wifi-issue-captive-portal-broken-45610cc016b5)

- [macOS 10.15.1 连接星巴克 Wi-Fi 无法弹出认证页面问题](https://v2ex.com/t/615867)