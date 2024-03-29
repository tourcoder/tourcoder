---
title: "博客迁移到 Cloudflare Pages"
slug: "hello-cloudflare-pages"
author: "Bin Hua"
date: 2021-09-21T07:39:09Z
tags: ["CloudFlare", "GitHub", "Pages"]
draft: false
---

之前本博客是架设在 GitHub Pages 上，利用 GitHub Actions 进行自动化部署，具体看[这篇](https://tourcoder.com/github-actions-of-my-blog/)，在最近几个月的试用下来，有三个问题很严重。

- GitHub Actions 抽风的时候很多，导致编译不成功的时候也很多。

- ssl 总是莫名其妙的出问题，导致网站无法被访问

- GitHub Pages 也会抽风，导致网站无法被访问

昨晚在将博客转移到 Linode 的 VPS 的时候发现 CloudFlare Pages 的广告，试用了下，感觉不错。主要是它和 GitHub 结合，基本不需要做其他的修改。大概步骤设置如下：

- 进入 pages.dev，创建一个项目，选择 GitHub 账号和对应的博客仓库关联。

- 我用的是 hugo，则在构建部署设置里，命令选择 hugo，输出目录和根目录不修改，环境变量变量名为 `HUGO_VERSION`，值 `0.81.0`，为 hugo 指定版本，使用当前 CloudFlare 默认版本会出现编译通不过的情况。生产力分支选择发布分支，我选择的是 master，当所有的内容合并到 master 分支后，启动部署。

![](https://storage.tourcoder.com/tcblog/hello-cloudflare-pages-001.png)

配置到此完成，测试下。更改博客的内容，提交并合并到 Master 分支，此时其他分支开始构建预览，并会在 GitHub 给出结果。

![](https://storage.tourcoder.com/tcblog/hello-cloudflare-pages-002.png)

![](https://storage.tourcoder.com/tcblog/hello-cloudflare-pages-003.png)

当构建成功后，CloudFlare 将自动完成后面的发布等工作。

![](https://storage.tourcoder.com/tcblog/hello-cloudflare-pages-004.png)

#### 需要注意

如果只是单个分支，推送到该分支，即自动完成构建和正式的发布。

我是两个分支，master 是作为发布分支，draft 是草稿分支，当我将写好的内容 push 到 draft 这个草稿分支后，CloudFlare 会开始构建并发布一个预览版本供我预览。预览后，我觉得没有问题，在 GitHub 上将 draft 分支合并到 master 分支，此时 CloudFlare 会自动基于 master 发布正式版。

### Backblaze

我给自己的博客库创建了一个 Codespace，每次写博客的时候，只要打开这个库，我就能用任何设备直接写，但这样做有个问题就是每次上传博文中要用到的图片就比较麻烦。而通过将图片传到外部图库，然后在博文中直接引用，是一个不错的办法。目前很多图库，我用的是 Backblaze 免费的存储服务。它的网址是 [https://www.Backblaze.com](https://www.Backblaze.com)。它目前免费的额度是

10GB 的存储容量 / 每天 1G 的流量 / 上传请求和下载请求各是每天 2500次，对我的博客来说，目前足够。另外通过 Cloudflare 还能实现无限流量，因为 Backblaze 加入了 Cloudflare 的带宽联盟，他和 Cloudflare 之间的流量是免费的。

- 注册 Backblaze 账号，创建一个 Bucket，在 `Bucket Settings` 里面的 `Bucket info` 填入 `{"cache-control":"max-age=720000"}`。

- 上传图片到这个 Bucket 里。

- 查看文件的详情，可以看到这个图片的 url 地址，比如 `https://f004.backblazeb2.com/bucketname/filename.png`。

- 在 Cloudflare 里创建一个二级域名的 CNAME，比如 `storage.your-domain.com`，指向 `f004.backblazeb2.com`。开启 proxy。

- 修改 `SSL/TLS` 为`完全（严格）`。

- 修改 `Rules`，增加一个规则。`https://storage.your-domain.com/*`，选择`缓存级别`为`标准`，`边缘缓存 TTL` 为 `1 个月`。

设置完成，上面图片的地址就变成了 `https://storage.your-domain.com/filename.png`。