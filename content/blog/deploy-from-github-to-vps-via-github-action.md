---
title: "通过 Github Action 将 GitHub 上的内容部署到 VPS"
slug: "deploy-from-github-to-vps-via-github-action"
author: "Bin Hua"
date: 2024-02-08T05:12:41Z
tags: ["github", "action", "deployment"]
draft: false
---

之前有写过自动部署的博文，但这几年实际操作中并没有那么深度使用，这些天访问 raw.githubcontent.com 总有点问题，就想着把 directConfig 的内容部署到自己的 vps 上，正好也能复习下 GitHub Action。

### 需求说明

我这次要完成的自动部署是当 master 分支有 push 的时候触发 GitHub Action 将内容直接部署到 VPS 上指定的文件夹里，因为这里只是几个静态文件，所以相对而言比较简单，更复杂的下次需要用的时候再来分享。

这里的需求的解决方案有两种

1. 在 Action 的“机器”上处理好所有的事情，最后将内容通过 `scp` 到 VPS 的指定目录去。（推荐）

2. 通过 Action 登录到 VPS 上，然后在 VPS 上处理所有的事情。（不建议，不建议的原因是生产力部署服务器，不应该做“部署过程”这件事，应该是做“部署结果”这件事，比如这里要用 git clone，不应该是在 VPS 操作，如果放在 VPS 上就要安装 git 等，操作的内容越多，要配置的东西越多，这是不对的。）

### 操作步骤

我这里用了第一种方式。

- 创建 Action 的文件

在项目仓库的根目录下创建文件，比如 `.github/workflows/main.yaml`，将下面的内容填写进去

```
name: deploy directConfig

on:
  push:
    branches: [ master ] # master 分支上 push 触发部署

jobs:

  build:
    # 在 ubuntu 上构建
    runs-on: ubuntu-latest 

    steps:
     # 拉取代码
     - uses: actions/checkout@v2 

     # 检查当前目录的文件
     - name: Check the folder
       run: ls -a

     # 删除 .git 和 .github 文件夹
     - name: Remove .git and .github folder
       run: rm -rf .git .github
       
     # 检查当前目录的文件
     - name: List files before renaming
       run: ls -a

     # 创建 rules 文件夹，并将内容移动到里面
     - name: Create rules folder and move all files into it
       run: mkdir rules && mv *.list rules/

     # 检查当前目录的文件
     - name: List files before renaming
       run: ls -a
       
     # 将内容 SCP 到 VPS 服务器
     - name: SCP rules 
       uses: appleboy/scp-action@master
       with:
        host: ${{ secrets.VPS_IP }}  # VPS 的 IP
        username: ${{ secrets.VPS_USER }}  # VPS 登录用户名
        port: ${{ secrets.VPS_PORT }} # VPS 端口
        key: ${{ secrets.SSH_KEY }} # 前面创建的私钥
        source: "rules" # 要上传的内容
        target: ${{ secrets.VPS_PATH }} # SCP 到的目录
```

里面的内容都有注释，很好理解，其中“检查当前目录文件”的内容是可以删除的，我是用来检查和调试的。

- 配置 GitHub 对应的仓库

在上面的 yaml 文件中，有一些 secrets 的信息，是不应该直接写在配置文件里的，要在 GitHub 对应的仓库里设置。具体位置 `Settings->Secrets and variables->Actions secrets and variables->Repository secrets`。

创建对应的参数，name 就是这里的 VPS_IP 等，对应的值（Secret）就是对应值。其中 SSH_KEY 是 VPS 的上创建的 key。用 ssh-keygen 来创建，然后将 .pub 的内容放入到 `~/.ssh/authorized_keys`，而这里的 key 是对应的私钥的内容。

此次，完成了所有的内容，当 master 分支 push 后，即可触发。