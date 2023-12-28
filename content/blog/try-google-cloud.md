---
title: "Google Cloud 体验"
slug: "try-google-cloud"
author: "Bin Hua"
date: 2017-03-12 06:57:51
tags: ["googlecloud"]
draft: false
---

体验了下 Google Cloud，还不错，这里分享下如何创建一个 VM，并且能通过外部 SSH 登录。

首先，创建一个项目，比如我创建了一个项目

![](https://storage.tourcoder.com/tcblog/try-google-cloud-create-project.PNG)

![](https://storage.tourcoder.com/tcblog/try-google-cloud-project-detail.PNG)

创建完项目后的状态，点左上角的菜单图标

![](https://storage.tourcoder.com/tcblog/try-google-cloud-choose-cc.PNG)

选择计算引擎

![](https://storage.tourcoder.com/tcblog/try-google-cloud-crea.PNG)

创建 VM 实例

名称 - 随便填写

地区 - 选择你想要在的地区

机器类型 - 就是你服务器的配置

启动磁盘 - 选择你的磁盘情况

身份验证 - 默认

防火墙 - 勾选两个

其他的暂时可以不配置。

![](https://storage.tourcoder.com/tcblog/try-google-cloud-crea-1.PNG)

再次点击左上角的菜单图标，然后选择网络，外部 IP 地址，生成一个 IP 地址，在创建的过程中，你可以将它附加在之前创建好的实例上。

基本到这里，你已经创建好一个 VM 实例了，那么怎么通过外部登录呢？

再次点击左上角的菜单图标，然后选择计算引擎，VM 实例

![](https://storage.tourcoder.com/tcblog/try-google-cloud-sshlogin.PNG)

如黄色标注的部分，点 SSH 下拉，你可以看到有多个连接方式，因为需要我的目标是使用其他 SSH 客户端，这里有说明。

因为我喜欢记忆复杂的密码，所以这里只介绍下密码的方式，点击上图中的黄色部分，在浏览器窗口中打开，登录进实例。

```
sudo mv /etc/nologin /etc/nologin.backup
```

改名 nologin 文件

```
sudo vi /etc/ssh/sshd_config
```

开启密码验证，将 `/etc/ssh/sshd_config` 文件中的 `PasswordAuthentication no` 改为 `PasswordAuthentication yes`

```
sudo groupadd users //创建用户组，通常这个组已经存在
sudo useradd -m -g users -s /bin/bash 你的用户名 //添加用户到组
sudo passwd 你的用户名  //设置用户密码
```

最后编辑文件

```
sudo vi /etc/sudoers
```

在该文件尾增加 `你的用户名 ALL=(ALL) ALL` 增加该用户的 sudo 权限，这种增加权限的方式，在每次执行 `sudo` 依旧会需要输入密码，去除输入密码，用 `你的用户名 ALL=(ALL:ALL) NOPASSWD: ALL`。也可以通过命令 `usermod -aG sudo 你的用户名` 将其加入到 sudo 权限组中。

```
sudo reboot
```

搞定，现在你可以在终端执行 ssh 你的用户名@ip 然后输入密码登录了。

注意：debian 8 后，已经禁止了 SSH 自动开启，如果使用的是 debian 8+，则需要将 ssh 添加到自动启动，注意权限

```
/etc/init.d/ssh start // 启动SSH服务，或者service ssh start
/etc/init.d/ssh status // 验证SSH服务状态
update-rc.d ssh enable // 添加开机自启动
update-rc.d ssh disabled // 关闭
```

其它登录方式，可以看[这里](https://cloud.google.com/compute/docs/instances/connecting-to-instance#standardssh)的说明，[Google Cloud](https://cloud.google.com/) 可玩的东西很多，想弄透，自行摸索。
