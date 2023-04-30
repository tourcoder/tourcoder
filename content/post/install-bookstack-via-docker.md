---
title: "搭建私有的 wiki"
slug: install-bookstack-via-docker
author: "Bin Hua"
lastmod: 2020-07-18 05:34:42
date: 2020-01-13 14:10:55
tags: ["维基百科", "self-hosted", "wiki", "Bookstack"]
---

很早就想搭建一个家庭私有的 wiki，主要是方便家庭成员分享一些人生经历，一些思考，还有家庭树方面的内容，而这些很多内容是不方便在博客上分享的。最近碰到了一个开源的程序 `Bookstack` 就很不错。这次通过 Docker 来部署搭建。

先创建私有网络

```
sudo docker network create wiki_network
```

接着创建一个 mysql，进入到该文件夹，通过 Docker 来安装 mysql

```
mkdir mysql

cd mysql

sudo docker run -d --net wiki_network  \
--restart=always \
-v $PWD/conf:/etc/mysql/conf.d \
-v $PWD/datadir:/var/lib/mysql \
-e MYSQL_DATABASE=bookstack \
-e MYSQL_USER=bookstack \
-e MYSQL_PASSWORD=DB密码 \
 --name="bookstack_db" \
 mysql:latest
```

在 conf 文件夹下新建文件 custom.cnf

```
vi custom.cnf
```

并填入如下内容

```
[mysqld]
performance_schema=off
performance_schema_max_table_instances=50
table_definition_cache=50
table_open_cache=20
```

重启 mysql 的这个 docker 即可生效。

返回到 mysql 文件夹上一层，新建一个文件夹 wiki，通过 Docker 来安装 bookstack

```
mkdir wiki

cd wiki

sudo docker run -d \
--net wiki_network \
--name=tcwiki \
-e PUID=1001 \
-e PGID=1001 \
-e DB_HOST=bookstack_db:3306 \
-e DB_USER=bookstack \
-e DB_PASS=DB密码  \
-e DB_DATABASE=bookstack  \
-p 3000:80 \
-v $PWD:/config \
--restart unless-stopped \
linuxserver/bookstack
```

这样一个 wiki 就安装完成了，访问 `http://server_ip:3000` 即可访问该 wiki，默认的账号是 `admin@admin.com`，密码是 `password`，至于如何通过域名访问，用 nginx 等相关的软件做 proxy 即可。

如果想要把数据备份到宿主服务器，运行命令

```
docker exec -it -e MYSQL_PWD=DB密码 bookstack_db mysqldump -u bookstack bookstack > wiki_backup.sql
```

数据恢复过去，则反过来

```
docker exec -i -e MYSQL_PWD=DB密码 bookstack_db mysql -u bookstack bookstack < wiki_backup.sql
```

而该 wiki 的其他文件，比如图片等在你所映射的文件夹下，比如这里就是 `wiki` 这个文件夹下。