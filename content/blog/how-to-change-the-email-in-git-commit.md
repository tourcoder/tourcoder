---
title: "Git 更改 commit 历史"
slug: "how-to-change-the-email-in-git-commit"
author: "Bin Hua"
date: 2018-02-08 07:26:39
tags: ["git", "GitHub"]
draft: false
---

之前我在 `git config` 中都会将 Email 地址设置成我当前使用的电脑的名字，比如我当前使用的电脑名字叫 tourcoder，所以我就会设置成 `tc@tourcoder.local`，命令是 `git config --global user.emai tc@tourcoder.local`。最近因为工作需要，我需要将 Email 设置成真实的地址，比如我这里改成了 `tc@****`，除了在全局变量中做了修改，还要修改之前的历史 commit 记录中的 Email 地址。于是我执行了脚本命令

```
git filter-branch --commit-filter '
    if [ "$GIT_AUTHOR_EMAIL" = "tc@tourcoder.local" ];
    then
        GIT_AUTHOR_EMAIL="tc@@****";
    fi
        git commit-tree "$@";
        ' -f HEAD
```

命令执行，且自动更改后，执行 `git log` 检查得到如下结果

![](https://storage.tourcoder.com/tcblog/gitloghistory.png)

通常情况下，所有的历史 commit 记录的 Email 地址都更改过来了，但是有时候会遇到一个问题，我们挑选任意一个 commit 查看，比如最上面的这个，执行命令 `git show --pretty=format:"%ce" 424c8b2089742b0965089b3317670c6152c2ed2c，oops`，并没有更改过来，还是 `tc@tourcoder.local`

![](https://storage.tourcoder.com/tcblog/onegitcommit.png)

那是因为需要更改 `GIT_COMMITTER_EMAIL`，即在上面的脚本中加入 `GIT_COMMITTER_EMAIL` 的内容即可。

```
git filter-branch --commit-filter '
    if [ "$GIT_AUTHOR_EMAIL" = "tc@tourcoder.local" ];
    then
        GIT_AUTHOR_NAME="tc"
        GIT_AUTHOR_EMAIL="tc@***";
	GIT_COMMITER_NAME="tc";
        GIT_COMMITTER_EMAIL="tc@***";
    fi
        git commit-tree "$@";
        ' -f HEAD
```

执行脚本，完成。在 git 手册中有一篇关于 `[git filter branch](https://git-scm.com/docs/git-filter-branch)` 的文章中提到，还可以通过 `--env-filter` 来修改，脚本命令是

```
git filter-branch --env-filter '
    if test "$GIT_AUTHOR_EMAIL" = "tc@tourcoder.local"
    then
        GIT_AUTHOR_EMAIL=tc@***
        GIT_COMMITTER_EMAIL=tc@***
    fi
' -- --all
```

也能达到一样的效果，更多的用法，可以去查看上面的文章。
