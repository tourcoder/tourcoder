---
title: "Docker 学习笔记"
slug: study-docker
author: "Bin Hua"
lastmod: 2020-07-18 06:09:07
date: 2017-06-10 07:05:02
tags: ["docker", "笔记"]
---

之前学习 Docker 时，在本子上做的笔记，整理下，放在自己的博客上，方便保存，同时也温习一下，需要注意的是，这些内容是我学习后的解释，便于理解，而非官方的解释。

**架构**

![](/imgs/study-docker-01.jpg)

左边是传统的虚拟化架构，右边是 Docker 技术。

和传统的对比，Docker 的特点有运行环境一致，性能高效，系统资源利用充分。
三要素

Docker 有三要素，镜像 (Image)，容器 (Container) 和 仓库 (Repository)。

镜像 (Image) 是带有最高权限（root）的最小服务单元，文件系统，它是基础。

容器 (Container) 实际运行的实体，可以理解为是一个进程，它和镜像的关系像是类和实例，很多的操作就是对它的操作，比如创建，删除，停止等。进程里不存数据，所以容器里也应该不写入数据，数据应该写入数据卷中，或者在上图中的母机中。

仓库 (Repository) 镜像分发，粗略理解参考 Github，使用率比较高的是 Docker Hub，国内也有一些镜像。
安装

进入官网下载，macOS 版，windows 版 和 ubuntu 版本，其他更多版本，查看[官方](https://www.docker.com/)。

我用的是 macOS，可以通过 Homebrew 安装

```
brew cask install docker
```

![](/imgs/study-docker-02.png)

安装完成。

**Docker 镜像**

三要素之一，可以理解为是一个最小化的、完整的、带有 root 权限属性的服务单元，文件系统。

**常见命令**

- 获取 `docker pull [OPTIONS] NAME[:TAG|@DIGEST]` 

    从镜像中心(registry)处获取一个镜像，默认来自 Docker Hub，主要的参数有  `-a, --all-tags`  获取仓库中所有的标签的镜像  `--disable-content-trust`  跳过镜像验证，这个是默认选项 

- 列出镜像命令 `docker images [OPTIONS] [REPOSITORY[:TAG]]` 

    列出镜像，主要的参数有  `-a, --all`  显示所有的镜像，但不包含中间镜像  `--digests`  显示 `digests  -f, --filter filter-content`  
    
    根据筛选条件进行筛选，比如 `docker images -f dangling=true` 表示列出虚悬镜像  `--format string`  使用 Go 模板打印图像  `--no-trunc` 不要截断输出  `-q, --quiet`  只显示镜像的 IDs 

- 删除镜像命令 `docker rmi [OPTIONS] IMAGE [IMAGE...]` 删除镜像

    主要参数有 `-f, --force` 强制删除镜像 `--no-prune` 不删除未标注的母镜像
    语句方式，比如 `docker rmi (docker images -q -f dangling=true)` 删除虚悬镜像   
**定制镜像**

有时候需要有团队内部的镜像，则可以通过 Dockerfile 来进行镜像的定制

主要是两个命令 FROM 和 RUN 都需要大写，形如

```
FROM 原始镜像或空镜像(scratch)
RUN  <命令> \
     && <命令> \
     && <命令> \
     && <命令>
```

然后执行命令 `docker build [OPTIONS] PATH | URL | -`，关于参数，可以通过 help 查看。

「举例」 我要基于最新版本的 nginx 创建一个私有镜像，并将默认的 index.html 内容变成 Hello Docker，那么创建 Dockerfile 文件，内容如下

```
FROM nginx
RUN echo 'Hello Docker' > /usr/share/nginx/html/index.html
```

这时在当前目录下运行命令 `docker build -t teamnginx .` 即可完成，点表示当前位置

还有一些，比如 `(COPY) (ADD) (CMD) (ENV  ) (ARG <参数名>)`，可以自行查找。

**Docker 容器**

```
docker run <仓库名>
```

启动容器，先搜索本地是否有该镜像，没有会从公网下载，类似有了一个 `docker pull` 的过程。比如 `docker run --name name -d -P 访问本地端口:内部端口 <仓库名>`，全一点的 `docker run -d -p 本地端口:内部端口 -v /本地地址:仓库位置 --name 本地名 仓库名`

```
docker exec -it 容器名 bash
```

进入容器，用终端命令行方式进入容器

```
docker commit [选项]<容器ID或容器名>[<仓库名>:<标签>]
```

可以参考 git commit。

```
docker diff 仓库名
```

参考 git diff

```
docker history
```

参考 git log

熟记更多的命令，会经常用到

```
docker start

docker ps

docker logs

docker stop

docker restart

docker attach

docker export <容器id> > xxx.tar

docker import 导入的文件  导入的位置

docker load

docker rm

docker search

docker rm -V 数据卷 //删除数据卷

docker stop $(docker ps -aq) //停止所以容器

docker rm $(docker ps -aq) //删除所有容器

docker rmi $(docker images -q) //删除所有的镜像
```