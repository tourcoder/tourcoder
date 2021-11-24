---
title: "解决 Homebrew 速度慢的问题"
slug: homebrew-slowly
author: Bin Hua
lastmod: 2020-08-13 09:39:25
date: 2019-10-13 15:47:03
tags: ["macOS", "cocoapods", "npm", homebrew", "brew", "ruby"]
---

最近 Homebrew 慢的出奇，甚至连安装其本身都出现了问题，归根揭底是 GitHub 在国内访问慢导致，一劳永逸的解决办法估计只有换源吧。更换的地方有两处，一是其本身，还有一个是 cask。我使用了中科大的源。

先安装 Homebrew，其[官网](http://brew.sh)有说明安装方式

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

但安装是非常慢，甚至经常中断安装，可以通过本地安装来解决这个问题，先下载安装文件，即下载上面地址中的文件

```
https://raw.githubusercontent.com/Homebrew/install/master/install
```

打开下载后的文件，编辑里面的

```
BREW_REPO = “https://github.com/Homebrew/brew“.freeze
```

更改成中科大的源

```
BREW_REPO = "https://mirrors.ustc.edu.cn/brew.git".freeze
```

在终端中执行该文件即可

```
/usr/bin/ruby install
```

这样就可以安装完成了！

在使用过程中也会出现慢的问题，同样将官源更改成中科大的源。

```
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.zshrc //如果是 `bash` 用户，将 `zshrc` 改成 `bash_profile`
source ~/.zshrc //同上

cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git
```

如果不喜欢，还是想用官方的，则将上面对应的地址换成下面官方的即可

```
https://github.com/Homebrew/brew.git
https://github.com/Homebrew/homebrew-core.git
https://github.com/Homebrew/homebrew-cask
```

其实在国内的环境下，很多时候各种库，插件，设置是操作系统都需要换源，中科大的这里是个很不错的源站，地址 [https://mirrors.ustc.edu.cn/help/index.html](https://mirrors.ustc.edu.cn/help/index.html)

还有一种解决办法，进入 hosts 增加一条

```
vi /etc/hosts
```

在里面增加一条

```
199.232.28.133 raw.githubusercontent.com
```

即可，因为是域名被污染了。

有时候在用 homebrew 安装软件时遇到 `Could not resolve HEAD to a revision` 的问题，解决办法是执行命令

```
git -C $(brew --repository homebrew/core) checkout master
```

或者

```
git -C $(brew --repository homebrew/core) reset --hard HEAD.
```

即可解决问题。


