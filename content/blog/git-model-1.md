---
title: "Git 开发模式的更新"
slug: "git-model-1"
author: "Bin Hua"
date: 2016-06-13 06:47:37
tags: ["GitHub", "git", "model"]
draft: false
---

现在大部分的团队都已经使用 Git 作为版本控制的主要软件，在这里分享下，我们团队中的 Git 开发模式

![](https://storage.tourcoder.com/tcblog/gitmodel_01.png)

这是早前我们开发模式，2016 年后我们改成了如下的模式

![](https://storage.tourcoder.com/tcblog/gitmodel_02.png)

两者之间不同的是，把 Release 分支合并到了主干 Master，这样做的原因是

- 始终保持 Master 是一个可使用的版本

- 增加了 Code Review 的主动性 

**2018 年分支方式再次更新**

**项目主仓库**

每一个项目应该是一个单独的库，只有一个分支

- dev 分支

    是唯一的开发环境的分支，也是该仓库中唯一的分支，该分支是受保护的

- release

    任何部署到生产力环境的内容，都是基于 dev 分支通过打 tag 的方式持续部署

**个人仓库**

每位开发者在创建期 fork 项目，然后在自己的本地进行开发，开发完成测试通过后，通过 pr 的方式将内容合并到项目主仓库的 dev 分支中。