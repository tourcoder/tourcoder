---
title: "Jekyll 结构的不合理"
slug: "unreasonable-in-jekyll"
author: "Bin Hua"
date: 2018-03-05 07:30:25
tags: ["bug", "GitHub", "jekyll"]
draft: false
---

过年期间，图省事将博客放到了 GitHub Pages，结合 Jekyll，省事多了。

因为我写文章，喜欢贴一些插图，在这过程过觉得 Jekyll 的结构设计有点不够合理。

当前 Jekyll 的基本结构如下

```
.
├── _config.yml
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   ├── page.html
|   └── post.html
├── _posts
|   ├── 2018-03-05-hello.md
|   └── 2018-03-06-hi.md
├── atom.xml
└── index.html
```

如果是纯文字情况下，这样的结构设计没有问题，但如果文章中包含图片，为了方便的引入图片，则上面的结构中增加内容

```
.
├── _config.yml
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   ├── page.html
|   └── post.html
├── _posts
|   ├── 2018-03-05-hello.md
|   └── 2018-03-06-hi.md
├── images
|   ├── img1.png
|   ├── img2.png
|   └── img3.png
├── atom.xml
└── index.html
```

增加了 images 这个文件夹，其实这种设计是不合理的。本着同性同管理的原则，这里的同性同管理的说法是我临时给的词，大概意思就是同种性能功能的内容应该在一处甚至一个文件夹里管理。在这里， markdown 文件（文字）和图片应该属于内容，即数据部分，应该是在同一个文件夹下，然后再按着同性同管理的原则把图片和 markdown 文件分开，所以，上面的结构应该改成

```
.
├── _config.yml
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   ├── page.html
|   └── post.html
├── _blogdata
|   ├── posts
|   |   ├── 2018-03-05-hello.md
|   |   └── 2018-03-06-hi.md
|   └── images
|       ├── img1.png
|       ├── img2.png
|       └── img3.png
├── atom.xml
└── index.html
```


虽然不完美，但清晰很多。

**Tips:**

- 设置短名称

    Jekyll 的 url 地址默认格式是 tourcoder.com/year/month/day/post-name.html，可以通过下面的方式设置成短名称，在 \_config.yml 中增加
    
    ```
    permalink: none
    ```

    这样就去掉了日期格式，但是在页面的结尾会有 .html
    
    ```
    permalink: "/:title"
    ```
    
    这样就完美的去掉了 .html，但是还是会有一定的问题，比如存档，但我的博客没有设置存档，哈哈哈哈