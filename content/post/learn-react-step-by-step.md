---
title: "React 学习笔记"
slug: "learn-react-step-by-step"
author: "Bin Hua"
date: 2023-06-25T06:18:06Z
tags: ["react", "前端"]
draft: true
---

一直以来，我在学习一个新的框架或语言的时有个特别的习惯，用这个框架或语言写一个博客系统，这几乎成了我用新技术写东西的 “hello world”，这次学习 react 也不例外。至于 react 是什么，可以看其[官网](https://react.dev/)介绍。

### 学习内容和目的

学习 react 的内容，并用它写一个博客系统。博客的主要内容有：

**前台**

- 文章列表页（首页）

- 文章详情页面

- 访客评论

**后台**

- 登录

- 文章列表

- 文章编辑

- 文章删除

- 登出

### 准备工作

安装好对应的环境，比如 node，npm（yarn），npx，mongodb（本项目所用的数据库）

### 具体步骤

**初始化 blog 应用**

通过 `npx create-react-app blog` 命令初始化创建一个名叫 blog 的 react 应用，执行该命令后，在 loading 一段时间后就会创建这个 blog 应用。其结构如下

![](/imgs/learn-react-step-by-step-001.png)

在 `public` 文件夹下的文件中

- favicon 是个性化图标

- index.html 是应用的主 html 文件

这两个是最主要的，logo192.png logo51.png 和 maifest.json 是 PWA 的文件，robots.txt 是 seo 用到的文件，这几个文件是非必须的。

在 `src` 文件夹下，

- app.js 主组件文件

- index.js 入口文件

- index.css 和 app.css 样式文件，非必须

- logo.svg logo 图片，非必须

- app.test.js 测试文件，非必须

- reportWebVitals.js 性能上报文件，非必须

- setupTests.js 测试文件，非必须

剩下的就是 package.json 和 readme 文件了。非必要的文件是可以删除和调整的，但我不打算现在删除它们，只是在后面根据项目开发情况调整。

**先写 UI 的部分**

根据上面的内容，增加几个页面，在 src 文件下增加一个 pages 文件夹，在里面增加

- HomePage.js 首页

- DetailPage.js 详情页面

- CommentList.js 访客评论列表

- CommentAdd.js 访客评论增加

- LoginPage.js 登录页面
  
- PostListPage.js 后台的文章列表页面

- AddPostPage.js 后台增加文章页面

- EditPostPage.js 后台修改文章的页面

先这样写，然后再考虑将一些内容做成独立的组件。

**首页 HomePage.js**

首页是一个文章的列表，外加一个导航栏，因为文章列表等内容是从数据库中读取，所以这里先不显示其内容，先弄导航栏。导航栏就两个内容，一个标题 blog 和一个链接 login，则 HomePage.js 的代码如下

```
import React from "react";

function HomePage() {
    return (
        <div className="topbar">
            <h1>Blog</h1>
            <a href="/login">Login</a>
        </div>
    );
  }
 export default HomePage;
```

这里的 className 就是我们平时用的 html 中的 class，所有的样式都写入到应用文件的样式文件中，即写入 app.css 中，去掉了里面的内容，增加如下内容

```
.topbar {
    background-color: #fff;
    height: 80px;
}
.topbar h1 {
  float: left;
  width: 20%;
}
.topbar a {
  float: right;
  padding: 30px;
}
```

这是顶部导航的内容，但如果在下面继续写博客内容的列表，比如

```
import React from "react";

function HomePage() {
    return (
        <div className="topbar">
            <h1>Blog</h1>
            <a href="/login">Login</a>
        </div>
        <ul className="post-list">
            <li><a href="/detail">Title</a></li>
            <li><a href="/detail">Title</a></li>
            <li><a href="/detail">Title</a></li>
        </ul>
    );
  }
 export default HomePage;
```

这样写就会出错，因为 react 要求每个组件 HTML 的最外层必须是由一个标签包裹，且不能存在并列的标签。这里的处理办法有两个，要么在外面再嵌套一层 div，要么按它的提示，在外面增加一个 Fragment。即增加后的完整代码是

```
import React from "react";
import { Fragment } from "react";

function HomePage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/login">Login</a>
            </div>
            <ul className="post-list">
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
            </ul>
        </Fragment>
    );
  }
  
  export default HomePage;
```

选择增加 Fragment，而不是 div 的原因是 fragment 最后不会出现的 html 页面中，而 div 会。此时更改 app.js 的内容，将首页组件的内容引入进来，即将 app.js 改成

```
import './App.css';
import HomePage from './pages/HomePage';

function App() {
  return (
    <div className="App">
      <HomePage />
    </div>
  );
}

export default App;
```

执行 `npm start` 就可显示出首页。

**详情页面 detail.js**

详情页面和首页差不多，不同的是，详情页面下面是整片文章的内容，代码如下

```
import React from "react";
import { Fragment } from "react";

function DetailPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/login">Login</a>
            </div>
            <div className="post-detail">
                <h2>Title</h2>
                <p>Content</p>
            </div>
        </Fragment>
    );
}

export default DetailPage;
```

要在 app.js 里和 homepage 一样直接引用，但这个是错误的，我是需要通过点击首页的列表的链接跳转到详情页面的，所以需要引入路由，即

```
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
```

将 app.js 的代码改成

```
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

此时，首页出现列表，点击列表的内容即可出现详情页面。

**登录页面 login.js**

和其他页面差不多，登录页面的代码如下

```
import React from "react";
import { Fragment } from "react";

function LoginPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/">Home</a>
            </div>
            <div className="login">
                <h2>Login</h2>
                <form>
                    <input type="text" placeholder="Username" /><br /><br />
                    <input type="password" placeholder="Password" /><br /><br />
                    <button type="submit">Login</button>
                </form>
            </div>
        </Fragment>
    );
}

export default LoginPage;
```

同样需要在 app.js 中引入，并修改 app.js 代码

```
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

