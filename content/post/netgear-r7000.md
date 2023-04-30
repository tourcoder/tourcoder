---
title: "Netgear R7000设置"
slug: netgear-r7000
author: "Bin Hua"
lastmod: 2020-08-13 09:16:39
date: 2018-09-21 07:46:29
tags: ["netgear", "网件"]
---

和小伙伴玩游戏，他总是掉网，后来一看是他买的破路由导致。让他买了个网件的路由器 R7000，并告诉他刷上梅林的固件。为什么买 R7000，因为我自己用的这款，一直感觉很棒。

**准备**

- 先下载需要用到的文件

    ```
    https://www.dropbox.com/s/jsa03cvtxr4bs9n/R7000.zip?dl=0
    ```

- Chrome 浏览器

**刷固件**
 
- 访问 `www.routerlogin.net` 进入自带的管理系统，将系统恢复到出厂设置，登录的用户名是 `admin`，密码是 `password` 

- 重启后再次访问上面的地址，在路径`高级-管理-固件更新`处上传上面解压出来的文件 `R7000_378.52_2.chk`，并更新路由器。 

- 重启后，再次进入，系统设置下的`恢复/导出/上传`设置中点击原厂设置后的恢复，将其恢复原厂设置。 

- 重启后，再次进入，固件升级中选择 `R7000_380.68_4-X7.7-koolshare.trx` 上传更新。如果你的网络中有其他路由器，可以先去内部网络(LAN)中设置访问地址，重启路由器。 

这样，固件刷新完成。

**一些设置**

设置都很简单，多试试就行，这里主要说明下路由借助 SS 翻 wall，找到下面`系统管理-系统设置-Persistent JFFS2 partition`，将两个选项都选择是，然后保存并重启路由。

重启后，进入到管理界面，在软件中心先升级软件平台，然后在离线安装下，上传安装包并安装。安装包哪里找？GitHub！

最后回到软件中心，设置并开启 SS 即可。

**关于信号和发射功率的问题**

- 单独设置 2.4G 和 5G

    ```
    2.4G
    无线模式 N only
    频道 1、6、11
    频道带宽 20 Mhz
    5G
    无线模式 N/AC mixed
    频道 149
    频道带宽 80 MHZ
    ```

- 地区设置成澳大利亚
		 
    进入到`「无线网络」-「专业设置」`拉到最下面，将地区改成`「澳大利亚」`，注意顶部的频段选择。
    
    需要注意是否 CFE 锁定，如果锁定，只能刷 CFE 解决。
    
- 硬盘无法挂载

    先检查硬盘格式是否为 ntfs，如果还是有问题，再进入到`「无线网络」-「专业设置」`，将里面的 `降低 USB 3.0 干扰` 关闭。

**网上看来的两组命令**

直接更改，该方法我这里没有起作用
		
- 安装 webshell，然后在里面执行命令

- 最大功率代码 wl txpwr_target_max

- 2.4G代码 wl -i eth1 txpwr_target_max

- 5G代码 wl -i eth2 txpwr_target_max

也是通过 webshell，或者通过 windows telnet 进入到路由

```
nvram set pci/1/1/maxp2ga0=120 
nvram set pci/1/1/maxp2ga1=120
nvram set pci/1/1/maxp2ga2=120
nvram set pci/2/1/maxp5ga0=120,120,120,120
nvram set pci/2/1/maxp5ga1=120,120,120,120
nvram set pci/2/1/maxp5ga2=120,120,120,120
nvram commit
reboot
```