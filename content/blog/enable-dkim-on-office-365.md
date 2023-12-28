---
title: "Office 365 中开启 dkim"
slug: "enable-dkim-on-office-365"
author: "Bin Hua"
date: 2019-04-01 05:03:32
tags: ["Email", "office365", "微软", "dkim", "代码", "microsoft365"]
draft: false
---

邮局系统开启 DKIM 是一件必做的事情，什么是 dkim 就不解释了，主要说下它的效果，看下面两张图

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-06.png)

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-07.png)

第一张是开启了 DKIM 的，第二张是没有开启 DKIM 的，开启了 dkim 发送和签名都是来自自己的域名，而没有开启的，发送是来自自己的域名，但签名是来自微软的。视觉上看着不爽不说，关键还暴露了注册 office 365 的二级域名等。如果像我这样，多个域名邮箱在同一个账户里，就更郁闷了，隐私泄露。

在 Office 365 中开启 dkim 的过程如下

首先在 office 365 管理员平台查看是否已经开启了 dkim

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-01.png)

如图所示，进入到管理员后台，选择 exchange

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-02.png)

然后选择界面中的 dkim 菜单

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-03.png)

选择域名，这里 tourcoder.com 是已经开启了 dkim，如果没有开启 dkim 的图如下

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-04.png)

只要点击 Enable 按钮即可，但很多时候，是没有 Enable 按钮的，是下图这么一个情况

![](https://storage.tourcoder.com/tcblog/enable-dkim-on-office-365-05.png)

那么这个时候就需要用到 PowerShell 命令行来操作。

首先添加两个 CNAME 的记录

```
name:selector1._domainkey
value:selector1-tourcoder-com._domainkey.tourcoder.onmicrosoft.com
```

```
name:selector2._domainkey
value:selector2-tourcoder-com._domainkey.tourcoder.onmicrosoft.com
```

然后在 Windows 系统中右键 PowerShell 选择管理员运行模式

第三步：输入下面的命令

```
Set-ExecutionPolicy RemoteSigned

$UserCredential = Get-Credential

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection

Import-PSSession $Session
```

这是通过 Power Shell 连接到 EXO，中途就需要输入管理员的帐号密码

第四步：输入下面的命令，开启 DKIM

```
Get-DkimSigningConfig -Identity tourcoder.com| Format-List
```

查看，如果不存在则会返回没有对象

```
New-DkimSigningConfig -DomainName tourcoder.com -Enabled $true
```

开启 DKIM，开启后在运行上面的命令即可有返回值。

至此命令执行完毕后，再次返回到之前的管理中心去看，这时 dkim 就完全开启了。

更新@20200406：本来以前到这里就解决了，但沙雕微软又出来搞事了。上面步骤中，登录管理员账户，必须要关闭管理员账户的二次认证。有时候你关闭了管理员的二次认证，但它还是要求进行二次认证。正确的操作是，点左侧的导航，选择 `全部`，然后选择 `Azure Active Directory`，会进入到 `Azure Active Directory admin center`，然后选择 `Azure Active Directory > Properties`，拉到底部，点击 `Manage Security defaults`，将这里的 `Yes` 改成 `No`。