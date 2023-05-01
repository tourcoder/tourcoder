---
title: "css hack 速查手册"
slug: "css-hack"
author: "Bin Hua"
lastmod: 2009-01-21 05:10:00
date: 2009-01-21 05:10:00
tags: ["css", "web前端"]
---

屏蔽IE浏览器（也就是IE下不显示）

```
*:lang(zh) select {font:12px  !important;} /*FF,OP可见，特别提醒：由于Opera最近的升级，目前此句只为FF所识别*/
select:empty {font:12px  !important;} /*safari可见*/
```

这里select是选择符，根据情况更换。第二句是MAC上safari浏览器独有的。

仅IE7与IE5.0可以识别

```
*+html  select {…}
```

当面临需要只针对IE7与IE5.0做样式的时候就可以采用这个HACK。

仅IE7可以识别

```
*+html  select {…!important;}
```

当面临需要只针对IE7做样式的时候就可以采用这个HACK。

IE6及IE6以下识别

```
* html  select {…}
```

这个地方要特别注意很多博客都写成了是IE6的HACK其实IE5.x同样可以识别这个HACK。其它浏览器不识别。

```
html/**/ >body  select {…}
```

这句与上一句的作用相同。

仅IE6不识别，屏蔽IE6

```
select { display /*屏蔽IE6*/:none;}
```

这里主要是通过CSS注释分开一个属性与值，注释在冒号前。

仅IE6与IE5不识别，屏蔽IE6与IE5

```
select/**/ { display /*IE6,IE5不识别*/:none;}
```

这里与上面一句不同的是在选择符与花括号之间多了一个CSS注释。不屏蔽IE5.5

仅IE5不识别，屏蔽IE5

```
select/*IE5不识别*/ {…}
```

这一句是在上一句中去掉了属性区的注释。只有IE5不识别，IE5.5可以识别。

盒模型解决方法

```
selct {width:IE5.x宽度; voice-family :"\"}\""; voice-family:inherit; width:正确宽度;}
```

盒模型的清除方法不是通过!important来处理的。这点要明确。

清除浮动

```
select:after {content:"."; display:block; height:0; clear:both; visibility:hidden;}
```

在Firefox中，当子级都为浮动时，那么父级的高度就无法完全的包住整个子级，那么这时用这个清除浮动的HACK来对父级做一次定义，那么就可以解决这个问题。

截字省略号

```
select { -o-text-overflow:ellipsis; text-overflow:ellipsis; white-space:nowrap; overflow:hidden; }
```

这个是在越出长度后会自行的截掉多出部分的文字，并以省略号结尾，很好的一个技术。只是目前Firefox并不支持。

只有Opera识别

```
@media all and (min-width: 0px){ select {……} }
```

针对Opera浏览器做单独的设定。

以上都是写CSS中的一些HACK，这些都是用来解决局部的兼容性问题，如果希望把兼容性的内容也分离出来，不妨试一下下面的几种过滤器。这些过滤器有的是写在CSS中通过过滤器导入特别的样式，也有的是写在HTML中的通过条件来链接或是导入需要的补丁样式。

IE5.x的过滤器，只有IE5.x可见

```
@media tty {
i{content:"\";/*" "*/}} @import ‘ie5win.css‘; /*";}
}/* */
```

IE5/MAC的过滤器，一般用不着

```
/*\*//*/
@import "ie5mac.css";
/**/
IE的if条件Hack
<!–[if IE]> Only IE <![endif]–>
所有的IE可识别
<!–[if IE 5.0]> Only IE 5.0 <![endif]–>
只有IE5.0可以识别
<!–[if gt IE 5.0]> Only IE 5.0+ <![endif]–>
IE5.0包换IE5.5都可以识别
<!–[if lt IE 6]> Only IE 6- <![endif]–>
仅IE6可识别
<!–[if gte IE 6]> Only IE 6/+ <![endif]–>
IE6以及IE6以下的IE5.x都可识别
<!–[if lte IE 7]> Only IE 7/- <![endif]–>
仅IE7可识别
```