---
title: "SQL SERVER防注入"
slug: "hacked-in-sql-server"
author: "Bin Hua"
lastmod: 2009-08-14 05:47:00
date: 2009-08-14 05:47:00
tags: ["sqlserver", "sql", "安全"]
---

该死，单位的 SQL 被通过一个ASP程序的漏洞挂马了，不同的是，这次挂马不是正常挂马，别人挂马是为了获利，进而挂上他们的链接 `<sc…`，而这次是非正常的，直接删除了数据。除了打上对应的漏洞的补丁外，在数据库方面也和大家分享下，如果防注入。

SQL2000的操作方法：

1、 不要使用sa用户连接数据库。

SA帐户拥有所有数据库和数据表的操作权限，在网页中使用SA连接数据库安全隐患非常大。

2、 新建一个public权限数据库用户，并用这个用户访问数据库。

为了增加安全系数，建议每个数据库建立独立的只有public权限管理帐户，并用这个用户访问数据库有利于SQL的安全性。

3、`[角色]`去掉角色 public 对 sysobjects 与 syscolumns 对象的 select 访问权限。

4、`[用户]用户名称-> 右键－属性－权限－在 sysobjects 与 syscolumns 上面打“×”`。

SQL2005的操作方法：

1、不要使用sa用户连接数据库。

SA帐户拥有所有数据库和数据表的操作权限，在网页中使用SA连接数据库安全隐患非常大。

2、新建一个public权限数据库用户，并用这个用户访问数据库。

为了增加安全系数，建议每个数据库建立独立的只有public权限管理帐户，并用这个用户访问数据库有利于SQL的安全性。

3、`打开数据库—视图–找到–sys.sysobjects–右键“属性”– 左侧“权限”—右侧下面` 在 `“SELECT”` 后面的“拒绝”后面把 “打对号”。

4、`打开数据库—视图–找到–sys.syscolumns–右键“属性”– 左侧“权限”—右侧下面` 在 `“SELECT”` 后面的“拒绝”后面把 “打对号”。

SQL2005到此为止问题解决。

用下面的东西查询，权限

```
DECLARE   @T   varchar(255),
@C   varchar(255)
DECLARE   Table_Cursor   CURSOR   FOR
Select   a.name,b.name   from   sysobjects   a,syscolumns   b
where   a.id=b.id   and   a.xtype= ‘u ‘   and   (b.xtype=99   or   b.xtype=35   or   b.xtype=231   or   b.xtype=167)
OPEN   Table_Cursor
FETCH   NEXT   FROM   Table_Cursor   INTO   @T,@C
WHILE(@@FETCH_STATUS=0)
BEGIN   print   @c
FETCH   NEXT   FROM   Table_Cursor   INTO   @T,@C
END
CLOSE   Table_Cursor
DEALLOCATE   Table_Cursor
```

单一替换

```
UPDATE table SET key = REPLACE(key, ‘ bad’, ”)
```

全文替换

可以看我以前写的一篇「删除相同数据」。