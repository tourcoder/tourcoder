---
title: "不翻墙下载 Google Drive 中的内容"
slug: "how-to-download-files-in-google-drive-without-vpn"
author: "Bin Hua"
lastmod: 2019-03-25 10:27:32
date: 2019-03-25 10:27:32
tags: ["Google", "googlecloud", "googlephoto", "google drive", "dropbox"]
---

众所周知的原因，Google Drive 是无法正常访问的，那么要下载里面的内容就需要用到梯子，但当你的文件过大时候，如果梯子不稳定或者速度慢，基本是没有希望将里面的内容下载下来的。这时候可以考虑用跳板的方式来处理这个问题。

- 一台 VPS

    去买一台海外的 VPS，该 VPS 需要能够被正常访问
    
- Gdrive 项目

    在该 VPS 上安装 Gdrive 这个项目文件，项目地址：[https://github.com/gdrive-org/gdrive](https://github.com/gdrive-org/gdrive)
    
    我使用的是 linux 服务器，所以执行如下命令
   
    ```
    wget -O /usr/bin/gdrive https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA&export=download
    chmod +x /usr/bin/gdrive
    ```
    
    然后执行 `gdrive about` 会给出一个链接，将该链接复制到浏览器里，会得到一个 code，将该 code 粘贴到终端处，即可完成授权。
    
- 操作命令

    可以通过项目的地址看到各种命令，这里需要用到的命令有两个 
    
    - `gdrive list`：查看文件命令，可以查看文件及其对应的 id

    - `gdrive download <id>`：下载对应的文件

- 下载到本地

    等文件下载到 VPS 后，就可以通过多种方式下载到自己的本地了。