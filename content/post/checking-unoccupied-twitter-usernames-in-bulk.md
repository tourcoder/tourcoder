---
title: "批量查看未被占用的 Twitter 用户名"
slug: checking-unoccupied-twitter-usernames-in-bulk
author: "Bin Hua"
lastmod: 2019-09-19 05:07:59
date: 2019-09-12 12:05:08
tags: ["nodejs", "twitter"]
---

前些天一个自己用来“批评”科技公司的 Twitter 账户被封了，原因是说我违反了他们的用户条款。其实我只是在那个帐号发了一些科技产品的 bug，不过无所谓了，重新注册一个即可。

#### 需求

现在目前 Twitter 允许注册用户名最短是 5 位，支持数字（0-9），26 个英文字母（不区分大小写）以及英文状态下的下划线。

而我打算这次用的用户名是以两个字母开头，后面跟着数字的组合方式，那么一共就有 1000 种可能性，即从 `000` 到 `999`。

#### 分析

秉着一贯懒的作风，我不打算围绕 API 来操作，我采用最简单粗暴的方式--通过服务器的状态码来判断。在 Twitter 上一个用户名所对应的账户一般有三个状态，正常，不存在和账户被悬挂（Account suspended）。通过对这三种状态的账户分析发现，访问正常和悬挂状态的账户，服务器返回正常，都是 200；而访问不存在的账户，服务器返回为 404，这就有了突破口。

#### 过程

这里用 `Node.JS` 来实现需求。

- 创建一个文件夹，并进入到该文件夹下

    ```
    mkdir demo && cd demo
    ```
    
- 初始化

    ```
    npm init
    ```
    
- 引入 module

    因为喜欢 `axios`，所以这里引入了它，其实可以用 NodeJS 自带的 `http(s)`
    
    ```
    npm install axios
    ```
    
- 编写代码

    先循环把数字列出来
    
    ```
    for(var i=0; i<1000; i++) {
      console.log(i);
    }
    ```
    
    列出来的数字是从 0 到 999，其中 0 到 99 都没有满足三位数，需要在前面加上 0 作为补充，这里我用迭代方式实现。
    
    ```
    function adjust(num, length) {
        for(var lens = (num + "").length; lens < length; lens = num.length) {
            num = "0" + num;
        }
        return num;
    }
    for(var i=0; i<1000; i++) {
      console.log(adjust(i, 3));
    }
    ```
    
    至此能列出 000 到 999 的三位数，一共 1000 个。
    
    加入账户访问请求部分的代码，即可得到完整的代码。
    
    ```
    const axios = require('axios');
    function adjust(num, length) {
        for(var lens = (num + "").length; lens < length; lens = num.length) {
            num = "0" + num;
        }
        return num;
    }
    for(var i=0; i<1000; i++) {
      (i=>{
        var username = "字母"+adjust(i, 3);
        var url = 'https://twitter.com/' + username
        axios.get(url)
        .then(response => {
          //username was token or account suspended
        })
        .catch(error => {
          console.log(username)
        });
      })(i)
    }
    ```
    
    执行该代码，显示出来的就是能够在 Twitter 上使用的用户名哦。
    
通过上面的代码，我发现还有 38 个格式为 `该两字母+数字` 的五字符用户名，随即挑选了一个，完事～