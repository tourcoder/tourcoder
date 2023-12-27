---
title: "利用 GitHub 协同工作"
slug: "collaboration-via-github"
author: "Bin Hua"
lastmod: 2019-05-07 03:01:53
date: 2019-05-07 03:01:53
tags: ["GitHub", "stuff", "workflow", "collaboration", "协同工作", "issue"]
---

GitHub 的强大不用我多说，今天这一篇就好好的写一下如何用 GitHub 进行有效的协同工作，基本是看完这篇文章后，GitHub 协同工作就会了。

#### 主仓库和开发仓库

这里有两个概念 -- 主仓库和开发仓库，很多团队是在同一个仓库进行协同开发，其实这是非常危险的事情，也不方便管理，我们团队使用的是主仓库和开发仓库的开发模式。

- 主仓库

    主仓库只作为协同工作时的协调库，以及持续部署的基础源。任何协同开发人员不可在主仓库创建分支，不得向主仓库 push 内容，所有内容必须经过 PR(Pull Request) 的方式进行提交。
    
- 开发仓库

    每位参与该协同项目的开发人员从主仓库 fork 出来的仓库，每位开发者必须要有自己的开发仓库。
    
#### 协同流程

创建一个仓库，比如叫 demo-collaboration，它是主仓库，如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-001.jpg)

将相应的协同人员加入到该仓库中，如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-002.jpg)

这样一个主仓库及创建完成，每位参与协同开发的开发者应该 fork 一份主仓库的内容，他将在 fork 后的仓库（即开发仓库）里进行开发工作，如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-003.jpg)


![](https://storage.tourcoder.com/tcblog/collaboration-via-github-004.jpg)

开发者在自己的开发仓库里进行开发，当开发完成后，将内容提交到 GitHub 上自己的开发仓库中（必须是自己的开发仓库），如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-005.jpg)

开发者将自己开发仓库的内容提交到主仓库，必须使用 PR 方式，点击上图中的 `New pull request`，即可进入下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-006.jpg)

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-007.jpg)

在进行 PR 的提交时，注意目的地和来源，左边是目的地，右边是来源，方式是`将来源的内容合并到目的地`。此时开发者的工作即完成，相应的 Code Review 人员进行代码审核后，将代码进行合并/拒绝等操作处理，如下图的合并完成。

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-008.jpg)

此时回到主仓库可以发现，该开发者的内容已经合并到主仓库中。

上面的内容就是协同工作的开发者如何向主仓库提交内容，下面将介绍如何从主仓库拉取内容到自己的开发仓库。

首先进入到自己的开发仓库，如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-009.jpg)

点击上图的 `New pull request`，进入下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-010.jpg)

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-011.jpg)

如上图，这里需要注意的是目的地和来源，和前面向主仓库提交合并申请不一样的是，这里是提交`把主仓库的内容合并到自己的开发仓库`的申请。

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-012.jpg)

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-013.jpg)

然后同样是 code review 等操作即将内容合并到了自己的开发仓库，如下图

![](https://storage.tourcoder.com/tcblog/collaboration-via-github-014.jpg)

以上基本就是一个基于协同工作的基础操作方式。

#### 一些常见问题

- 保护主仓库

    有时候难免会有一些开发者操作失误，向主仓库 push 内容，这时候就需要用到主仓库的设置
    
    ![](https://storage.tourcoder.com/tcblog/collaboration-via-github-015.jpg)
    
    在主仓库中点 `Settings -> Branches` 在这里进行操作即可，栏目介绍的英文都简单，选择相应的内容勾选即可。
    
- Code Review

    在协同工作过程中，这个步骤必须要做。