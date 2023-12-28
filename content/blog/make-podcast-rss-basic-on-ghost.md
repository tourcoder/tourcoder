---
title: "基于 Ghost 做一个 Podcast 源"
slug: "make-podcast-rss-basic-on-ghost"
author: "Bin Hua"
date: 2019-10-18 07:03:43
tags: ["Apple", "ghost", "podcast"]
draft: false
---

精力旺盛，心血来潮，想弄一个 `Podcast` 玩玩，看了一圈后，还是想基于自己的博客平台来做 rss 源。分享下大致的过程。

#### 开始之前

本博客已经有不少博文，其输出的 rss 是不满足 `Podcast` 的需求的，所以需要单独区分开来，博文的 rss 还是沿用之前的 `tourcoder.com/rss`，而 `Podcast` 的则使用新的地址 `tourcoder.com/podcast/rss`。而将两个源内容通过 tag 来区分，带有 `tctalk` 标签的即为 `Podcast` 内容，其他的则为图文博文。

#### 改造 `routes.yaml`

进入 `Ghost` 管理后台，选择 `Labs`，将 `routes.yaml` 下载下来，更改里面的内容

```
routes:
  /podcast/rss/:
    template: podcast/rss
    content_type: text/xml

collections:
  /:
    permalink: /{slug}/
    template: index
    filter: tag:-tctalk
  /podcast/:
    permalink: /podcast/{slug}/
    filter: tag:tctalk

taxonomies:
  tag: /tag/{slug}/
  author: /author/{slug}/
```

增加了 `Podcast` 的 rss 地址及 rss 模板地址，在主 rss 中排除了标签为 `tctalk` 的内容，在 `podcast` 的 rss 中显示标签为 `tctalk` 的内容。

完成这部分内容后，将其保存在刚才下载的位置上传。

#### 新增 rss 模板

如上面的配置，需要新建一个 `rss.hbs` 的模板放在主题的根目录的 `podcast` 文件夹里，即在主题的根目录下创建一个 `podcast` 文件夹，里面增加一个名叫 `rss.hbs` 的文件。

```
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
    xmlns:slash="http://purl.org/rss/1.0/modules/slash/" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
    xmlns:rawvoice="http://www.rawvoice.com/rawvoiceRssModule/" xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0">
<channel>
<title>{{@site.title}}</title>
<link>https://tourcoder.com/podcast</link>
<language>zh-cn</language>
<copyright>&#169; {{date format="YYYY"}} TOURCODER</copyright>
<itunes:author>TOURCODER</itunes:author>
<description>{{@site.description}}</description>
<itunes:owner>
    <itunes:name>TOURCODER</itunes:name>
    <itunes:email>hello@tourcoder.com</itunes:email>
</itunes:owner>
<itunes:explicit>false</itunes:explicit>
<itunes:image href="https://tourcoder.com/podcast/podcastlogo.jpg"/>
<itunes:category text="Comedy" />
<itunes:category text="Technology" />
<itunes:category text="Arts" />
{{#get "posts" filter="tag:tctalk" include="tags,authors" as |episode|}}
    {{#foreach episode}}
    <item>
        <title>{{title}}</title>
        <link>{{url absolute="true"}}</link>
        <pubDate>{{date format="ddd, DD MMM YYYY HH:mm:ss ZZ"}}</pubDate>
        <guid isPermaLink="false">{{id}}</guid>
        <category><![CDATA[ {{primary_tag}} ]]></category>
        <description>{{custom_excerpt}}</description>
        <content:encoded><![CDATA[ {{content}} ]]></content:encoded>
        <enclosure url="{{og_description}}" length="1" type="audio/mpeg"/>
        <itunes:subtitle>{{custom_excerpt}}</itunes:subtitle>
        <itunes:summary><![CDATA[ {{content}} ]]></itunes:summary>
    </item>
    {{/foreach}}
{{/get}}

</channel>
</rss>
```

关于这个格式的说明，每个 podcast 服务商要求不一样，这里是根据 Apple 的要求来写的，具体更多说明，请看 Apple 官方文档，[https://help.apple.com/itc/podcasts_connect/#/itcb54353390](https://help.apple.com/itc/podcasts_connect/#/itcb54353390)

#### 改造 `package.json`

在主题的 `package.json` 文件中开启 `ghost-api`，即 `engines` 下增加 `"ghost-api": "v2"`。

```
{
    "name": "tcui-ng",
    "description": "Next Generation TCUI for Ghost.",
    "version": "0.0.1",
    "engines": {
        "ghost": "^2.2.0",
        "ghost-api": "v2"
    },
    "license": "MIT",
    "author": {
        "name": "tourcoder",
        "email": "hello@tourcoder.com",
        "url": "https://tourcoder.com"
    },
    "gpm": {
        "type": "theme",
        "categories": [
            "tcui",
            "blog",
            "Personal Blog"
        ]
    },
    "keywords": [
        "tcui",
        "ghost-theme",
        "blog",
        "responsive"
    ],
    "config": {
        "posts_per_page": 10
    }
}
```

完成后，将该主题压缩，并上传激活，到此，一个基于 `ghost` 的 `podcast` 的 rss 算是改造完成了。

最后测试一下，发表一篇只打上 `tctalk` 标签的博文，发送后查看 `tourcoder.com/rss` 源汇总并没有这篇文章，而 `tourcoder.com/podcast/rss` 中出现了这篇文章，成功。

注意：音频文件的链接地址应该放在当前帖子的 `facebook description` 里面。路径为 `Post settings -> Facebook Card -> Facebook description`。

#### 发布

这里只演示下在 Apple iTunes 上的发布，Apple Podcast 本身是不存储文件的，它只读取前面制作的 rss 源。

进入到 [https://podcastsconnect.apple.com/](https://podcastsconnect.apple.com/) 登录后，输入源的地址，点击验证，没有问题的话，即可得到如下图的界面

![](https://storage.tourcoder.com/tcblog/make-podcast-rss-basic-on-ghost-01.jpg)

等待 Apple 审核即可。

**20191021 更新**：已经上线，在 podcast 中搜索「代码旅行」即可，不过因为一些不可抗力，中国区暂时没有上线。