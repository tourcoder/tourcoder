---
title: "通过 GitLab Console 重置用户密码"
slug: "reset-user-password-for-gitlab-user-via-console"
author: "Bin Hua"
date: 2023-08-08T08:46:22Z
tags: ["gitlab", "githuab"]
draft: false
---

可以通过 ssh 登录服务器重置 gitlab 用户密码，一般是重置管理员密码，因为一般用户的密码完全可以通过管理员后台来重置。

ssh 登录到服务器，然后执行 `gitlab-rails console`，在出现提示符后，输入 `user = User.where(@root).first`，再输入 `user.password='Aa123456@'`，最后输入 `user.save!`。
