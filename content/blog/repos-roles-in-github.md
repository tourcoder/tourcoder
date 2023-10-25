---
title: "Github 和代码权限"
slug: "repos-roles-in-github"
author: "Bin Hua"
lastmod: 2017-10-09 07:11:10
date: 2017-10-09 07:11:10
tags: ["git", "GitHub"]
---

在经过一圈的折腾后，我们又回到 Github，用它来进行协同开发，之前我们用过其他同类的服务(commitcode,bb)，也用开源软件搭建过私有服务(gitlab,gs)，甚至基于开源自己也二次开发了一套，但现在全都抛弃，回到Github，主要有两点：

- Github 社区氛围是真的太好了，让程序员在这样的氛围下，利大于弊

- Github 配套的延伸产品很多，拿来即可使用，省事

但它的问题显而易见，比如权限问题，其实这个问题不只是我们遇到，相信很多公司都遇到了这样的问题，尤其是一些做产品的早期创业公司。

对一些大公司来说，在协同开发的过程中，它有足够的能力保护代码的安全，软性的方面有大公司的强势和开发人员对公司的敬畏等，硬性方面有公司的规章法律文件，以及即便拿到代码也只是部分代码等，所以保护代码在大公司并不是非常重要的事情，当然也有大公司权限做得很变态的，比如 Google，它们自己开发的工具已经让权限控制到每个文件。

但小的创业公司就不这样了，人少，没有规范的制度，加上早期的产品不会太复杂，基本每个开发都会很容易的拿到所有的代码，一旦发生这样的恶意事件，分分钟就会有一个竞品出现，而 Github 这样开放式的 workflow 就容易让这一担忧变成现实，所以保护代码可能尤其显得重要。

现在我们强行要求的开发流程是 fork -> clone -> develop -> push -> pull request -> code review -> merge，这是一个非常漂亮的快速开发流，但因为 Github 的弱权限管理，当只有一个 repo 的时候，这个流程会导致所有的开发人员都会很轻易的获得这个 repo 里所有的代码。

目前我们的解决办法是：

- 一个项目按模块的方式创建多个 repo，以 repo 为单元进行开发，这样做好处是即便发生代码丢失，最多也是丢失一个模块的代码，而不会获得整个项目源码，但这样做的坏处是多模块之间的协同工作就会很痛苦。

- 一个项目只创建一个 repo，但核心部分的代码全部封装加锁，这样做的好处是即便发生代码丢失，核心代码的安全至少有个保障，但这样做的坏处是必须要有人写这些核心的代码，对早期创业团队的人员要求会很高。

我们想要的：

- 一个项目只有一个 repo
    
- 在这个 repo 上有更为细节化的权限控制，做到每开发者只能得到自己的代码

我们可能会做的：

- 在之前自己开发的软件上加入这样的功能，时间是个问题！

最后的话才是最重要的，如果你没有办法保证你的代码安全，不如就对所有开发同事公开，甚至开源吧。

**update@201701013**: 今天遇到灾难，github 删除了我所有的私有库，并且 flag 了我的账户，瞬间让我对它没有了信心。商业代码看来还是要选择自行架设。