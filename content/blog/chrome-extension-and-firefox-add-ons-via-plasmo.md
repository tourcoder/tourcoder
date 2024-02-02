---
title: "用 Plasmo 开发 Chrome 和 Firefox 扩展的一点分享"
slug: "chrome-extension-and-firefox-add-ons-via-plasmo"
author: "Bin Hua"
date: 2024-02-01T08:20:49Z
tags: ["chrome", "firefox", "react", "plasmo"]
draft: false
---

用 [Plasmo](https://www.plasmo.com/) 开发了个 Chrome 的扩展，还蛮简单方便的，至于如何开发，请去看[官方文档](https://docs.plasmo.com/)。

在开发完成后，有几个注意点

1. 与 Chrome 不同，Firefox 需要在 `manifest.json` 文件里增加一条属性 `browser_specific_settings`，格式如下

    ```
    "browser_specific_settings": {
        "gecko": {
            "id": ""
        }
    }
    ```

    这里的 id 的要求是
    
    ```
    must match pattern "^\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}$"
    must match pattern "^[a-zA-Z0-9-._]*@[a-zA-Z0-9-._]+$"
    ```
    
    参考 email 地址，不过要注意这个是提交后无法修改的，不要写成 email 地址，虽然 Firefox 官方文档是写成 email 地址。如果不设置这个 `browser_specific_settings`，在上传到 Firefox 的时候会报错。

2. 也不要在项目源文件里直接增加上面的 `browser_specific_settings` 属性，因为这个属性会导致 Chrome 那边也报错。所以这个简单的处理办法是直接在编译完成的 `manifest.json` 里写就行了。