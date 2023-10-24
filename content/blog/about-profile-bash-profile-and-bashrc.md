---
title: "一张表格看懂 profile,bashrc,bash_profile 的区别"
slug: "about-profile-bash-profile-and-bashrc"
author: "Bin Hua"
lastmod: 2019-01-05 07:58:19
date: 2019-01-05 07:58:19
tags: ["macOS", "linux", "bash"]
---

在 Linux/macOS 系统中，经常会使用到 profile，bash-profile 和 bashrc，那么他们具体表达的意思是什么呢？通过一张表格可以看出来

|名称|位置|作用及作用域|
|---|---|---|
|profile|/etc/profile|用于设置系统级的环境变量和启动程序，在这个文件下配置会对所有用户生效。当用户登录时，文件会被执行，并从 /etc/profile.d 目录的配置文件中查找 shell 设置。|
|bashrc|系统级位于/etc/bashrc、用户级位于 ~/.bashrc| bashrc 文件只会对指定的 shell 类型起作用，bashrc 只会被 bash shell 调用|
|bash_profile|~/.bash_profile|只是针对某一个用户的设置，当该用户登录时，文件会被执行|

其中，在 profile 中增加环境变量时，通过 export 方式，比如 `export HOST=tourcoder.com;` 表示将 HOST 改成 tourcoder.com，如果是多个变量值，用 `:` 分割，形如 `变量名=变量1:变量2;`

当添加完变量后，需要生效，可以重启电脑生效，但也可以强制生效，执行命令

```
source /etc/profile
```

查看是否生效，可以用命令 `echo $变量名` 来查看。