---
title: "基于 Backblaze 和 Cloudflare 搭建私有的图床"
slug: "set-up-private-photo-library-using-backblaze-cloudflare-integration"
author: "Bin Hua"
date: 2024-10-12T04:49:43Z
tags: ["Backblaze", "Cloudflare", "Private cloud storage"]
draft: false
---

最早的时候，「代码旅行」这个博客的图片和 markdown 文件一样都是存放在这个库的，很不方便，后来将它移动到了 Backblaze，并使用 Cloudflare 打破了它的流量限制，分享下大致的配置。

### Backblaze 端

在 Backblaze 新建一个 bucket，然后找到这个 bucket 所在的区域即可。最简单的方式，上传一张图片到这个 bucket，看这个图片的返回地址。比如我的一张图片返回地址是 `https://f004.backblazeb2.com/file/tourcoder/tcblog/a-note-app-01.png`，那么前面的 `f004.backblazeb2.com` 可以理解为是 bucket 的所在区域。

因为这里的图片是对外公开的，在 `Bucket Settings` 里设置 bucket 属性为「公开」。图片一般不会更改所以，设置个缓存还是有必要的，`Bucket info` 里填写 `{"cache-control":"max-age=720000"}`，时间可以按需填写。

### Cloudflare 端

- 解析域名到刚才获取到的地址，建议用二级域名，比如我用的是 `storage.tourcoder.com`，给它做一个 cname 的解析到 `f004.backblazeb2.com`

- 在`规则->重写 URL` 中增加一个规则：

  选择「自定义筛选表达式」，然后设置「主机名」「等于」「域名」我用的是 `storage.tourcoder.com`；下面「重写到」「动态」`concat("/file/tourcoder", http.request.uri.path)`，这里的 `tourcoder` 是 bucket 的名字。

- 检查 `SSL/TLS` 中是否已经配置了严格，就是双加密（必须）

- 缓存（可选）：既然是图库一般图片上传后都很少更新，还是有必要增加缓存的。在「规则->页面规则」里增加一个规则即可。URL 设置为 `https://storage.tourcoder.com/*`，时间按需设置。

基本完成了。最后表扬下 Backblaze，还是蛮稳的，我的博客它存储图片用了这么久，没有出现过问题。