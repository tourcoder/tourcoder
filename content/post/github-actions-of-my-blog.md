---
title: "基于 Github Actions 部署我的博客"
slug: "github-actions-of-my-blog"
author: Bin Hua
lastmod: 2021-06-02T22:34:08+08:00
date: 2021-06-02T22:34:08+08:00
tags: ["GitHub", "hugo"]
---

之前有说过我的博客移到了 GitHub Pages，我写博客的步骤是：

- 在开发机上直接写博文

- 用 `hugo` 来生成页面

- 将所有的内容 `git push` 到 GitHub 完成发布

最近在使用 GitHub Actions 做东西，顺便升级了下自己的博客。写博文的步骤更新成：

![](/imgs/github-actions-of-my-blog-01.png)

- 开发机上写博文

- 将写好的内容 `git push` 到 draft 分支

- 将 draft 分支的内容合并到主分支 master

- 当分支合并完成后，触发 Action

- 由 Action 来执行 hugo 生成页面并部署发布到展示内容的分支

看着似乎多了些步骤，我这样做的原因放到博文最后我再说明。整个 Action 的代码如下

```
name: GitHub Pages
on:
  push:
    branches: [ master ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2.3.4
      - name: Hugo setup
        uses: peaceiris/actions-hugo@v2.4.13
      - name: Build
        run: hugo --minify
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3.8.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_branch: gh
          cname: tourcoder.com
```

需要注意的是，GitHub 官方并没有提供合并到 master 的直接操作动作。换个角度考虑从一个分支合并到 master，也可以理解成是 push 的动作。当然也可以用 merge 方式，可以参考[这篇文章](https://github.community/t/triggering-workflow-on-merge/17165)。

最后说下为什么我改成现在的方式

1. 试一下 hugo 在 GitHub Actions 上的使用，我专注于产出内容，其它操作的东西交给 CI

2. 我的开发机是一台在 AWS 上的 VPS，没有图形化界面，我日常是 SSH 到该 VPS 后工作，写博客也不例外。它有一个不方便的地方是当博文中用到图片时，我需要 scp 传一张图片到该 VPS，太麻烦，同时我又不想给图片专门开发一个图床或者上传功能，而 GitHub 可以直接上传图片，在 GitHub.com 上也可以直接新建一个文件直接写，连开发机都不需要用。

3. 以前的操作方式是原稿内容，素材等和生成后的页面是混合在一起的，无意间内容多了一倍，也不便于管理，现在最终呈现的内容和原稿等在不同的分支里，方便管理。
