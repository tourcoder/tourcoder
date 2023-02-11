---
title: "Hugo 中最后更新的时间显示"
slug: "lastmod-in-hugo"
author: Bin Hua
date: 2023-02-11T03:00:28Z
tags: ["hugo", "最后更新"]
---

我的这个博客是基于 hugo + GitHub + Cloudflre pages 构成，因为我不定期更新博客的旧内容，所以增加了个提示，即在博文下面提醒阅读者本篇博文的最后更新时间。

**原始做法**

在文章模板中增加 `lastmod` 字段，比如这篇博文

```
---
title: "Hugo 中最后更新的时间显示"
slug: "lastmod-in-hugo"
author: Bin Hua
date: 2023-02-11T03:00:28Z
lastmod: 2023-02-11T03:00:28Z
tags: ["hugo", "最后更新"]
---
```

每次更新这篇博文时，手动修改 `lastmod` 中的时间日期即可，但这个实在有点折腾。在查找文档和询问后，可以通过下面方式实现

**当前做法**

不更改模版中的内容，即不用增加 `lastmod`，通过修改配置文件来实现，在 `config.toml` 增加

```
[frontmatter]
  lastmod = ['lastmod', ':git', ':fileModTime', 'date', 'publishDate']
```

具体的每个解释说明，可以看官方文档中的 [Configure Dates](https://gohugo.io/getting-started/configuration/#configure-dates)。

至于引用，在主题模板中需要显示`最后更新时间`的地方增加 `{{ .Lastmod }}` 即可。