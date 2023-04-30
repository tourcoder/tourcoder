---
title: "全角字符与半角字符的相互转换(C#)"
slug: half-and-all-in-csharp
author: "Bin Hua"
lastmod: 2020-07-18 06:16:15
date: 2009-08-04 05:46:16
tags: ["dotnet"]
---

```
/// <summary>全角半角的相互转换
///
/// </summary>
public class ConvertDBCAndSBC
{

/// <summary>半角转成全角
/// 半角空格32,全角空格12288
/// 其他字符半角33~126,其他字符全角65281~65374,相差65248
/// </summary>
/// <param name=”input”></param>
/// <returns></returns>
public string DBCToSBC(string input)
{
char[] cc = input.ToCharArray();
for(int i=0;i<cc.Length;i++)
{
if(cc[i] == 32)
{
// 表示空格
cc[i]=(char)12288;
continue;
}
if(cc[i] < 127 && cc[i] > 32)
{
cc[i]=(char)(cc[i]+65248);
}
}
return new string(cc);
}

/// <summary>全角转半角
/// 半角空格32,全角空格12288
/// 其他字符半角33~126,其他字符全角65281~65374,相差65248
/// </summary>
/// <param name=”input”></param>
/// <returns></returns>
public string SBCToDBC(string input)
{
char[] cc = input.ToCharArray();
for (int i = 0; i < cc.Length; i++)
{
if(cc[i] == 12288)
{
// 表示空格
cc[i] = (char)32;
continue;
}
if (cc[i] > 65280 && cc[i] < 65375)
{
cc[i] = (char)(cc[i] – 65248);
}

}
return new string(cc);
}
}
```

测试代码

```
static void Main(string[] args)
{
Console.Write(”请输入要转为半角的字符：”);
string str = Console.ReadLine();
Console.WriteLine(”半角：” + new ConvertDBCAndSBC().SBCToDBC(str));
Console.ReadLine();

Console.Write(”请输入要转为全角的字符：”);
string str2 = Console.ReadLine();
Console.WriteLine(”全角：” + new ConvertDBCAndSBC().DBCToSBC(str2));
Console.ReadLine();
}
```