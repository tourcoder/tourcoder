---
title: "用 Cloudflare Worker 不完美解决 App Store 链接的中国区重定向问题"
slug: "an-imperfect-fix-for-app-store-china-redirect-with-cloudflare-worker"
author: "Bin Hua"
date: 2026-09-12T13:37:47Z
tags: ["Cloudflare", "Workers", "App Store", "iOS"]
draft: false
---

在使用网页版的 App Store 时会发现一个问题，应用的无区域码的链接，形如 `apps.apple.com/app/appname/id<number>`，在访问时会被重定向到 `apps.apple.com/cn/iphone/today`，而非这个应用的页面。即便是硬编码，加上其他非中国区域，如 `apps.apple.com/cn/app/appname/id<number>`，也是同样的问题。

只能通过硬编码 `/cn`，即 `apps.apple.com/cn/app/appname/id<number>`，应用多了就比较难维护，还会出现锁定地区的问题。这里图省事，我利用 CloudFlare worker 来解决这个问题。

Worker 的代码如下

```
export default {
  async fetch(req) {
    const url = new URL(req.url);
    const t = new URL('https://apps.apple.com' + url.pathname + url.search);

    const cc = (req.cf?.country || '').toUpperCase();
    const lang = (req.headers.get('accept-language') || '').toLowerCase();

    if ((cc === 'CN' || lang.startsWith('zh-cn')) && !/^\/[a-z]{2}\//.test(t.pathname)) {
      t.pathname = '/cn' + t.pathname;
    }

    return Response.redirect(t.toString(), 302);
  },
};
```

**部署**

1. Cloudflare 后台 -> Compute (Workers & Pages) -> Create application -> Start from Hello World → 起个名字，比如 `1234` -> Deploy

2. Edit code -> 用上面的代码覆盖当前代码 -> Deploy

此时就已经完成了，得到类似 `1234.<账户子域>.workers.dev` 这样格式的一个 worker，美观和统一性考虑，应该增加自己的域名，选择这个 worker 顶部菜单中的 `Domains -> Custom Domains and Routes -> Add Domain`，增加一个自己的域名，比如 `apps.tourcoder.com`，也可以顺手关闭上面的那个自动生成的域名。

此时访问 `apps.tourcoder.com/app/appname/id<number>`，就会根据情况自动跳转中国区或者外区了。

但并不完美，在常见“翻墙分流”时有这么一个情况，如果访问 `apps.tourcoder.com/app...` 的是外网 IP，访问 `apps.apple.com/...` 的是国内的 IP，而浏览器又是英文语言，那么还是会跳转到 `apps.apple.com/cn/iphone/today`😮‍💨

**扩展**

方便对多个商店应用的跳转管理，worker 代码也可以扩展下，大致样例如下

```
const STORES = {
  appstore: 'https://apps.apple.com',
  googleplay: 'https://play.google.com',
};

export default {
  async fetch(req) {
    const url = new URL(req.url);
    const seg = url.pathname.split('/').filter(Boolean);
    const host = STORES[(seg.shift() || '').toLowerCase()];

    if (!host || !seg.length) return Response.redirect('https://tourcoder.com', 302);

    const t = new URL(host + '/' + seg.join('/') + url.search);

    const cc = (req.cf?.country || '').toUpperCase();
    const lang = (req.headers.get('accept-language') || '').toLowerCase();
    const isCN = cc === 'CN' || lang.startsWith('zh-cn');

    if (host.includes('apple') && isCN && !/^\/[a-z]{2}\//.test(t.pathname)) {
      t.pathname = '/cn' + t.pathname;
    }

    return Response.redirect(t.toString(), 302);
  },
};
```

上面增加了 Google Play，同时收集了错误导流到主站。

最后，期待大家完美的解决方案。