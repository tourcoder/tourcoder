---
title: "踩坑 outlook 的域名邮箱"
slug: "outlook-premium-email-box"
author: "Bin Hua"
lastmod: 2020-08-13 09:40:26
date: 2019-11-09 15:08:42
tags: ["office365", "outlook", "微软"]
---

**最新更新**：以下内容是一个产品试用过程，在这几天试用下来，可以用非常糟糕这个词形容，bug 出奇的多，并不建议你在实际使用。

outlook 的域名邮箱就是使用你当前的 outlook/hotmail/live/msn 邮箱，增加一个个性域名的邮箱，官方名字叫 `Personalized email address`。这个服务其实很早就有了，那时候是单独的订阅，但现在已经取消，用了更为鸡肋的方式替代。我之前用了它的单独订阅，但忘了续费导致过期无法再继续使用（微软客服说的，如果过期，再续费就算是新的订阅者，而那个服务不面向新的订阅着，呵呵）。

废话少说，介绍下今天的产品，就是这个鸡肋。

#### 准备工作

- 确保你想用来做邮箱的域名在 Godaddy，比如我这里用的是本博客的域名 tourcoder.com，我将它转移到 Godaddy，并且必须要用 Godaddy 的 Nameservers，切记！！！

- Office 365 个人或者是家庭订阅版账户。

#### 如何获得

如果你是 Office 365 个人或者家庭订阅版的用户，你就已经拥有了这个，你需要做的就是激活使用它。

#### 激活使用

访问 outlook.live.com，用的订阅版账户登录，在界面的右上角会有一个钻石的标志，点它。

![](/imgs/outlook-premium-email-box-001.png)

在弹出的窗口中，点击 `Feature` 里面 `Personalized email address` 后面的 `Get Started`，如下图

![](/imgs/outlook-premium-email-box-002.png)

因为域名已经转移到 Godaddy，所以点下图中最下面的 `I already own a Godaddy domain`

![](/imgs/outlook-premium-email-box-003.png)

注意，这里有一个坑，如果你想要用一个新域名，不要通过上面的 `Get a domain` 来注册一个新域名，我尝试了多次，都无法成功，最后先在 Godaddy 注册好域名，然后再使用，就没有问题。

![](/imgs/outlook-premium-email-box-004.png)

输入自己要用的域名

![](/imgs/outlook-premium-email-box-005.png)

会自动验证，注意另外一个坑，如上面准备工作中所说，一定要用 Godaddy 的 Nameservers，不然会验证通不过。其实可以通过设置让验证通过，但是，即便这里通过了，后面的操作会出现大量错误问题，所以一定要用 Godaddy 的 Nameservers。

![](/imgs/outlook-premium-email-box-006.png)

连接 Godaddy，如上所说，如果不用它的 Nameservers，这个界面是访问不到的。

![](/imgs/outlook-premium-email-box-007.png)

验证成功后，会自动返回到 outlook.live.com 的邮箱界面。

![](/imgs/outlook-premium-email-box-008.png)

输入邮箱的用户名

![](/imgs/outlook-premium-email-box-009.png)

这样，域名邮箱就完成设置了，和你的 hotmail 邮箱是同一个邮箱。

#### 坑及填坑


- 说这个邮箱是鸡肋是因为它只支持创建一个邮箱，没有别名，要知道它的前身可是可以设置很多别名的。

- 说能最多邀请五个人使用这个域名邮箱，但事实是你需要购买 Office 365 家庭订阅版。

- 我使用 cloudflare 来解析域名 tourcoder.com 的，可换成 Godaddy 的 DNS 解析后，会带来很多不方便，我也不想这么做，最好的解决办法是，先将域名使用 Godaddy 来做解析，在上面流程的所有设置后，进入到 Godaddy 的域名解析处查看域名的具体解析，比如 tourcoder.com 的解析是

    ```
    | cname | autodiscover | autodiscover.outlook.com |
    | cname | _domainconnect | _domainconnect.gd.domaincontrol.com |
    | mx | @ | 110718435.pamx1.hotmail.com (Priority: 0) |
    | txt | @ |	v=spf1 include:outlook.com -all |
    | txt |	_outlook |	110718435 |
    ```

    其中第一、二、三条的解析大家都一样，重点就是这里的数字，我通过新买域名和用当前旧域名均做了测试，发现这里的同一个账户获取到的数字是一样的，这样，只在要 cloudflare 里面按上面的解析做设置即可。
    
- 费用方面，office 365 个人订阅版目前的价格是 69.99 美金/年，而家庭版是 99.99 美金/年，还包含了其他的服务，比如 office 套装和 onedrive 的 1T 容量。

#### 最后的话

本次一共花了 240 元不到，其中接近 180 元是冤枉钱（注册一个新域名和给转以来的域名购买隐私保护），而本订阅我没有买，是送的。