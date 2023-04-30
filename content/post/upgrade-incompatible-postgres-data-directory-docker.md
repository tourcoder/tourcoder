---
title: "Docker 中升级 postgres"
slug: "upgrade-incompatible-postgres-data-directory-docker"
author: "Bin Hua"
lastmod: 2021-01-03 08:01:43
date: 2021-01-03 07:59:43
tags: ["docker", "postgresql", "docker-compose"]
---

在将 Docker 方式安装的 Postgres 升级时总是不成功，通过 `docker logs --details 该数据容器的id` 查看，得到如下信息

```
PostgreSQL Database directory appears to contain a database; Skipping initialization

2021-01-03 02:46:10.988 UTC [1] FATAL:  database files are incompatible with server
2021-01-03 02:46:10.988 UTC [1] DETAIL:  The data directory was initialized by PostgreSQL version 10, which is not compatible with this version 13.1 (Debian 13.1-1.pgdg100+1).
``` 

**解决办法**

1. 先导出数据，至于 docker 中怎么导出数据，可以看[这篇文章](/deploy-via-docker/)

2. 执行命令 `docker volume ls`，找到该数据 Drive

3. 执行命令 `docker volume rm 该drive的名字` 即可。

剩下的就是拉起新的容器，导入数据即可。


