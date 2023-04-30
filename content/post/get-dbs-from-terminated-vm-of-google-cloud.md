---
title: "一次找回 Google Cloud VM 实例中数据的过程分享"
slug: get-dbs-from-terminated-vm-of-google-cloud
author: "Bin Hua"
lastmod: 2020-08-13 09:30:28
date: 2019-05-21 02:01:23
tags: ["googlecloud", "iterm", "SDK", "vm", "snapshots", "images"]
---

Google Cloud 的 VM 实例在停止后无法再次重启，总是提示

```
Starting VM instance "***" failed. Error: The zone 'projects/***/zones/***' does not have enough resources available to fulfill the request. Try a different zone, or try again later.
```

字面意思就是该区现在没有资源，让转区或者稍后再试。想着要找回 VM 中的数据，而多次尝试启动 VM 总是失败，搜索官方文档找到了这篇[参考文章](https://cloud.google.com/compute/docs/instances/moving-instance-across-zones)，这篇文章说可以将当前实例移动到其他有资源的区，随即按上面的步骤操作。

![](/imgs/get-dbs-from-terminated-vm-of-google-cloud.png)

如果上图，初始化并得到授权

```
./bin/gcloud compute instances list
```

列出当前所有的实例

```
./bin/gcloud compute instances move vm001 \
    --zone sourcezonename --destination-zone targetzonename
```

将实例移动到指定的区去。但此时悲剧发生，系统总是提示错误

```
Moving gce instance vm001...failed.
ERROR: (gcloud.compute.instances.move) Instance cannot be moved while in state: TERMINATED
```

查询后发现原因是该实例没有启动，是关闭状态，处于关闭状态的机器是不能被转移的，同时在查找的过程中，网上给出来的说法就两个字“凉凉”，认为在这个时候基本没有任何办法。

我并不觉得，感觉是没有道理的，忽然想到是否可以通过快照的方式来解决？随即为该实例创建了快照，但后面发现似乎无法将快照内容恢复到一个新的 VM 中。

细想一下，创建实例是基于 image，那么我是否可以将该实例做成 image 呢？果不其然，在 Google cloud 后台是可以基于快照创建 image 的。

就这样，基于之前备份的快照创建新的 image，然后再基于这个新建的 image 创建新的实例，登录该实例会发现所有的数据等都在里面。

最后我必须要要吐槽下，撸羊毛可以，但很多人同时撸多个羊毛，这个就有点恶心了。