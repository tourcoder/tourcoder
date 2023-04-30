---
title: "SQL server中的随机数"
slug: "rand-in-sqlserver"
author: "Bin Hua"
lastmod: 2020-07-18 06:16:07
date: 2009-07-29 05:45:37
tags: ["sql server", "sql"]
---

随机函数：rand()

在查询分析器中执行：select rand()，可以看到结果会是类似于这样的随机小数：0.36361513486289558，像这样的小数在实际应用中用得不多，一般要取随机数都会取随机整数。那就看下面的两种随机取整数的方法：

方式一

A：生成的数是这样的：12.0

```
select floor(rand()*N)
```

B：生成的数是这样的：12

```
select cast( floor(rand()*N) as int)
```

方式二

A：生成的数是这样的：12.0

```
select ceiling(rand() * N)
```

B：生成的数是这样的：12

```
select cast(ceiling(rand() * N) as int)
```

其中里面的N是一个你指定的整数，如 100，可以看出，两种方法的 A 方法是带有 .0 这个的小数的，而 B 方法就是真正的整数了。

大致一看，这两种方法没什么区别，真的没区别？其实是有一点的，那就是他们的生成随机数的范围：

方法1的数字范围：0 至 N-1 之间，如 `cast( floor(rand()*100) as int)` 就会生成 0 至 99 之间任一整数

方法2的数字范围：1 至 N 之间，如 `cast(ceiling(rand() * 100) as int)` 就会生成 1 至 100 之间任一整数

**比较 CEILING 和 FLOOR**

CEILING 函数返回大于或等于所给数字表达式的最小整数。FLOOR 函数返回小于或等于所给数字表达式的最大整数。例如，对于数字表达式 12.9273，CEILING 将返回 13，FLOOR 将返回 12。FLOOR 和 CEILING 返回值的数据类型都与输入的数字表达式的数据类型相同.
