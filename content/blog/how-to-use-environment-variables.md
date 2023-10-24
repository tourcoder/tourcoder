---
title: "如何使用环境变量"
slug: "how-to-use-environment-variables"
author: "Bin Hua"
lastmod: 2022-07-20T01:34:19Z
date: 2022-07-20T01:34:19Z
tags: ["安全", "nodejs"]
---

用 GitHub 协同工作，稍不留神就会把密钥等传上去，挺简单的一个方法是，将这些重要的数据写在环境变量文件中，在上传代码时通过 .gitignore 不上传这些文件即可。

### Nodejs

通过 `dotenv` 来实现。

先安装 

```
npm install dotenv --save
```

然后在根目录创建一个 `.env` 文件，写入相关内容，格式是 `key=value`，比如

```
SECRET="123123"
```

引用并且使用

```
const dotenv = require("dotenv")
dotenv.config()
console.log(process.env.SECRET)
```


