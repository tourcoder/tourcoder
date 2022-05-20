---
title: "我常用设备的配置"
slug: "the-configuration-on-my-devices"
author: Bin Hua
lastmod: 2021-08-21T21:57:26+08:00
date: 2021-08-21T21:57:26+08:00
tags: ["macOS", "Debian", "iOS", "iPadOS", "watchOS", "MacBoo Pro", "iPhone", "iPad", "Apple Watch"]
---

整天整理了下自己的 MacBook Pro，发现以前写如何配置设备写了好几篇，太散乱，索性整理到这篇博文里。其实我有很长一段时间不折腾系统了，很多配置都是默认配置。这篇博文主要记录我日常使用的设备的配置情况及少量我必用的应用。

我日常用的设备有一台在 AWS 上的服务器作为开发机，一台 MacBook Pro，一部 iPhone，一台 iPad Pro 以及一块 Apple Watch。

### 开发机

我有一台架构在 aws 上的服务器作为开发机，在 GitHub 上我也分享过[它的配置信息](https://github.com/tourcoder/nerd)，只不过那个是英文版，这里列下中文版吧。

- 系统

Debian 系列，当前版本是 9.5+

- 机器名称

Nerd，修改 `/etc/hostname`
	
- 用户

除了本身的预置的 root 和 admin 这类用户外，我会增加一个新用户，并给予它 sudo 的权限
	
```
adduser nerdone
usermod -aG sudo nerdone
```
	
为了省事，设置了密码登录的方式，即修改 `/etc/ssh/sshd_config ` 中的 `PasswordAuthentication`
	
```
sudo sed -ri 's/^#?(PasswordAuthentication)\s+(yes|no)/\1 yes/' /etc/ssh/sshd_config
sudo service sshd restart
```

- 常用工具

  - Docker
	
  通过 [Dockerman](https://github.com/tourcoder/dockerman) 安装。
		
  - Git
	
  直接通过命令 `sudo apt install git -y` 安装。
	
  - Go
	
  通过 [glv](https://github.com/glv-go/glv) 安装。
	
  - NodeJS
	
  通过 [nvm](https://github.com/nvm-sh/nvm) 安装。
	
  - ZSH 和 ohmyzsh
	
  安装 ZSH，并查看版本
		
  ```
  sudo apt install zsh -y
  zsh --version
  ```
		
  将 zsh 设置为登录默认的 shell
		
  ```
  whereis zsh
  sudo usermod -s /usr/bin/zsh $(whoami)
  ```
		
  安装 ohmyzsh
		
  ```
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```
		
  更新 ohmyzsh
		
  ```
  upgrade_oh_my_zsh
  ```
		
  中文乱码问题，在 `~/.zshrc` 中增加
		
  ```
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  ```
		
  主题是我做的一个简单的主题，进入 `~/.oh-my-zsh/themes`，新建 `simple.zsh-theme` 文件，将下面的内容填写进去
		
  ```
  # simple.zsh-theme
  if [ $UID -eq 0 ]; then NCOLOR="red"; else NCOLOR="green"; fi
  local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"
  # primary
  promptPROMPT='$FG[237]------------------------------------------------------------%{$reset_color%}
  $FG[032]%~\
  $(git_prompt_info) \
  $FG[105]%(!.#.»)%{$reset_color%} '
  PROMPT2='%{$fg[red]%}\ %{$reset_color%}'
  RPS1='${return_code}'
  # color vars
  eval my_gray='$FG[237]'
  eval my_orange='$FG[214]'
  # git settings
  ZSH_THEME_GIT_PROMPT_PREFIX="$FG[075]($FG[078]"
  ZSH_THEME_GIT_PROMPT_CLEAN=""
  ZSH_THEME_GIT_PROMPT_DIRTY="$my_orange*%{$reset_color%}"
  ZSH_THEME_GIT_PROMPT_SUFFIX="$FG[075])%{$reset_color%}"
  ```
		
  编辑 `~/.zshrc`，将里面的 `ZSH_THEME` 后面的值改成 `simple`。
		 
这基本就是我的开发机 Nerd 的配置情况。

### MacBook Pro

- 系统

  都会更新最新最稳定版本的系统，开发者测试版本的系统我会用另外一台 MacBook Air 进行测试。

- 机器名称

  Deck，点屏幕右上角的苹果 logo 选择进入`系统偏好设置->分享`里修改。
	
- 用户

  - 通常我只会使用一个用户，并允许它管理该电脑，同时允许它通过 Apple ID 重置密码。
	
  - 关闭访客账户的所有权限。

  - 在登录选项中选择用户名和密码的方式，其他一律不选择。

  具体设置位置在`系统偏好设置->用户和组`里修改。
	
- 系统偏好里的设置

  以下设置均在`系统偏好设置`里进行设置。

  - Dock 和菜单栏

  - Dock 选择左侧显示，并且自动隐藏，关闭已经关闭的应用还显示在 Dock 上面的功能。
		
  在终端中输入命令
			
  ```
  defaults write com.apple.dock static-only -boolean true
  killall Dock
  ```
			
  即可，如果需要恢复则输入命令
			
  ```
  defaults delete com.apple.dock static-only
  killall Dock
  ```

  - 菜单栏只放了时间和控制中心这两个图标，其他系统自带的图标一律放在控制中心里。

  - 关闭 `Spotlight` 的快捷键，其之前的快捷键分配给另外一个更好用的类似应用 `Raycast`。

  - 辅助功能里，在`指针控制`中开启`触控板`的`三指拖拽`功能。

  - 屏幕时间里，开启`内容和隐私`功能，并取消`其他`下面`更改密码`的选项的选择；在`选项`中，开启屏幕时间，并开启`使用屏幕密码`。

  - 触控板里，选择轻点代替点击。

  - 安全和隐私里，在`通用`设置出，开启`立刻需要密码`功能，需要安装第三方的非 App Store 验证的应用，可以通过命令实现，打开`终端`这种应用，在里面输入
	
  ```
  sudo spctl --master-disable
  ```
	
  然后下面就多了一个`任何来源`的选项。
	
  开启 `FileValut` 功能，`FileVault` 会把整个硬盘每个文件每个字节全部加密，没有密码看不到数据。
		
- 其他设置

  - 关闭 message 和 facetime

  - 开机登录密码

  设置一个复杂的开机登录密码
		
  - 固件密码

  设置一个固件密码让被人即便拿到电脑也无法获取里面的内容，操作步骤是
		
    - 开机，按下 Command 和 R 键来启动恢复模式，选择`工具-固件密码实用工具`。
		
    - 在固件工具窗口中，选择打开固件密码，输入两次密码，然后确定。
		
    - 退出固件工具，重启电脑即可。

  - 隐藏用户

  有时候不希望别人登录电脑时显示自己的账户，可以通过隐藏的方式，以下 hiddenuser 就是要隐藏的用户名
		
  ```
  sudo dscl . create /Users/hiddenuser IsHidden 1
  ```
		
  以管理员的身份登录后执行上面的命令即可隐藏，如果想显示，则将上面的 1 改成 0。而隐藏个人目录和共享点则是命令
		
  ```
  sudo chflags hidden /Users/hiddenuser
  sudo dscl . delete "/SharePoints/Hidden User’s Public Folder"
  ```
  
  - Apple Watch 或 Touch ID 授权终端中的 sudo 命令

  编辑 `/etc/pam.d/sudo`，在第一行增加 `auth sufficient pam_tid.so` 即可。

- 必装软件

  其实随着 macOS 系统的逐步更新，很多以前必装的软件都逐步变得不重要，就说一些常规的吧。
	
  - Homebrew

  严格说它并不是一个软件，它是一个安装软件和包的工具，通过 
		
  ```
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
		
  安装即可。
	
  - Micro Snitch

  一款隐私保护的应用，它能检测那些应用在使用摄像头和麦克风，官网地址：[https://obdev.at/products/microsnitch/](https://obdev.at/products/microsnitch/)
		
  - Spectacle

  它通过键盘控制各应用窗口的位置，对我这种快捷键爱好者来说很适宜。官网地址：[https://www.spectacleapp.com/](https://www.spectacleapp.com/)，它的源码托管在 [GitHub](https://github.com/eczarny/spectacle) 上。
		
  - Surge (ClashX)

  因为 Surge 收费的原因，有人写了开源的版本 ClashX，它们主要被用来科学上网，其实它们是目前很好的调试工具。我基本只用 Surge。官网地址：[Surge](https://nssurge.com)，ClashX 是 macOS 下版本的，它是一个开源的，还有其他系统下的版本，具体去 GitHub 搜索。
		
  - SimPholders

  一款查看  Xcode 开发模拟器里面数据的工具，很棒，官网地址：[https://simpholders.com](https://simpholders.com)。
		
  - Raycast

  以前我用的是收费版本的 Alfred，现在已经改用这个伪开源的 Raycast，主要是它的自定义能力强，我喜欢这点。官网地址：[https://raycast.com](https://raycast.com)。
		
  - Pixelmator Pro

  图片处理工具，感觉和 Photoshop 差不多。官网地址：[https://www.pixelmator.com/pro/](https://www.pixelmator.com/pro/)。
		
  - Mounty

  在 macOS 下面比较窝心的一件事是 NTFS 格式外接盘的读取写入，之前用的一家最出名的实在有点贵，还是每年付，在网上发现了它。官网地址：[http://mounty.app/](http://mounty.app/)。
		
  - usbkill

  usbkill 是一个检测 usb 接口安全的工具，官网地址是：[https://github.com/hephaest0s/usbkill](https://github.com/hephaest0s/usbkill)
		
  - iTerm

  我比较喜欢的终端，它的主题我使用的是 minimal。官网地址：[https://iterm2.com](https://iterm2.com)。
		
  - AppCleaner

  更有效的清理删除应用，官网地址：[https://freemacsoft.net/appcleaner/](https://freemacsoft.net/appcleaner/)。
		
  - Dropbox

  目前我觉得最好用的网盘了，官网地址：[https://dropbox.com](https://dropbox.com)。
		
  - MacDown

  Markdown 格式文档写作工具，我这篇博文就是用它写的，官网地址：[https://macdown.uranusjr.com](https://macdown.uranusjr.com)。
		
  - MindNode

  我用来做脑图的应用，官网地址：[https://mindnode.com](https://mindnode.com)。
		
  - NameChanger

  有时候我写东西时批量命名会弄错，就用它来批量修改名字，比用命令行简便。官网地址：[https://mrrsoftware.com/namechanger/](https://mrrsoftware.com/namechanger/)。
		
  - Beyond Compare

  可以说是一个数据比较工具，很强大，官网地址：[https://www.scootersoftware.com](https://www.scootersoftware.com)。
		
  - Xcode

  开发 Apple 的应用必用的工具，官网地址：[https://developer.apple.com/xcode/](https://developer.apple.com/xcode/)。 千万不要从 AppStore 下载这玩意，要么去 [https://developer.apple.com/downloads/more](https://developer.apple.com/downloads/more) 下载，要么用 `xcode-install` 下载。先安装它，`gem install xcode-install`，然后选择自己要安装的 xcode 版本即可，`xcode-install` 项目地址 [https://github.com/xcpretty/xcode-install](https://github.com/xcpretty/xcode-install)。
  
  ```
  xcversion install 版本号 //安装
  xcversion update //更新
  xcversion list //列出所有版本
  ```
	 
  - Sublimetext

  非常好用的编码工具，官网地址：[http://sublimetext.com](http://sublimetext.com)。
        
  - VSCode

  微软出的开发工具，官网地址：[https://code.visualstudio.com](https://code.visualstudio.com)。
		
  应用软件基本是这些日常使用到的。
  
  - ImageOptim

  图片压缩软件，官网地址 [https://imageoptim.com/mac](https://imageoptim.com/mac)
  
  - Xscope
  
  测绘软件，官网地址 [https://xscopeapp.com/](https://xscopeapp.com/)
  
  - Take a break

  这是我最近最喜欢的应用，设置个时间，到时间了，提醒我站起来走一走，下载地址 [https://apps.apple.com/app/apple-store/id1457158844](https://apps.apple.com/app/apple-store/id1457158844)
  
  - VLC

  播放器
  
  - UninstallPKG

  PKG 残留包的卸载工具，官网地址 [https://www.corecode.io/uninstallpkg/](https://www.corecode.io/uninstallpkg/)
  
  - Camo Studio

  让手机的摄像头作为视频摄像头，官网地址 [https://reincubate.com/camo/](https://reincubate.com/camo/)
  
  - ColorSlurp

  取色工具，官网地址 [https://colorslurp.com/](https://colorslurp.com/)
  
  - DTMG

  移除 safari 里 Google 搜索结果的追踪链接，是 safari 的一个插件，下载地址 [https://apps.apple.com/us/app/dtmg-target-links/id1595441111?mt=12](https://apps.apple.com/us/app/dtmg-target-links/id1595441111?mt=12)
  
  - WiFi Scanner

  检索 WiFi 信号，下载地址 [https://apps.apple.com/us/app/wifi-scanner/id411680127?mt=12](https://apps.apple.com/us/app/wifi-scanner/id411680127?mt=12)
  
  - Kap

  录屏并能导出 gif，官网地址 [https://getkap.co/](https://getkap.co/) 
  
  - ASCIINEMA

  终端录屏工具，在终端用命令行操作，官网地址 [https://asciinema.org/](https://asciinema.org/)。
	
- 环境配置

  - ohmyzsh
	
  和开发机上安装一样，具体看开发机。
	
  - proxy

  虽然 surge 有增强模式，但有时候终端是需要更为方便的代理模式，zsh 中编辑 `~/.zshrc` 或者 bash 中编辑 `~/.bash_profile`
		
  ```
  alias proxy='export all_proxy=socks5://127.0.0.1:6153'
  alias unproxy='unset all_proxy'
  ```
		
  最后 `source ~/.zshrc` 使其生效即可。执行 `proxy` 启动终端代理模式，`unproxy` 取消终端代理模式。
	
  - git

  macOS 默认已经安装了 git，只不过版本比较低，通过 Homebrew 来安装最新版本的。
		
  ```
  brew install git //安装 git
  brew link git //关联 git，其实这步不用做，基本安装后即自动关联
  ```
		
  此时检查版本还不是最新版本,需要编辑 `~/.zshrc`，在里面增加
		
  ```
  export PATH=$(brew --prefix)/bin:$PATH
  ```
		
  最后 `source ~/.zshrc` 使其生效即可。
		
  - 显示完整的地址栏

  ```
  defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
  ```
		
  可以显示 Finder 当前目录的完整路径，取消则将 `YES` 改成 `NO` 即可。
		
  - 刷新 DNS

  有时候需要刷新下 DNS，则在 `~/.zshrc` 中增加一个 `alias`
		
  ```
  alias resetdns='sudo killall -HUP mDNSResponder;say DNS cache has been flushed'
  ```
		
  最后 `source ~/.zshrc` 使其生效即可。每次需要刷新 DNS 时，在终端中输入 `resetdns` 即可。
		
### iPhone 和 iPad Pro

iPhone 和 iPad Pro 我现在并不常用，也只是做了一些基本的设置，主要是安全隐私的。

- 进入 `设置->隐私->分析与改进`，关闭这里的`共享 iPhone 分析`和`共享 iCloud分析`。

- 进入 `设置->隐私->Tracking`，关闭这里的`允许 App 请求跟踪`。

- 进入 `设置->隐私->定位服务->系统服务->重要地点`，关闭这里的`重要地点`，并清除一次历史记录。

- 进入 `设置->隐私->Apple 广告`，关闭这里的`个性化广告`

- 进入 `设置->面容 ID 与密码`，拉到最下面，开启`抹掉数据`，当输入 10 次错误的密码后，iPhone 上的数据会被抹掉。

- 进入 `设置->Safari 浏览器`，将这里的`阻止跨网站跟踪`打开。

- 进入 `设置->通用->隔空投送`，平时应该是处于`接受关闭`或者`仅限联系人`的状态。

- App 的权限不乱给。

- 美区的 Apple ID，一个是 App 比较多，另外就是安全系数更高。

至于应用也没有几个，主要是我日常 iPhone / iPad 用的少。

### Apple Watch

基本的默认设置，只安装了 AutoSlepp，AutoWake, HeartWatch，全方位的检测自己身体情况的。其他的应用一律没装。
