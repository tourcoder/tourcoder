---
title: "被逼，做了一次“流氓”"
slug: css-hacker-01
author: Bin Hua
lastmod: 2020-08-13 08:46:38
date: 2009-04-29 05:39:11
tags: ["web前端", "css"]
---

一个项目一下子恢复到最初的table的混乱状态，尤其是table的居左，居中，居右问题，如果一个页面一个页面修改，那要死人了，怎么办？

```
myalign:expression(this.align="center");
```

来帮你忙！

```
table{myalign:expression(this.align="center");}
```

OK，搞定，FF下面，IE下面全部正常，Oh,yeah