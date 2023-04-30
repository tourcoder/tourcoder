---
title: "Git Submodule 的使用"
slug: use-git-submodule
author: "Bin Hua"
lastmod: 2020-07-18 06:10:04
date: 2018-02-11 07:27:29
tags: ["git", "submodule"]
---

之前都是博客源码和内容文件放在一起，总感觉怪怪的，今天更新了下本博客的结构，让代码和内容分开，Repository 也分成了代码和内容两个部分。分开后的结构是这样的：

博客代码部分在 GitHub 的显示

![](/imgs/submodule-01.png)

那么怎么把这两个库关联起来，便于开发呢？这就用到了本篇的知识点 Git Submodule，关于 Git Submodule 的更详细介绍，可以去[这里](https://git-scm.com/docs/git-submodule)查看。这里我是用我的博客为例子

![](/imgs/submodule-02.png)

进入到博客代码的库，用 `git submodule add` 命令引入子库。 比如我这里引入的博客内容的库，`git submodule add https://github.com/***/blogdata.git blogdata`，执行完成后查看，发现库里多了个 `blogdata` 的文件夹。执行 `add，commit，push` 命令后，查看 `GitHub` 上的代码库，发现多了个 `blogdata` 的文件夹和 `.gitmodules` 的文件，如下图

![](/imgs/submodule-03.png)

这里的 blogdata 是一个链接，点这个文件夹可以跳转到 blogdata 所在的库。

![](/imgs/submodule-04.png)

![](/imgs/submodule-05.png)

在主库根目录中增加点内容，然后提交到主库中，blogdata 是不会有任何变化的，比如我在主库增加了 example.js 这个文件。

![](/imgs/submodule-06.png)

![](/imgs/submodule-07.png)

如果我们在子库 `blogdata` 中进行了更改，并且提交到库中，如上面的操作，这时候不但子库的内容发生了变化，主库中的 `blogdata` 的“指针”也发生了变化。

![](/imgs/submodule-09.png)

![](/imgs/submodule-10.png)

![](/imgs/submodule-11.png)

如果要更新本地的 `blogdata` 内容，有两种方式，一个是在主库下面执行命令 `git submodule foreach git pull`，如上图；还有一种是进入到该子目录中执行命令 `git pull`。

![](/imgs/submodule-12.png)

将内容克隆到本地，也有两种方式，一种是使用参数 `--recursive` 的递归方式，如执行命令 `git clone https://github.com/***/blog.git --recursive`；还有一种方式是把主库先拉下来，然后执行命令 `git submodule init`，然后再更新 `git submodule update`，即可完成，具体看上图（上图中的前半部分是我在获取分支的内容）。

![](/imgs/submodule-13.png)

Submodule 的删除有点繁琐，需要删除不少内容，如上图，删除掉本地文件，删除掉缓存，删除掉 .gitmodules 文件，如上图。

![](/imgs/submodule-14.png)

还要删除掉主库配置文件中的 Submodule 的部分。

![](/imgs/submodule-15.png)

删除掉后，提交

![](/imgs/submodule-16.png)

这时可以看到，GitHub 上该主库又变回原来模样了。

上面基本是 `Git Submodule` 的使用，更新，删除；我只用用自己的博客做个简单的试用，它的用途很广，欢迎大家自行挖掘。