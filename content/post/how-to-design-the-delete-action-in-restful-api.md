---
title: "RESTFUL API 中删除操作的设计"
slug: how-to-design-the-delete-action-in-restful-api
author: Bin Hua
lastmod: 2020-08-13 09:41:24
date: 2019-12-05 05:59:22
tags: ["api", "restful"]
---

RESTFUL API 中删除操作的设计比较特殊，并不是一味的使用一个 DELETE 就可以解决问题。

归纳起来，删除操作有三个情况，如下

1. 删除某个资源

2. 批量删除多个资源

3. 删除某个资源中的某些属性

其中最好处理的是第一个情况，可以通过 DELETE 直接实现，即直接通过 DELETE 该资源的 URL 的形式，如下

```
{api}/resource/<resourceID>
```

而第二和三种情况因为 URL 长度的问题可能无法使用 URL。虽然在 RESTFUL 设计中并没有明确说明 URL 长度限制是多少，但 URL 的长度还是和浏览器，WEBSERVICE（NGINX，IIS，APACHE）有一定的关系，不同的浏览器有着不同的长度限制，同样不同的 WEBSERVICE 有着不同的长度限制，所以直接用 URL 的话难免会存在一定的问题。

先说第三种情况`删除某个资源中的某些属性`，删除某个资源的某些属性本质是更改该资源的部分属性，应该是一个更新的操作，而非删除了该资源，那么则可以使用 PUT 操作来实现更新，即在 BODY 中附加操作的内容，而 URL 地址是该资源的地址，即

```
{api}/resource/<resourceID>
```

再说第二种情况`批量删除多个资源`，如上面所说，因为 URL 长度问题，如果将多个资源拼接到 URL 中势必会出现问题，那么这时候可以用 POST 操作来实现，在 BODY 中附加操作的内容，而 URL 地址是资源合集的地址，即

```
{api}/resource/
```

在实际项目操作中，为了统一好看，我对第二种情况的处理还是使用 DELETE 操作，URL 地址是资源合集的地址，而要操作的内容放在 HEAD 里面，而非 BODY 里面。