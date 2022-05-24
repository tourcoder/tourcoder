---
title: "macOS 下设置 Python 的默认版本为 Python 3"
slug: "how-to-set-default-python-verion-to-python3-on-macos"
author: Bin Hua
lastmod: 2022-05-24T14:11:41Z
date: 2022-05-24T14:11:41Z
tags: ["python", "macOS"]
---

macOS 下默认的 python 版本是 2.7，可以通过设置将其更改为 python 3.

先安装，我是通过 homebrew 来安装的

```
brew install python3
```

找到 python3 的安装位置

```
which python3
```

一般都会在 `/usr/local/bin/python3`

在 `~/.zshrc` 中增加一个新的 alias

```
alias python='/usr/local/bin/python3'
```

最后 `source ~/.zshrc` 使其生效即可。