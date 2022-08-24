---
title: "如何开发并发布一个 Office 插件 (Add-in)"
slug: "how-to-build-and-publish-an-office-add-in"
author: Bin Hua
lastmod: 2022-08-24T08:50:12+08:00
date: 2022-08-24T08:50:12+08:00
tags: ["Microsoft", "office", "add-in", "howto"]
---

这几天学习开发了一个 Microsoft office word 的 add-in，也刚提交审核，分享点经验。

1. 官方的文档还是比较全的，具体可以看[这里](https://docs.microsoft.com/zh-cn/office/dev/add-ins/develop/develop-overview)官方的文档，但有些部分你需要阅读英文，因为中文页面显示的也是英文，我已经在 [GitHub](https://github.com/OfficeDev/office-js-docs-pr/issues/3590) 上给他们提交了这个问题。

2. 目前每个应用对应的 API 也是不完整的，比如我是为 word 开发 add-in，有些想做的操作，目前还不被支持。

3. 开发好的东西，需要打包，放到你的服务器上，能被访问到。其中 `manifest.xml` 是要上传审核。

4. 我是用企业身份发布的，用个人身份发布，我没有尝试，也欢迎用个人身份的人分享经验。

5. 用企业身份发布，要验证企业身份（Partner），还要验证开发者账户（Developer），切记一定要验证开发者身份，不然无法上传发布应用。具体的操作在 [Microsoft Partner](https://partner.microsoft.com/)。

6. 应用的发布在 Microsoft Partner Center 后台的 Marketplace offers，进去后创建应用，填写相关的内容即可。

**补充个细节**

基本就上面这些内容，我唯一遇到问题的地方是开发者账户验证。开发者身份需要的资料和 Partner 身份需要的资料是一样的，我提交了很多次，都不给我通过，但他们又说不清楚自己要的东西，最后甚至发一封邮件甩锅给我，关键他发来的邮件是谎话连篇，我昨天早上九点多回怼了一封邮件揭穿了谎言，然后晚上十一点多收到邮件说帮我解决了，一早醒来一看，开发者账户通过验证了。浪费了我很多天时间。

![](/imgs/how-to-build-and-publish-an-office-add-in.png)
