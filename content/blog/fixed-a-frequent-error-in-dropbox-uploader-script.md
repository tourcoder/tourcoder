---
title: "修复一个 Dropbox Uploader 脚本中频繁出现的问题"
slug: "fixed-a-frequent-error-in-dropbox-uploader-script"
author: "Bin Hua"
date: 2023-12-27T09:02:48Z
tags: ["dropbox", "uploader"]
draft: false
---

我有时候会用 [Dropbox Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) 这个脚本将一些内容自动备份到 Dropbox，具体的操作方式可以看我以前的[博文](https://tourcoder.com/auto-backup-on-linux/)。

但最近向新建的 Dropbox app 上传内容时总是提示下面的错误

```
Some error occured. rerun the script with "-d" option and check the output and logfile: /tmp/du_resp_debug.
```

在上传脚本增加了 `-d` 参数后运行，即 `./dropbox_uploader.sh -d upload local_file dropbox` 后根据错误发现是权限的问题，缺少写入权限。

可以打开 `https://www.dropbox.com/account/connected_apps` 这个页面查看你的 app 是否有写入权限，没有的话，在进入该 app 的设置页面增加写入权限即可。

然后在服务器端已经关联的账号，可以用 `./dropbox_uploader.sh unlink` 先取消关联，然后再重新关联即可。

补充两句

- 以前在 dropbox 开发者中心创建 app 的时候，会自动有写入权限，弹窗提示。但现在也弹窗提示了，但创建完成后没有写入权限，需要另外配置。

- 如果只是修改了 app 的权限，增加写入权限，也不能写入，服务器端一定要重新关联。

不知道是不是只有我遇到了，这个很奇怪！