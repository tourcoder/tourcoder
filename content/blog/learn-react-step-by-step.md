---
title: "React 学习笔记"
slug: "learn-react-step-by-step"
author: "Bin Hua"
date: 2023-06-25T06:18:06Z
tags: ["react", "前端"]
draft: false
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

### 初始化

**初始化 blog 应用**

通过 `npx create-react-app blog` 命令初始化创建一个名叫 blog 的 react 应用，执行该命令后，在 loading 一段时间后就会创建这个 blog 应用。其结构如下

![](https://storage.tourcoder.com/tcblog/learn-react-step-by-step-001.png)

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

### 先写 UI 的部分

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

这里的 className 就是我们平时用的 html 中的 class，所有的样式都写入到应用文件的样式文件中，即写入 app.css 中，但并不建议这么做。这样写在团队合作的时候会不方便，会有很多问题，在后面写样式时，会有专门讲这块内容。这里就是删除 app.css 文件，并在 app.js 文件中删除对应的引用。

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

**详情页面 DetailPage.js**

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

**评论列表页面 CommentList.js**

评论列表的内容也是从数据库中读取的，结构代码如下

```
import React from "react";
import { Fragment } from "react";

function CommentList() {
    return (
        <Fragment>
            <div className="comment-list">
                <h2>Comments</h2>
                <ul>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                </ul>
            </div>
        </Fragment>
    );
}

export default CommentList;
```

评论内容是在页面详情的下面，其实可以是一个组件，然后引入到页面详情里

```
import React from "react";
import { Fragment } from "react";
import CommentList from "./CommentList";
import CommentAdd from "./CommentAdd";

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
            <CommentAdd />
            <CommentList />
        </Fragment>
    );
}

export default DetailPage;
```

**评论增加 CommentAdd.js**

评论是开放式的，无需登录，则代码如下

```
import React from "react";
import { Fragment } from "react";

function CommentAdd() {
    return (
        <Fragment>
            <div className="comment-add">
                <h2>Leave your comment</h2>
                <form>
                    <input type="text" placeholder="Name" />
                    <textarea placeholder="Comment"></textarea>
                    <button type="submit">Add Comment</button>
                </form>
            </div>
        </Fragment>
    );
}

export default CommentAdd;
```

和评论列表一样，也应该将它引入到详情页面，继续修改详情页面的内容

```
import React from "react";
import { Fragment } from "react";
import CommentList from "./CommentList";
import CommentAdd from "./CommentAdd";

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
            <CommentAdd />
            <CommentList />
        </Fragment>
    );
}

export default DetailPage;
```

**登录页面 LoginPage.js**

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
                    <input type="text" placeholder="Username" />
                    <input type="password" placeholder="Password" />
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

到此，前台部分的页面都串联起来了，只写了个基本的样式，具体的样式美化等放到后面再做。

**后台帖子列表页面 PostListPage.js**

后台的内容都是需要用户登录后才可以访问的，目前先不做认证，只是先把页面写出来，并完成跳转逻辑，点击帖子的标题跳转到帖子编辑页面

```
import React from "react";
import { Fragment } from "react";

function PostListPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/logout">Logout</a>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
            </div>
            <ul className="post-list">
                <li><a href="/post_edit">Title</a></li>
                <li><a href="/post_edit">Title</a></li>
                <li><a href="/post_edit">Title</a></li>
            </ul>
        </Fragment>
    );
}

export default PostListPage;
```

同样，在 app.js 中增加对应的路由

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/posts" element={<PostListPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

**后台帖子增加页面 PostAddPage.js**

同样，增加帖子的页面也是需要登录后才可以的，目前还是不做这个处理

```
import React from "react";
import { Fragment } from "react";

function PostAddPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/logout">Logout</a>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
            </div>
            <div className="post-add">
                <h2>Add Post</h2>
                <form>
                    <label htmlFor="title">Title</label>
                    <input type="text" id="title" name="title" />
                    <label htmlFor="content">Content</label>
                    <textarea id="content" name="content"></textarea>
                    <input type="submit" value="Add Post" />
                </form>
            </div>
        </Fragment>
    );
}

export default PostAddPage;
```

在 app.js 中也需要增加对应的路由内容

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';
import PostAddPage from './pages/PostAddPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/posts" element={<PostListPage />} />
          <Route path="/post_add" element={<PostAddPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

**后台帖子修改页面 PostEditPage.js**

修改帖子和增加帖子差不多，不同的是修改贴子默认显示了该贴的内容，代码如下

```
import React from "react";
import { Fragment } from "react";

function PostEditPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/logout">Logout</a>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
            </div>
            <div className="post-edit">
                <h2>Edit Post</h2>
                <form>
                    <input type="text" placeholder="Title" />
                    <textarea placeholder="Content"></textarea>
                    <button type="submit">Update</button>
                </form>
            </div>
        </Fragment>
    );
}

export default PostEditPage;
```

在 app.js 中依旧需要引入对应的路由

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';
import PostAddPage from './pages/PostAddPage';
import PostEditPage from './pages/PostEditPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/posts" element={<PostListPage />} />
          <Route path="/post_add" element={<PostAddPage />} />
          <Route path="/post_edit" element={<PostEditPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

**后台评论的管理 PostComment.js**

图省事，将后台评论的管理写成一个组件，放在帖子编辑下面，代码如下

```
import React from "react";
import { Fragment } from "react";

function PostComments () {
    return (
        <Fragment>
            <div className="comment-list">
                <h2>Comments</h2>
                <ul>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                </ul>
            </div>
        </Fragment>
    );
}

export default PostComments;
```

同样需要在帖子编辑页面引入该组件

```
import React from "react";
import { Fragment } from "react";
import PostComments from "./PostComment";

function PostEditPage() {
    return (
        <Fragment>
            <div className="topbar">
                <h1>Blog</h1>
                <a href="/logout">Logout</a>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
            </div>
            <div className="post-edit">
                <h2>Edit Post</h2>
                <form>
                    <input type="text" placeholder="Title" />
                    <textarea placeholder="Content"></textarea>
                    <button type="submit">Update</button>
                </form>
            </div>
            <PostComments />
        </Fragment>
    );
}

export default PostEditPage;
```

到这里，一个基础博客的页面的框架都写完了。

### 样式的调整

在写上面的 UI  框架时，我只写了个简单样式，在 react 中引入样式的方式有很多种，比如在全局中直接写样式，即在 index.html 中直接引入一个全局的样子，或者将样式写入到 app.css 中， 但这样写有个问题，会彼此收到影响，也不方便团队的合作。而內联的模式，比如下面这段代码

```
import React from 'react';

function MyComponent() {
  const style = {
    color: 'blue',
  };

  return <div style={style}>Hello, World!</div>;
}
```

看似不错，但会给组件带来大量的代码，存在同样问题的还有像 styled-components 和 emotion 这样的 CSS-in-JS 库。我用样式模块的方式单独写，然后引入到组件中。

拿首页 homepage.js 来说，新建一个 homepage.module.css 的样式模块文件，将首页的样式写入到里面，然后引入到 homepage.js 里。但如果这样写的话，又会产生另外一个问题，pages 文件夹下面的文件会越来越多，那么为了项目容易看，可以每个组件变成一个文件夹，这个文件夹里面包含了 index.js 的组件文件和组件的样式文件，当然也可以扩展增加其他的东西，比如图片。 homepage.js 就可以改成 homepage 文件夹下包含 index.js 文件和 homepage.module.css，即

homepage.module.css 文件内容

```
.topbar {
  background-color: #fff;
  height: 80px;
  width: 960px;
  margin: 8px auto;
  display: flex;
}
.topbar h1 {
  font-size: 30px;
  font-weight: 700;
  color: #333;
  margin: 0;
  line-height: 80px;
  flex: 1;
}
.topbar a {
  line-height: 80px;
}
.postlist {
  width: 960px;
  margin: 20px auto;
  list-style: none;
  border: 0;
  padding: 0;
}
.postlist li {
  line-height: 44px;
  list-style: none;
}
```

和 app.css 直接被引用就能生效不一样，以 .module.css 结尾的样式文件，引用是不一样的，所以需要修改 homepage/index.js 的代码内容

```
import React from "react";
import { Fragment } from "react";
import styles from './homepage.module.css';

function HomePage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/login">Login</a>
            </div>
            <ul className={styles.postlist}>
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
            </ul>
        </Fragment>
    );
}
  
export default HomePage;
```

这里的 `<div className={styles.topbar}>` 中 `{styles.topbar}` 是插入 js 表达式，即从 styles 这个对象中找到 topbar 属性的值。下面的也是一样的意思。

用同样的方式改写其他的几个页面，新建文件夹，并在里面增加对应的 index.js 文件和 css 模块文件

**详情页面 DetailPage.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import CommentList from "../CommentList";
import CommentAdd from "../CommentAdd";
import styles from './detailpage.module.css';

function DetailPage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/login">Login</a>
            </div>
            <div className={styles.postdetail}>
                <h2>Title</h2>
                <p>Content</p>
            </div>
            <CommentAdd />
            <CommentList />
        </Fragment>
    );
}

export default DetailPage;
```

对应的样式文件如下

```
.topbar {
  background-color: #fff;
  height: 80px;
  width: 960px;
  margin: 8px auto;
  display: flex;
}
.topbar h1 {
  font-size: 30px;
  font-weight: 700;
  color: #333;
  margin: 0;
  line-height: 80px;
  flex: 1;
}
.topbar a {
  line-height: 80px;
}
.postdetail {
    width: 960px;
    margin: 20px auto;
    border: 0;
    padding: 0;
}
```

**评论列表页面 CommentList.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './commentlist.module.css';

function CommentList() {
    return (
        <Fragment>
            <div className={styles.commentlist}>
                <h2>Comments</h2>
                <ul>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                    </li>
                </ul>
            </div>
        </Fragment>
    );
}

export default CommentList;
```

对应的样式如下

```
.commentlist {
    margin: 60px auto 10px;
    width: 960px;
}
.commentlist ul {
    list-style: none;
    padding: 0;
    border: 0;
}
```

**评论增加 CommentAdd.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './commentadd.module.css';

function CommentAdd() {
    return (
        <Fragment>
            <div className={styles.commentadd}>
                <h2>Leave your comment</h2>
                <form>
                    <div className={styles.form}><input type="text" placeholder="Name" /></div>
                    <div className={styles.form}><textarea placeholder="Comment"></textarea></div>
                    <div className={styles.form}><button type="submit">Add Comment</button></div>
                </form>
            </div>
        </Fragment>
    );
}

export default CommentAdd;
```

对应的样式如下

```
.commentadd {
    margin: 30px auto;
    width: 960px;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    padding: 20px 0;
}
.commentadd .form {
    padding: 5px 0;
}
.commentadd input {
    width: 200px;
    height: 30px;
    border: 1px solid #ddd;
    padding: 5px;
    font-size: 14px;
}
.commentadd textarea {
    width: 50%;
    height: 100px;
    border: 1px solid #ddd;
    padding: 5px;
    font-size: 14px;
    resize: none;
}
```

**登录页面 LoginPage.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './loginpage.module.css';

function LoginPage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/">Home</a>
            </div>
            <div className={styles.login}>
                <h2>Login</h2>
                <form>
                    <div className={styles.form}><input type="text" placeholder="Username" /></div>
                    <div className={styles.form}><input type="password" placeholder="Password" /></div>
                    <div className={styles.form}><button type="submit">Login</button></div>
                </form>
            </div>
        </Fragment>
    );
}

export default LoginPage;
```

对应的样式如下

```
.topbar {
    background-color: #fff;
    height: 80px;
    width: 960px;
    margin: 8px auto;
    display: flex;
  }
  .topbar h1 {
    font-size: 30px;
    font-weight: 700;
    color: #333;
    margin: 0;
    line-height: 80px;
    flex: 1;
  }
  .topbar a {
    line-height: 80px;
  }
  .login {
      width: 960px;
      margin: 20px auto;
      border: 0;
      padding: 0;
  }
  .login .form {
    padding: 5px 0;
}
.login input {
    width: 200px;
    height: 30px;
    border: 1px solid #ddd;
    padding: 5px;
    font-size: 14px;
}
```

**后台帖子列表页面 PostListPage.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './postlistpage.module.css';

function PostListPage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
                <a href="/logout">Logout</a>
            </div>
            <ul className={styles.postlist}>
                <li><a href="/post_edit">Title</a></li>
                <li><a href="/post_edit">Title</a></li>
                <li><a href="/post_edit">Title</a></li>
            </ul>
        </Fragment>
    );
}

export default PostListPage;
```

对应的样式如下

```
.topbar {
background-color: #fff;
height: 80px;
width: 960px;
margin: 8px auto;
display: flex;
}
.topbar h1 {
font-size: 30px;
font-weight: 700;
color: #333;
margin: 0;
line-height: 80px;
flex: 1;
}
.topbar a {
line-height: 80px;
margin-left: 10px;;
}
.postlist {
    width: 960px;
    margin: 20px auto;
    border: 0;
    padding: 0;
    list-style: none;
}
.postlist li {
    line-height: 44px;
    list-style: none;
}
```

**后台帖子增加页面 PostAddPage.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './postaddpage.module.css';

function PostAddPage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
                <a href="/logout">Logout</a>
            </div>
            <div className={styles.postadd}>
                <h2>Add Post</h2>
                <form>
                    <div className={styles.form}><label htmlFor="title">Title</label></div>
                    <div className={styles.form}><input type="text" id="title" name="title" /></div>
                    <div className={styles.form}><label htmlFor="content">Content</label></div>
                    <div className={styles.form}><textarea id="content" name="content"></textarea></div>
                    <div className={styles.form}><input type="submit" value="Add Post" /></div>
                </form>
            </div>
        </Fragment>
    );
}

export default PostAddPage;
```

对应的样式如下

```
.topbar {
background-color: #fff;
height: 80px;
width: 960px;
margin: 8px auto;
display: flex;
}
.topbar h1 {
font-size: 30px;
font-weight: 700;
color: #333;
margin: 0;
line-height: 80px;
flex: 1;
}
.topbar a {
line-height: 80px;
margin-left: 10px;;
}
.postadd {
    width: 960px;
    margin: 20px auto;
    border: 0;
    padding: 0;
    list-style: none;
}

.postadd .form {
    padding: 5px 0;
}
.postadd input {
    width: 200px;
    height: 30px;
    border: 1px solid #ddd;
    padding: 5px;
    font-size: 14px;
}
.postadd textarea {
    width: 50%;
    height: 100px;
    border: 1px solid #ddd;
    padding: 5px;
    font-size: 14px;
    resize: none;
}
```

**后台帖子修改页面 PostEditPage.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import PostComments from "../PostComment";
import styles from './posteditpage.module.css';

function PostEditPage() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
                <a href="/logout">Logout</a>
            </div>
            <div className={styles.postedit}>
                <h2>Edit Post</h2>
                <form>
                    <div className={styles.form}><input type="text" placeholder="Title" /></div>
                    <div className={styles.form}><textarea placeholder="Content"></textarea></div>
                    <div className={styles.form}><button type="submit">Update</button></div>
                </form>
            </div>
            <PostComments />
        </Fragment>
    );
}

export default PostEditPage;
```

对应的样式如下

```
.topbar {
    background-color: #fff;
    height: 80px;
    width: 960px;
    margin: 8px auto;
    display: flex;
    }
    .topbar h1 {
    font-size: 30px;
    font-weight: 700;
    color: #333;
    margin: 0;
    line-height: 80px;
    flex: 1;
    }
    .topbar a {
    line-height: 80px;
    margin-left: 10px;;
    }
    .postedit {
        width: 960px;
        margin: 20px auto;
        border: 0;
        padding: 0;
        list-style: none;
    }
    
    .postedit .form {
        padding: 5px 0;
    }
    .postedit input {
        width: 200px;
        height: 30px;
        border: 1px solid #ddd;
        padding: 5px;
        font-size: 14px;
    }
    .postedit textarea {
        width: 50%;
        height: 100px;
        border: 1px solid #ddd;
        padding: 5px;
        font-size: 14px;
        resize: none;
    }
```

**后台评论的管理 PostComment.js**

修改后的代码如下

```
import React from "react";
import { Fragment } from "react";
import styles from './postcomment.module.css';

function PostComments () {
    return (
        <Fragment>
            <div className={styles.commentlist}>
                <h2>Comments</h2>
                <ul>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                    <li>
                        <h3>Name</h3>
                        <p>Comment</p>
                        <p>Delete</p>
                    </li>
                </ul>
            </div>
        </Fragment>
    );
}

export default PostComments;
```

对应的样式如下

```
.commentlist {
    margin: 60px auto 10px;
    width: 960px;
}
.commentlist ul {
    list-style: none;
    padding: 0;
    border: 0;
}
```

改完后，页面的基本样式也有了，到此，项目的目录结构如下图

![](https://storage.tourcoder.com/tcblog/learn-react-step-by-step-002.png)

### 通用组件

拆分组件是一个技术活，要拆得精细巧妙，复用率要高。在这个 blog 应用中，很容易可以看出，在前后台的导航页面可以在不同的页面复用，那么分别将它们拆成组件，然后在其他的页面引用即可。专门创建一个 components 的文件夹

**前台导航 navbar**

代码如下

```
import React from "react";
import { Fragment } from "react";

import styles from './navbar.module.css';

function Navbar() {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/login">Login</a>
            </div>
        </Fragment>
    );
}

export default Navbar;
```

对应的样式

```
.topbar {
    background-color: #fff;
    height: 80px;
    width: 960px;
    margin: 8px auto;
    display: flex;
  }
  .topbar h1 {
    font-size: 30px;
    font-weight: 700;
    color: #333;
    margin: 0;
    line-height: 80px;
    flex: 1;
  }
  .topbar a {
    line-height: 80px;
  }
```

此时，在需要使用导航的页面都引入该组件，比如首页，修改后的代码是

```
import React from "react";
import { Fragment } from "react";
import Navbar from "../../components/navbar";
import styles from './homepage.module.css';

function HomePage() {
    return (
        <Fragment>
            <Navbar />
            <ul className={styles.postlist}>
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
                <li><a href="/detail">Title</a></li>
            </ul>
        </Fragment>
    );
}
  
export default HomePage;
```

同时将 homepage.module.css 中的对应的样式删除即可。其他还有两个页面（详情页面和登录页面）也做相应的修改，通过这种方式引入导航组件到其页面。

此时遇到一个问题，首页和详情页面的导航完全是一样的，左侧是 logo，右侧是一个 login 的链接，但在登录页面的导航，左侧是 logo，但右侧是 home 的链接。此时就需要对 Navbar 进行修改，需要用到路由中的 `useLocation` 这个函数钩子。修改后的代码如下

```
import React, { Fragment } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './navbar.module.css';

function Navbar() {
    const location = useLocation();

    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                {location.pathname === '/login' ? (
                    <a href="/">Home</a>
                ) : (
                    <a href="/login">Login</a>
                )}
            </div>
        </Fragment>
    );
}

export default Navbar;
```

这里用了一个三元表达式

```
{location.pathname === '/login' ? (
    <a href="/">Home</a>
) : (
    <a href="/login">Login</a>
)}
```

这样就完成了前台页面导航的更改。

**后台导航 menubar**

和前台导航差不多，不过不同的是，后台几个页面的导航是一样的，直接写就行。

```
import React from "react";
import { Fragment } from "react";
import styles from './menubar.module.css';

function Menubar () {
    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <a href="/posts">Posts</a>
                <a href="/post_add">Add</a>
                <a href="/logout">Logout</a>
            </div>
        </Fragment>
    );
}

export default Menubar;
```

同样还有样式，样式内容和 navbar 的内容一样，然后在其他页面引入这个组件，并去掉自身样式中多余的内容，至此，公用组件的内容也完成。


### 数据交互

React 是前端技术，主要关注前端界面，是一个用户界面库。它无法直接和数据库进行交互，它做的事情是将获取到的数据保存在组件的状态中，然后渲染啊呈现这些数据。而获取数据的方式有多种，一般常用的是通过 API 方式获取或第三方实时数据服务获取，比如 Firebase 的 Filestore。

**API**

因为这些是后端的内容，先用 mockjs 来替代一下。目前除了增加和编辑帖子，增加评论外，其他的都是只读接口，可以直接用 mockjs 模拟出数据。至于 mockjs 是什么，可以看其[官网](http://mockjs.com/)介绍。

安装 mockjs

```
npm install mockjs
```

在 src 文件夹下新建一个文件 mock.js

```
import Mock from 'mockjs'

const domain = '/api/'

Mock.mock(domain + 'posts', function () {
    let result = {
        code: 200,
        message: true,
        data: Mock.mock({
            'array|5-10': [{
                'id|+1': 1000000,
                'title': '@title',
                'body': '@sentence',
            }],
        }),
    }
    return result
})
```

上面是模拟了 posts 的接口，部分代码解释

- 生成一个 5 到 10 个帖子元素的数组

- 其中 id 是 7 位数，自增；

- title 随机；body 内容随机

需要注意的是，mockjs 只是一个模拟了 API 的响应，并没有启动过一个 web 服务，所以通过 URL 访问是访问不到的。它只是在请求 API 的时候拦截，并将自己的内容呈现出来。将该文件引入到 src/index.js 中，即 `import './mock';`，然后在对应的页面发送请求即可，比如在首页获取所有的帖子，即

先安装 axios

```
npm install axios
```

修改首页的代码

```
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Fragment } from "react";
import Navbar from "../../components/navbar";
import styles from './homepage.module.css';

function HomePage() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        axios.get('/api/posts')
        .then(response => {
            setPosts(response.data.data.array);
        })
    }, []);

    return (
        <Fragment>
            <Navbar />
            <ul className={styles.postlist}>
                {posts.map(post => (
                    <li key={post.id}>
                        <a href="/detail">{post.title}</a>
                    </li>
                ))}
            </ul>
        </Fragment>
    );
}
  
export default HomePage;
```

这样，首页就完成了帖子列表的内容，同样的方式，修改后台的帖子列表，前后台的评论列表。

**Firebase**

有一些功能需要写入到数据库，而 mockjs 无法实现这样的功能，这里借助 firebase 来实现这样的功能。先进入到 firebase.google.com，创建一个 Cloud Firestore 的数据库，并且给它预置一个集合 users 和两条数据，其中密码部分没有加密。

![](https://storage.tourcoder.com/tcblog/learn-react-step-by-step-003.png)

回到代码处继续，先将 firebase 添加到项目工程中

```
npm install firebase
```

在 src 文件夹下创建一个 firebase.js 的文件，创建一个 firebase 的模块

```
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAWdaf9piNHOkcGaq4gLNYtidskd3EvtRBhI",
  authDomain: "react-demos-blog.firebaseapp.com",
  projectId: "react-demos-blog",
  storageBucket: "react-demos-blog.appspot.com",
  messagingSenderId: "63456776876",
  appId: "1:2129823432:web:2a0ad498dkl42b4e121a8c"
};


const firebaseapp = initializeApp(firebaseConfig);
export const db = getFirestore(firebaseapp);
```

这里所有的参数应该通过 dotENV 的方式载入到项目中，但这里测试用的，就直接在模块文件里写入这些内容。

先写登录功能，登录功能如果结合 firebase 的话，应该是用它的 auth 功能，但在这里我使用常规的接口请求的方式来做，预置的数据在开头已经说明。直接修改 loginpage 里的代码

```
import React, { Fragment, useState } from "react";
import { useNavigate } from 'react-router-dom';
import Navbar from "../../components/navbar";
import styles from './loginpage.module.css';
import { collection, getDocs, query, where } from "firebase/firestore";
import { db } from "../../firebase";

function LoginPage() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (event) => {
        event.preventDefault();

        const q = query(collection(db, "users"), where("username", "==", username));
        const querySnapshot = await getDocs(q);
        if (querySnapshot.empty) {
            alert("User not found");
            return;
        }
        querySnapshot.forEach((doc) => {
            const data = doc.data();
            if (data.password === password) {
                navigate("/posts");
                return;
            }
            alert("Incorrect password");
        })
    };

    return (
        <Fragment>
            <Navbar />
            <div className={styles.login}>
                <h2>Login</h2>
                <form onSubmit={handleLogin}>
                    <div className={styles.form}><input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} /></div>
                    <div className={styles.form}><input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} /></div>
                    <div className={styles.form}><button type="submit">Login</button></div>
                </form>
            </div>
        </Fragment>
    );
}

export default LoginPage;
```

从上面代码可以看出，当输入错误的用户名或者密码时，都会弹窗提示错误。而当输入正确的用户名和密码后，会通过 useNavigate 这个钩子函数跳转到后台的 posts 页面去。

接着完成增加帖子与 firebase 交互的内容，增加帖子用到了 firestore 的 addDoc 这个函数，修改后的代码如下

```
import React, { Fragment, useState } from "react";
import Menubar from "../../components/menubar";
import styles from './postaddpage.module.css';
import { db } from "../../firebase";
import { addDoc, collection } from 'firebase/firestore';

function PostAddPage() {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleTitleChange = (event) => {
        setTitle(event.target.value);
    };

    const handleContentChange = (event) => {
        setContent(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const docRef = await addDoc(collection(db, "posts"), {
                title: title,
                content: content,
                timestamp: Date.now()
            });
            setTitle('');
            setContent('');
            alert("Post added successfully");
        } catch (error) {
            console.error("Error adding document: ", error);
        }
    };

    return (
        <Fragment>
            <Menubar />
            <div className={styles.postadd}>
                <h2>Add Post</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.form}><label htmlFor="title">Title</label></div>
                    <div className={styles.form}><input type="text" id="title" name="title" value={title} onChange={handleTitleChange} /></div>
                    <div className={styles.form}><label htmlFor="content">Content</label></div>
                    <div className={styles.form}><textarea id="content" name="content" value={content} onChange={handleContentChange}></textarea></div>
                    <div className={styles.form}><input type="submit" value="Add Post" /></div>
                </form>
            </div>
        </Fragment>
    );
}

export default PostAddPage;
```

修改后台帖子的列表的页面，代码如下

```
import React, { Fragment, useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import Menubar from "../../components/menubar";
import styles from './postlistpage.module.css';
import { db  } from "../../firebase";
import { collection, getDocs } from "firebase/firestore";

function PostListPage() {
    const [posts, setPosts] = useState([]);
        
    useEffect(() => {
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        const querySnapshot = await getDocs(collection(db, "posts"));
        const posts = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
        setPosts(posts);
    };

    return (
        <Fragment>
            <Menubar />
            <ul className={styles.postlist}>
                {posts.map(post => (
                    <li key={post.id}>
                        <Link to={`/post_edit/${post.id}`}>{post.title}</Link>
                    </li>
                ))}
            </ul>
        </Fragment>
    );
}

export default PostListPage;
```

除了读出 firestore 里面的内容之外，标题链接的方式也做了修改，将 a 标签改成了 react-router-dom 中的 link，因为这里牵涉到一个传参和路径的问题，同时需要修改 app.js 文件中的路由。即 app.js 修改后的内容

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';
import PostAddPage from './pages/PostAddPage';
import PostEditPage from './pages/PostEditPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/posts" element={<PostListPage />} />
          <Route path="/post_add" element={<PostAddPage />} />
          <Route path="/post_edit/:id" element={<PostEditPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

编辑帖子，需要先通过刚才输入的参数读取到 firestore 中对应的数据，然后填充到输入框中，同时当输入框中有修改，提交后能更新 firestore 中对应的内容，代码如下

```
import React, { Fragment, useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Menubar from "../../components/menubar";
import PostComments from "../PostComment";
import styles from './posteditpage.module.css';
import { db } from "../../firebase";
import { getDoc, updateDoc, doc } from "firebase/firestore";

function PostEditPage() {
    const { id } = useParams();
    const [title, setTitle] = useState(''); 
    const [content, setContent] = useState('');

    useEffect(() => {
        const fetchPost = async () => {
            const docRef = doc(db, "posts", id);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                const data = docSnap.data();
                setTitle(data.title);
                setContent(data.content);
            } else {
                alert("No such post!");
            }
        };

        fetchPost();
    }, [id]);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const docRef = doc(db, "posts", id);
        await updateDoc(docRef, { title: title, content: content });

        alert('Post updated successfully');
    };

    return (
        <Fragment>
            <Menubar />
            <div className={styles.postedit}>
                <h2>Edit Post</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.form}><input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} /></div>
                    <div className={styles.form}><textarea placeholder="Content" value={content} onChange={(e) => setContent(e.target.value)}></textarea></div>
                    <div className={styles.form}><button type="submit">Update</button></div>
                </form>
            </div>
            <PostComments />
        </Fragment>
    );
}

export default PostEditPage;
```

同样前台的首页做对应的修改，从 firestore 里获取到真实的数据，并且将跳转更改成 link

```
import React, { useEffect, useState, Fragment } from 'react';
import { Link } from 'react-router-dom';
import Navbar from "../../components/navbar";
import styles from './homepage.module.css';
import { db } from "../../firebase";
import { collection, getDocs } from "firebase/firestore";

function HomePage() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        const querySnapshot = await getDocs(collection(db, "posts"));
        const posts = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
        setPosts(posts);
    };

    return (
        <Fragment>
            <Navbar />
            <ul className={styles.postlist}>
                {posts.map(post => (
                    <li key={post.id}>
                        <Link to={`/detail/${post.id}`}>{post.title}</Link>
                    </li>
                ))}
            </ul>
        </Fragment>
    );
}
  
export default HomePage;
```

前台的详情页面也做对应的修改，同样 app.js 中的路由也要做修改，修改后 app.js 代码

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';
import PostAddPage from './pages/PostAddPage';
import PostEditPage from './pages/PostEditPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/detail/:id" element={<DetailPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/posts" element={<PostListPage />} />
          <Route path="/post_add" element={<PostAddPage />} />
          <Route path="/post_edit/:id" element={<PostEditPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

修改后的详情页面代码

```
import React, { Fragment, useState, useEffect } from "react";
import Navbar from "../../components/navbar";
import CommentList from "../CommentList";
import CommentAdd from "../CommentAdd";
import styles from './detailpage.module.css';
import { useParams } from "react-router-dom";
import { collection, doc, getDoc } from "firebase/firestore";
import { db } from "../../firebase";

function DetailPage() {
    const { id } = useParams();
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        fetchPost();
    }, [id]);

    const fetchPost = async () => {
        const docRef = doc(db, "posts", id);
        const docSnap = await getDoc(docRef);

        if (docSnap.exists()) {
            const data = docSnap.data();
            setTitle(data.title);
            setContent(data.content);
        } else {
            alert("No such post!");   
        }
    };

    return (
        <Fragment>
            <Navbar />
            <div className={styles.postdetail}>
                <h2>{title}</h2>
                <p>{content}</p>
            </div>
            <CommentAdd postId={id} />
            <CommentList postId={id} />
        </Fragment>
    );
}

export default DetailPage;
```

在上面的代码中，也修改了 commentadd 和 commentlist 两个组件的引入方式

```
<CommentAdd postId={id} />
<CommentList postId={id} />
```

通过 id 将这两个组件和详情页面关联起来，这两个组件也要做对应的修改。

评论增加页面代码的修改

```
import React, { Fragment } from "react";
import styles from './commentadd.module.css';
import { useParams } from "react-router-dom";
import { db } from "../../firebase";
import { collection, addDoc } from "firebase/firestore";

function CommentAdd() {
    const { id } = useParams();
    const [author, setAuthor] = React.useState("");
    const [content, setContent] = React.useState("");

    const handleAuthorChange = (e) => {
        setAuthor(e.target.value);
    };

    const handleContentChange = (e) => {
        setContent(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const docRef = await addDoc(collection(db, "comments"), {
                author: author,
                content: content,
                postid: id
            });
            setAuthor("");
            setContent("");
            alert("Comment added!");
        } catch (error) {
            console.error("Error adding post: ", error);
        }
    };

    return (
        <Fragment>
            <div className={styles.commentadd}>
                <h2>Leave your comment</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.form}><input type="text" placeholder="Name" name="author"  value={author} onChange={handleAuthorChange} /></div>
                    <div className={styles.form}><textarea placeholder="Comment" name="content" value={content} onChange={handleContentChange}></textarea></div>
                    <div className={styles.form}><button type="submit">Add Comment</button></div>
                </form>
            </div>
        </Fragment>
    );
}

export default CommentAdd;
```

评论显示页面

```
import React, { useEffect, useState } from 'react';
import { Fragment } from "react";
import styles from './commentlist.module.css';
import { useParams } from "react-router-dom";
import { db } from "../../firebase";
import { collection, query, where, getDocs } from "firebase/firestore";


function CommentList() {
    const { id } = useParams();
    const [comments, setComments] = useState([]);

    useEffect(() => {
        fetchComments();
    }, []);

    const fetchComments = async () => {
        const q = query(collection(db, "comments"), where("postid", "==", id));
        const querySnapshot = await getDocs(q);
        const comments = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
        setComments(comments);
    };

    return (
        <Fragment>
            <div className={styles.commentlist}>
                <h2>Comments</h2>
                <ul>
                    {comments.map(comment => (
                        <li key={comment.id}>
                            <h3>{comment.author}</h3>
                            <p>{comment.content}</p>
                        </li>
                    ))}
                </ul>
            </div>
        </Fragment>
    );
}

export default CommentList;
```

同样也将后台编辑页面下面的评论列表更新下，代码更改后如下

```
import React, { Fragment, useEffect, useState } from "react";
import styles from './postcomment.module.css';
import { useParams } from "react-router-dom";
import { db } from "../../firebase";
import { collection, query, where, getDocs, doc, deleteDoc } from "firebase/firestore";

function PostComments () {
    const { id } = useParams();
    const [comments, setComments] = useState([]);

    useEffect(() => {
        fetchComments();    
    }, []);

    const fetchComments = async () => {
        const q = query(collection(db, "comments"), where("postid", "==", id));
        const querySnapshot = await getDocs(q);
        const comments = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
        setComments(comments);
    };

    const deleteComment = async (commentId) => {
        if (window.confirm('Delete this comment?')) {
            await deleteDoc(doc(db, "comments", commentId));
            alert('Comment deleted successfully');
            fetchComments();
        }
    };

    return (
        <Fragment>
            <div className={styles.commentlist}>
                <h2>Comments</h2>
                <ul>
                    {comments.map(comment => (
                        <li key={comment.id}>
                            <h3>{comment.author}</h3>
                            <p>{comment.content}</p>
                            <button onClick={() => deleteComment(comment.id)}>Delete</button>
                        </li>
                    ))}
                </ul>
            </div>
        </Fragment>
    );
}

export default PostComments;
```

同时增加了删除评论的功能。

至此，每个页面的和 firebase 实现了互通。

### 页面访问权限的处理

在这么多的页面组件中，有一些是需要登录后才可以被看到和操作，所以需要设置权限。在 react 中有多个设置权限的方式，常用的有路由守卫，高阶组件，还有一些第三方库，比如 Redux 或者 MobX 等。比如路由守卫的方式，先创建一个 AuthContext 及相关的钩子，在组件文件夹下创建 AuthContext.js 文件，写入下面的代码

```
import React, { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export function useAuth() {
    return useContext(AuthContext);
}

export function AuthProvider({ children }) {
    const [token, setToken] = useState(() => {
        return window.localStorage.getItem("token");
    });

    useEffect(() => {
        if (token) {
            window.localStorage.setItem("token", token);
        } else {
            window.localStorage.removeItem("token");
        }
    }, [token]);

    return (
        <AuthContext.Provider value={{ token, setToken }}>
            {children}
        </AuthContext.Provider>
    );
}
```

这里用到了浏览器的 localStorage，通过判断浏览器是否有 token 来判断是否有访问权限。

接着创建一个 useAuthRoute 钩子组件，useAuthRoute.js，写入如下代码

```
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

function useAuthRoute() {
    const { token } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (!token) {
            navigate("/login");
        }
    }, [token, navigate]);
}

export default useAuthRoute;
```

然后修改 app.js 中路由文件的内容，修改后的代码

```
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { AuthProvider } from './components/AuthContext';

import HomePage from './pages/HomePage';
import DetailPage from './pages/DetailPage';
import LoginPage from './pages/LoginPage';
import PostListPage from './pages/PostListPage';
import PostAddPage from './pages/PostAddPage';
import PostEditPage from './pages/PostEditPage';

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <Router>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/detail/:id" element={<DetailPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/posts" element={<PostListPage />} />
            <Route path="/post_add" element={<PostAddPage />} />
            <Route path="/post_edit/:id" element={<PostEditPage />} />
          </Routes>
        </Router>
      </AuthProvider>
    </div>
  );
}

export default App;
```

比如要在增加帖子页面需要增加访问权限，则修改后的代码是

```
import React, { Fragment, useState } from "react";
import Menubar from "../../components/menubar";
import styles from './postaddpage.module.css';
import { db } from "../../firebase";
import { addDoc, collection } from 'firebase/firestore';
import useAuthRoute from "../../components/useAuthRoute";

function PostAddPage() {
    useAuthRoute();    

    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleTitleChange = (event) => {
        setTitle(event.target.value);
    };

    const handleContentChange = (event) => {
        setContent(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const docRef = await addDoc(collection(db, "posts"), {
                title: title,
                content: content,
                timestamp: Date.now()
            });
            setTitle('');
            setContent('');
            alert("Post added successfully");
        } catch (error) {
            console.error("Error adding document: ", error);
        }
    };

    return (
        <Fragment>
            <Menubar />
            <div className={styles.postadd}>
                <h2>Add Post</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.form}><label htmlFor="title">Title</label></div>
                    <div className={styles.form}><input type="text" id="title" name="title" value={title} onChange={handleTitleChange} /></div>
                    <div className={styles.form}><label htmlFor="content">Content</label></div>
                    <div className={styles.form}><textarea id="content" name="content" value={content} onChange={handleContentChange}></textarea></div>
                    <div className={styles.form}><input type="submit" value="Add Post" /></div>
                </form>
            </div>
        </Fragment>
    );
}

export default PostAddPage;
```

上面代码引入了 useAuthRoute，并在渲染前调用 useAuthRoute() 这个钩子。把其他有访问权限的页面也做相应的处理。同样，在登录页面就要处理，当成功登录后需要保存 token，登录页面修改后的代码如下

```
import React, { Fragment, useState } from "react";
import { useNavigate } from 'react-router-dom';
import Navbar from "../../components/navbar";
import styles from './loginpage.module.css';
import { collection, getDocs, query, where } from "firebase/firestore";
import { db } from "../../firebase";
import { useAuth } from "../../components/AuthContext";

function LoginPage() {
    const { setToken } = useAuth();

    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (event) => {
        event.preventDefault();

        const q = query(collection(db, "users"), where("username", "==", username));
        const querySnapshot = await getDocs(q);
        if (querySnapshot.empty) {
            alert("User not found");
            return;
        }
        querySnapshot.forEach((doc) => {
            const data = doc.data();
            if (data.password === password) {
                navigate("/posts");
                setToken(username);
                return;
            }
            alert("Incorrect password");
        })
    };

    return (
        <Fragment>
            <Navbar />
            <div className={styles.login}>
                <h2>Login</h2>
                <form onSubmit={handleLogin}>
                    <div className={styles.form}><input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} /></div>
                    <div className={styles.form}><input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} /></div>
                    <div className={styles.form}><button type="submit">Login</button></div>
                </form>
            </div>
        </Fragment>
    );
}

export default LoginPage;
```

这里我只是简单的保存了下用户名，实际生产力环境下应该保存返回的 token。而登出，则最基本的是清理掉浏览器保存的 token，严格的做法应该也清理服务器端的 token。修改下后台导航的内容，增加登出功能

```
import React, { Fragment } from "react";
import styles from './menubar.module.css';
import { Link } from 'react-router-dom';
import { useAuth } from "../../components/AuthContext";

function Menubar () {
    const { setToken } = useAuth();
    
    const handleLogout = (event) => {
        event.preventDefault();
        setToken(null);
    };

    return (
        <Fragment>
            <div className={styles.topbar}>
                <h1>Blog</h1>
                <Link to="/posts">Posts</Link>
                <Link to="/post_add">Add</Link>
                <Link to="#" onClick={handleLogout}>Logout</Link>
            </div>
        </Fragment>
    );
}

export default Menubar;
```

到这里，一个基于 react 的简单 blog 程序写完了。

### 代码优化

我的这些代码中，还有大量 html 的印记，并没有完全的用 react，最典型的，在一些链接，我用的是 a 标签。

我就不对这些代码进行优化了。

### 总结

React 并不难学，但每个知识点一定要掌握，比如 setValue 这类的。强烈建议把官方的文档多看几遍。

官方网址：[https://react.dev](https://react.dev)

我也推荐尚硅谷出的视频教程，B 站就有。

本次学习所有的代码内容均放在 [GitHub](https://github.com/tourcoder/learn-react-step-by-step) 上。
