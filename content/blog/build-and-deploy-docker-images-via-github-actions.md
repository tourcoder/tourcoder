---
title: "通过 Github Actions 创建并发布 Docker images"
slug: "build-and-deploy-docker-images-via-github-actions"
author: "Bin Hua"
date: 2021-12-01T13:16:36Z
tags: ["GitHub", "Actions", "Docker", "SSH"]
draft: false
---

厌烦了每次手动的创建 docker images，然后还需要发布到 GitHub Container Registry。研究了下 GitHub Actions 在这方面的应用，写了个 demo，记录下操作步骤。

创建一个项目，这里是 dockerdemo，只有一个文件 app.js

```
const Koa = require("koa");
const port = "9000";
const app = new Koa();
app.use(async ctx => {
  ctx.body = 'Hello World';
});
app.listen(port);
```

如果正常执行，即 `node app.js`，访问 `http://localhost:9000` 可以得到 `Hello World`。

创建 Dockerfile 文件

```
FROM tourcoder/nodebasic:latest
RUN mkdir -p /tcdocker/dockerdemo
COPY . /tcdocker/dockerdemo
WORKDIR /tcdocker/dockerdemo
RUN npm install
EXPOSE 9000
CMD node app.js
```

没有什么特别的地方。

创建 Action，即在项目的根目录下的 `.github/workflows/` 文件夹下创建一个 `.yml` 文件，名字随意，我写了 `github.yml`

```
name: GitHub Actions Demo
on:
  push:
    branches: [ master ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2.4.0
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1.6.0
      - name: Login to Github Packages
        uses: docker/login-action@v1.10.0
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GHCR_TOKEN }}
      - name: Build image and GitHub Container Registry
        uses: docker/build-push-action@v2.7.0
        with:
          context: ./
          tags: |
            ghcr.io/tourcoder/dockerdemo/dockerdemo:latest
          push: ${{ github.ref == 'refs/heads/master' }}
```

本来我是想自己写一个这个 Action 的，但 GitHub Marketplace 里面有 Docker 公司写好的，索性用了它的。每一步的作用可以看 `name` 的说明。这里需要说明的内容是

- `github.actor`: 会自动获取

- `password`: 在 `https://github.com/settings/tokens` 创建一个 token，权限是 `repo` 以及 `package` 的权限，得到一个 token，然后进入项目的 `settings->secrets->actions`，创建一个 `secret`，在 `name` 部分写入内容，我这里是 `GHCR_TOKEN`，而在 `Value` 里写入刚才获取到的 token。

- 最后一个 push 表示只是对 master 分支起作用，即向 master 分支 push 或 merge 才会激发该 action。致此，一个通过 Github Actions 创建并发布 Docker images 的功能就实现了。

#### 利用 GitHub Actions 将 images 自动 pull 到服务器

GitHub 并不建议这么做，应该的做法是在服务器上进行部署的操作，这里我只是做了一个实验。大概的步骤是通过 ssh 登录到服务器，然后执行 docker pull 命令即可，用 GitHub Actions 就是下面的内容

```
- name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.DEPLOY_HOST }}
          username: ${{ secrets.DEPLOY_USERNAME }}
          key: ${{ secrets.DEPLOY_KEY }}
          port: ${{ secrets.DEPLOY_PORT }}
          script: |
            sudo docker pull ghcr.io/tourcoder/dockerdemo/dockerdemo:latest
```

几个参数的解释

|参数名|说明|
|---|---|
|host|服务器地址|
|username|登录名|
|key|登录的密钥，需要用私钥，而非 .pub 公钥|
|port|ssh的端口，默认为 22|

将这些内容都写入到该项目的 `settings->secrets->actions` 中，和上面创建 token 时候一样。

**备注**

1. 在执行最下面一行的 `sudo docker` 时会遇到问题 `sudo: no tty present and no askpass program specified`，解决办法是将用户名的 sudo 设置成无需密码，即编辑 `/etc/sudoers`，增加一行 `用户名 ALL = NOPASSWD: /etc/docker, /usr/bin/docker, /usr/libexec/docker`，需要重启。

2. 本地创建密钥 `ssh-keygen -t rsa -C "密钥名"`，公钥需要上传到服务器 `ssh-copy-id -i id_rsa.pub 登录名@服务器地址`，而在 GitHub 的项目设置里用的是私钥 `id_rsa`。

3. 在拉取 ghcr 的内容时提示未认证，有两种处理办法，一种是在上面的发布脚本里写 `cat ~/ghtoken | sudo docker login ghcr.io -u tourcoder --password-stdin`，但真不建议这样做，建议在服务器上执行一次这个命令比较好。

最后

项目地址：[这里](https://github.com/tourcoder/dockerdemo)
