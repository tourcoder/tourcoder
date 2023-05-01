---
title: "本站搜索的改进"
slug: "improve-the-search-feature"
author: "Bin Hua"
lastmod: 2019-06-12 01:10:54
date: 2019-06-12 01:10:54
tags: ["Google", "search"]
---

Ghost 自身是没有带站点搜索功能的，考虑到搜索的需要，我通过 page 实现了一个简单的搜索。

创建一个页面，在页面内容中增加搜索功能的 html 代码即可，代码如下

```
<div class="page">
    <div class="searchf">
        <form action="https://www.google.com/search" onsubmit="return dispatch()" target="_blank" class="search-form">
            <input type="search" placeholder="输入要查内容，回车查询" class="skeywords search-form" name="q" id="q" value="">
            <input name="sitesearch" type="hidden" value="tourcoder.com" />
            <input type="submit" name="submit" value="搜索" />
        </form>
    </div>
</div>
```

其实 Google 搜索在很多年前就提供了一个可自定义的站内搜索，访问 [https://www.google.com/cse/](https://www.google.com/cse/) ，进行必要的定制后会得到相应的 js 代码，如下

```
<script>
  (function() {
    var cx = '007392108407227551164:a9wq4h81k0o';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
</script>
<gcse:searchbox-only></gcse:searchbox-only>
```

同样将代码替换掉之前的搜索代码即可。