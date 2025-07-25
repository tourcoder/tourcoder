---
title: "比较 Google Workspace 和 Google One"
slug: "compare-google-workspace-and-google-one"
author: "Bin Hua"
date: 2022-10-22T06:41:17Z
tags: ["GoogleWorkspace", "GoogleOne", "Google", "GSuite"]
draft: false
---

Google 有两套账户体系，一套是以 `@gmail.com` 为后缀的账户或者以用户自己其他 email 地址（比如 foobar@yahoo.com）为用户名的账户。另外一套账户是以用户自有域名邮箱为用户名的账户。根据功能特色，我将这两套账户体系分别称为 `Google One(Personal account)` 和 `Google Workspace(Workspace account)`。

这两套账户体系衔接着 Google 的各种服务，但每个账户的服务又不完全一样。Google One 有的服务，Google Workspace 未必有；Google One 免费的功能，Google Workspace 可能要收费等等，反之亦然。

写这篇博文，我是想把这两套账户体系理一理，说点我日常使用的功能中，它们之间差异的地方，让大家有个清楚的认识，便于发现哪一个账户体系才是适合自己的。

|功能|Google One|Google Workspace|胜利方|
|---|---|---|---|
|自有域名|不支持，只能用 gmail.com，或者不用 gmail 服务，用现有的 email，变相用自己域名|支持，且支持多个域名|Workspace|
|多邮箱|只有一个以 @gmail.com 结尾的邮箱，可以通过 username+alias@gmail.com 或在 username 各个字母数字之间加点号变成很多个邮箱。但现在很多其他服务已经不支持这种变形，比如 Apple ID，Cloudflare 等将所有的变形都识别为一个邮箱|理论上有无限个邮箱，因为可以增加一个或多个域名，主用户名只有一个，但可以有无限个别名|Workspace|
|容量|默认有免费的 15G 容量，收费版价格是 100G 容量每年 19.99 美元起，其他容量的价格清单可以看[这里](https://one.google.com/about/plans)|没有免费版，收费版价格是 30G 容量每年 84 美元起，其他价格看[这里](https://workspace.google.com/pricing.html)|One|
|容量共享|可以和 5 个家庭成员共享容量|由 GSuite 转过来的 Starter 已经可以共享，只有 300G，未开启共享的由所购买的 plan 决定容量|One|
|Google Voice|免费使用，且可买断号码|收费使用，每个月 10 美元起，无法买断号码|One|
|Google Play|家庭成员之间可以共享自己 Google Play 上的内容|无法共享|One|
|Google Chat|无法使用一些专门为 workspace 做的功能，比如无法使用 Chat 里面的其他 app 功能。|都能使用，但根据付费不一样，能用的程度也不一样。比如 84 美元一年的这个套餐就不支持`将外部人员拉入到群组`中|50%-50%|
|Google Drive|有一个 computers 功能，非常好用|没有 computers 功能|One|
|Google Photos|根据购买的 plan 确定|开启共享了由共享的总容量决定，没有开启由所购买的 plan 的容量决定|Google One|
|AI|有专门的方案，还可以家庭共享|视 license 而定|Google One|

**总结**

- Google Workspace 主要是面向工作的，是为公司/团队来设置的。但有些用户，需要用自己的域名来构建邮箱，作为自己个人账户使用，所以我才会写这篇博文，将 Workspace 和 One 做了比较。

- 这里有一个特殊的地方，就是本文开头说到的，Google 的个人账户用户名也可以是自己其他的 email 地址，比如 `foobar@yahoo.com`，那么这个账户里是没有 gmail 功能的，和 gmail 关联的一些功能都无法使用。

- 容量这块费用相差很大。以我自己的实际使用举例说明，我在这里存放的照片视频还有 480G+，我老婆备份的照片视频还有 200G+，我还有一个账户里面有 18G+ 的资料，我现在用的 Google One 是 2T 每年收费 99.99 美元。~~但如果我换成 Google Workspace 的话，我需要买三个 2T 容量的账户，费用是每个账户每年 144 美元，三个账户就是 432 美元。就是因为容量没法共享，而且不支持单独购买，其实我完全可以为那个只有 18G+ 资料的账户买一个一年 72 美元的套餐，但在 Google Workspace 里目前还无法这么做，要按最高的容量需求的账户来买。~~ 被我删除部分的计算也方式也是对的，只不过 2T 的价格涨到了 168 美元/年，三个账户就是 504 美金/年。这里有个办法是是因为现在 Google Workspace 共享容量，可以用基础版的 Starter（以前的 G Suite 转过来的，包含 300G 共享，现在的新版每个用户是 30G） + 额外购买容量（100G，1T，10T 三个可选，其中 1T 是 40 美元/月，10T 是 300 美元/月）。怎么算，都是 Google One 完胜！！！

- AI 部分，Google One 完爆 Google Workspace。Google One 就不说了一个订阅家庭共享，最新的模型等。Google Workspace 要达到 Google One 所使用的到的模型必须要订阅标准版 (Standard) 开始起的方案。Starter 基本没用，没有 Deep Research, Canvas, Vids 等。

- 我本人更喜欢用 Google One 这套，但我很希望 Google 能给增加一个域名邮箱的功能的。

- 以前的 GSuite legacy 现在升级后，就是我这里提到的一年 84 美元的套餐（Starter），以前觉得它会是传家宝一样的数字资产，现在觉得它有点真鸡肋。
