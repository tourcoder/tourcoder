---
title: "修正 GitLab 安装时因 UTF-8 引起的错误"
slug: "how-to-fix-utf-8-error-when-installing-gitlab"
author: "Bin Hua"
date: 2021-11-22T03:34:54Z
tags: ["GitLab", "GitHub", "issue", "Git"]
draft: false
---

昨天在安装 GitLab 时遇到一个错误

```
execute[/opt/gitlab/embedded/bin/initdb -D /var/opt/gitlab/postgresql/data -E UTF8] (postgresql::enable line 49) had an error: Mixlib::ShellOut::ShellCommandFailed: Expected process to exit with [0], but received '1'
```

目测是因为 GitLab 默认使用的是 postsql 数据库，系统的编码导致了一个错误，想到每次 SSH 登录时经常冒出编码的提示，尝试修复这个问题，我最后的解决办法如下

```
echo "LC_ALL=en_US.UTF-8" >> /etc/environment
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
locale-gen en_US.UTF-8
```

如果提示 `locale-gen: command not found`，则安装即可 `apt install locales -y`，记得权限和重启服务器。

另外，我尝试了在 `/etc/profile` 里面增加

```
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

并 `source /etc/profile`，未能成功修复这个问题。
