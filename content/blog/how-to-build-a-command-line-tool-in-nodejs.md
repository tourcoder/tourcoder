---
title: "用 NodeJS 写 CLI"
slug: "how-to-build-a-command-line-tool-in-nodejs"
author: "Bin Hua"
lastmod: 2019-08-07 03:31:10
date: 2019-08-07 03:31:10
tags: ["nodejs", "terminal", "iterm", "clt", "cmd"]
---

CLI 即 command-line interface 的简写，中文称命令行界面，是指可在用户提示符下键入可执行指令的界面，通常不支持鼠标，用户通过键盘输入指令，计算机接收到指令后，予以执行。因为最近工作需要，使用 NodeJS 写了一次 CLI。

- commander 

    这是一个 npmjs.org 上的 module，通过它可以更简便的写 CLI，具体可以看[这里](https://www.npmjs.com/package/commander)。
    
- 直接写

    以 `hello world` 为事例
    
    - 创建并初始化

        ```
        mkdir clt-demo
        cd clt-demo
        npm init
        ```
        
    - 对 `package.json` 进行修改

        先看 `package.json` 的代码
        
        ```
        {
          "name": "clt-demo",
          "version": "0.0.1",
          "description": "a demo for writing CLT with NodeJS",
          "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
          },
          "keywords": [
            "nodejs",
            "CLT"
          ],
          "license": "MIT",
          "preferGlobal": true,
          "bin": {
            "commandname": "app.js"
          }
        }
        ```

        对 `package.json` 做了几点的操作
        
        - 去掉入口 `main` 属性，因为是 clt，应该是从命令来进入。

        - 增加 `preferGlobal`，其对应的值为 `true`，目的是提醒用户在安装时是否使用了 `--global` 参数。

        - 增加 `bin` 属性，其值是一个对象，对象中 `key` 为执行的命令名，`value` 为入口执行文件。

        `package.json` 的内容基本结束。
        
    - 编辑 `app.js` 文件

        这里是要写一个 `hello world`
        
        ```
        #! /usr/bin/env node
        console.log('hello world');
        ```
        
        - 第一行 `#! /usr/bin/env node`，叫 `Shebang`，关于它的解释，可以翻阅 [wikipedia](https://zh.wikipedia.org/wiki/Shebang)。

        - 第二行 就是打印出 `hello world`。

    - `npm link`

        该命令用来将上面写好的脚本安装到系统中
        
    到这一步基本完成了一个 `hello world` 的 `clt`，执行上面 `package.json` 中 `bin` 中 `key` 的命令即可得到 `hello world`。
    
    ![](https://storage.tourcoder.com/tcblog/how-to-build-a-command-line-tool-in-nodejs-001.png)
        
- 发布 `CLT`

    可以看之前的写的[「在 NPMJS 上发布并维护包」](/publish-and-update-package-on-npmjs/)。
    
- 源码

    [GitHub](https://github.com/tourcoder/cli-demo)
    
- 学习资料

    [Writing Command Line Tools with Node](https://javascriptplayground.com/node-command-line-tool/)
