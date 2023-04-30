---
title: "开发 Alfred 的 Workflow"
slug: "make-a-workflow-for-alfred"
author: "Bin Hua"
lastmod: 2020-08-13 09:38:31
date: 2019-10-11 13:49:58
tags: ["workflow", "alfred"]
---

我在以前的博文中写过 Alfred 这一个神器，它是我必用的应用之一，购买它的许可后，就能够使用 workflow，绝对的效率神器。

恰好最近在做开发的时候，需要访问不同端口的 localhost，索性就开发了个 workflow，方便打开不同端口的 localhost。效果如下

![](/imgs/make-a-workflow-for-alfred-07.png)

输入 `qp`，空格，再输入端口，回车即可调用默认浏览器访问对应端口的 localhost。

开发这个 `Workflow` 的过程非常简单，基本没有写代码的过程。

1. 进入到 `Alfred` 中 `Workflow` 选项，点击底部 `help` 旁边的加号，选择 `Blank Workflow`

    ![](/imgs/make-a-workflow-for-alfred-01.png)
    
    填写对应的内容，保存。
    
2. 点击左侧刚才保存的 Workflow，在右侧工作区的空白处点击右键

    ![](/imgs/make-a-workflow-for-alfred-02.png)
    
    选择 `Inputs->Keyword` 
    
3. 在弹出的窗口中填写对应的内容

    ![](/imgs/make-a-workflow-for-alfred-03.png)
    
    keyword 即是呼起功能的关键词，输入说明，然后保存。
    
4. 再在工作区空白处点击右键

    ![](/imgs/make-a-workflow-for-alfred-04.png)
    
    选择 `Actions->Open URL`
    
5. 同样在弹出的窗口中填写对应的内容

    ![](/imgs/make-a-workflow-for-alfred-05.png)
    
    这里的 `{query}` 即是输入的内容，下面选择默认浏览器，然后保存。
    
6. 最后用一根线将两个链接起来即可。

    ![](/imgs/make-a-workflow-for-alfred-06.png)
    
这个 workflow 就开发完成了，如果想要给别人使用，只要点工作区右上角的分享按钮即可。

其实这个 workflow 也不算是开发，想要学习更为复杂的，可以看官方的[文档](https://www.alfredapp.com/help/workflows/)。