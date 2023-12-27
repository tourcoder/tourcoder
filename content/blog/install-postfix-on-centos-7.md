---
title: "CentOS 7 上安装配置 postfix"
slug: "install-postfix-on-centos-7"
author: "Bin Hua"
lastmod: 2019-03-15 05:04:34
date: 2019-03-15 05:04:34
tags: ["Gmail", "centos", "postfix"]
---

最近被 Google 弄得贼闹心，加上邮件转发的需要，所以尝试用开源软件在 CentOS 7 上搭建了邮件服务。之前买过 exchange server，也用过 zimbra 都太臃肿，这次用 postfix 来搭建。

**注意** 这只是一个学习，非常不建议个人搭建邮局服务器，时间成本，维护成本等等非常不划算，邮局系统是非常复杂的。

#### 准备条件

- 2GB/2CPUs 的 vps

- CentOS 7.5

    因为域名是 tourcoder.com，所以先将 hostname 改成 mail.tourcoder.com，执行命令 `hostnamectl set-hostname mail.tourcoder.com`

- postfix

- 域名 tourcoder.com

    提前做好解析（1）创建 name 为 mail 的 A 记录到本 VPS 的 IP（2）创建 name 为 @ 的 mx 记录到 mail.tourcoder.com，优先级为 10（3）设置 SPF，记录为 `v=spf1 a mx 123.123.123.123 ~all`，这里的 ip 地址是服务器的 ip 地址，可以去掉

#### 概念

便于理解，这里我画了一张图

![](https://storage.tourcoder.com/tcblog/install-postfix-on-centos-7-1.jpg)

发件人通过 MUA (邮件用户代理，即我们常用的邮件客户端) 操作，让 MTA (邮件传输代理，即 postfix) 将邮件传输到 MDA (邮件投递代理，保存在某一个地方，比如数据库中)，而收件人通过 MUA 访问 MDA 投递的位置收取邮件。

基本是这么一个原理，但实际产品要比这个复杂得多。

#### 操作步骤

默认的情况下， CentOS 自带了 postfix，只需要进行配置，打开 postfix 的配置文件

```
vi /etc/postfix/main.cf
```

按照下面的内容进行配置

第 75 行（vi/vim 命令 :75）

```
myhostname = mail.tourcoder.com
```

第 83 行

```
mydomain = tourcoder.com
```

第 99 行

```
myorigin = $mydomain
```

第 116 行

```
inet_interfaces = all
```

第 119 行

```
inet_protocols = ipv4
```

取消第 165 行的注释，注释掉 164 行

```
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
```

第 264 行，这里的 `123.123.123.123` 表示当前服务器的 IP 地址，是为了授权其他网络通过本服务器发送邮件。

```
mynetworks = 127.0.0.0/8 123.123.123.123
```

第 419 行

```
home_mailbox = Maildir/
```

第 425 行

```
mail_spool_directory = /var/mail
```

`main.cf` 文件的配置就结束了，打开 `/etc/postfix/master.cf` 文件将 smtps 的注释取消

```
smtps inet  n -  y  -  - smtpd
```

最后重启 postfix

```
service postfix restart
```

这时 postfix 基本就配置完成了。


#### 测试

为了方便，就直接在同台机器上进行测试，用 telnet，操作步骤如下

- 连接 SMTP 服务器，命令 `telnet 127.0.0.1 25`

- 连接成功后，输入命令 `MAIL FROM:<test@tourcoder.com>`，告诉服务器发件人的地址，回车

- 输入命令 `RCPT TO:<hi@test.tourcoder.com>`，告诉服务器收件人的地址，回车

- 输入命令 `DATA` 回车

- 输入命令 `FROM:test@tourcoder.com`，回车

- 输入命令 `TO:hi@test.tourcoder.com`，回车，这和上面一行结合解决 `undisclosed recipients` 的问题

- 输入命令 `Subject: test` 回车

- 输入命令 `test body`，回车

- 输入命令 `.`，回车，注意这里就是一个命令点，表示内容结束，传输邮件

这时候会得到 `250 2.0.0 Ok:queued as ADFSDAFLJ`，这样的内容，表示邮件已经进入发送队列。此时你可以用命令 `quit` 退出关闭 telnet。

#### 配置 STMP 用户

也可以通过 `cyrus` 来配置 STMP 用户，一般在 centOS 会自动安装，也可以通过 `rpm -qa | grep cyrus` 来检查是否已经安装

先更改 `/etc/postfix/main.cf` 文件

```
vi /etc/postfix/main.cf
```

在底部增加

```
smtpd_client_restrictions = permit_sasl_authenticated
smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous
```

然后重启 postfix，接着增加用户

```
saslpasswd2 -c -u tourcoder.com noreply
```

这里的 `noreply` 是用户名，回车会要求给该用户增加密码。完成后可以通过 `sasldblistusers2` 命令查看是否成功。最后配置 `/etc/sasl2/smtpd.conf` 文件

```
vi /etc/sasl2/smtpd.conf
```

将里面的内容替换成

```
pwcheck_method: auxprop
auxprop_plugin: sasldb
mech_list: plain login CRAM-MD5 DIGEST-MD5
```

同样重启后完成即可。

#### 问题

有时候有些服务商会屏蔽 25 这个端口，比如我当前服务器使用的服务商就屏蔽了，可以通过其他的端口来发送邮件，比如 250，操作

- 编辑 `/etc/postfix/master.cf` 文件，增加一行 `smtp2 inet  n - n - － smtpd`

- 编辑 `/etc/services`，增加 `smtp2 2525/tcp mail2` 和 `smtp2 2525/udp mail2`

- 防火墙增加该端口

- 重启 `service postfix restart`


#### 状态码

- 220 服务就绪

- 250 请求邮件动作正确，完成（HELO,MAIL FROM,RCPT TO,QUIT 指令执行成功会返回此信息）

- 235 认证通过

- 221 正在处理

- 354 开始发送数据，结束以 ．（DATA指令执行成功会返回此信息）

- 500 语法错误，命令不能识别

- 550 命令不能执行，邮箱无效

- 552 中断处理：用户超出文件空间来自: 

#### 一些命令

- 查看 postfix 的发送记录，`vi /var/log/maillog`

- 查看发送队列中的邮件 `postqueue -p` 或者 `mailq`

- 删除所有发送队列中的邮件 `postsuper -d ALL`

- 删除所有发送队列中 deferred 的邮件 `postsuper -d ALL deferred`


#### MAIL QUEUES
 
- incoming 收信箱
 
- active 正在准备发送的邮件
 
- defered 无法发送的邮件,等待重发
 
- corrupt 无法读取或者损坏的邮件
 
- hold 暂停的邮件,需要手工启动 DELIVERY STATUS REPORTS
 
- bounce 每一位收件者的送信状态,记录为什么退信由 bounce(8) 管理
 
- defer 每一位收件者的寄送状态,说明为什么延迟由 defer(8) 管理
 
- trace 每一位收件者的寄送状态信息，说明被 Postfix 用 `sendmail -v` 或 `sendmail -bv` 命令执行的状态由 trace(8) 管理

更多说明看 [https://postfix.org](https://postfix.org)