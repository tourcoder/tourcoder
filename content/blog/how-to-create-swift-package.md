---
title: "体验 Swift Package 的开发并发布的流程"
slug: "how-to-create-swift-package"
author: "Bin Hua"
date: 2024-05-07T01:54:59Z
tags: ["ios", "macos", "swift", "package", "howto"]
draft: false
---

五一期间在更新一个 cocos2d-iphone 的游戏时发现很多包是通过 cocoapods 管理的，心血来潮就想试试 swift package，遂记录一下折腾的过程。

### 开发包

#### 创建

创建包的方式有两种，一种是直接通过 Xcode 来创建，也可以通过命令行来创建，两者大差不离。我自然选择的是命令行方式创建。

- 创建文件夹并进入 `mkdir projectname && cd $_`，需要注意这里的文件夹名就是包的名字。

- 在终端里输入 `swift package init`，即可获得一个完整的包的必要内容，其结构如下

  ```
  .
  ├── Package.swift
  ├── Sources
  │   └── InformationCheck
  │       └── InformationCheck.swift
  └── Tests
      └── InformationCheckTests
          └── InformationCheckTests.swift
  ```

  注解

  Package.swift：这是 Swift Package Manager（SPM）所需的清单文件，它描述了包的元数据，包括名称、版本、依赖关系等。可以在这个文件中指定包含在包中的源文件和目录，还有包的各种配置选项。

  Sources/InformationCheck/InformationCheck.swift：这是包的源代码文件。通常包含一个或多个源码文件。

  Tests/InformationCheckTests/InformationCheckTests.swift：这是用于测试软件包中的代码的测试文件，用于测试InformationCheck模块中的代码。

- 在根目录下增加 `README.md` 文件，用来解释这个包的信息，比如介绍说明，使用方法等。

至此，一个包就创建完成了。

#### 编码

主要的代码都在 Sources 这个文件夹里进行，可以有一个或者多个源码文件。需要注意的是随着源码内容的不同，在 Package.swift 里应该有对应的配置修改。关于这个文件的配置，可以翻阅[官方文档](https://developer.apple.com/documentation/packagedescription/package)。

#### 测试

测试的方式也比较简单，直接执行命令 `swift test` 即可。

### 发布包

发布的方式和 cocoapods 大差不离，为了更好的组织和维护，建议通过打 tag 来管理。我的想法是既然开源了，直接把代码丢到 GitHub 上就行了，未通过 `swift build` 来做编译。我的操作是

```
git tag -a 0.0.1 -m 'version 0.0.1'
git push origin 0.0.1
```

也可以发布一个二进制文件，[官方文档](https://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages)也有对应的说明。

### 使用包

当需要用到一个包的时候，比如这里的 InformationCheck，直接在 Xcode 中的 Package Dependencies 输入这个包的源码地址即可，在引入时记得锁版本（这也是打 tag 管理的好处）。

然后在需要用的地方 import 包。

### 源码

本篇博文所牵涉到的源码和演示

包的代码：[tourcoder/InformationCheck](https://github.com/tourcoder/InformationCheck)

演示：[tourcoder/swiftpackagedemo](https://github.com/tourcoder/swiftpackagedemo)

### 其它

推荐 Swift 包索引的网站 [https://swiftpackageindex.com/](https://swiftpackageindex.com/)。