---
title: "加入了记忆访客名字的功能"
slug: a-function-called-remember-guest-name
author: "Bin Hua"
lastmod: 2020-08-13T08:45:59Z
date: 2009-02-04T05:35:29Z
tags: ["dotNet"]
---

加入了 Cookies 记忆访客用户名的功能，至于他说的加入链接和 Email 的，过几天再搞吧，要动数据库的结构的，正好因为 TAG 的设计，要动数据库结构，所以等这个一起了。

Cookies 记忆访客用户名代码如下：

写入

```
string vname1 = HttpUtility.UrlEncode(vname);
HttpCookie newCookie = new HttpCookie("tccom");
newCookie.Values["visitorname"] = vname1;
 newCookie.Expires = DateTime.Now.AddDays(1);
Response.Cookies.Add(newCookie);
```

读出

```
if (Request.Cookies.Get("tccom") != null)
        {
            string vname1 = HttpUtility.UrlDecode(Request.Cookies.Get("tccom").Values.Get("visitorname"));
            this.vname.Value = vname1 ;
        }
```

这里说明下，`HttpUtility.UrlDecode`, `HttpUtility.UrlEncode` 是为了解决中文的乱码问题.

大家帮忙测试下这个功能哈~
