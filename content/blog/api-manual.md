---
title: "REST API 规范手册"
slug: "api-manual"
author: "Bin Hua"
date: 2013-07-25 06:36:11
tags: ["restful", "api"]
draft: false
---

这是我之前写 REST API 的规范手册，在具体的项目中会有调整

**通用说明 - header 返回**

接口存在，返回 200，并同时返回以下信息

```
HTTP 200 No Error

Content-Security-Policy:
Server:
API-Media-Type: version.v1; format=json
Status: 200 OK
Access-Control-Allow-Origin: *
Date: Sun, 07 Jan 2018 15:26:30 GMT+8
Content-Type: application/json; charset=utf-8
```

接口不存在，返回 404，并同时返回以下信息

```
HTTP 404 Not Found

Content-Security-Policy:
Server:
API-Media-Type: version.v1; format=json
Status: 404 Not Found
Access-Control-Allow-Origin: *
Date: Sun, 07 Jan 2018 15:26:30 GMT+8
Content-Type: application/json; charset=utf-8
```

**通用说明 - 请求地址**

要为 REST API 设置专门域名，并加 SSL，请求地址中需要有版本号，如 `https://domain.com/v1/`

**通用说明 - 格式**

- 所有的数据请求和返回都应该是标准的 json 格式（GET 的请求方式除外）
    
    格式结构 `{"fbstatus": "","fbmsg": "","fbcontent": "" }`

    fbstatus 有多个状态 比如 0-请求成功，1-请求失败 fbmsg 和 fbstatus 对应，fbstatus 为 0，则 fbmsg 显示 success，fbstatus 为 1，则 fbmsg 显示 fail。 具体的 fbstatus 需要查看下面的内容，这里只是一个解释。

- 如果缺少某个字段，应该将该字段显示出来，并赋予 null 值

- 所有的返回时间应该是毫秒的时间戳 

**通用说明 - 请求方式**

请求方式用如下几种

GET：客户端从服务器获取资源

POST：客户端在服务器创建资源

PUT/PATCH：客户端在服务器更新资源，建议用 PUT

DELETE：客户端从服务器删除资源

**通用说明 - 身份验证**

任何接口的访问都需要身份验证，即 AccessToken 和 AccessKey，他们将作为参数出现在请求的内容中，需要先验证身份

- 如果身份验证正确，则返回相应的请求结果

- 如果身份验证错误，则返回如下信息 

    ```
    {
        "fbstatus": "401",
        "fbmsg": "Unauthorized",
        "fbcontent": "null"
    } 
    ```

**通用说明 - 信息过滤**

过滤有两个方面：分页和条件筛选

- 分页

    ```
    ?limit=10
    ?start=10&limit=10
    ```

    上面是一种分页方式，limit 表示显示多少条信息，start 表示从第几条开始显示，还有一种分页方式

    ```
    ?page=1&count_per_page=10
    ```

    我个人不喜欢这种方式。

- 条件筛选

    条件筛选就是信息过滤，根据不同的条件获取到不同的内容

    ```
    ?sort_by=id&order_by=desc
    ?photo_id=99
    ```

    上面第一条是排序的筛选，下面是某一条的筛选，指定了特定的筛选条件。

**fbstatus 说明**

fbstatus 和服务器的 status code 是不一样的东西，但也会包含一些 status code，比如 401。

```
100 - GET / POST 请求成功，并且 fbcontent 有返回值
101 - GET / POST 请求失败，需要重新发送请求
104 - GET 请求成功，但所查询的内容不存在，即 fbcontent 的值为 null
300 - 更新或删除请求成功，fbcontent 返回值可以是有内容或者为 null，具体看实际操作中的需要，建议更新操作显示内容
301 - 更新或删除请求失败，fbcontent 返回 null
401 - 没有访问权限，AccessKey 和 AccessToken 不正确
```

**Hypermedia API**

因为项目的私有问题，基本都不会做 Hypermedia API 的内容。