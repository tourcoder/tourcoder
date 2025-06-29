---
title: "在 iPad 上折腾 Debian"
slug: "install-debian-12-on-ipad-via-utmse"
author: "Bin Hua"
date: 2025-06-29T08:03:38Z
tags: ["iPad", "Debian", "UTMSE"]
draft: false
---

以前用 iPad 写码的时候我用两种方式

- 通过 ssh 到远程服务器，在服务器上写

- Web IDE

但这些都要借助网路，我就想有一个本地的 Debian，机缘巧合之下，先是遇到了 iSH，然后就碰到了这次的主角 - UTM se。这里的 se 版本是在 AppStore 上下载的 app，有一定的限制，如果需要更强大的功能，可以通过侧载。具体看[官网](https://getutm.app) 。这里记录下我的折腾经过。

第一次我安装错了版本，架构选错了，Debian 的镜像也选错了，正确的是应该选择 **arm64 的架构和 arm64 的 Debian 镜像**。

官方也提供了自己修改的镜像，桌面版的，具体看[这里](https://mac.getutm.app/gallery/)，但可惜**我的 iPad Pro 有点古早，Debian 11 和 12 都尝试了，都跑得不怎么样，太卡了**。

最后下载了 Debian-12.11.0-arm64-netinst.iso 网络安装版，并成功安装，此过程也遇到几个问题，

- 显示问题，Display output is not active

  进入系统安装菜单，可以选择 Install，也可以选择 Graphical Install，如果选择 Graphical Install 可以直接进入安装界面，但安装界面的文字渲染有问题，不显示文字，只能盲装。因为我只需要一个最小安装版的，所以我选择了 Install，这里的坑是大概率会出错，Display output is not active，这里的解决办法是，将光标移动到  Install 这一行，然后按键盘 e 键，在显示的内容里 `linux /install.aarch64/vmlinuz ... quiet` 这一行后面加上 `console=ttyS0 fb=false video=efifb:off`，然后按 `Ctrl+x` 启动。

  这个问题在系统安装完成后，也还是会出现这个问题，不用管，等个几分钟就自动跳过了，回头我研究下怎么修复。

- 网络问题

  因为我是最小化安装，软件包等都几乎是零的状态，甚至连网络都无法连接上。排查方式是

  - ip a 命令看是否存在除了 lo 之外的显卡，一般是 enp0s 开头。看它后面是否有 `state UP ` 和 `inet` 开头的 ip 地址，如果没有，说明没有自动获取，用 NetworkManager 或 nmtui 来处理。但因为是最小版本，这些都没有，只能通过手动临时处理。如果 `state DOWN`，先要将网卡起来 `ip link set <你的卡名字> up`

  ```
  sudo nano /etc/network/interfaces
  ```
  
  编辑里面的内容，将 enp0s1 替换成实际的

  ```
  # The primary network interface
  auto enp0s1
  iface enp0s1 inet dhcp

  # The loopback network interface
  auto lo
  iface lo inet loopback
  ```

  保存后重启网路服务 `sudo systemctl restart network.service` 或 `sudo ifup enp0s1`。

  继续配置下 DNS `sudo nano /etc/resolv.conf`，加入

  ```
  nameserver 8.8.8.8
  nameserver 8.8.4.4
  ```

  现在有了个临时网络，赶紧装 network-manager 和 nmtui。安装完成后，nmtui 命令进入网络编辑链接即可。


- 虚拟机的配置

  这是我当前虚拟机主要的内容

  - 架构：arm64

  - 系统：QEMU 9.1 ARM Virtual Machine(virt-9.1)

  - QEMU：开启了 UEFI Boot, RNG Device

  - Network：Emulated Network Card 是 virtio-net-pci

  其他均默认。