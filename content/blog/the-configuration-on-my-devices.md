---
title: "我常用设备的配置"
slug: "the-configuration-on-my-devices"
author: "Bin Hua"
date: 2021-08-21T21:57:26Z
tags: ["macOS", "Debian", "iOS", "iPadOS", "watchOS", "MacBoo Pro", "iPhone", "iPad", "Apple Watch"]
draft: false
---

**这篇博文会保持不定期的日常更新**

整天整理了下自己的 MacBook Pro，发现以前写如何配置设备写了好几篇，太散乱，索性整理到这篇博文里。其实我有很长一段时间不折腾系统了，很多配置都是默认配置。这篇博文主要记录我日常使用的设备的配置情况及少量我必用的应用。

我日常用的设备有一台在 AWS 上的服务器作为开发机，一台 MacBook Pro，一部 iPhone，一台 iPad Pro 以及一块 Apple Watch。

### 开发机

我有一台架构在 AWS 上的服务器作为开发机，在 GitHub 上我也分享过[它的配置信息](https://github.com/tourcoder/nerd)，只不过那个是英文版，这里列下中文版。

- 系统：Debian 系列，当前版本是 9.5+

- 机器名称：Nerd，修改 `/etc/hostname`
	
- 用户：除了本身的预置的 root 和 admin 这类用户外，我会增加一个新用户，并给予它 sudo 的权限
	
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

  - Podman: 直接通过命令 `sudo apt install podman -y` 安装，比起 Docker，我现在基本用它。如果喜欢 Docker，可以通过 [Dockerman](https://github.com/tourcoder/dockerman) 安装。
		
  - Git：直接通过命令 `sudo apt install git -y` 安装。
 
  - Pidan: Git helper，安装方式在 [https://github.com/Pidan/pidan](https://github.com/Pidan/pidan)。
	
  - Go：通过 [glv](https://github.com/glv-go/glv) 安装。
	
  - NodeJS：通过 [fnm](https://fnm.vercel.app) 安装，之前长时间用 nvm，但现在转到 fnm 了，它更好。
	
  - ZSH 和 ohmyzsh
	
  安装 ZSH，并查看版本
		
  ```
  sudo apt install zsh -y
  zsh --version
  ```
		
  将 zsh 设置为登录默认的 shell
		
  ```
  whereis zsh
  sudo usermod -s /usr/bin/zsh $(whoami) //macOS: sudo chsh -s /bin/zsh $(whoami)
  echo $SHELL
  ```
		
  安装 ohmyzsh
		
  ```
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```
		
  更新 ohmyzsh
		
  ```
  omz update
  ```
		
  中文乱码问题，在 `~/.zshrc` 中增加
		
  ```
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  ```
		
  主题是我做的一个简单的主题 [larn](https://github.com/tourcoder/larn.zsh-theme)，进入 `~/.oh-my-zsh/themes`，将 larn 主题添加进去，最后编辑 `~/.zshrc`，将里面的 `ZSH_THEME` 后面的值改成 `larn`。

  - nvim，lazy.vim 和主题

  nvim 的安装可以看官方 GitHub 上的[安装指南](https://github.com/neovim/neovim/blob/master/INSTALL.md)

  lazy.vim 的安装可以看官方 GitHub 上的[安装指南](https://github.com/folke/lazy.nvim)

  我也写了一个小主题 [larn](https://github.com/tourcoder/larn.nvim)
		 
这基本就是我的开发机 Nerd 的配置情况。

### 随身带的开发机

最近在学习做一些前端的东西，这玩意包太大了，搞得系统很乱，不能忍受，就在本地安装了个虚拟机，将和 npm 开发相关的项目都丢进去了。

配置的东西和上面的开发机差不多。虚拟机用的是 [VirtualBox](https://www.virtualbox.org/) + [Debian](https://debian.org)。

话说甲骨文这么多年没有把 VirtualBox 变成收费项目，也是佩服的。用 Debian 是因为我太喜欢它了。

另外系统还要设置的东西有两个

一个是使用账户 `su -` 进去后，在 `/etc/sudoers` 里给当前用户增加个 sudo 的权限。

另外一个是共享文件夹，在 macOS 中在要共享的文件夹属性里修改成共享，然后在 VirtualBox 里设置共享文件夹指向这个文件夹，设置完后重启下虚拟机。最后进入系统后，用命令 `sudo mount -t vboxsf 共享的文件夹名 /mnt` 即可将内容挂载到 `/mnt` 下。

### MacBook Pro

这个博客关于 macOS 信息写得很多，其他的基本不用看了，看这篇文章即可。

- 系统：目前设置的系统版本是 macOS 15，即 macOS sequoia，更新到最新最稳定版本。

- 机器名称：Deck，点屏幕左上角的苹果 logo 选择进入`系统设置->通用->关于`里修改。
	
- 用户：具体设置位置在`系统设置->用户和组`里修改。

  - 我一般设置两个账户，普通账户和管理员账户，允许管理员账户通过 Apple ID 重置密码。
  
  - 给普通账户增加 sudo 权限，在管理员账户下编辑 `/etc/sudoers` 文件，增加一行 `普通用户名  ALL = (ALL) ALL`。
	
  - 关闭访客账户的所有权限。

  - 在「登录选项」中选择用户名和密码的方式，其他一律不选择（设置->锁屏）。
 
  - 隐藏用户：主要是用来隐藏管理员账户，hiddenuser 就是要隐藏的管理员用户名。
		
    ```
    sudo dscl . create /Users/hiddenuser IsHidden 1
    ```
      
    以管理员的身份登录后执行上面的命令即可隐藏，如果想显示，则将上面的 1 改成 0。而隐藏个人目录和共享点则是命令
      
    ```
    sudo chflags hidden /Users/hiddenuser
    sudo dscl . delete "/SharePoints/Hidden User’s Public Folder"
    ```

    这些命令可能会有修改，更新可以看[官方文档](https://support.apple.com/zh-cn/102099)。
	
- 系统里的设置：以下设置均在`系统设置`里进行设置。
  
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

  - 菜单栏（控制中心）只放了时间和控制中心这两个图标，其他系统自带的图标一律放在控制中心里。

  - 关闭 `Spotlight` 的快捷键，其之前的快捷键分配给自制的类似应用 `H9`，从 macOS 26 开始，换回了 `Spotlight`，够用了。但关闭了一些外置硬盘等索引 `Settings -> Spotlight -> Search Privacy` 里添加不要索引的盘，命令行就是 `sudo mdutil -i off /Volumes/盘符名`，`sudo mdutil -E /Volumes/盘符名` 删除已有索引。

  - 辅助功能里，在`指针控制`中开启`触控板`的`三指拖拽`功能。

  - 屏幕时间里，开启`内容和隐私`功能，并取消`其他`下面`更改密码`的选项的选择；在`选项`中，开启屏幕时间，并开启`使用屏幕密码`。

  - 触控板里，选择轻点代替点击。
 
  - 锁屏管理里，开启`立刻需要密码`功能。

  - 隐私和安全里，需要安装第三方的非 App Store 验证的应用，可以通过命令实现，打开`终端`这种应用，在里面输入 `sudo spctl --master-disable`，然后下面就多了一个`任何来源`的选项。

    关闭 `分析和改进` 和 `Apple 广告` 里的所有内容。
    
    开启 `FileValut` 功能，`FileVault` 会把整个硬盘每个文件每个字节全部加密，没有密码看不到数据。

    开启 `Lockdown Mode`，需要注意，开启它 AirDrop 会出现问题。

    高级中的内容都开启。
		
- 其他设置

  - 关闭并删除本地的 timemachine 快照，这块太占空间了。在磁盘工具中选择左侧的磁盘，点顶部菜单的视图 -> APFS，删除快照即可。也可以通过命令行操作，比如查看本地快照 `tmutil listlocalsnapshots /`，查看本地快照日期 `tmutil listlocalsnapshotdates`，删除某个快照 `tmutil deletelocalsnapshots '2024-09-20-127238'`

  - 关闭 message 和 facetime

  - 开机登录密码：设置一个复杂的开机登录密码
		
  - (这一步在 Apple M 系列芯片上已经没有了)固件密码：设置一个固件密码让被人即便拿到电脑也无法获取里面的内容，操作步骤是
		
    - 开机，按下 Command 和 R 键来启动恢复模式，选择`工具-固件密码实用工具`。
		
    - 在固件工具窗口中，选择打开固件密码，输入两次密码，然后确定。
		
    - 退出固件工具，重启电脑即可。
  
  - Apple Watch 或 Touch ID 授权终端中的 sudo 命令

    编辑 `/etc/pam.d/sudo`，在第一行增加 `auth sufficient pam_tid.so` 即可。

- 必装软件

  其实随着 macOS 系统的逐步更新，很多以前必装的软件都逐步变得不重要，就说一些常规的吧。
	
  - [Micro Snitch](https://obdev.at/products/microsnitch/)：一款隐私保护的应用，它能检测那些应用在使用摄像头和麦克风
		
  - [Spectacle](https://www.spectacleapp.com/)：它通过键盘控制各应用窗口的位置，对我这种快捷键爱好者来说很适宜，它的源码托管在 [GitHub](https://github.com/eczarny/spectacle) 上。
		
  - [Surge](https://www.spectacleapp.com/)：macOS 下很棒的网络调试工具。
		
  - [SimPholders](https://simpholders.com)：一款查看  Xcode 开发模拟器里面数据的工具，很棒。
		
  - [H9](https://binhua.org/h9)：以前我用的是收费版本的 Alfred，还有 Raycast，但越来越臃肿，就自己写了个简单的。
		
  - [Pixelmator Pro](https://www.pixelmator.com/pro/)：图片处理工具，感觉和 Photoshop 差不多。

  - [BuhoNTFS](https://www.drbuho.com/buhontfs)：收费版本的 NTFS 工具，比上面的要好。
		
  - [usbkill](https://github.com/hephaest0s/usbkill)：usbkill 是一个检测 usb 接口安全的工具。
		
  - [iTerm](https://iterm2.com)：我比较喜欢的终端，它的主题我使用的是 minimal。
		
  - [AppCleaner](https://freemacsoft.net/appcleaner/)：更有效的清理删除应用。
		
  - [NameChanger](https://mrrsoftware.com/namechanger/)：有时候我写东西时批量命名会弄错，就用它来批量修改名字，比用命令行简便。
		
  - [Beyond Compare](https://www.scootersoftware.com)：可以说是一个数据比较工具，很强大。
		
  - [Xcode](https://developer.apple.com/xcode/)：开发 Apple 的应用必用的工具。千万不要从 AppStore 下载这玩意，要么去[这里](https://developer.apple.com/downloads/more) 下载，要么用 `xcode-install` 下载。先安装它，`gem install xcode-install`，然后选择自己要安装的 xcode 版本即可，`xcode-install` 项目地址在 [GitHub](https://github.com/xcpretty/xcode-install) 上。
  
    ```
    xcversion install 版本号 //安装
    xcversion update //更新
    xcversion list //列出所有版本
    ```
	 
  - [Sublimetext](http://sublimetext.com)：非常好用的编码工具。
        
  - [VSCode](https://code.visualstudio.com)：微软出的开发工具。
  
  - [Xscope](https://xscopeapp.com/)：测绘软件。
  
  - [VLC](https://www.videolan.org/)：功能强大的播放器。
  
  - [UninstallPKG](https://www.corecode.io/uninstallpkg/)：PKG 残留包的卸载工具。
  
  - [ColorSlurp](https://colorslurp.com/)：取色工具。
  
  - [TargetLinks](https://apps.apple.com/us/app/dtmg-target-links/id1595441111?mt=12)：移除 Safari 里 Google 搜索结果的追踪链接，是 Safari 的一个插件。
  
  - [WiFi Scanner](https://apps.apple.com/us/app/wifi-scanner/id411680127?mt=12)：检索 WiFi 信号。

  - [Firefox](https://www.mozilla.org/en-US/firefox/)：我默认使用的浏览器，同时也安装了 Chrome，主要是用来开发调试，一个特别的设置，在输入框输入 `about:config`，搜索 `browser.fullscreen.exit_on_escape`，将它的值改成 `false`，解决 ESC 键退出浏览器全屏。

  - [Lulu](https://github.com/objective-see/LuLu/releases)：Lulu 算是一款保护你隐私的应用，它检测网络链接的请求，并及时地通知。
 
  - [The Unarchiver](https://theunarchiver.com/)：我很喜欢的解压应用。

  - [Thunderbird](https://www.thunderbird.net/)：邮件客户端，我以前并不喜欢在电脑上安装邮件客户端，但现在邮件账户有点多，就安装了 Thunderbird 客户端。为什么不用 macOS 自带的原生的 Mail？那破玩意结合 Siri 就是一个隐私收集器，各种信息被收集，更致命的是它还把信息通过 iCloud 同步，且不给拒绝同步的选项，我有发过[推文吐槽](https://x.com/tourcoder/status/1956225408208396354)。不用其它客户端是因为它们基本都内置了 AI 功能，我很讨厌。除了邮箱服务商提（比如：Google Workspace）供的 AI 功能，其它第三方的带有 AI 功能的邮件客户端，我一律不会使用。

  - [nvim](https://neovim.io)：我是直接下载安装包，解压改名成 `.nvim-macos-arm64`，然后在 `~/.zshrc` 里增加 `export PATH="$HOME/.nvim-macos-arm64/bin:$PATH"`。
	
- 环境配置

  - [ohmyzsh](http://ohmyz.sh/)：和开发机上安装一样，具体看开发机。
	
  - proxy：虽然 surge 有增强模式，但有时候终端是需要更为方便的代理模式，zsh 中编辑 `~/.zshrc` 或者 bash 中编辑 `~/.bash_profile`
		
    ```
    alias proxy='export all_proxy=socks5://127.0.0.1:6153'
    alias unproxy='unset all_proxy'
    ```
		
    最后 `source ~/.zshrc` 使其生效即可。执行 `proxy` 启动终端代理模式，`unproxy` 取消终端代理模式。
	
  - git：macOS 默认已经安装了 git，只不过版本比较低，通过 Homebrew 来安装最新版本的。
		
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

  - 其它环境，主要有 go，python，node 和 git。macOS 15 已经默认自带 python3 和 git。而 go 和 node 的安装可以看上面开发机部分。
 
  - 可选：fcrackzip/john-jumbo/hashcat，密码破解的命令行
		
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

安装的应用不是很多，iPad Pro 和 iPhone 上都差不多

- [GitHub](https://github.com)：代码管理器

- 支付宝

- Testflight：测试发布

- [Twitter](https://twitter.com)

- Gmail：邮件客户端，里面还包含了 Chat 和 Meetings

- Termius：移动端的终端

- Google Voice：语音通话

- 微信

- Telegram：主要用来聊天的

- Authenticator：二次认证

- Surge iOS：之前用的 Loon 和小火箭作为备选了

- Net Analyzer：网络应用

- Speedtest：网络测试应用

- 无忧行：移动公司的应用，我的移动的手机号码就是通过它虚拟化，可以在全球任何一个地方接中国号码的电话

- Youtube：视频应用

- Procreate：画图应用。

- GoodNotes：笔记应用，在 Notability 突然变卦后入手了 GoodNotes，但没想到这破玩意也随着变相收费了。

### Apple Watch

基本的默认设置，只安装了 AutoSleep，AutoWake, HeartWatch，全方位的检测自己身体情况的。其他的应用一律没装。

### Refer

一些其他的 macOS 设置的内容

- [macOS 简易手册](https://tourcoder.com/macos-manual/)

- [macOS 上必装的应用](https://tourcoder.com/essential-apps-on-macos/)

- [macOS 的安全设置](https://tourcoder.com/how-to-keep-your-data-safe-on-macos/)

- [macOS 下设置 Python 的默认版本为 Python 3](how-to-set-default-python-verion-to-python3-on-macos)

- [CentOS 和 Ubuntu](https://tourcoder.com/centos-ubuntu/)
