---
title: "通过 Github Actions 创建并发布 Docker images"
slug: "build-and-deploy-docker-images-via-github-actions"
author: Bin Hua
lastmod: 2021-12-01T13:16:36Z
date: 2021-12-01T13:16:36Z
tags: ["GitHub", "Actions", "Docker"]
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

项目地址：[这里](https://github.com/tourcoder/dockerdemo)
