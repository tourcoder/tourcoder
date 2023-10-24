---
title: "webpack 学习笔记"
slug: "webpack-manual"
author: "Bin Hua"
lastmod: 2019-01-22 06:00:55
date: 2019-01-22 06:00:55
tags: ["nodejs", "webpack", "npm"]
---

越来越多的 module 被放到了 npmjs.org 上，甚至一些 css 框架都被放在了上面，我本身认为 npmjs 上只是放 M 和 V 的东西，没想到 C 的东西也放在了上面。对 css 内容的调用，除了最直接的

```
<link rel="stylesheet" href="node_modules/module_name/module.css">
```

调用方式外，还有一种方式就是 webpack 打包。

新建一个文件夹，比如 temp，进入该文件夹，并初始化

```
cd temp
npm init
```

在一顿回车后，该文件夹下会自动生成一个 package.json 的文件，执行命令

```
npm install --save-dev webpack
```

安装 webpack，此时 package.json 中也发生了变化。

```
{
  "name": "temp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "webpack": "^4.29.0"
  }
}
```

在当前文件夹下新建两个文件夹

- src

    源码文件夹，保存模块，数据等源码

- dist

    发布文件夹，保存主访问文件 index.html 以及 webpack 生成文件
    
在 src 中增加 index.js 和 pg.js 文件，代码如下

index.js
    
    const pg = require('./pg.js');
    document.querySelector("body").appendChild(pg());
    
pg.js
    
    module.exports = function() {
        var pg = document.createElement('div');
        pg.textContent = "Hello world";
        return pg;
    };
  
在 dist 中编辑主访问文件 index.html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Hello World</title>
      </head>
      <body>
        <script src="webpack.js"></script>
      </body>
    </html>
    
这里 webpack.js 文件是打包后的文件，然后执行打包命令进行打包

    node_modules/.bin/webpack src/index.js --output dist/webpack.js --mode development
    
![](/imgs/webpack-manual-01.png)
    
运行后即在 dist 文件夹下看到多了一个 webpack.js 的文件，用浏览器访问 index.html 文件，即可看到
    
![](/imgs/webpack-manual-02.png)
    
到此，一个简单的利用 webpack 打包的流程就完成了，更多关于 webpack 的高级玩法，可以去下面查看

- Webpack 官网：[https://webpack.js.org/](https://webpack.js.org/)

- Webpack@GitHub：[https://github.com/webpack](https://github.com/webpack)