---
title: "NGROK 使用指南"
slug: "ngrok-abc"
author: "Bin Hua"
date: 2021-06-18T11:50:07Z
tags: ["ngrok", "开发工具"]
---

日常情况下，我都是在一台带有公网独立 IP 的 vps 上做开发，给外部提供调试链接是一件很方便的事。而在没有公网 IP 的本地电脑上，就有一个好用的东西提供了类似的服务 -- ngrok。这个东西使用极其简单，以 macOS 为例

- 先去官网下载

  进入 [http://ngrok.com](https://ngrok.com)，注册账号获取 Authtoken，并下载系统对应的版本，我这下载了 macOS 的版本。

- 将下载的文件解压后放到一个目录下，比如我放入了 `~/workspace/tool` 这个目录下

- 进入到这个目录，并执行命令进行授权(如已经授权，此步可以省略)

  ```
  ./ngrok authtoken 官网得到的token
  ```

- 将程序衍射到外网

  ```
  ./ngrok http 端口号
  ```

  这里的端口号是本地程序运行的端口号，比如我的程序端口号是 3700，则执行 `./ngrock http 3700` 即可得到如下结果

  ![](https://storage.tourcoder.com/tcblog/ngrok-abc-01.jpg)

  如上图，`http://2d2a38beadcf.ngrok.io` 这个就是与本地程序衍射的外部链接，除了 http 链接外，它还提供了 https 的链接。

完事，更多用法可以参考 `./ngrok help`。

还可以用个更省事的办法，就是将执行文件 `ngrok` 移动到 `/usr/local/bin`，然后直接用 `ngrok` 来运行，比如 `ngrok http 3000`。
