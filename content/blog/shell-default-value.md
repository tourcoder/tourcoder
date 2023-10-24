---
title: "Shell 的变量默认值"
slug: "shell-default-value"
author: "Bin Hua"
lastmod: 2021-05-01T14:21:06Z
date: 2021-05-01T14:21:06Z
tags: ["shell"]
---

一共有两种格式， `${bar-default_value}` 和 `${bar:-default_value}`，在不同的时候显示的结果也不一样

```
#!/usr/bin/env bash
bar1=${bar-"text"}
echo $bar1
```

这里并没有定义 bar，得到的结果是 `text`

```
#!/usr/bin/env bash
bar=""
bar1=${bar-"text"}
echo $bar1
```

这里定义了 bar，但没有赋值，输出结果是空

```
#!/usr/bin/env bash
bar="bar_value"
bar1=${bar-"text"}
echo $bar1
```

这里定义了 bar，并且赋值了，输出结果是 `bar_value`

```
#!/usr/bin/env bash
bar1=${bar:-"text"}
echo $bar1
```

这里也没有定义 bar，输出结果是 `text`

```
#!/usr/bin/env bash
bar=""
bar1=${bar:-"text"}
echo $bar1
```

这里定义了 bar，但没有赋值，输出结果是 `text`

```
#!/usr/bin/env bash
bar="bar_value"
bar1=${bar:-"text"}
echo $bar1
```

这里定义了 bar，并且赋值了，输出结果是 `bar_value`

总结，`${bar-default_value}` 和 `${bar:-default_value}` 只有在 bar 被定义但没有赋值的情况下是不同的，其他情况一致。需要注意的是 `bar=" "` 算是赋值了，两者显示结果是一样的。


