---
title: "项目中数据库的演变"
slug: "nosql-1"
author: "Bin Hua"
lastmod: 2016-06-12 06:47:02
date: 2016-06-12 06:47:02
tags: ["mysql", "mongodb", "nosql"]
---

作为后端开发的人员，一直以来，我使用 Mysql 作为主力数据库，然而在数据库管理方面，同时维护着多个数据库和表是一件非常痛苦的事情，尤其是表及其键值的增加修改等，每每这个时候，就想着要解决这种痛苦。

**用 json 串来解决这些问题**

数据表 user 的键值有 4 个， `id name tel sex`，常规做法就是，执行下面的 sql 语句，创建这个表

```
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(80) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `tel` varchar(255) NOT NULL,
  `sex` int(80) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
```

这个时候因为项目需求的变更，我们需要增加用户的生日(birth)，这时我们会在数据表中增加 birth 这一键值，这样依次操作，有的是还有一个现象，新增加的键值只是为一条或几条数据服务，而不是为所有的数据服务，那么这些数据的这一个键值的内容就是空，有些浪费。

如果我把这些内容全部通过 json 串的形式封装在一个表的键值中会怎么样呢？

上面的内容就可以写成

```
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(80) NOT NULL AUTO_INCREMENT,
  `jsonstring` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
```

而这里的 `jsonstring` 是上面键值的 json 串合集，形式如

```
{"name":"","tel":"","sex":"","birth":""}
```

键值的增加对服务器的影响不会太大，灵活性提高。

**NoSQL**

上面的这个方案好是好，但是在性能和搜索上依旧有一定的问题，而 NoSql 的引入不失为另外一种比较好的解决办法。

NoSQL 和传统的关系型数据库不一样，它是一种非关系型的，可水平扩展的数据库，特点鲜明，缺点也鲜明，它主要是为了解决大型应用的问题，你也可以把它理解为我们上面一个解决方案的更高级形式。

目前有很多的 NoSQL 数据库，目前我使用的数据库是 [mongodb](https://www.mongodb.com) ，简单介绍下它的安装，在 Mac OSX 上使用。

![](/imgs/nosql-1-01.png)

下载

![](/imgs/nosql-1-02.png)

解压

![](/imgs/nosql-1-03.png)

在根目录下创建 `/data/db` 文件夹，并赋予他们权限

在刚才 mongodb 目录下，执行 ./mongod 会提示你上面的内容，点同意
这时就已经运行了 mongodb，可以从终端中看到，端口是 27017，用浏览器访问 `http://localhost:27017` 会得到一句话

```
It looks like you are trying to access MongoDB over HTTP on the native driver port.
```

mongodb 内置了一个小的 http 的 web 管理界面，默认端口是 28017，你需要通过执行

```
sudo mongod --httpinterface
```

然后通过 `http://localhost:28017` 来访问，更多关于创建数据库使用数据库等，可以去官方网站查看内容。

**20160613 补充内容**：

在 Mac 上可以通过 Homebrew 来安装

```
brew install mongodb
```

安装完成后，可以直接通过

```
brew services start/restart mongodb
```

来启动重启 mongodb，注意是后台运行的哦，这时候可以访问 `http://localhost:27017`，但 28017 的端口不能访问，可以去设置下 `mongod.conf` 文件

```
vi /usr/local/etc/mongod.conf
```

net 下增加如下内容

```
http.enabled: true
http.RESTInterfaceEnabled: true
```

完成！

**update@20160927 : LessDB（1）**

**前言**

外包项目做得多，总会遇到工作量重复的问题，后来我开发了一个 UnitServer 的框架解决后端服务器部分的问题，但在数据库方面，一直觉得还有更好的解决方案，上次也提过了 NoSQL 这个方案，原文见这里。

**为什么 LessDB**

对我来说，一个数据库自所以好，是因为我能很好的使用它，当然这只是我这种实用主义者的想法。但真的判断一个数据库好坏，其实没有一个标准，下面的几个参数内容仅供参考。

- 安全

- 性能

- 兼容

- 可移植

- 生产效率

目前来说市面上的关系数据库也好，还是 NoSQL 的一批数据库也罢，它们都做得很好。

但我还是觉得很麻烦，不好用，比如关系数据库就需要创建烦人的键值和表，很多数据库都非嵌入式的等等。

这些问题导致我想做一个小型的数据库，因为小，就起了个名字 LessDB。

**目前的进展和问题**

通俗点说，LessDB 的设计思路就是嵌入式的 NoSQL。基于 C/C++ 开发，我才完成 Objects 部分的模式设计处理，也是因为自身在这方面的技术能力有限，目前 LessDB 遇到的问题还是挺多。
其他

[UnQLite](https://unqlite.org/) 对我帮助很大。