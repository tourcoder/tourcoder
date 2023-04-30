---
title: "Podman 和它的一切"
slug: "podman-and-its-more"
author: "Bin Hua"
date: 2023-04-29T10:46:20Z
tags: ["podman", "docker", "container"]
draft: false
---

在 Docker 各种“威胁”后，我决定尝试用 Podman 来替代 Docker。这篇文章会记录我在使用 Podman 的过程中遇到的问题和解决方案，应该是不定期更新的。

### 安装

Podman 的安装比较简单，在 macOS上直接用 Homebrew 安装

```
brew install podman
```

而在其他系统下安装 Podman，可以参看[官方文档](https://podman.io/)。

### 初始化

和 Docker 不一样，Podman 需要初始化

```
podman machine init
podman machine start
```

### 拉起容器

比如我需要拉起一个 MongoDB 的容器，则可以使用

```
podman run -d --name mongo -p 27017:27017 mongo
```

其实 Podman 在使用上和 Docker 差不多，命令行及参数也基本一致，可以去官网看详细的介绍。


### 遇到的问题

- 在 macOS 中映射到本地硬盘时遇到 `Error: statfs: no such file or directory` 的问题

    解决办法：初始化 machine 的时候，增加 `-v 宿主目录:容器目录` 参数，然后启动 machine 即可

    ```
    podman machine init -v /Users/nnn:/home/mmm
    ```