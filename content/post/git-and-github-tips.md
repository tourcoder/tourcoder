---
title: "Git and Github Tips"
slug: "git-and-github-tips"
date: 2020-01-09T07:39:54Z
tag: ["git", "GitHub"]
---

### .gitignore 无法过滤文件夹或文件

有时候会遇到一个问题，如果在第一次 `git push` 后增加 `.gitignore` 文件，已经被 push 到 git 服务器的文件夹或文件还会继续更新，要想从 git 服务器端删除，需要将本地的该文件夹或文件删除，然后再 push 一次，但其实可以通过添加 `--cache` 这个参数来实现

```
git rm --cached filename
git rm --cached foldername
```

上面一个是过滤某个文件，一个是过滤某个文件夹，然后再 push，这时就会发现 git 服务器上已经没有该文件或文件夹了。

### 在 linux 上不用输入账号密码直接 push

可以利用 `credential` 来实现，这里配合 Github，先去 GitHub 申请一个 token，在 linux 的用户根目录下打开 credential 文件，如果没有则新建，比如 `vi ~/.git-credentials`，内容输入

```
https://your_github_username:your_token@github.com
```

保存，然后

```
git config --global credential.helper 'store --file ~/.git-credentials'
```

这样每次不用输入账号密码了，直接使用即可。也可以在项目根目录下进入 `.git`，配置里面的 `config` 文件

```
[credential]
        helper = store
```

将上面的内容增加到该文件里，保存后，在第一次输入密码后以后就不需要了。

### Git 中如何删除一个远程的分支？ 

执行命令 `git push origin :branch_name`，这个命令有点很无厘头，别忘了 : 号。

### Git 走代理 

此法解决速度慢的问题

```
git config --global http.proxy 'socks5://127.0.0.1:port' 
git config --global https.proxy 'socks5://127.0.0.1:port' 
```

取消则用

```
git config --global --unset http.proxy
git config --global --unset https.proxy
```

同样其它类似的设置取消，也用这种方式 `git config --global --unset 所设置的内容名`

### Git 获取远程分支
    
```
git checkout -b local_branch origin/remote_branch
```

### Git 增加 push 体积
    
```
git config --global http.postBuffer 524288000
```

### 解决 `fatal: refusing to merge unrelated histories` 的问题

在命令后面增加参数 `--allow-unrelated-histories`
