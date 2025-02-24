---
title: "如何阻止您域名上的电子邮件欺骗"
slug: "how-to-stop-email-spoofing-on-your-domain-name"
author: "Bin Hua"
date: 2025-02-23T05:50:18Z
tags: ["email", "安全"]
draft: false
---

最近总是收到一些垃圾邮件，和其他直接发送给我的垃圾邮件不同的是，这些邮件都是回复我域名上的邮箱，但我并没有设置这些邮箱，这是典型的「域名仿造邮件」了。这个问题可以通过设置来解决，下面分享下。

- 配置 SPF（Sender Policy Framework）

SPF 用来声明哪些服务器有权使用你的域名发送邮件，换句话说是阻止未授权服务器发邮件，比如我使用的是 Google Workspace，那么这里就设置一个类型为 txt 的记录，其值为

```
v=spf1 include:_spf.google.com -all
```

也可以将 all 前面的 `-` 改成 `~`，即 

```
v=spf1 include:_spf.google.com ~all
```

`-` 是表示「硬失败，强制拒绝伪造邮件」

`~` 是表示「软失败，标记但不拒绝」

- 配置 DKIM（DomainKeys Identified Mail）

DKIM 用来给邮件添加数字签名，收件方可验证邮件内容是否被篡改，也是添加一个 txt 的记录，这个记录的值的格式是 `v=DKIM1; k=rsa; p=公钥`

- 配置 DMARC（Domain-based Message Authentication, Reporting & Conformance）

DMARC 用来规定收件服务器如何处理未通过 SPF 和 DKIM 验证的邮件，并可接收报告，是可选项。其方法也是增加一条 txt 记录，名称为 `_dmarc`，值的格式是 `v=DMARC1; p=reject; rua=mailto:email@example.com; ruf=mailto:email@example.com; fo=1`

`p=reject`：直接拒绝未通过验证的邮件。

`p=quarantine`：把可疑邮件丢进垃圾箱，也可设置为 none。

`rua`：聚合报告 (Aggregate Report) 接收地址，包含每天的统计数据（如通过/未通过 SPF 和 DKIM 的数量等）。

`ruf`：取证报告 (Forensic Report) 接收地址，当邮件未通过验证时，立即发送详细的失败信息（包含原始邮件内容）。

`fo`：失败报告选项，决定何时发送取证报告： 0 是 SPF 和 DKIM 都失败时才发送；1 是 SPF 或 DKIM 任何一个失败就发送；d 是 DKIM 失败时发送；s 是 SPF 失败时发送。