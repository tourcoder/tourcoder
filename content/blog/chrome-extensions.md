---
title: "Chrome 插件开发"
slug: "chrome-extensions"
author: "Bin Hua"
lastmod: 2018-03-06 07:31:14
date: 2018-03-06 07:31:14
tags: ["Google", "chrome", "代码示例"]
---

烦透了 Chrome 打开一个新标签时的下面的缩略图，所以就想是不是可以开发一个 Chrome 的插件，说干就干。看了下 Chrome Extensions 的官方开发指南，从文档中可以看出，重点是 `manifest.json` 这个文件

**开发**

manifest.json 这是插件非常重要的文件，关于它的内容，请参看官方文档 [manifest](https://developer.chrome.com/extensions/manifest) 部分。这里我只对部分内容进行说明：

```
{
    //必有项
    "manifest_version": 2,    //manifest 编写规范版本，目前主流 2
    "name": "插件名字",
    "version": "1.0.0", //版本号

    //建议项
    "default_locale": "en",  //编码,
    "description": "",  //插件描述
    "icons": {  //插件图标，PNG 格式
        "16": "icon16.png",
        "48": "icon48.png",
        "128": "icon128.png"
    },

    //只能选一个或都不选
    "browser_action": {},  //图标显示在地址栏外，能在所有页面显示
    "page_action": {},     //图标显示在地址栏里最右边，只在特定页面显示

    //可选
    "author": "",  //作者
    "automation": true,  //自动化
    "background": {   // 可常驻浏览器后台的脚本，可以连接其他页面
        "persistent": false
    },
    "chrome_url_overrides": {    //返回的页面链接，只支持 bookmarks、history、newtab 三个页面
        "bookmarks": "bookmarks.html",
        "history": "history.html",
        "newtab": "newtab.html"
    },
    ... //更多省略
}
```

我只是想弄一个空白页面，所以，我的配置如下：

```
{
  "manifest_version": 2,
  "name": "RCT",
  "description": "remove chrome thumbnails",
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "version": "1.0.0",
  "chrome_url_overrides": {
    "newtab": "tab.html"
  }
}
```

同时在增加一个空白的 tab.html 页面，代码如下

```
<!DOCTYPE html>
<html data-ng-app="mychromeextension" data-ng-csp="">
<head lang="en">
    <meta charset="UTF-8">
    <title>New Tab</title>
</head>
<body>
</body>
</html>
```

放入之前已经做好的 icon，这样一个简单的插件开发完成。

**调试**

查看该插件是否能够正常的运作，在 chrome 的地址栏中输入 chrome://extensions 并回车，即可看到插件列表，勾选页面顶部的开发者模式，点击左侧的载入未打包的插件，即可，如下图

![](/imgs/chromeextensions_01.png)

这样就可以调试所开发好的插件了。

**发布到 Chrome 网上应用店**

点[这里](https://chrome.google.com/webstore/developer/dashboard)登录网上应用商店

![](/imgs/chromeextensions_02.png)

点这里的添加内容，即可进入发布页面

![](/imgs/chromeextensions_03.png)

上传完成后，会进入一个编辑页面，主要是让你填写完整的信息内容，需要注意的是，如果你是要对外公开发布的，是需要一次性交 5 美元的费用。

![](/imgs/chromeextensions_04.png)

预览发布即可。

**Tips**

我们也可以通过 chrome://version 查看本地的个人文件夹位置，然后就可以查看插件的源码了 :)

**参考资料**

[Chrome Extensions 官方开发指南](https://developer.chrome.com/extensions)
