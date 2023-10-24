---
title: "解决 AWS Codecommit 在 pull / push 的 403 错误"
slug: "codecommit-pull-push-403-error"
author: "Bin Hua"
lastmod: 2017-06-05 07:02:25
date: 2017-06-05 07:02:25
tags: ["Codecommit", "aws", "git"]
---

最近使用了下 AWS 推出的 Codecommit 的版本控制托管服务，简单明了，加上我也在用他家的云服务，配合部署，很方便。

不过很多时候，在通过 https 方式进行 push/pull 的时候，经常很烦人的出现 403 的错误

```
fatal: unable to access 'https://git-codecommit.us-west-2.amazonaws.com/v1/repos/projecta/': The requested URL returned error: 403
```

检查权限等问题，都是没有错的，官方也没有一个很好的解答，在搜索，并进行多种测试后发现可以通过下面的方式解决问题

![](/imgs/codecommit-pull-push-403-error-01.png)

打开 Keychain Access 这个应用，搜索 git-codecommit，你会发现相关的信息，双击有提交问题的库的信息，在弹出的窗口中选择 Access Control 这个标签

![](/imgs/codecommit-pull-push-403-error-02.png)

将下面的列表框中的内容，清空，并保存。

这时你再在终端中输入 `git pull/push` 命令时，就会弹出窗口

![](/imgs/codecommit-pull-push-403-error-03.png)

这里一定要选择 `Deny`，即拒绝，这样，你就能正常提交代码到 Codecommit 了，非常美中不足的是，每次提交，你都会遇到这个弹窗，每次你都要选择拒绝。

另外，通过 SSH 目前没有遇到这个问题，至于怎么设置 SSH 的方式，可以看下面 AWS 官方的这篇文章

[Setup Steps for SSH Connections to AWS CodeCommit Repositories on Linux, macOS, or Unix](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-unixes.html)
