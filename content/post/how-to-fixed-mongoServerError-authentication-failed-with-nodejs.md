---
title: "修正 nodejs 连接 mongodb 时出现的错误"
slug: "how-to-fixed-mongoServerError-authentication-failed-with-nodejs"
author: Bin Hua
lastmod: 2021-12-12T15:45:40+08:00
date: 2021-12-12T15:45:40+08:00
tags: ["mongodb", "nodejs"]
---

在服务器上通过 docker 拉起了一个 mongodb，通过客户端链接一切正常。但在 nodejs 中用 MongoClient 去连接时总是提示错误

```
MongoServerError: Authentication failed
```

**排查**

我在连接数据库时用了

```
mongodb://username:password@server
```

没有指定数据库，尝试了下指定数据库

```
mongodb://username:password@server/dbname
```

问题解决了。

**其他**

我又去搜索了下这个原因，也有人遇到这样的问题，不过他们的解决办法是在数据库后增加 `w=1` 即

```
mongodb://username:password@server/dbname?w=1
```

有待确定。
