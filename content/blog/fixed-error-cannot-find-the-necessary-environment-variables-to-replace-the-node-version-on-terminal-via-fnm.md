---
title: "解决通过 fnm 安装的 nodejs 在终端中无法使用和切换的问题"
slug: "fixed-error-cannot-find-the-necessary-environment-variables-to-replace-the-node-version-on-terminal-via-fnm"
author: "Bin Hua"
date: 2024-10-07T05:59:01Z
tags: ["fnm", "nodejs", "terminal", "iTerm", "macOS", "zsh"]
draft: false
---

发现在 macOS 15 上通过 fnm 安装的 nodejs 在终端重启后总是无法被使用和切换，执行命令 `node -v` 会得到提示「找不到 node 命令」。

研究后发现，安装路径问题导致了 shell 配置文件中对应的代码执行失败。我用的是 zsh，所以配置文件是 `~/.zshrc`，以下同样。

安装完 fnm 后会在  shell 配置文件中自动添加

```
# fnm
FNM_PATH="/Users/your_account_name/Library/Application Support/fnm"
if [ -d "$FNM_PATH" ]; then
  export PATH="/Users/your_account_name/Library/Application Support/fnm:$PATH"
  eval "`fnm env`"
fi
```

**从上面的代码可以看出，fnm 的安装目录是 `/Users/your_account_name/Library/Application Support/fnm`，但 fnm 的实际安装目录是 `/Users/your_account_name/.local/share/fnm`，该目录可以通过 `fnm env` 命令获取到。**

所以，修改上面的安装目录即可解决问题

```
# fnm
FNM_PATH="$HOME/.local/share/fnm"
if [ -d "$FNM_PATH" ]; then
  export PATH="$FNM_PATH/bin:$PATH"
  eval "$(fnm env)"
else
  echo "FNM_PATH does not exist"
fi
```

上面代码中的 `else` 部分可以直接去掉。还有一个解决办法是直接将 `fnm env` 命令获取到的内容，一股脑贴在 shell 配置文件里也行。