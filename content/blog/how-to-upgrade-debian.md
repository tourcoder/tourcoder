---
title: "如何对 Debian 进行大版本升级"
slug: "how-to-upgrade-debian"
author: "Bin Hua"
date: 2021-12-14T15:09:46Z
tags: ["Debian", "how-to"]
draft: false
---

发现 Docker 的安装脚本在 Debian 的服务器上已经不被支持，通过 `cat /etc/os-release` 查看，得到如下结果

![](https://storage.tourcoder.com/tcblog/how-to-upgrade-debian-001.png)

也可以通过命令 `lsb_release -a` 获取更为简短的信息

![](https://storage.tourcoder.com/tcblog/how-to-upgrade-debian-002.png)

执行命令 `cat /etc/apt/sources.list` 确认一下包源

![](https://storage.tourcoder.com/tcblog/how-to-upgrade-debian-003.png)

果然也是旧的，那执行命令更新包源，并再次查看是否已经更新，我使用了 10 包源

```
sed -i 's/stretch/buster/g' /etc/apt/sources.list
sed -i 's/jessie/stretch/g' /etc/apt/sources.list
```

![](https://storage.tourcoder.com/tcblog/how-to-upgrade-debian-004.png)

最后执行命令 

```
apt upgrade -y
apt dist-upgrade
```

![](https://storage.tourcoder.com/tcblog/how-to-upgrade-debian-005.png)

再次查看，可以看出，系统已经更新到 Debian 10 了。还应该通过 `apt autoremove` 来清理下系统。
