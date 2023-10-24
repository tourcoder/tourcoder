---
title: "jQuery 插件 wTooltip"
slug: "wtooltip"
author: "Bin Hua"
lastmod: 2009-09-28 05:50:13
date: 2009-09-28 05:50:13
tags: ["web前端", "jquery"]
---

今天听同事说，她用了 2 天的时间还没做好一个提示的功能，细问下，原来是要实现一个鼠标移到连接字上，显示出说明文字，但不能使用TITLE,ALT之类，细想下，jQuery插件可以轻松解决这个问题，而且还有很好的延伸作用。

首先，我们需要用到 jQuery 库文件和 wTooltip 库文件

添加引用 jQuery 和 wTooltip

然后写HTML部分的代码

```
<a href=”">这里是连接</a>
```

具体的JS部分

```
<script type=”text/javascript”>

$(document).ready(function() {

$(”a”).wTooltip(); //提示的内容为你连接的内容

});

</script>
```

完成…

扩展延伸

一，自定义提示内容

```
$(”a”).wTooltip({content: “提示内容”});
```

二，使用ajax调用远程提示

```
$(”#block-whatever p”).wTooltip({

content: “提示内容”,

ajax: “http://www.tourcoder.com/?query=keyword”

});
```

三，自定义提示窗口样式

```
$(”#block2 p”).wTooltip({

content: “提示内容”,

style: {

border: “2px solid green”,

background: “blue”,

color: “white”,

fontWeight: “bold”

}

});
```
