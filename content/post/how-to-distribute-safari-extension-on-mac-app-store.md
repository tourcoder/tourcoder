---
title: "如何在 Mac App Store 里发布一个 Safari 扩展"
slug: "how-to-distribute-safari-extension-on-mac-app-store"
author: "Bin Hua"
lastmod: 2021-11-16T17:43:47Z
date: 2021-11-16T17:43:47Z
tags: ["Safari", "extension", "Apple", "AppStore"]
---

成功在 Mac App Store 上上架了一个 Safari 插件，整个过程资料缺失的是发布过程，连 Apple 官方都没有详细的说明，特分享一下我的发布过程。

### 创建应用

因为是在 macOS 上的应用，所以选择的是 `macOS -> Safari Extension App`

![](/imgs/how-to-distribute-safari-extension-on-mac-app-store-001.jpg)


### Certificates

需要创建两个 Certificates，一个是 Mac App Distribution，另外一个是 Mac Installer Distribution

### Identifiers

需要创建两个 Identifiers，一个是 `com.name.your_app_name`，另外一个是 `com.name.your_app_name.Extension`

### Provisioning Profiles

需要创建两个 Provisioning Profiles，一个是为 `com.name.your_app_name` 创建，另外一个是为 `com.name.your_app_name.Extension` 创建。

### 在 Xcode 中配置

![](/imgs/how-to-distribute-safari-extension-on-mac-app-store-002.jpg)

![](/imgs/how-to-distribute-safari-extension-on-mac-app-store-003.jpg)

如上图所示，在 `target` 中，为 app 和 extension 选择对应的 Identifier 和 Provisioning Profile。

最后打包提交到 AppStore 即可。至于开发过程和日常开发 macOS 上的应用一样，没有什么特别。
