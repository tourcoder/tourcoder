---
title: "修复 Centos 下 Appstream 错误"
slug: "how-to-fix-appstream-error-on-centos"
author: "Bin Hua"
date: 2022-03-05T17:26:41Z
tags: ["Centos", "Appstream"]
draft: false
---

今天在 centos 上操作 `yum update` 时遇到了一个错误，错误信息是

```
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
```

原因是 Centos 8 的支持周期在 2021 年最后一天结束了，需要手动更新下。

进入到 `/etc/yum.repos.d/` 里面，然后执行如下两个命令

```
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
```

这时候再执行更新就不会出错啦，哈哈哈