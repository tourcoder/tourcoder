---
title: "A Markdown bug in Jekyll"
slug: a-markdown-bug-in-jekyll
author: Bin Hua
lastmod: 2020-07-18T06:10:24Z
date: 2018-03-06T16:47:00Z
tags: ["bug", "jekyll"]
---

#### reproduce

- Summary

    The strikethrough doesn't work.

- Operating Environment

    GitHub Pages
    
- Reproduce

    - Create a markdown file in folder \_post, such as `2018-03-09-bugs.md`
    
    - Write following text in `2018-03-09-bugs.md` 
    
        ```
        ---
        layout: post
        title: A bug of Jekyll
        ---
        
        - ~~飘啊飘~~
        
        - ~~飘~~
        
        - ~~测试~~
        ```
        

        Review this post, you will see this
        
        ![](/imgs/markdown-error-in-jekyll-01.png)

        The strikethrough doesn't work.

        If I deleted `- ~~飘~~`, works well, if I deleted `- ~~飘啊飘~~` and `- ~~测试~~`, left code like following
        
        ```
        ---
        layout: post
        title: A bug of Jekyll
        ---
        
        - ~~飘~~
        ```

        The strikethrough doesn't work too. I tried more Chinese characters, only this one `飘` can cause this issue. It's so strange.

**Update@2018-03-09 13:29(GMT+8)**

I installed Jekyll at local, and created a new site, and added more text at the bottom in the default markdown(welcome-to-jekyll.markdown) file in `_posts` folder

```
~~should be deleted~~

~~飘~~

~~飘飘~~
```

It's a bug, look at following image

![](/imgs/markdown-error-in-jekyll-02.png)