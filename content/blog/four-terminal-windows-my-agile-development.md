---
title: "四个窗口，我的敏捷开发"
slug: "four-terminal-windows-my-agile-development"
author: "Bin Hua"
date: 2024-10-06T06:34:16Z
tags: ["terminal", "development"]
draft: false
---

最近写了一点 iOS/macOS app，虽然偏前端，但更多的时间在写服务器端的接口和服务。这里介绍写我敏捷开发的模式。

### 技术栈

- 语言：Nodejs(Javascript)，Go

- 数据库：Firebase，MongoDB

- 工具：iTerm2，Sublime Text（主要是批处理使用）

### 操作方式

在开发的时候，我主要用 iTerm2，平铺 4 个窗口，这也是我很喜欢 iTerm2 的原因之一。

- 左侧区：上面是 document，打开需求文档，实时整理自己的思路；下面是 vi/vim，为编码区

- 右侧区：上面是拉起服务和查看日志，比如 pm2(log)；下面是 command 区，比如执行 curl/git 等命令

左右两侧在实际使用中拖拽调整宽度，上下也一样方式调整高度。

### 后续想法

最近有个新想法，在 document 中集成 AI，因为现在 AI 这部分还是 iTerm2 和浏览器之间切换的。