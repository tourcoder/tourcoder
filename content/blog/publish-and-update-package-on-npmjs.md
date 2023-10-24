---
title: "在 NPMJS 上发布并维护包"
slug: "publish-and-update-package-on-npmjs"
author: "Bin Hua"
lastmod: 2019-03-28 04:44:57
date: 2019-03-28 04:44:57
tags: ["nodejs", "npm", "yarn", "npmjs"]
---

做 nodejs 的开发基本都会用到 npm 都包，那么如何在 npmjs 上发布并维护一个包呢？

#### 准备条件

- 一个 [NPMJS](http://npmjs.com) 的账户

#### 步骤

- 编写包

    一个包应该至少包含三个文件，package.json，readme.md 和代码文件。虽然 readme.md 文件是非必需的，但一个清晰的文档文件能节省使用者很多事情，建议每一个发包者都应该写好 readme.md 文件。
    
    - readme.md 文件：主要是关于这个包的说明及用法

    - package.json 文件：通过 `npm init` 初始化得到，里面包含了一些必要的信息，得到的结构如下

    ```
    {
      "name": "npmdemo",
      "version": "0.0.1",
      "description": "npmdemo",
      "main": "app.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "keywords": [
        "npm",
        "demo"
      ],
      "author": "tourcoder",
      "license": "ISC"
    }
    ```
    
    - 代码文件，比如这里的 demo 代码如下，app.js

    ```
    exports.hello = function hello(name){
      console.log("hello "+ name);
    }
    ```
    
- 发布包

    - 增加用户

        执行命令 `npm adduser`，这时候会要求输入用户名密码等信息，将之前在 NPMJS 上注册的信息填写进去，完成后得到如下信息
        
        ```
        Username: tourcoder
        Password:
        Email: (this IS public) hello@tourcoder.com
        Enter one-time password from your authenticator app: 123123
        Logged in as tourcoder on https://registry.npmjs.org/.
        ```
        
        如果在 NPMJS 上面的账户开启了二次认证，会像上面第四行的信息一样出现要求输入二次验证的内容。
        
    - 发布

        在终端中直接输入 `npm publish` 等待校验后，会发布到 NPMJS 上，发布成功的形式如下
        
        ```
        npm notice
        npm notice 📦  npmdemo@0.0.1
        npm notice === Tarball Contents ===
        npm notice 260B package.json
        npm notice 70B  app.js
        npm notice === Tarball Details ===
        npm notice name:          npmdemo
        npm notice version:       0.0.1
        npm notice package size:  400 B
        npm notice unpacked size: 369 B
        npm notice shasum:        
        npm notice integrity:     
        npm notice total files:   2
        let sayhello=require('npmdemo');
        npm notice
        + npmdemo@0.0.1
        ```
        
- 更新包

    在 NPMJS 是没有更新概念的，它的更新就是发布一个更新的版本，比如更改了上面包的代码，再次使用前面的发布流程再次发布一次即可。
        
    **需要特别注意**：需要把 package.json 中的版本号更改下，这样就说明已经更新了该包。
    
- 删除包

    NPMJS 似乎是不能够删除包的，而且根据包发布的时间长短，取消已经发布的包的方式也不一样，具体看这里的[官方说明](https://www.npmjs.com/policies/unpublish)。
    
- 如何使用包

    ```
    npm install 包名
    ```
    
    具体看包的使用说明即可，这时可以看出 readme.md 文件的重要了。
    
#### 相关内容

除了 NPM 之外，facebook 出了一个 yarn，官方网站为 [https://yarnpkg.com](https://yarnpkg.com)

它的建包发包过程可以看这里 

- 建包 [https://yarnpkg.com/lang/zh-hans/docs/creating-a-package/](https://yarnpkg.com/lang/zh-hans/docs/creating-a-package/)

- 发包 [https://yarnpkg.com/zh-Hans/docs/publishing-a-package](https://yarnpkg.com/zh-Hans/docs/publishing-a-package)

也是发布在 NPMJS 上的哦。