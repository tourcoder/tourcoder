---
title: "通过 Highlightr 在 Swift 中实现代码高亮"
slug: highlight-codes-via-highlightr-in-swift
author: Bin Hua
lastmod: 2019-09-23 07:11:10
date: 2019-09-23 07:11:10
tags: ["iOS", "App", "swift", "highlightr"]
---

前些天在一款应用中需要对代码进行高亮显示，用到了 `Highlightr` 这个第三方库，这个类库搜使用的核心库是 [highlight.js](https://highlightjs.org/)。

#### 实验环境

- iOS

- 类库地址：[https://github.com/raspu/Highlightr](https://github.com/raspu/Highlightr)

#### 操作步骤

在 `Highlightr` 官方库的说明文档中已经写得很清楚，先安装后使用。

- 安装

    简便的安装方式有两种，即 CocoaPods 和 Carthage，我习惯了 CocoaPods，就直接用它了。将 Highlightr 添加到 podfile 
    
    ```
    pod 'Highlightr'
    ```
    
    执行安装
    
    ```
    pod install
    ```
    
    安装完成后打开项目的 `xcworkspace` 文件。
    
- 使用

    我使用的是 `UITextView` 来接受文字内容，部分代码如下
    
    ```
    lazy var tvContent:(UITextView) = {
		let textView = UITextView(frame: CGRect(x: 0, y: 0, width: self.view.frame.size.width, height: self.view.frame.size.height))
		return textView
	}()
    let highlightr = Highlightr()
    func initUI() {
		self.view.addSubview(tvContent)
		let code = "code content"
		self.tvContent.attributedText = self.highlightr?.highlight(code!)
	}
    ```
    
    注意点，`UITextView` 这里用 `attributedText` 来接受内容，不能用 `text`，用 `text` 来接受内容会出现截断的情况。
    
    `Highlightr` 还可以实时进行代码高亮，官方的示例代码如下
    
    ```
    let textStorage = CodeAttributedString()
	textStorage.language = "Swift"
	let layoutManager = NSLayoutManager()
	textStorage.addLayoutManager(layoutManager)
	let textContainer = NSTextContainer(size: view.bounds.size)
	layoutManager.addTextContainer(textContainer)

	let textView = UITextView(frame: yourFrame, textContainer: textContainer)
    ```
    
    除此之外，它还可以更改显示的风格 (Themes)，显示的开发语言。
    
挺好的一个库，值得一用。