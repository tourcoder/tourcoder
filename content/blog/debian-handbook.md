---
title: "Debian 学习手册"
slug: "debian-handbook"
author: "Bin Hua"
date: 2024-05-01T11:47:51Z
tags: ["linux", "debian", "学习手册"]
draft: false
---

最近考虑将工作平台转移到 Debian 平台去，遂在一台惠普电脑折腾桌面版的 Debian。其实这个系统我并不陌生，毕竟我的服务器都是用的它，有点陌生的是桌面 [Gnome](https://www.gnome.org/)。

这里记录下我在折腾的过程中遇到的问题及解决方法，这篇应该是随着我的折腾不断更新的。

### 安装

我是从 Debian 官方下载了 iso 文件，然后制作成 U 盘安装，安装全程没有遇到任何问题，也没有什么特别需要注意的。

### 配置

- 给用户增加 sudo 的权限

  在终端中输入 `su`，进入 root 模式，在 `/etc/sudoers` 文件中增加 `用户名 ALL=(ALL:ALL) ALL` 即可。当然也可以用命令 `usermod -aG sudo 用户名`。

- 中文输入法

  输入法把我折腾得有点灰心，`fcitx` 总是不断的出问题。最后还是用了 gnome 自带的 `ibus`。因为我前面安装 fcitx 时怕冲突，卸载了 ibus，所以重新安装。执行命令 `sudo apt install ibus` 和 `sudo apt install ibus-pinyin`，然后配置一下即可。需要注意的是有时候在输入中文后，显示的内容是 `[Invalid UTF-8]`，则修改 ibus 的配置

  1. General 的 Half/Full Width 中选 Half

  2. Pinyin mode 中勾选 Full Pinyin 和 incomplete pinyin

  3. 重启 ibus restart

- 默认的 firefox-esr 浏览器无法输入中文

  我没有解决，我换用了 Chrome

- Chrome 浏览器

  在 Chrome 官网下载 deb 的包，执行 `sudo dpkg -i chrome.deb`，但总是出现问题，问题是缺少 `fonts-liberation libu2f-udev` 这些依赖，可以直接安装它们，也可以通过安装时出错时给出的信息来解决，错误信息中有一条 `apt --fix-broken install`，执行它就行。

- 科学上网

  科学上网用的是 clash-verge，直接下载 deb 安装。没用 clash for windows 的原因是安装完后，发现 cfw 没有「系统代理」这个选项。

- 开发环境

  这些内容就没有说的必要了，就是一些我在日后开发中会用到的。py/node/c/c++/go/docker/sublimetext/vscode/zsh/git。

- 软件安装平台

  Homebrew 是个不错的东西，但我觉得如果在 Debian 上使用它，是对 apt 和 deb 的侮辱😂，所以我自然是直用 apt 和 deb 了。
