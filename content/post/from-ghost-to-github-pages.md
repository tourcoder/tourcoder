---
title: "From Ghost to Github Pages"
slug: from-ghost-to-github-pages
author: Bin Hua
lastmod: 2020-12-25 07:21:08+08:00
date: 2020-12-25 07:21:08+08:00
tags: ["GitHub", "Ghost", "pages", "hugo", "golang", "nodejs", "cloudflare"]
---

把本博客从 Ghost 迁移到了 GitHub Pages，原因有二

1. 受不了 Ghost 日趋臃肿

2. 我的 GitHub Pro 还有 10 个月到期，不用也浪费。

整个迁移过程还是挺简单的，大致步骤如下：

1. 先登录 Ghost 的后台导出内容，会是一个 json 格式的文件。

2. 将该 json 格式的文件转化成 markdown 文件，可以用 [ghostjson2markdown](https://github.com/tourcoder/ghostjson2markdown) 这个开源工具操作。

3. 将生成的 markdown 文件使用静态博客生成工具生成静态的页面，我使用的是 hugo，官网 [gohugo.io](https://gohugo.io)，具体怎么操作，在其官网有。这里会生成的一个 public 的文件夹，里面就是整个网站的内容了。

4. 去 GitHub 创建一个仓库，开启 GitHub Pages 功能，如下图

	![](/imgs/from-ghost-to-github-pages-01.png)

	如果不绑定自己的域名可以用 GitHub pages 的自带域名，还可以开启 ssl，使用自己的域名也可以使用 ssl。这里一个小提示，如果是二级域名，系统会提示你使用 cname 绑定的方式，如果是 apex，即不是二级域名，则指向 ip 地址。

5. 将第三步生成的静态页面（public 文件夹中内容）上传到这个代码库中即可。


#### 说明

hugo 这类的静态生成器的原理就是根据 markdown 中内容生成一个一个的文件夹及文件夹里面的 index.html 文件。比如 `https://tourcoder.com/about` 这个内容，通过 hugo 这类工具生成了一个 `about` 的文件夹，在这个文件夹里有一个 `index.html` 的 html 文件。

#### 优缺点

如果愿意开源博客的写作过程，则 GitHub 是免费的，这个算是一个优点吧。

但 GitHub pages 自定义域名如果用 https，需要第三方，这点很烦人，而 cloudflare 这类第三方的确很好，但也有个问题就是在国内经常会出现访问不了的情况（需要验证，因为国内很多 IP 都被视为了垃圾 IP）。

愿意动手玩玩 GitHub action 的，也可以直接写 markdown 文件，剩下的内容交给 GitHub action 去处理，也省事。

另外就是 GitHub 倒掉，数据丢失的可能性不是太大，安全有保障。

#### 后期可能的方案

本博客还是会迁移到我私人的服务器去，迁移的原因是 cloudflare 在国内访问的问题，会用 Caddy + hugo 的方式部署。

**半个小时后补充：**

还是搬到了自己的服务器，hugo 生成静态页面，设置 Caddy 指向这个页面，具体操作如下。

1. 在服务器上安装 hugo，然后新建一个站点，执行命令 `hugo` 即可生成一个 `public` 的文件夹，如上面所说这个文件夹里面就是整个网站的内容。

2. 在服务器上安装配置 Caddy，将域名指向 `public` 文件夹，至于怎么安装配置，去看[这篇文章](/centos-ubuntu)，`Caddyfile` 内容如下

	```
	tourcoder.com {
	 root * /home/tcblog
	 file_server
	}
	```

3. 完成。

在我看来目前这样比较好，一方面因为站点是静态页面，所以服务器的消耗不是很大，另外一个方面随时可以登录到服务器去写博客，内容都在 `content`，写完后执行 `hugo` 命令即可生成内容，不需要做其他的事情。甚至可以在本地电脑上写好 `markdown` 格式的文件，写好后传到服务器上，然后执行命令也行。至于利用其他自动化部署就不展开谈了。

**2021 年 3 月 31 日更新**

我将博客移回了 GitHub，原因是我的服务器被墙了。

因为我的博客是用 hugo 生成的，它生成的默认发布目录是 `public`，可以通过在 `config.toml` 中修改，增加一行 `publicDir = '你需要的文件夹名字，也可以带上路经'`，比如 GitHub pages 使用的是 docs 或者 root。

**Hugo 的安装**

Hugo 是基于 Golang 开发，所以先安装 Golang，最快的安装方法 [http://github.com/tourcoder/glv](http://github.com/tourcoder/glv)。

然后在 CentOS 下编辑 `/etc/yum.repos.d/hugo.repo`，没有该文件直接创建即可，将下面的内容填入里面

```
[daftaupe-hugo]
name=Copr repo for hugo owned by daftaupe
baseurl=https://copr-be.cloud.fedoraproject.org/results/daftaupe/hugo/epel-7-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/daftaupe/hugo/pubkey.gpg
repo_gpgcheck=0
enabled=1
```

最后执行 `yum install hugo -y`.

在 Debian/Ubuntu 下安装，先去 hugo 的发布页面找到对应的 deb 文件，[https://github.com/gohugoio/hugo/releases](https://github.com/gohugoio/hugo/releases)，然后执行即可。比如我的系统是 Debian 64 位，则

```
wget https://github.com/gohugoio/hugo/releases/download/v0.83.1/hugo_0.83.1_Linux-ARM64.deb
```

然后执行 `sudo dpkg -i 文件名.deb` 即可。

至于 macOS 下，用 `brew install hugo`。
