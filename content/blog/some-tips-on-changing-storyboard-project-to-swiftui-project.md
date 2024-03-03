---
title: "Storyboard 项目改成 SwiftUI 项目的几个设置"
slug: "some-tips-on-changing-storyboard-project-to-swiftui-project"
author: "Bin Hua"
date: 2024-03-02T10:22:59Z
tags: ["iOS", "macOS", "Swift", "SwiftUI", "Storyboard"]
draft: false
---

在创建一个 iOS 的 app 时没注意选项，误将 SwiftUI 框架选成了 Storyboard，没重新创建，直接做了更改，记录下更改的内容

- 删除所有的除了 `Assets` 和 `Info.plist` 的文件

- 创建入口文件，比如 `AppNameApp`，其代码如下

    ```
    import SwiftUI

    @main
    struct AppNameApp: App {
            var body: some Scene {
                
            }
    }
    ```

- 设置 `Info.plist` 文件

    将 `Delegate Class Name` 里面的内容改成 `$(PRODUCT_MODULE_NAME).AppNameApp`，并删除 `UISceneStoryboardFile` 和其值 `Main`，大致的代码如下

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    <key>UIApplicationSceneManifest</key>
    <dict>
        <key>UIApplicationSupportsMultipleScenes</key>
        <false/>
        <key>UISceneConfigurations</key>
        <dict>
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
            <key>UISceneConfigurationName</key>
            <string>Default Configuration</string>
            <key>UISceneDelegateClassName</key>
            <string>$(PRODUCT_MODULE_NAME).AppNameApp</string>
            </dict>
        </array>
        </dict>
    </dict>
    </dict>
    </plist>
    ```

- 设置 `TARGETS`

    将 `Build Settings` 中 `UIKit Main Storyboard File Base Name` 值删除

已经将一个 Storyboard 项目改成了 SwiftUI 项目。

有时候会遇到需要清理模拟器才行，遇到强制清理不行，建议重新构建模拟器，

```
gem install snapshot
fastlane snapshot reset_simulators
```