---
title: "如何在 hugo 中集成 mermaid"
slug: "how-to-integrate-mermaid-in-hugo"
author: "Bin Hua"
date: 2023-03-09T10:10:41Z
tags: ["hugo", "mermaid"]
draft: false
---

[Mermaid](http://mermaid.js.org/) 是一个能通过 markdown 画流程图，甘特图等图表的库，我很喜欢。今天尝试将它集成到 hugo 的系统里。

- 在主题中引入 mermaid 的库文件，比如在 `footer.html` 文件中引入该库文件

    ```
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.4.3/mermaid.min.js"></script>
    ```

- 利用 hugo 中的 `shortcodes` 来实现对 mermaid 的载入，在 `shortcodes` 里创建 `mermaid.html`，并将下面的代码输入进去

    ```
    <div class="mermaid"> 
        {{ safeHTML .Inner }}
    </div>
    ```

- 最后看效果，比如

    {{<mermaid>}}
    graph LR
    A(Hello)-->B(One)
    A-->C(Two)
    {{</mermaid>}}

    这个流程的写法是

    ```
    graph LR
    A(Hello)-->B(One)
    A-->C(Two)
    ```

    当然需要用 `<mermaid>` 和 `</mermaid>` 将上面代码包含在里面。

至于 mermaid 还有哪些用法，去其官网看吧。

- 官网地址：[https://mermaid.js.org](https://mermaid.js.org)