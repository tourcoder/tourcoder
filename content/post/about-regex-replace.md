---
title: "关于Regex.Replace只替换第一个的问题"
slug: "about-regex-replace"
author: "Bin Hua"
lastmod: 2009-08-20 05:47:43
date: 2009-08-20 05:47:43
tags: ["正则"]
---

都知道正则表达式吧，老牛X老牛X的东西了，就是如果你长时间不用，可能很难入门，我也是，当时看的时候都明白了，用的时候也只是那么一两回，几天不用， 全忘光了，今天又遇到一个这样的问题，一个关于 Regex.Replace 只替换第一个的问题，记得在 js 里用 replace 的时候就是只替换第一个匹配的，没办法只能用正则去替换，如今在 asp.net 里用正则去替换自己想要替换掉的内容，无奈也只替换掉了第一个，今天就来说一下我的解决办法：

我的代码是这样的:

```
string s = “asdfdf1<img src=\”sadfsadf\” width=\”sadf\” height=\”2323\” border=\”0\” />1sadfsd<img src=\”sdfdsf\” />fs<img src=\”asdf\” width=\”safds\” >dsdfsdfa”;
Regex.Replace(s, @”<img.*?>”, “”, RegexOptions.IgnoreCase);
Response.Write(s);
```

可以注意到，s 字符串里有三个图片，我想把图片全部替换掉，当然得用正则了，因为里面的内容不一样，所以就写了 `<img.*?>` 这样一个正则表达式，如果你正则不会的话，那你去百度一下，有一个30分钟学会正则表达式，文章还不错。地址：

[http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm](http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm)

当然了我上面的代码就是只替换第一个，如果想把里面的图片代码全替换掉怎么办呢，看下面的代码：

```
//赋给变量后就可以多次替换
string teststr = “asdfdf1<img src=\”sadfsadf\” width=\”sadf\” height=\”2323\” border=\”0\” />1sadfsd<img src=\”sdfdsf\” />fs<img src=\”asdf\” width=\”safds\” >dsdfsdfa”;
string pattern = @”<img.*?>”;
Response.Write(Regex.Replace(teststr,pattern,”###”,RegexOptions.IgnoreCase));
```

其实比上面只多了一步，把正则赋值给了一个变量，奇怪的是这样就可以把想要替换的东西全部替换掉了，具体原因我也说不太明白。

我在 csdn 上还看到了另一个问题，有人问，如果只替换第二个怎么办，下面把代码粘出来：

```
string teststr = “asdfdf1<img src=\”sadfsadf\” width=\”sadf\” height=\”2323\” border=\”0\” />1sadfsd<img src=\”sdfdsf\” />fs<img src=\”asdf\” width=\”safds\” >dsdfsdfa”;
MatchCollection mc = Regex.Matches(teststr, @”<img.*?>”);
Match m=mc[1];//替换第二个
string  sBody = new Regex(m.Value).Replace(teststr, “xxx “, 1, m.Index);

Response.Write(sBody);
```

这样的话，就可以只替换第二个，当然你也可以换成第三个第四个，好了，问题就总结到这儿，有问题给我留言。