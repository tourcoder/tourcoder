---
title: "Apple ID 的奇怪设计"
slug: what-a-wired-design-of-apple-id
author: "Bin Hua"
lastmod: 2020-08-13 09:39:09
date: 2019-10-13 04:02:25
tags: ["bug", "Apple", "Apple ID"]
---

这几天腿受伤，不怎么方便外出，用手机的时间相对于多了点，发现了很多 iOS 和 macOS Catalina 的 bug，昨天给他们提交 bug 提交到晚上十点多，最后还发了个推吐槽了下其中的一个和 Apple ID 相关的 bug。

**准备工作**

- 两个 Apple ID

    first@appleid.com
    
    second@appleid.com
    
- 一部 iPhone

    当前登录的 Apple ID 是 `second@appleid.com`，而 `first@appleid.com` 在这部 iPhone 上曾经登录使用过。

**复现**

在 `appleid.apple.com` 点击忘记密码，请求重置 `first@appleid.com`，在几个下一步后，会提示去该部 iPhone 设置密码，此时该 iPhone 也弹窗让输入新的密码，输入新密码完成后，该 Bug 也出现。

**Bug**

- 在请求重置 `first@appleid.com` 的密码时，此 iPhone 不应该弹窗，让输入，因为 `first@appleid.com` 已经没有在它上面使用了，只是**曾经**登录使用过，这个还说得过去。

- 居然是请求重置 `first@appleid.com` 的密码，但完成上面的复现步骤后，会发现 `first@appleid.com` 和 `second@appleid.com` 的密码都被重置了，这个就很莫名其妙了。

**解决办法**

目前最好的解决办法就是，当你的 iPhone / iPad 要转手给别人之前，要彻底重置系统成新的，而当你的这些设备丢失后，记得第一时间进入 iCloud 远程将手机进行锁定或者擦除。
