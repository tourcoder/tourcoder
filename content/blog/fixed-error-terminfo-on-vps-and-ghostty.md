---
title: "修正在 Ghostty 上登录 vps 后 terminfo 丢失的问题"
slug: "fixed-error-terminfo-on-vps-and-ghostty"
author: "Bin Hua"
date: 2026-07-17T09:17:27Z
tags: ["Terminal", "Ghostty", "bugfixed"]
draft: false
---

在 Ghostty 里登录到 VPS 后，在执行一些命令时总会提示错误，比如 `'xterm-ghostty': unknown terminal type.` 这是因为 Ghostty 后设置 `TERM=xterm-ghostty`，但 VPS 本身没有这个终端类型的 terminfo 条目，所以导致报上面的错误。

解决办法有几个：

1. 把 Ghostty 的 terminfo 复制到 VPS，这个几乎是最安全也最方便的方式

在不登录 VPS 的状态下，在 Ghostty 里执行 `infocmp -x xterm-ghostty | ssh <vps> -- tic -x -` 即可。这个操作会把本机的 terminfo 定义编译安装到远程的 `~/.terminfo/` 里，一次，以后所有程序都正常。远程可能会提示 tic 找不到，如果这样的话，先在 VPS 上装 ncurses（我用的是 Debian，它是自带的，不会报这个错误，只会报软件包旧了）。

2. 用 Ghostty 内置的 SSH 集成

在 Ghostty 配置文件 `~/.config/ghostty/config` 增加内容

```
shell-integration-features = ssh-terminfo
```

这样，ssh-terminfo 会自动把 terminfo 传到远程主机。

3. ssh 时临时改 TERM

在登录的时候，用类似下面的命令

```
TERM=xterm-256color ssh 你的vps
```

当然也可以在环境变量文件里设置，大差不离。其实在第二个方法里，用 `shell-integration-features = ssh-env` 也是变相的在 ssh 时把 TERM 改成 xterm-256color。

上面的方法任选一个后，重新登录到 VPS 后，执行 `infocmp xterm-ghostty`，如果不是报 unknown terminal type 等错误，而是能输出一大段定义，那就是成功了。
