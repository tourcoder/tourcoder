---
title: "手动清除远程桌面记录"
slug: "remove-history-of-remote-history"
author: "Bin Hua"
lastmod: 2020-08-13 08:48:41
date: 2009-07-22 05:43:18
tags: ["windows", "远程"]
---

运行regedit，打开注册表，找到 `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default`
右边的那些键值就记录了IP或者域名。 而最后一次连接的IP或者域名还会保留，直接删除“我的文档”下的“Default.rdp”文件

另外，如果想让远程桌面不保存记录 可以将 `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default`
这个键值的权限设置为不可改写, 同样Default.rdp也是，这样一来远程桌面连接就不会记录你的登陆信息了。