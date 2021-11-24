---
title: "解决 firebase login 时的验证失败的问题"
slug: "fix-authentication-error-on-running-firebase-login"
author: Bin Hua
lastmod: 2021-05-30T16:31:46+08:00
date: 2021-05-30T16:31:46+08:00
tags: ["firebase", "node"]
---

写了个简单的笔记和收藏夹的合体应用，懒得再去搭建后端，使用了 firebase，挺方便的。

![](/imgs/fix-authentication-error-on-running-firebase-login-01.jpg)

不过在验证时总是出现问题，即执行命令 `firebase login` 时会出错

```
Error: Authentication Error: Your credentials are no longer valid. Please run firebase login --reauth
For CI servers and headless environments, generate a new token with firebase login:ci
```

开始我以为是因为访问 `localhost` 导致，因为直接用 `firebase login` 时会调用默认浏览器访问账户，但第一次总是不成功，都会第二次调用后才可以得到登录用的授权码，使用该授权码后就会出现上面的错误，遂用不调用本地的方式尝试 `firebase login  --no-localhost`，能成功在第一次就获取到授权码了，但问题依旧。

搜索后在 stackoverflow 上看到这么一个解决方法，[https://stackoverflow.com/questions/44471670/firebase-init-command-failing-to-execute](https://stackoverflow.com/questions/44471670/firebase-init-command-failing-to-execute)，即 `export NODE_TLS_REJECT_UNAUTHORIZED=0`，但问题还是存在，而用不使用代理的服务器测试后觉得问题还是出现在代理上。

最后将 http 也进行了代理，问题完美解决，方案如下

1. 设置环境变量

    ```
    export NODE_TLS_REJECT_UNAUTHORIZED=0
    ```

    Windows cmd 下使用 set。

2. 对 http 进行代理

    ```
    export http_proxy=http://127.0.0.1:8080
    ```

    代理的信息根据自己的情况来。
