---
title: "给博客集成了 Utterances"
slug: "integrated-utterances-to-my-blog"
author: "Bin Hua"
date: 2024-06-26T13:20:05Z
tags: ["GitHub", "utterances", "issue", "blog"]
draft: false
---

刷到个基于 GitHub issues 的评论系统，觉得挺好玩的，就把它集成到了这个博客。折腾过程非常简单。

访问这个网站 [https://utteranc.es/](https://utteranc.es/)，也就是它的官网，根据官网的说明来做。

- 设置仓库是公开的状态。

- 将插件 [utterances](https://github.com/apps/utterances) 安装到仓库。

- (可选项) 如果是 fork 的仓库，则记得在设置里开启 issues。

- 设置 mapping 和主题。

- 复制下面的代码，然后将代码复制到对应位置。比如这个博客用的是 hugo，这段代码是放置在主题的 single.html 模板里面的。

- 完成了。

注意：这里有个门槛，需要有 GitHub 的账号才能评论，但这也是一个很好的防 spam 的好门槛，不是吗？

### 资源

[Utterances](https://utteranc.es/)