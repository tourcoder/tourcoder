---
title: "修复 Gemini Cli Google Oauth Personal 的错误: Google Cloud Project Is Required"
slug: "fixing-gemini-cli-google-oauth-personal-error-google-cloud-project-is-required"
author: "Bin Hua"
date: 2025-12-28T03:20:20Z
tags: ["gemini", "gemini cli", "terminal", "vibecoding", "iterm"]
draft: false
layout: "single-blog"
---

When logging into **Gemini CLI** with a personal Google account can fail with this error:
有时候登录 **Gemini CLI** 的个人账户时，总会出现下面的错误:

```
Failed to login. Message: This account requires setting the GOOGLE_CLOUD_PROJECT or GOOGLE_CLOUD_PROJECT_ID env var.
```

这乍一看可能会让人困惑，因为[官方文档](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.md) 指出，**个人 Google 帐户不需要 Google Cloud 项目——*但也有例外情况***。

实际上，其中一个例外情况是，Gemini CLI 在 OAuth-Personal 登录期间仍然会检查以下环境变量是否存在。

### 修复方法

设置虚拟值并重试登录：

```
export GOOGLE_CLOUD_PROJECT="no-project-required"
export GOOGLE_CLOUD_PROJECT_ID="no-project-required"
```

完成。