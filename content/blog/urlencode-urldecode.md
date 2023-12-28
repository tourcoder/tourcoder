---
title: "UrlEncode和UrlDecode"
slug: "urlencode-urldecode"
author: "Bin Hua"
date: 2009-07-20 05:42:35
tags: ["http", "urlencode", "urldecode"]
draft: false
---

HttpUtility.UrlEncode 方法:

对 URL 字符串进行编码，以便实现从 Web 服务器到客户端的可靠的 HTTP 传输。

重载列表

将字节数组转换为已编码的 URL 字符串，以便实现从 Web 服务器到客户端的可靠的 HTTP 传输。

```
public static string UrlEncode(byte[]);
```

对 URL 字符串进行编码，以便实现从 Web 服务器到客户端的可靠的 HTTP 传输。

```
public static string UrlEncode(string);
```

使用指定的编码对象对 URL 字符串进行编码，以便实现从 Web 服务器到客户端的可靠 HTTP 传输。

```
public static string UrlEncode(string, Encoding);
```

从数组中的指定位置开始一直到指定的字节数为止，将字节数组转换为 URL 编码的字符串，以便实现从 Web 服务器到客户端的可靠的 HTTP 传输。

```
public static string UrlEncode(byte[], int, int);
```

HttpUtility.UrlDecode 方法：

将已经为在 URL 中传输而编码的字符串转换为解码的字符串。

重载列表

将已经为在 URL 中传输而编码的字符串转换为解码的字符串。

```
public static string UrlDecode(string);
```

使用指定的解码对象将 URL 编码的字节数组转换为已解码的字符串。

```
public static string UrlDecode(byte[], Encoding);
```

使用指定的编码对象将 URL 编码的字符串转换为已解码的字符串。

```
public static string UrlDecode(string, Encoding);
```

使用指定的编码对象，从数组中的指定位置开始到指定的字节数为止，将 URL 编码的字节数组转换为已解码的字符串。

```
public static string UrlDecode(byte[], int, int, Encoding);
```

Server是HttpServerUtility类的实例，是System.Web.UI.Page的属性。

HttpServerUtility.UrlEncode 方法：

编码字符串，以便通过 URL 从 Web 服务器到客户端进行可靠的 HTTP 传输。

重载列表

对字符串进行 URL 编码，并返回已编码的字符串。

```
public string UrlEncode(string);
```

URL 对字符串进行编码，并将结果输出发送到 TextWriter 输出流。

```
public void UrlEncode(string, TextWriter);
```

例：

```
String TestString = “This is a .”;
StringWriter writer = new StringWriter();
Server.UrlEncode(TestString, writer);
String EncodedString = writer.ToString();
```

HttpServerUtility.UrlDecode 方法：对字符串进行解码，该字符串为了进行 HTTP 传输而进行编码并在 URL 中发送到服务器。

重载列表

对字符串进行 URL 解码并返回已解码的字符串。

```
public string UrlDecode(string);
```

对在 URL 中接收的 HTML 字符串进行解码，并将结果输出发送到 TextWriter 输出流。

```
public void UrlDecode(string, TextWriter);
```

需要注意的几点：

1、 HttpUtility.UrlEncode，HttpUtility.UrlDecode是静态方法，而Server.UrlEncode，Server.UrlDecode是实例方法。

2、 Server是HttpServerUtility类的实例，是System.Web.UI.Page的属性。

3、 用HttpUtility.UrlEncode编码后的字符串和用Server.UrlEncode进行编码后的字符串对象不一样:

例如：

```
string url=”http://search.99read.com/index.aspx?book_search=all&main_str=奥迷尔”;
Response.Write(HttpUtility.UrlEncode(url));
Response.Write(”
“);
Response.Write(Server.UrlEncode(url));
```

输出结果是：

```
http%3a%2f%2fsearch.99read.com%2findex.aspx%3fbook_search%3dall%26main_str%3d%e5%a5%a5%e8%bf%b7%e5%b0%94
http%3a%2f%2fsearch.99read.com%2findex.aspx%3fbook_search%3dall%26main_str%3d%b0%c2%c3%d4%b6%fb
```

原因：Server.UrlEncode的编码方式是按照本地程序设置的编码方式进行编码的，而HttpUtility.UrlEncode是默认的按照.net的utf-8格式进行编码的。

如果改一下程序：

```
string url1=”http://search.99read.com/index.aspx?book_search=all&main_str=奥迷尔”;
Response.Write(HttpUtility.UrlEncode(url1,System.Text.Encoding.GetEncoding(”GB2312″)));
Response.Write(”
“);
Response.Write(Server.UrlEncode(url1));
```

输出的结果是：

```
http%3a%2f%2fsearch.99read.com%2findex.aspx%3fbook_search%3dall%26main_str%3d%b0%c2%c3%d4%b6%fb
http%3a%2f%2fsearch.99read.com%2findex.aspx%3fbook_search%3dall%26main_str%3d%b0%c2%c3%d4%b6%fb
```

4、有时候可能别的系统传递过来的url是用别的编码方式编码的。

介绍自己编写的一个方法，可以获取指定编码格式的QueryString。

```
public string GetNonNullQueryString(string key,Encoding encoding)
{
//引用System.Collections.Specialized和System.Text命名空间
string stringValue;
System.Collections.Specialized.NameValueCollection encodingQueryString;
//该方法是在2.0中新增的
encodingQueryString = HttpUtility.ParseQueryString(Request.Url.Query,encoding);
//’里面的key就是你提交的参数的Key
return encodingQueryString[key] != null ? encodingQueryString[key].Trim() : “”;
}
```

调用：

```
string url = GetNonNullQueryString(”url”,Encoding.UTF8).Trim();
```

在对URL进行编码时，该用哪一个？这两都使用上有什么区别吗？

测试：

```
string file=”文件上（传）篇.doc”;
string Server_UrlEncode=Server.UrlEncode(file);
string Server_UrlDecode=Server.UrlDecode(Server_UrlEncode);
string HttpUtility_UrlEncode=System.Web.HttpUtility.UrlEncode(file);
string HttpUtility_UrlDecode=System.Web.HttpUtility.UrlDecode(HttpUtility_UrlEncode);
Response.Write(”原数据：”+file);
SFun.WriteLine(”Server.UrlEncode：”+Server_UrlEncode);
SFun.WriteLine(”Server.UrlDecode：”+Server_UrlDecode);
SFun.WriteLine(”HttpUtility.UrlEncode：”+HttpUtility_UrlEncode);
SFun.WriteLine(”HttpUtility.UrlDecode：”+HttpUtility_UrlDecode);
```

输出：

原数据：文件上（传）篇.doc

```
Server.UrlEncode：%ce%c4%bc%fe%c9%cf%a3%a8%b4%ab%a3%a9%c6%aa.doc
Server.UrlDecode：文件上（传）篇.doc
HttpUtility.UrlEncode：%e6%96%87%e4%bb%b6%e4%b8%8a%ef%bc%88%e4%bc%a0%ef%bc%89%e7%af%87.doc
```

HttpUtility.UrlDecode：文件上（传）篇.doc

区别在于：HttpUtility.UrlEncode()默认是以UTF8对URL进行编码，而Server.UrlEncode()则以默认的编码对URL进行编码。

在用 ASP.Net 开发页面的时候, 我们常常通过 System.Web.HttpUtility.UrlEncode 和 UrlDecode 在页面间通过 URL 传递参数. 成对的使用 Encode 和 Decode 是没有问题的.

但是, 我们在编写文件下载的页面的时候, 常常用如下方法来指定下载的文件的名称:

```
Response.AddHeader(”Content-Disposition”,”attachment; filename=”
+ HttpUtility.UrlEncode(fileName, Encoding.UTF8));
```

之所以转换成 UTF8 是为了支持中文文件名.

这 时候问题就来了, 因为 HttpUtility.UrlEncode 在 Encode 的时候, 将空格转换成加号(’+'), 在 Decode 的时候将加号转为空格, 但是浏览器是不能理解加号为空格的, 所以如果文件名包含了空格, 在浏览器下载得到的文件, 空格就变成了加号.

一个解决办法是, 在 HttpUtility 的 UrlEncode 之后, 将 “+” 替换成 “%20″( 如果原来是 “+” 则被转换成 “%2b” ) , 如:
fileName = HttpUtility.UrlEncode(fileName, Encoding.UTF8);
fileName = fileName.Replace(”+”, “%20″);
不明白微软为什么要把空格转换成加号而不是”%20″. 记得 JDK 的 UrlEncoder 是将空格转换成 “%20″的.
经检查, 在 .Net 2.0 也是这样.

上面是从别的地方拷贝的，写得很好，我自己的一个程序中也遇到同样的问题，默认aspx是以utf-8为编码的，在我这个程序中必须用gb2312为默认编码（），问题出现了，以前没有问题的HttpUtility.UrlDecode在 Page.Request回的值是乱码这就是上面说的HttpUtility.UrlDecode默认以UTF8对URL进行编码，这种情况下面只需将 HttpUtility.UrlDecode改成Server.UrlEncode即可。
