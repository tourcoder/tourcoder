---
title: "MongoDB 学习手册"
slug: mongoldb-manual
author: Bin Hua
lastmod: 2020-08-06 06:20:06
date: 2018-11-06 05:51:00
tags: ["mongodb", "database", "笔记"]
---

#### 安装

因为我现在使用 Debian 较多，所以内容都是基于 Debian。

**在 Debian 9 下安装**

```
curl https://www.mongodb.org/static/pgp/server-4.0.asc | sudo apt-key add -
```

下载密钥并传给 apt-key

```
sudo vi /etc/apt/sources.list.d/mongodb-org-4.0.list
```

新增 mongodb 的源，将下面的内容添加进去

```
deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main
```

更新并安装即可

```
sudo apt update -y
sudo apt-get install mongodb-org -y
```

**在 Debian 10 下安装**

```
sudo apt install dirmngr gnupg apt-transport-https software-properties-common ca-certificates curl
```

安装软件包

```
curl -fsSL https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main'
```

添加密钥，并且添加源

```
sudo apt update -y
sudo apt install mongodb-org -y
```

更新并安装。

#### 启动

```
sudo systemctl enable mongod
sudo systemctl start mongod
```

其他常用命令

```
sudo systemctl status mongod

sudo systemctl stop mongod

sudo systemctl start mongod

sudo systemctl restart mongod

sudo systemctl disable mongod
```

#### 配置

配置文件在 `/etc/mongod.conf`，每次更改都应重启下 `sudo systemctl restart mongod`

**允许远程访问**

```
bindIp: 127.0.0.1
```

将这里的 `127.0.0.1` 绑定改成需要访问的 ip 地址，也可以改成 `0.0.0.0` 表示全都可以访问

**设置访问密码**

进入到数据库中

```
mongo
```

然后执行下面的命令

```
use mydb

db.createUser(
	{
		user: "mydbadmin",
		pwd: "mydbpassword",
		roles: [ { role: "readWrite", db: "mydb" }]
	}
)
```

上面表示为 mydb 这个数据库创建一个用户，该用户可读写。还需要设置下 `/etc/mongod.conf` 的内容，将 `security:` 反注释，并增加 `authorization: enabled`，即

```
security:
  authorization: enabled
```

重启 mongodb 后只有通过账号密码才可以访问数据库 `mongo -u mydbadmin -p --authenticationDatabase mydb`。

如果想访问多个数据库，也可以通过在 admin 这个中增加用户即可。

```
mongo -u mongoAdmin -p --authenticationDatabase admin

db.createUser(
    {
        user: "mongoAdmin", 
	pwd: "743033ac311de5f0514e0d5fb0a12c279f5df441", 
	roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
)
```

#### 数据处理

**备份导出数据**

```
mongodump -h ip --port 端口 -u 用户名 -p 密码 -d 数据库 -o 文件保存的路径
```

比如默认端口是 27017，没有密码，则

```
mongodump -h 127.0.0.1 --port 27017 -d 数据库 -o 文件保存的路径
```

上面的内容都可以做对应的调整。

**恢复导入数据**

```
mongorestore -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 --drop 文件保存的路径
```

同样，上面的内容都可以做对应的调整。
