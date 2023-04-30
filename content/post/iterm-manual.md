---
title: "iTerm 学习笔记"
slug: iterm-manual
author: "Bin Hua"
lastmod: 2020-08-13 09:23:56
date: 2019-01-19 13:20:45
tags: ["terminal", "iterm", "vim", "vi"]
---

2019 年在工作学习方面有几个 flag，其中一个就是全面掌握 vi/vim，而 iTerm 是很好的 vi/vim 学习工具。

也许有人要问，iTerm 不就是一个命令行工具么，怎么就成了 vi/vim 的学习工具了呢？用 Terminal 不是一样么？主要是它的一些特点，比如分屏。

### iTerm 的下载

目前 iTerm 3 还不是稳定版本，我选择了稳定版的 iTerm 2，下载地址 [iTerm 2 Download](https://www.iterm2.com/downloads.html)。

### iTerm 配置

安装 ohmyzsh，具体安装，可以看我以前写的[这篇文章](/macstyle-1-devconfig/)，这里推荐一个皮肤 [powerlevel9k](https://github.com/bhilburn/powerlevel9k)

在 iTerm 2 下当用 vim 来编辑的时候，会出现中文乱码的情况，输入命令 `vim ~/.vimrc`，编辑这个文件（不管是否存在），加入下面的内容

```
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
```

ZSH 的乱码编辑 `~/.zshrc` 文件，在文件里加入

```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

最后 source 一下即可解决中文乱码问题。

到这里 iTerm 就弄好了。

### 一些常用快捷键

- cmd + d 垂直分屏

- cmd + shift + d 水平分屏

- cmd + opt + 方向键 切换到指定位置的分屏

- cmd + ] 或者 [ 在最近使用的分屏直接切换

- cmd + 数字: 切换标签页

- cmd + 方向键 按方向切换标签页

- cmd + shift + s 保存当前窗口快照

- cmd + opt + b 快照回放

### proxy 设置

因为我使用的是 ohmyzsh，所以编辑 `~/.zshrc`，如果使用的是 bash，则编辑 `~/.bash_profile`，在结尾增加

```
# proxy
alias proxy='export all_proxy=socks5://127.0.0.1:1080'
alias unproxy='unset all_proxy'
```

然后通过 `source ~/.zshrc` 使配置生效。在使用前输入 `proxy` 即可开启代理， `unproxy` 关闭代理。
