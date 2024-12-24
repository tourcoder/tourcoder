---
title: "Google Cloud VM 中的 OS login"
slug: "os-login-in-google-cloud-vm"
author: "Bin Hua"
date: 2024-12-24T06:29:07Z
tags: ["googlecloud", "oslogin"]
draft: false
---

在 Google Cloud VM 有个不能算是问题的烦人事情 -- OS Login，它会自动的更新用户目录下 `.ssh/authorized_keys` 文件，即便这个文件是用户自己创建的。要解决这个问题有几个办法。

- 禁止 OS login（不建议）

  编辑 vm 的元信息，即点击 vm 的名字进入到详情页面，点击顶部的编辑后，找到元信息项，然后增加一组键值，键为 enable-oslogin，值为 false。如果已经存在 enable-oslogin 则将它的值改成 false 即可。记得重启 vm。

  不建议的原因是，因为它更安全，通过 Google Cloud IAM 控制 SSH 密钥的访问权限，更适合多用户和多实例的场景，还可以避免因手动错误导致的密钥丢失或覆盖。

- 配置 Google Cloud 的 SSH 密钥

  进入到 Google Cloud Compute Engine 的元数据项，在 ssh 密钥标签下增加一个项，将从 `id_rsa.pub` 获取到的内容填写在这里即可。当然如果本地配置了 Google Cloud 的 SDK，也可以通过命令执行

  ```
  gcloud compute os-login ssh-keys add \
    --key-file=id_rsa.pub \
    --project=PROJECT_ID
  ```

其实 OS Login 在众多云服务商处还是蛮广泛使用的，处理方法大差不离。