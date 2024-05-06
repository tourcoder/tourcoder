---
title: "Gnome 学习手册"
slug: "gnome-handbook"
author: "Bin Hua"
date: 2024-05-01T11:47:51Z
tags: ["linux", "debian", "学习手册"]
draft: false
---

最近考虑将工作平台转移到 Debian 平台去，遂在一台惠普电脑折腾桌面版的 Debian。其实这个系统我并不陌生，毕竟我的服务器都是用的它，有点陌生的是桌面 [Gnome](https://www.gnome.org/)。

这里记录下我在折腾的过程中遇到的问题及解决方法，这篇应该是随着我的折腾不断更新的。

### 安装

我是从 [Debian](https://debian.org) 官方下载了 iso 文件，然后制作成 U 盘安装，安装全程没有遇到任何问题，也没有什么特别需要注意的。在安装的过程中会让选择桌面，选择 Gnome 即可。

### 配置

下面是一些常规配置，更为详细的配置，可以看我的开发机配置或者服务器版本的配置，在本博客中搜索相关关键字即可，或者阅读「[CentOS 和 Ubuntu](/centos-ubuntu)」。

- 给用户增加 sudo 的权限

  在终端中输入 `su`，进入 root 模式，在 `/etc/sudoers` 文件中增加 `用户名 ALL=(ALL:ALL) ALL` 即可。当然也可以用命令 `usermod -aG sudo 用户名`。

- 中文输入法

  输入法把我折腾得有点灰心，`fcitx` 总是不断的出问题，最后还是用了 gnome 自带的 `ibus`。因为是自带的，所以是不需要安装操作的。但我前面安装 fcitx 时怕冲突，卸载了 ibus，所以重新安装。执行命令 `sudo apt install ibus` 和 `sudo apt install ibus-pinyin`，然后配置一下即可。需要注意的是有时候在输入中文后，显示的内容是 `[Invalid UTF-8]`，则修改 ibus 的配置

  1. General 的 Half/Full Width 中选 Half

  2. Pinyin mode 中勾选 Full Pinyin 和 incomplete pinyin

  3. 重启 ibus restart

- 默认的 firefox-esr 浏览器无法输入中文

  我没有解决，我换用了 Chrome😛

- Chrome 浏览器

  在 Chrome 官网下载 deb 的包，执行 `sudo dpkg -i chrome.deb`，大概率会出现问题。问题是缺少一些依赖，比如 `fonts-liberation libu2f-udev`，可以直接安装它们，也可以通过安装时出错时给出的信息来解决，错误信息中有一条 `apt --fix-broken install`，执行它就行。

- 科学上网

  科学上网用的是 clash-verge，直接下载 deb 安装。没用 clash for windows 的原因是安装完后，发现安装后的 cfw 没有「系统代理」这个选项。

- 开发环境

  这些内容就没有说的必要了，就是一些我在日后开发中会用到的，我以前的博文都有说过。主要是 python/node/c/c++/go/docker/sublimetext/vscode/zsh/git/vim。

- 软件安装平台

  Homebrew 是个不错的东西，但我觉得如果在 Debian 上使用它，是对 apt 和 deb 的侮辱😂，所以我自然是只用 apt 和 deb 了。

- 启动器

  Alfred 和 raycast 都没有 Linux 版本，但 Gnome 自带的已经足够好用了，按 Windows 键就可以呼叫出来。也有其他的替代品，目前我都没有尝试，可以看[这里](https://alternativeto.net/software/alfred/?platform=linux)

### 吐槽

目前，我对 Gnome 桌面还处在熟悉的阶段，有些功能我还不太会用，所以有些吐槽可能还不准确。

- 手势

  目前的手势还是比较弱的。

- 触控板

  我以前一直用 Mac 的原因是我讨厌用鼠标，而 Mac 的触控板是非常棒。但现在 Gnome 结合的触控板还是有点难用的。比如拖拽一个窗口，要么是一手安装一手拖拽，要么是双击锁定窗口拖拽（这个大概率会不成功）。

- 窗口组织软件

  试用了几个窗口组织的软件，目前没有满意的，欢迎推荐一个[给我](mailto:code@tourcoder.com)，也许我可能会写一个。

- 电池时间/电源适配器

  这个和系统关系不是特别大，这更多的是电脑本身。现在的电源适配器还是一个小砖块，这就很离谱。至于电池续航能力，我希望这情况能有改善。


### 资料

Gnome 官网：[www.gnome.org](https://www.gnome.org/)


