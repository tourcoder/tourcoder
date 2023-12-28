---
title: "NodeJS 学习笔记"
slug: "study-nodejs"
author: "Bin Hua"
date: 2015-07-04 06:42:39
tags: ["nodejs", "笔记"]
draft: false
---

**前言: 关于NodeJS**

Chrome V8 Javascript 引擎上的运行时(runtime)。官方网站 [http://nodejs.org](http://nodejs.org) ， 开源地址 [https://github.com/nodejs/node](https://github.com/nodejs/node) 。

**第二章 安装配置**

- 2.1 安装及配置

    均去官网下载对应的系统版本进行安装，下载地址 [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
    
    - 2.1.1 Windows 下安装

        下载对应的 msi 或 exe 文件，双击安装，如下图，一并安装的还有 Node 包管理器 (Node Package Manager 又叫 NPM)
        
        ![](https://storage.tourcoder.com/tcblog/study-nodejs-install_on_windows_01.PNG)
        
        ![](https://storage.tourcoder.com/tcblog/study-nodejs-install_on_windows_02.PNG)

        可以自由的选择安装位置
        
        ![](https://storage.tourcoder.com/tcblog/study-nodejs-install_on_windows_03.PNG)

        选择安装的内容

        多个下一步后，完成安装，安装位置是上图中你定义的位置。

        在命令行中运行 node -v， 可以看到你所安装的 nodejs 的版本，运行 npm -v 则可以看到你的 NPM 的版本。

    - 2.1.2 Mac OSX 下安装

        下载对应的 APK 文件，双击安装，如下图，一并安装的还有 Node 包管理器
        
        ![](https://storage.tourcoder.com/tcblog/study-nodejs-install_on_osx_01.png)

        在多个继续的点击后，进入最后一步
        
        ![](https://storage.tourcoder.com/tcblog/study-nodejs-install_on_osx_02.png)

        可以看出，Node 的安装位置是 `/usr/local/bin/node`，而 NPM 的安装位置是 `/usr/local/bin/npm`

        在终端中运行 node -v， 可以看到你所安装的 nodejs 的版本，运行 npm -v 则可以看到你的 NPM 的版本。

        _还可以通过 homebrew 来安装，访问 http://brew.sh/ 安装好 homebrew 后，在终端中输入 `brew install nod` 即可安装_
        
    - 2.1.3 Linux 下安装

        一般情况下，可以通过不同的发行版本直接安装，比如 Debian/Ubuntu 就可以直接用 `sudo apt-get install nodejs` 来安装，其他发行版本类似。

        也可以用 nvm 来安装，先执行 `wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash` 安装 nvm，然后直接安装 nodejs 即可。

        常用的 nvm 命令

        ```
        nvm ls 列出本地已经安装的node版本
        nvm ls-remote 列出所有的node版本
        nvm install --lts 安装lts版本
        nvm install  安装指定版本
        nvm use  使用指定版本
        nvm help  查看帮助 
        ```

    - 2.1.4 编译源码安装

        因为 Linux 发行版本时间的缘故，有时候需要通过编译源码来安装，Windows 和 Mac OSX 下也可以编译源码的方式安装，但这里只介绍 Linux 下编译源码安装，以 Ubuntu 为例

        - 安装基本工具 g++ 编译 Node.JS，命令 `sudo apt-get install g++` 
        
        - python 基本系统已经预置，版本需要 2.5+ 
        
        - libssl-dev 提供 SSL/TLS 加密的支持，命令 `sudo apt-get install libssl-dev`
    
        - 下载并编译源码安装 将源码下载到系统系统中某一个地方，比如 ~ 目录下
        
            ```
            wget https://nodejs.org/dist/v4.4.4/node-v4.4.4.tar.gz 
            tar -xvf node-v4.4.4.tar.gz 
            cd node-v4.4.4 
            ./configure 
            sudo make 
            sudo make install 
            ```
            
            完成安装。如同上面的操作，查看 nodejs 和 npm 的版本。 

- 2.2 Node 包管理器

    Node 包管理器 (Node Package Manager 又叫 NPM)，Node.JS 0.6 版本后，已经包含在 Node.JS 的发行包中，在安装 Node.JS 的同时会自动安装。如果你想手动安装，执行一下命令

    ```
    curl http://npmjs.com/install.sh | sudo sh
    ```
    
    完成安装，更多的新版本的获取可以访问官网 [http://npmjs.com](http://npmjs.com) 。
    
- 2.3 多版本理器

    因为 Node.JS 版本更新速度快，会存在新旧版本不兼容等问题，这时候需要用到了 Node.JS 的多版本管理器。直接通过如下命令安装

    ```
    git clone https://github.com/tj/n.git //从服务器上 clone 到电脑端
    cd n //进入文件夹
    make install //安装
    ```
    
    安装完成后，可以在 `/usr/local/bin/n` 中看到相关的文件，更多命令通过 `n --help` 查看。也可以通过命令 `sudo npm install -g n` 直接安装。如果需要升级 nodejs 版本，则使用命令 `sudo n stable` 来安装最新稳定版。有时候需要执行命令 `sudo npm cache clean -f` 清理缓存。
    
**第三章 Node.JS 基础知识**

- 3.1 Hello World

    用任意编辑器新建一个文件，命名为 helloworld.js，里面写入如下内容

    ```
    console.log('hello world');
    ```
    
    _console.log 将在后面详细讲解_

    在终端中进入 helloworld.js 文件所在的文件夹，执行

    ```
    node helloworld.js
    ```
    
    这时你会在终端中看到 hello world 文字的出现。这就是运行 Node.JS 程序最基本的方法。

    更多的关于 Node 的用法，可以通过 node --help 查看。

- 3.2 模块

    模块 (Module) 是 Node.JS 的基本组成，通常一个 js 文件就是一个模块，通过 require 这个对象加载到程序中

    ```
    var http = require('http');
    ```
    这就是加载 http 这个模块，在 nodejs 中有一些官方内置的模块称之为核心模块，通过其名字（模块标识）直接引入，比如上面的 http，还有 fs 等；而用户自己写的模块称之为文件模块，其标识就是文件的路径，用 `.` 或 `../` 开头的相对或绝对路径，比如某一个自己写的 `tc.js` 模块就可以用
    
    ```
    var ntc = require('./tc.js'); // require 函数返回了一个对象，表示 ntc 是引入的 tc.js 这个模块
    ```
    
    - 3.2.1 模块的创建和加载

        如上所述，每一个 js 文件其实就是一个模块，node 会在执行该文件时自动的给该文件的代码内容外面套一层函数，比如 001.js 的代码内容是
        
        ```
        var x = 100;
        ```
        
        在执行时，会变成
        
        ```
        function (exports, require, module, __filename, __dirname) {
            var x = 100;
        }
        ```
        
        可以通过 `arguments.callee` 来查看，即
        
        ```
        var x = 100;
        console.log(arguments.callee + ''); //这里加 + '' 的内容是为了拼串，显示出字符串，如果不加则显示 [Function (anonymous)]，因为 callee 这个属性保存的是当前函数执行的对象
        ```
        
        通过 `function (exports, require, module, __filename, __dirname) {}` 可以看出，模块的代码是包装在一个函数里执行的，并且在执行的时候，传入了五个实参。
        
        |实参|说明|备注|
        |---|---|---|
        |exports|将变量或函数暴露到外部|它是 module 的属性，即 `module.exports==exports`|
        |require|用来引入外部的模块||
        |module|表示当前模块自身，就是当前文件||
        |__filename|当前文件模块的文件完整路径||
        |__dirname|当前文件模块所在的文件夹完整路径||
        
        因为每个模块都是被包含在一个函数里执行的，所以里面的变量是局部变量，而非全局变量，可以通过 `global` 来查询，即 `console.log(global)`。`global` 是 node 中的一个全局对象，类似于网页中的 `window`，在全局中的创建的变量会作为 `global` 的属性保存，在全局中创建的函数都会作为 `global` 的方法保存。也可以通过上面的 `arguments` 证明，因为全局中没有 `arguments`。

        通过 exports 这个对象来创建，exports 是模块公开的接口，将内容暴露出去

        ```
        var name; //定义一个变量
        exports.setName = function(thisName) {
          name = thisName;
        };
        exports.useName = function(){
          console.log('hi ' + name);
        };
        ```

        这里完成了一个模块的设计，保存文件为 module-name.js，通过 exports 这个对象把 setName 和 useName 设置为模块的访问接口。

        如上面所说，通过对象 require 加载到程序中进行使用

        ```
        var nameModule = require('./module-name'); //模块的位置，该程序文件和模块文件在同一个文件夹下
        nameModule.setName('tc'); //调用函数，有参数
        nameModule.useName(); //调用函数，无参数
        ```
        
        保存文件为 name.js，执行该文件 `node name.js` 会得到结果 `hi tc`。

        需要注意的是，无论加载多少次 Module，最后的的输出结果都是由最后一个所确定，如

        ```
        var nameModule1 = require('./module-name');
        nameModule1.setName('tc');
        
        var nameModule2 = require('./module-name');
        nameModule2.setName('tcoder');

        nameModule1.useName();
        ```

        保存文件为 name2.js，执行得到的结果是 `hi tcoder` ，而不是 `hi tc`。
        
    - 3.2.2 单一对象的模块创建

        只把一个对象封装到模块中，如

        ```
        function sayHi() {
          var name;
          this.setName = function(thisName) {
            name = thisName;
          };
          this.useName = function() {
            console.log('hi ' + name);
          };
        };
        module.exports = sayHi; //也可以写成 exports.sayHi = sayHi;
        ```
        
        其中 `module.exports` 和 `exports`
        
        ||用法|例子|
        |---|---|---|
        |module.exports|module.exports 既可以通过点，也可以通过直接赋值的形式|module.exports.abc = def 或者 module.exports = {abc: def} 赋值对象|
        |exports|exports 只能使用点向外暴露内部变量|exports.abc = def|

        保存文件为 sayhi.js，加载该文件

        ```
        var sayHiC = require('./sayHi');
        sayHello = new sayHiC();  //创建一个新对象
        sayHello.setName('tc');
        sayHello.useName();
        ```
        
        保存文件为 sayhic.js，执行该文件，同样可以得到 `hi tc` 这个结果。

- 3.3 包

    - 3.3.1 包的创建

        包类似于函数库，类库，将镀铬功能封装起来，用于发布更新依赖管理和版本控制，Node.JS 根据 CommonJS 规范实现了包机制，用上面提到的 NPM 来管理包。按 CommonJS 严格规范，包主要有下面的内容组成

        - package.json 必须放在包的最顶层目录下
    
        - 二进制文件必须放在 bin 目录下
        
        - Javascript 代码放在 lib 目录下
        
        - 文档放在 doc 目录下
        
        - 单元测试放在 test 目录下

        前面说到的文件和模块是一一对应的，同样文件夹还可以是作为文件而被使用，基本的包就可以视为是一个文件夹的模块，比如，创建一个文件夹叫 apackage，在这个文件夹下创建一个 `index.js` 的文件

        ```
        exports.bao = function () {
          console.log('hi package');
        };
        ```

        如同模块的写法一样。在 apackage 这个文件夹外，创建一个新文件命名为 `testpackage.js`

        ```
        var pg = require('./apackage');
        pg.bao();
        ```

        运行该文件，可以得到 `hi package`，这个结果。这个就是如何把一个文件夹封装成一个包。
        
    - 3.3.2 package.json 文件

        package.json 文件可以理解为包的配置文件，它定义了包的一些相关的信息，Node.JS 程序在调用一个包是 package.json 文件起了很重要的作用。更多关于它的说明请访问 [https://docs.npmjs.com/files/package.json](https://docs.npmjs.com/files/package.json) 本文件可以通过包管理工具 NPM 创建，`npm init`即可创建一个 package.json 的文件。
        
    - 3.3.3 包的安装和管理

        包的管理由 NPM 搞定，安装包也非常方便 `npm install package_name` 即可完成包的安装，此时这种安装是安装在当前的目录下的，会自动生成一个 mode_modules 的文件夹，如果想安装全局模式的包则运行 `npm install -g package_name`，加上 `-g` 这个参数。

        _注意：如果全局安装了，则不可以用 require 来进行使用，但可以 `npm link` 来消除这个限制 ，如果全局安装了amodule，则 `npm link amodule` 即可_
        
        至于如何发一个包到 NPM 上，参考[这里](https://tourcoder.com/publish-and-update-package-on-npmjs/)。
       
**第四章 常用 API 的学习**

NODEJS 常用 API 可以从其官网 [https://nodejs.org](https://nodejs.org) 查看，也有一个不错的中文站点 [https://nodejs.cn](https://nodejs.cn)。

- assert 断言
- async_hooks 异步钩子
- buffer 缓冲区
- child_process 子进程
- cluster 集群
- console 控制台
- crypto 加密
- debugger 调试器
- dgram 数据报
- diagnostics_channel 诊断通道
- dns 域名服务器
- domain 域
- Error 错误
- events 事件触发器
- fs 文件系统
- global 全局变量
- http 超文本传输协议
- http2 超文本传输协议2.0
- https 安全超文本传输协议
- inspector 检查器
- Intl 国际化
- module 模块
- net 网络
- os 操作系统
- path 路径
- perf_hooks 性能钩子
- process 进程
- punycode 域名代码
- querystring 查询字符串
- readline 逐行读取
- repl 交互式解释器
- report 诊断报告
- stream 流
- string_decoder 字符串解码器
- timers 定时器
- tls 安全传输层
- trace_events 跟踪事件
- tty 终端
- url 网址
- util 实用工具
- v8 引擎
- vm 虚拟机
- wasi WebAssembly系统接口
- webcrypto Web加密
- Webstream Web流
- worker_threads 工作线程
- zlib 压缩

**update@20180507 : Nodejs 项目调试**

最近在用 nodejs，koa，ejs 开发一个网站项目时总遇到一些问题，调试就显得非常重要，这里记录下一些调试的方式。

**官方指南**

Node.js 官方给出了一些调试指南的，查看[这里](https://nodejs.org/en/docs/guides/debugging-getting-started/)，已经非常全面。

- VSCode

    点击左侧的 Debug，然后点击顶部的 Setting （齿轮），输入 node.js，在弹出的文件 lanuch.json 中更改 Program 路径为自己的执行的文件路径，如下

    ```
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "type": "node",
                "request": "launch",
                "name": "Launch Program",
                "program": "${workspaceFolder}/app.js"
            }
        ]
    }
    ```

    最后点击顶部绿色的运行按钮开始运行即可。
