---
title: "Try Wrangler Through a Donation Page Project"
slug: "try-wrangler-through-a-donation-page-project"
author: "Bin Hua"
date: 2026-01-09T13:50:27Z
tags: ["cloudflare", "wrangler"]
draft: false
---

前几天写了个[捐赠页面](/)，想着基于 Cloudflare 的技术栈来搭建，顺道体验了下 Wrangler 这个我没怎么用过的工具。

在这次折腾中，Wrangler 承担了很多关键的角色：

- 项目脚手架
- 本地开发服务器
- 环境变量与加密环境变量管理
- 远程日志与调试
- 发布与版本管理

让我们开始...

### 项目背景

这个项目的功能非常简单：

- 一个 Cloudflare Pages 托管的前端页面
- 一个 Workers API 接收捐赠请求
- Worker 中调用 Stripe 创建支付链接
- 支付完成后通过 Resend 发送确认邮件

强调一下：**业务并不重要，重要的是这个过程足够贴近真实生产环境，主要是折腾下 Wrangler**。

### 安装 Wrangler 并登录

执行如下命令

```
npm install -g wrangler
```

登录

```
wrangler login
```

会跳转到浏览器里完成授权。

### 初始化项目

```bash
wrangler init demoworker
cd demoworker
```

这一步主要是几个点：

- Wrangler 会询问你是否创建 Worker / Pages 项目
- 会自动生成 `wrangler.jsonc` 文件，以前的文件是 `wrangler.toml`
- 项目结构已经天然适配 Cloudflare 平台

**wrangler.jsonc**

这里把 `wrangler.jsonc` 拿出来解释一下，它是整个项目的核心配置文件，主要承担：

- Worker 名称
- 入口文件
- 运行环境（compatibility_date）
- 绑定的环境变量/加密环境变量

例如：

```
{
  "name": "demoworker",
  "main": "src/index.js",
  "compatibility_date": "2026-01-01"
}
```

后续的本地调试、远程部署中，Wrangler 几乎所有行为都以这个文件为准。

然后就是开发这个项目。

### 本地调试

执行命令 `wrangler dev` 即可，这条命令做了很多事情

- 启动一个本地的 workers 运行时
- 模拟了 Cloudflare 的 request/response 行为
- 自动监听文件的变更并且热重载

### 远程调试

本地调试有一定的局限性，比如有些 API 行为不能在本地复现等，那么可以通过增加参数 `--remote` 让调试跑在 Cloudflare 上，即命令

```
wrangler dev --remote
```

这条命令的本质是：代码运行在 Cloudflare Workers 的真实边缘网络中，但调试终端仍映射在本地，这能提供更接近真实生产环境的测试效果。

### 环境变量

在做本地调试时，用到的一些环境变量通过本地的文件 `.dev.vars` 来保存，格式和 `.env` 文件一样的

```
THE_SECRETKEY=xxxxx
``` 

但在做远程调试或生产环境部署，则需要把一些参数注入到 Worker 里，那么可以通过

```
wrangler secret put THE_SECRETKEY
```

这样的方式注入加密环境变量到 Worker 的环境中。

对于非敏感的环境变量，则可以直接写在 `wrangler.jsonc` 文件中

```
{
  "name": "demoworker",
  "main": "src/index.js",
  "compatibility_date": "2026-01-01",

  // 非敏感环境变量
  "vars": {
    "SITE_URL": "https://your-production-site.com"
  }
}
```

### 查看日志

当代码部署到线上后，需要查看日志的话，执行 `wrangler tail` 即可，它可以

- 实时查看线上 Worker 的日志
- 输出 `console.log`
- 快速定位线上问题

### 发布和部署

- 创建和部署数据库 D1

  可以通过命令或者在网页上的管理平台创建一个数据库（foodb）

  ```
  wrangler d1 create foodb
  ```

  这里会产生一个 database_id 需要记录下来，在配置文件的时候用到

  将数据结构应用到数据库上

  ```
  wrangler d1 execute foodb --file ./your_sql_path/schema.sql --remote
  ```

- 发布 Workers

  直接在对应的项目目录里执行 `wrangler deploy` 即可完成部署。如果是首次部署，记得上面写到的加密环境变量的注入。

- 发布 Pages

  先将项目构建完成，比如 `npm run build`，然后执行 `wrangler pages deploy publish_folder --project-name your_project_name_on_pages` 即可。