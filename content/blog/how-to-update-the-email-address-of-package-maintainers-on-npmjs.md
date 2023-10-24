---
title: "更新 NPMJS 中维护人员的 email 地址"
slug: "how-to-update-the-email-address-of-package-maintainers-on-npmjs"
author: "Bin Hua"
lastmod: 2019-12-17 07:20:04
date: 2019-12-17 07:20:04
tags: ["npm", "npmjs"]
---

做过 NPMJS 包的人都知道，通过命令 `npm info 包名字` 可以查看到维护人员的 Email 地址，如下图中红色标注出来的

![](/imgs/how-to-update-the-email-address-of-package-maintainers-on-npmjs-000.png)

但有时候遇到一个问题是想更改这里的 Email 地址，在官网找到相关资料，有小伙伴和我说唯一的办法是删除掉这个包，然后用新的 Email 地址重新上传。再和 NPMJS 官方多次联系后，我基本确认两个事情

1. 官方是不会轻易的删除已经发布的包的，尤其是已经有很多人使用的包

2. 没有办法修改已经发布的包的维护人的 Email 地址

但真的是这样吗？在一些摸索后，倒是找到了一个靠谱的办法，算是他们的漏洞，将流程分享出来

第一步，先登录 NPMJS.COM 的账号，将里面的 Email 地址改成想显示出来的 Email 地址。

第二步，登录命令行工具，运行命令 `npm login` 登录 NPMJS 的账号，这里需要注意，使用的源应该是官方的源，而非第三方的源，记得先修改下源。

第三步，登录后，运行命令 `npm owner add tourcoder 包名字`，比如我这里执行 `npm owner add tourcoder a-yarn-demo`，会出现增加成功的提示，如下图

![](/imgs/how-to-update-the-email-address-of-package-maintainers-on-npmjs-002.png)

第四步，等待一两分钟，执行命令 `npm owner rm tourcoder 包名字`，完成，这时会发现维护人的 Email 地址更新好了。

![](/imgs/how-to-update-the-email-address-of-package-maintainers-on-npmjs-003.png)

这个所谓的漏洞可能是一个设计的“缺陷”，NPM 应该在执行一些命令，比如所有者命令时，会做账户刷新校验，然后根据数据进行了更新。

话说这个操作让我忽悠了一小伙伴的十元红包，哈哈哈哈