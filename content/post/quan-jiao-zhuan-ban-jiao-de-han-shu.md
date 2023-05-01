---
title: "全角转半角的函数"
slug: "quan-jiao-zhuan-ban-jiao-de-han-shu"
author: "Bin Hua"
lastmod: 2009-10-13 04:14:00
date: 2009-10-13 04:14:00
tags: ["php", "全角半角"]
---

一个很无聊的 php 函数，全角转半角

```
function convert2half($str){
    $str = str_replace("～", "~", $str);
    $str = str_replace("｀", "`", $str);
    $str = str_replace("！", "!", $str);
    $str = str_replace("@", "@", $str);
    $str = str_replace("＃", "#", $str);
    $str = str_replace("¥", "$", $str);
    $str = str_replace("％", "%", $str);
    $str = str_replace("&", "&", $str);
    $str = str_replace("＊", "*", $str);
    $str = str_replace("（", "(", $str);
    $str = str_replace("）", ")", $str);
    $str = str_replace("—", "_", $str);
    $str = str_replace("－", "-", $str);
    $str = str_replace("＋", "+", $str);
    $str = str_replace("＝", "=", $str);
    $str = str_replace("｜", "|", $str);
    $str = str_replace("｝", "}", $str);
    $str = str_replace("］", "]", $str);
    $str = str_replace("｛", "{", $str);
    $str = str_replace("［", "[", $str);
    $str = str_replace("“", "\"", $str);
    $str = str_replace("”", "\"", $str);
    $str = str_replace("‘", "'", $str);
    $str = str_replace("’", "'", $str);
    $str = str_replace("：", ":", $str);
    $str = str_replace("；", ";", $str);
    $str = str_replace("？", "?", $str);
    $str = str_replace("／", "/", $str);
    return $str;
}
```