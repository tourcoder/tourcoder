---
title: "删除相同数据"
slug: "delete-the-same-data"
author: "Bin Hua"
draft: false
date: 2009-01-20 04:58:00
tags: ["sql", "database"]
---

大家在数据的移动过程，导来导去，难免会有数据重复的情况，通过下面的方式，可以帮你解决数据重复的问题

方法一：该方法比较保险点

```
declare @max integer,@id integer
declare cur_rows cursor local for select 主键,count(*) from 数据表 group by 主键 having count(*) > 1
open cur_rows
fetch cur_rows into @id,@max
while @@fetch_status=0
begin
select @max = @max -1
set rowcount @max
delete from 数据表 where 主键 = @id
fetch cur_rows into @id,@max
end
close cur_rows
set rowcount 0
```

方法二：该方法，一般是没有问题的，但在处理一些键值的空与null的时候，会出现问题

```
select distinct * into #Tmp from 数据表
drop table 数据表
select * into 数据表 from #Tmp
drop table #Tmp
```