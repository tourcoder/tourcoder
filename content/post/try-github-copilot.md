---
title: "试用 Github Copilot"
slug: "try-github-copilot"
author: Bin Hua
lastmod: 2021-07-14T11:37:30+08:00
date: 2021-07-14T11:37:30+08:00
tags: ["GitHub", "Copilot", "VSCode"]
---

有幸获得了 GitHub Copilot 的邀请，今天正好有时间，就写一个简单的中文教程吧。

### GitHub Copilot 是什么？

GitHub Copilot 的 slogan 是 Your AI pair programmer，顾名思义就是你的结对编程伙伴，它是基于 AI 的。其官网是 [https://copilot.github.com](https://copilot.github.com)。

现阶段，它是以 Visual Studio Code 的插件形式出现的，所以目前需要 Visual Studio Code 的支持，当然 GitHub Codespaces 也支持。

### 如何使用

- 准备工作

  - Visual Studio Code
  
  - 安装 GitHub Copilot 插件
    
    可在 Visual Studio Code 插件市场里搜索 GitHub Copilot，然后安装，或者访问[https://marketplace.visualstudio.com/items?itemName=GitHub.copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) 安装。安装好后入下图
    
    ![](/imgs/try-github-copilot-001.png)
    
- 使用步骤

  在 VSCode 中授权登录已经拥有 GitHub Copilot 权限的 GitHub 的账号，需要用到 GitHub 账号的原因应该是目前它处于邀请测试阶段，还有代码安全的问题。
  
  ![](/imgs/try-github-copilot-002.png)
   
  ![](/imgs/try-github-copilot-003.png)
  
  ![](/imgs/try-github-copilot-004.png)
  
  新建项目，编写代码，可能是因为网络的原因，刚开始我使用 GitHub Copilot 官方的示例代码都未能唤起 Copilot，无法正常使用，但在“优化”好网络后，能正常唤起 Copilot 了。
  
  ![](/imgs/try-github-copilot-006.png)
  
  有点意思。
  
  ![](/imgs/try-github-copilot-007.png)
  
  Copilot 还可以设置全局停止使用或者针对某个语言停止使用。
  
### 一些问题

Copilot 虽然是一个很好的东西，但代码安全问题是一个逃避不开的话题，Copilot 在和你结对编程的同时，它其实是在扫描整个代码的，尽管 GitHub 已经给出安全方面的说法，但这点并不适合所有的团队。

Copilot 的代码来自 GitHub 开源库，直接无视开源协议，取用其他人开源的代码。具体可以看这条推文 [https://twitter.com/mitsuhiko/status/1410886329924194309](https://twitter.com/mitsuhiko/status/1410886329924194309)

### 相关资料

- GitHub Copilot 官网：[https://copilot.github.com](https://copilot.github.com)

- GitHub Copilot 插件：[https://marketplace.visualstudio.com/items?itemName=GitHub.copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
  
