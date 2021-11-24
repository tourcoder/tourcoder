---
title: "macOS 下通过 Aria2 进行高速下载"
slug: how-to-download-faster-on-macos
author: Bin Hua
lastmod: 2020-08-13 09:40:15
date: 2019-11-08 07:23:57
tags: ["macOS", "aria2", "百度网盘"]
---

目前看来，Aria2 是 macOS 下比较干净舒服的高速下载方式了，但很多人卡在了配置上。

#### 下载安装

去它的官网下载文件，[https://github.com/aria2/aria2/releases](https://github.com/aria2/aria2/releases) ，选择最新版的 dmg 文件下载，然后安装即可。

#### 配置

打开终端工具，输入 `vi ~/.aria2/aria2.conf`，然后将下面的内容复制到里面

```
# Basic Options
dir=/Users/YourUsername/Downloads
input-file=/Applications/aria2c/session.dat
log=/Applications/aria2c/aria2.log
max-concurrent-downloads=15
max-connection-per-server=15
check-integrity=true
continue=true

# BitTorrent/Metalink Options
bt-enable-lpd=true
bt-max-open-files=16
bt-max-peers=8
dht-file-path=/opt/var/aria2/dht.dat
dht-file-path6=/opt/var/aria2/dht6.dat
dht-listen-port=6801
#enable-dht6=true
listen-port=6801
max-overall-upload-limit=0K
seed-ratio=0

# RPC Options
enable-rpc=true
rpc-allow-origin-all=true
rpc-listen-all=true
rpc-listen-port=6800
#rpc-secret=123456
#rpc-secure=true

# Advanced Options
daemon=true
disable-ipv6=true
#enable-mmap=true
force-save=true
file-allocation=none
log-level=warn
max-overall-download-limit=0K
save-session=/Applications/aria2c/session.dat
always-resume=true
split=10
min-split-size=10M

#百度网盘
user-agent=netdisk;5.2.6;PC;PC-Windows;6.2.9200;WindowsBaiduYunGuanJia
referer=http://pan.baidu.com/disk/home
```

其中第二行 `dir=/Users/YourUsername/Downloads` 中的路径可以按你的需求来写。

#### 下载工具

其实 aria2 是一个命令行下载工具，但网上还是有不少人围绕它开发了带有 UI 界面的工具，比如我常使用的 `Aria2GUI`，去其官网下载即可 [https://github.com/yangshun1029/aria2gui/releases](https://github.com/yangshun1029/aria2gui/releases) ，当然如果你有开发能力，你也可以自己开发一个。

这样，每次要下载的时候，直接打开 Aria2GUI 下载就好了，和用迅雷等其他下载软件一样。

#### 扩展

百度网盘里的东西，可以用浏览器插件导出下载地址，我使用的是 Firefox 下的 BaiduExporter，挺好的。