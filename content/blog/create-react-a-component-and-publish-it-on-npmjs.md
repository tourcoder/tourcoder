---
title: "创建 React 组件并发布到 npm，附一些问题解决"
slug: "create-react-a-component-and-publish-it-on-npmjs"
author: "Bin Hua"
date: 2024-02-06T15:15:20+08:00
tags: ["react", "npm", "yed", "sass", "node-sass"]
draft: false
---

最近在写一个 React 的项目，也产生了一些组件。特意弄了一个网站 [yeci.org](https://yeci.org)，会逐步将这些组件放在这个网站上。

回到正题，写篇博文记录下如何创建一个 React 组件并将它发布到 npmjs。

**技术栈**

- React

- Webpack

- Sass

- Babel

### 创建组件

- 创建文件夹，并进入

```
mkdir Realert && cd $_
```

- 初始化

```
npm init
```

- 安装 React 和 React-dom，组件依赖

```
npm i react react-dom -D
```

- 安装其它构建依赖
 
```
npm i webpack webpack-cli webpack-dev-server html-webpack-plugin style-loader css-loader sass-loader node-sass @babel/core @babel/cli babel-loader @babel/preset-env @babel/preset-react -D
```

下面是依赖的说明

Babel: 用来编译

Webpack: 构建

Webpack-dev-server: 本地开发服务器

style-loader: 从 js 字符串创建 style 标签及内容 <style>...</style>
 
css-loader: 将 css 转化成 CommonJS
 
sass-loader: 将 sass 编译成 css，可选
 
node-sass/sass: 可选


- 在 package.json 中增加 `"start": "webpack-dev-server --mode development"` 来启动本地开发服务器

```
{
  "name": "component-name",
  ...
  "scripts": {
    "test": "...",
    "start": "webpack-dev-server --mode development"
  }
}
```

- 配置 webpack.config.js 和 .babelrc

 根目录下创建 webpack.config.js

 ```
  const path = require('path');
  const HtmlWebpackPlugin = require("html-webpack-plugin");
  const htmlWebpackPlugin = new HtmlWebpackPlugin({
   template: path.join(__dirname, "demo/index.html"),
   filename: "./index.html"
  });
  module.exports = {
   entry: path.join(__dirname, "demo/index.js"),
   module: {
     rules: [{
       test: /\.(js|jsx)$/,
     use: "babel-loader",
     exclude: /node_modules/
   },{
     test: /\.scss$/, /**如果不用 sass，则 .css$**/
     use: ["style-loader", "css-loader", "sass-loader"] /**sass-loader 根据前面可选**/
   }]
  },
   plugins: [htmlWebpackPlugin],
   resolve: {
     extensions: [".js", ".jsx"]
   },
   devServer: {
     port: 8008
  }};
 ```

 同样根目录下创建文件 .babelrc，基础的通用配置

 ```
 {
  "presets": ["@babel/preset-env", "@babel/preset-react"]
 }
 ```

- 现在来写这个组件

在根目录下创建 src 目录，并在 src 目录下，创建两个文件 index.js 和 index.scss

index.js 的代码如下

```
import React from 'react';
import './index.scss'

const Alert = () => {
  return (
    <div>
      <h1>Hello World</h1>
      <p>React + Sass</p>
    </div>
  )
}
export default Alert;
```

index.scss 的代码


```
div {
  h1 {
    font-size: 18px;
    color: #0f0;
  }

  p {
    font-size: 16px;
    color: #00f;
  }
}
```

就写一个 Hello World 吧。

- 调试组件

在根目录下创建 demo 文件夹，并在 demo 目录下创建 index.html 和 index.js 文件

index.html 的代码


```
<html>
<head>
 <title>Demo</title>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
</head>
<body>
 <noscript>
 You need to enable JavaScript to run this app.
 </noscript>
 <div id="root"></div>
</body>
</html>
```

index.js 的代码


```
import React from 'react';
import ReactDOM from 'react-dom/client';
import Component from '../src';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Component />
  </React.StrictMode>
);
```


执行 npm start 即可看到演示。

### 发布到 npm

- 添加 transpile 用来在 babel 编译时拷贝静态文件到打包的目录下

修改 package.json

```
{
  "name": "component-name",
  ...
  "scripts": {
    "test": "...",
    "start": "webpack-dev-server -mode development",
    "transpile": "babel src -d dist --copy-files"
  }
}
```

执行打包 `npm run transpile`，此时会生成一个 dist 文件夹，里面就是代码文件了。最后检查后就可以 `npm publish` 到 npmjs。

### 一些注意点

- 需要告知入口的位置，比如这里打包后，入口位置是在 dist/index.js，应该将 package.json 里面的 `main / module` 的值改成 `dist/index.js`，切记！

- 用 prepublishOnly 来自动执行前置过程，比如 npm publish 发布前，让其执行 transpile 的过程

```
{
  "name": "component-name",
  ...
  "scripts": {
    "test": "...",
    "start": "webpack-dev-server -mode development",
    "transpile": "babel src -d dist --copy-files",
    "prepublishOnly": "npm run transpile"
  }
}
```

- 在 package.json 中增加 peerDependency 告知用户一些要求，比如

```
peerDependencies": {
   "react": "^18.2.0",
   "react-dom": "^18.2.0"
}
```

- 增加 .npmignore 文件忽略一些内容

```
src/
demo/
.babelrc
.gitignore
webpack.config.js
```

- Requires Babel "^7.0.0-0", but was loaded with "6.26.3" 的问题

检查你的 babel-cli 等是不是 @babel 开头的。如果是，就改变全局的 babel 版本，如果不是，安装 @babel/cli 之类的包。

- sass 引入后打包是个巨坑，慎用。

本博文牵涉到的代码在 [GitHub](https://github.com/tourcoder/tcdemo_react_component_sass)，组件在 [npmjs](https://www.npmjs.com/package/tcdemo_react_component)