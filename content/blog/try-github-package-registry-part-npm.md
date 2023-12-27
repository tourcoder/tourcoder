---
title: "GitHub Package Registry 试用(NPM 部分)"
slug: "try-github-package-registry-part-npm"
author: "Bin Hua"
lastmod: 2019-09-12 04:02:55
date: 2019-09-12 04:02:55
tags: ["nodejs", "GitHub", "docker", "webpack", "npm", "npmjs"]
---

纯粹的巧合，在我发邮件给 NPMJS 请他们协助我删除掉我账户里面所有的 Package 后三个小时，我发现自己的 GitHub 账户里已经可以使用 GitHub Package Registry 服务。

![](https://storage.tourcoder.com/tcblog/githubpackage000.png)

那么究竟是如何使用的呢？

**准备工作**

因为我的 GitHub 账户开启了二次认证，我需要创建一个 AccessToken，其权限是对 Package 的操作权限，如下图

![](https://storage.tourcoder.com/tcblog/githubpackage003.png)

将内容保存下来。

**创建项目**

![](https://storage.tourcoder.com/tcblog/githubpackage001.png)

在项目的导航中可以清楚的看到有一个 `packages` 菜单项，需要注意的是，如果创建的是空项目是没有这组菜单项的。

### NPM 部分

**配置 package.json 文件**

点 `packages` 该选项后，进入到本文第一张图的界面，选择对应的 `Package Type`，这里我选择了 `NPM`，则出现下面的内容

```
 // Step 1: Use `publishConfig` option in your package.json
publishConfig: {registry: "https://npm.pkg.github.com/tourcoder"}

// Step 2: Authenticate
$ npm login --registry=https://npm.pkg.github.com/tourcoder

// Step 3: Publish
$ npm publish 
```

完成第一步内容，即配置 package.json。

**授权许可**

执行上面步骤中的第二步，因为网络问题，它不是太稳定，总会报错，如下图

![](https://storage.tourcoder.com/tcblog/githubpackage002.png)

遇到上面的情况，除了多尝试几次之外，没有更好的办法。

在多次尝试后，我顺利进入了输入用户名，密码和 Email 环节。这里的密码就是准备工作中创建的 `AccessToken`，Email 是要对外公开的。

![](https://storage.tourcoder.com/tcblog/githubpackage004.png)

在输入完成后，还是遇到了问题，然后任凭我怎么操作，都是上面和下面的错误来会循环出现。后面实在太困，跑去睡觉了。

现在饭点时间继续更新，去看了下别人发布的 `Package`，我发现自己的 `package.json` 文件中两个问题

1. name: 应该是 `@githubusername/packagename` 这样的形式

2. publishConfig: 在 `GitHub Username` 之前有一个 @ 符号。

随即做了更改，同时刷新了下包地址配置，发现要求变成了如下形式

```
 // Step 1: Use `publishConfig` option in your package.json
publishConfig: {registry: "https://npm.pkg.github.com/@tourcoder"}

// Step 2: Authenticate
$ npm login --registry=https://npm.pkg.github.com/

// Step 3: Publish
$ npm publish 
```

和上面对比，可以清楚的看到有几点更改，第一步中有一个 @ 符号，第二步中去掉了链接尾部的 `GitHub username`。

重新执行第二步

![](https://storage.tourcoder.com/tcblog/githubpackage005.png)

输入帐号密码和 Email 地址，会得到成功登录的提示。随即执行第三步

![](https://storage.tourcoder.com/tcblog/githubpackage006.png)

这样一个包就发布完成了。

**包的使用**

进入到 [GitHub Search](https://github.com/search)，搜索包的名字，比如 `randomUpperCase`，点击结果左侧的 `Packages`

![](https://storage.tourcoder.com/tcblog/githubpackage007.png)

点击进入该包

![](https://storage.tourcoder.com/tcblog/githubpackage008.png)

这里发现一个有意思的事情包的名字是 `@tourcoder/randomuppercase`，说明我之前把 `package.json` 文件中的 `name` 从 `randomuppercase` 修改成 `@tourcoder/randomuppercase` 是多此一举的。

根据上面的提示，进行安装 `npm install @tourcoder/randomuppercase@0.0.2`，但却得到了错误提示，不存在。

![](https://storage.tourcoder.com/tcblog/githubpackage009.png)

那是因为在项目中需要创建 `.npmrc` 文件，加入如下内容

```
registry=https://npm.pkg.github.com/githubusername
```

这里的 `githubusername` 是想引入的包的所有者在 GitHub 上的 username，简单点说就是 `npm install @tourcoder/randomuppercase@0.0.2` 这个命令中 @ 和 / 之间的部分。

然后再来执行刚才的安装命令 `npm install @tourcoder/randomuppercase@0.0.2`，即可成功安装。

![](https://storage.tourcoder.com/tcblog/githubpackage010.png)

至于在代码中如何调用，和 NPM 基本一样。

```
const ruc = require("@tourcoder/randomuppercase");
console.log(ruc("abcd1234"));
```

下面源码中 `demo` 文件夹内容即是一个演示。

**源码**

[GitHub](https://github.com/tourcoder/randomUpperCase)

本文只是一个指导说明。

**和 NPMJS 比较**

GitHub package registry 没有办法和 NPMJS 单独比较，前者是一个多种类的包管理，后者是 nodejs 方面的。但拿出 nodejs 方面比较的话，那只有一句话，NPMJS 的创始人好像就是写 NPM 的人，所以不管是命令，还是配置，或者方便程度等等，NPMJS 有先天性的优势，算是根正苗红。

**参考文档**

[Configuring NPM for use with GitHub Package Registry](https://help.github.com/en/articles/configuring-npm-for-use-with-github-package-registry)
