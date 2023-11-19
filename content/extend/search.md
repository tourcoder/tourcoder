---
title: "搜索"
slug: "search"
author: "Bin Hua"
date: 2015-01-01 09:09:00
tags: ["search", "搜索"]
menu:
  main:
    name: "搜索"
    weight: 5
---

本站搜索是基于 Google，如果你没有翻墙，将无法使用该搜索功能

<div class="page">
    <div class="searchf">
        <form action="https://www.google.com/search" onsubmit="return dispatch()" target="_blank" class="search-form">
            <input type="search" placeholder="输入要查内容，回车查询" class="skeywords search-form" name="q" id="q" value="">
            <input name="sitesearch" type="hidden" value="tourcoder.com" />
            <input type="submit" name="submit" value="搜索" />
        </form>
    </div>
</div>
