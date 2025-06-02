---
title: "如何删除 Cloudflare Pages 拥有大量部署的项目"
slug: "how-to-delete-pages-with-many-deployments-on-cloudflare"
author: "Bin Hua"
date: 2025-06-01T01:29:26Z
tags: ["cloudflare", "pages", "How-to"]
draft: false
---

需要删除一个部署在 Cloudflare Pages 上的项目，但总是提示错误，错误信息是

```
Your project has too many deployments to be deleted, follow this guide to delete them: https://cfl.re/3CXesln。
```

### 原因

因为部署太多，导致无法删除，我测试得知，基本超过 100 次部署就会有这个问题。

### 解决

需要删除过的部署，让数量控制在 100 个之内即可

- 方法一：直接手动删除

  如果部署的次数比 100 多不多少，就手动删除一些，将部署的内容控制在 100 个之内即可删除项目了。

- 方法二：使用 Cloudflare API 删除部署

  先要获取一些基本信息：

  - Account ID：仪表盘 -> 账户
  
  - Project Name：Pages 里这个项目的名称

  - API Token：个人资料 -> API Token，注意给 Pages 的相关权限

  通过终端列出所有的部署

  ```
  curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments" \
  -H "Authorization: Bearer {api_token}"
  ```

  对应找到每个部署的 ID，然后删除（最好不要，能到这里就是因为部署量大，要批量删除）

  ```
  curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}" \
  -H "Authorization: Bearer {api_token}"
  ```    

  用脚本批量删除（推荐，下面脚本只是一个参考）

  ```
  #!/bin/bash
  ACCOUNT_ID="your_account_id"
  PROJECT_NAME="your_project_name"
  API_TOKEN="your_api_token"

  # 获取所有部署 ID
  DEPLOYMENTS=$(curl -s -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pages/projects/$PROJECT_NAME/deployments" \
  -H "Authorization: Bearer $API_TOKEN" | jq -r '.result[].id')

  # 遍历并删除每个部署
  for DEPLOYMENT_ID in $DEPLOYMENTS; do
    echo "Deleting deployment: $DEPLOYMENT_ID"
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pages/projects/$PROJECT_NAME/deployments/$DEPLOYMENT_ID" \
    -H "Authorization: Bearer $API_TOKEN"
    sleep 1  # 添加延迟以避免 API 速率限制
  done
  ```

  最后可以通过命令行直接删除项目，也可以去 Cloudflare 的面板去删除项目。

### 参考文档

Cloudflare 官方的文档：[https://cfl.re/3CXesln](https://cfl.re/3CXesln)
