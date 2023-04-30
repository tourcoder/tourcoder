---
title: "通过 CSS 设置自动暗黑模式"
slug: "set-dark-mode-in-css"
author: "Bin Hua"
date: 2023-04-28T14:21:06Z
tags: ["css", "web", "html"]
draft: false
---

把自己的个人介绍页面设置了下自动暗黑模式，即当白天的时候，页面显示为白色背景，当晚上的时候，页面显示为黑色背景。这样可以让页面更加的舒适，也可以让自己的眼睛更加的舒服。

第一步：先在 `head` 里声明 color-scheme，这个属性是用来声明页面的主题颜色的，有两个值，一个是 `light`，一个是 `dark`，分别代表了浅色主题和深色主题。

```
<meta name="color-scheme" content="light dark">
```

也可以通过 `:root { color-scheme: light dark; }` 在样式表里声明。

第二步：通过 `@media (prefers-color-scheme: dark)` 来实现调用，比如当系统主题为白色的时候是默认的样式，而当系统主题为黑色的时候，就会调用 `@media (prefers-color-scheme: dark)` 里的样式。

```
body {
  background-color: #fff;
}
@media (prefers-color-scheme: dark) {
  body {
    background-color: #000;
  }
}
```

上面表示当白色主题时，页面的背景色是白色，而当黑色主题时，页面的背景色是黑色。其他的设置也按这个操作即可。