---
title: "Docker 部署项目笔记(持续更新)"
slug: deploy-via-docker
author: Bin Hua
lastmod: 2020-07-27 02:47:12
date: 2019-10-29 07:16:56
tags: ["nodejs", "GitHub", "docker", "package"]
---

不用过多的介绍 Docker，最简单的理解方式就是单实例运行方案，其官网地址是 [http://docker.com](http://docker.com) 。

#### 为什么用 Docker 部署项目

用 Node.JS 来解释下，做 Node.JS 项目的会用到很多第三方的包，通常做法是通过执行命令 `npm install package_name` 直接在服务器上安装，但这样做是有一定的风险，主要是因为第三方包的不可控。Node.JS 就发生过比较著名的 `left-pad` 事件，所以通过 Docker 这类工具来部署尤其重要。

这是一篇系列的笔记，我会持续更新里面的内容。需要注意的是，我在是 macOS Catalina 上进行的操作，其它系统大同小异。

#### 安装 Docker

Docker 的安装无需说明，官网有相关的文档，请看[这里](https://docs.docker.com/install/) 选择对应的系统版本安装即可，我使用的是 macOS，所以下载对应的客户端即可，我是通过 `brew cask install docker` 安装的。而 linux 下的安装方式也比较简单

```
curl -sSL https://get.docker.com/ | sh
service docker start
```

安装完成后，运行 docker，可以通过 `docker version` 查看当前安装的 docker 版本情况。我写了一个一键安装 Docker 和 Docker Compose 的脚本，可以从[这里](https://github.com/tourcoder/dockerman)下载。

#### Node.JS 项目

**项目任务**

- 完成 Hello World

    访问 `http://localhost:8080` 时显示 `Hello World`。
    
**步骤**

- 创建项目并初始化

    ```
    mkdir dockerdemo && cd dockerdemo
    npm init
    ```
    
- 先写好项目要求中的代码，并测试通过

    创建文件，并写入代码，完整的代码内容如下
    
    ```
    const Koa = require("koa");
    const port = "3000";
    const app = new Koa();
    app.use(async ctx => {
      ctx.body = 'Hello World';
    });
    app.listen(port);
    ```
    
    因为用到了 koa，所以需要先安装，在源码根目录下安装 `npm install koa`，完成后执行 `node app.js`，这时候访问 `http://localhost:3000`，就会出现 `Hello World`，如下图
    
    ![](/imgs/deploy-via-docker-01.png)
    
    至此，项目代码完成，并通过了测试。
    
- `.dockerignore` 文件

    如同 `.gitignore` 文件一样作用一样，`.dockerignore` 文件会忽略掉里面的文件，比如 Node.JS 中的 `node_module` 等，内容如下
    
    ```
    node_modules
    package-lock.json
    ```
    
- `Dockerfile` 文件

    先看其内容
    
    ```
    FROM node:latest
    RUN mkdir -p /home/tourcoder/dockerplex
    COPY . /home/tourcoder/dockerplex
    WORKDIR /home/tourcoder/dockerplex
    RUN npm install
    EXPOSE 3000
    CMD node app.js
    ```
    
    - 第一行：使用 Node.JS 的最新版本（latest），这里的 latest 可以是其他版本，比如 `node:12.0`，具体根据自己的需求来，版本信息可以看[这里](https://hub.docker.com/_/node/)。

    - 第二行：在容器中创建一个目录，其中 -p 参数是创建多层级文件夹，如果不存在该文件夹的话会自动创建，如果存在也不会报错。

    - 第三行：将当前目录下的内容拷贝到之前在容器创建的目录下

    - 第四行：定位容器的工作目录

    - 第五行：在容器的工作目录下执行后面的命令 `npm install`，后面也可以加上参数，比如在国内 Node.JS 的官方源慢，就可以使用国内的源，即 `RUN npm install --registry http://npmreg.mirrors.ustc.edu.cn`。

    - 第六行：expose 字面意思就是暴露，即将容器的某一端口暴露出来，允许外部使用，这里暴露的是 3000 端口。

    - 第七行：执行命令，如果有多个命令，之间用 `&&` 来拼接。

- 创建 image 文件

    执行如下命令
    
    ```
    docker build -t dockernodejsdemo .
    ```
    
    `-t` 参数的作用是指定后面的名字，也可以在名字后面增加 `:版本号`，如果不增加，则是 `latest`。
    
    ![](/imgs/deploy-via-docker-02.png)
    
    命令执行完成后，可以通过 `docker images` 命令看到已经生成了 image。
    
    ![](/imgs/deploy-via-docker-03.png)
    
    这样 image 文件创建完成。但这种情况下，创建的的 image 文件会很大，比如我这个文件就有 900 多 M，那么可以给它瘦身。查看 Dockerfile 文件，可以看出 node 来自 `node:latest`，它本身就很大，把它改成精简版，做成一个基础镜像，具体看[这里](https://pkgs.alpinelinux.org/packages)，它包含了大多数精简版的包。那么本文的 node 包就可以用这种方式精简。
   
    - 在项目外新建一个 `Dockerfile`，然后输入内容

      ```
      FROM alpine:latest
      RUN apk add --no-cache --update nodejs npm
      ```
      
    - 打包

      ```
      docker build -t basicnode:latest .
      ```
      
      打包完成后会发现，一下子从 900 多 M 精简到了 50 多 M。
      
    项目里调用的话，就是将之前项目的 `Dockerfile` 文件中的 `FROM node:latest` 换成 `FROM basicnode:latest` 即可，其它步骤一样。我这个项目最后打包出来，只有 80 多 M。

- 给 image 打 tag

    给 image 打 tag，执行命令

    ```
    docker tag IMAGE_ID docker.pkg.github.com/tourcoder/dockerdemo/IMAGE_NAME:VERSION
    ```

    这里 IMAGE_ID 即为需要上传的 image 对应的 `IMAGE ID`，可以通过 `docker image ls` 查看。

    后面就是 IMAGE_NAME 和版本
    
- 发布 image 文件

    私有的项目是不建议发布到第三方平台，这里只简单介绍下如何上传到 github package 上。

    先获取权限，新建一个空白的 txt 文件 GH_TOKEN.txt，然后将 AccessToken 的内容粘贴在里面。然后执行如下命令登录

    ```
    cat ~/GH_TOKEN.txt | docker login docker.pkg.github.com -u tourcoder --password-stdin
    ```
    
    执行完成后，即可得到如下

    ![](/imgs/deploy-via-docker-05.png)

    表示已经登录成功。
    
    发布 image，执行命令
    
    ```
    docker push docker.pkg.github.com/tourcoder/dockerdemo/IMAGE_NAME:VERSION
    ```
    
    ![](/imgs/deploy-via-docker-04.png)
    
    完成即可。

- 使用 image

    如果是使用本地的 image，则执行命令
    
    ```
    docker run -d -p 3030:3000 dockernodejsdemo
    ```
    
    其中
    
    - 参数 `-p` 表示映射的端口，即将容器暴露出来的端口 3000 映射到本机的 3030 端口。参数 `-d` 表示在后台运行。

    - 最后是 image 的名字。

    如果使用的是刚才上传的 image，则执行命令
    
    ```
    docker pull docker.pkg.github.com/tourcoder/dockerdemo/dockernodejsdemo:0.0.1
    ```
    
    先将 image 拉到本地来，然后再执行上面本地的命令即可。需要注意在拉入到本地来之前，需要登录，即命令。
    
    ```
    cat ~/GH_TOKEN.txt | docker login docker.pkg.github.com -u tourcoder --password-stdin
    ```
        
#### 部署 nginx

```
docker run -d -p 80:80 --name myNginx -v $PWD/nginx.conf:/etc/nginx/nginx.conf:ro -v $PWD/conf.d:/etc/nginx/conf.d nginx
```

几点注意点：

1. 需要提前在本地创建 `nginx.conf` 文件，如果不创建该文件，上面的命令会自动创建一个 `nginx.conf` 的文件夹

2. 创建容器后，`nginx.conf` 文件是空白，所以 nginx 这个容器是没有运行的，需要在 `nginx.conf` 写入相关内容

    ```
    user  nginx;
    worker_processes  1;

    error_log  /var/log/nginx/error.log warn;
    pid        /var/run/nginx.pid;


    events {
        worker_connections  1024;
    }


    http {
        include       /etc/nginx/mime.types;
        default_type  application/octet-stream;

        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                          '$status $body_bytes_sent "$http_referer" '
                          '"$http_user_agent" "$http_x_forwarded_for"';

        access_log  /var/log/nginx/access.log  main;

        sendfile        on;
        #tcp_nopush     on;
    
        keepalive_timeout  65;

        #gzip  on;

        include /etc/nginx/conf.d/*.conf;
    }
    ```
    
    这是初始内容，也可以很省事的从容器里复制过来，执行命令 `docker cp 容器 ID:/etc/nginx/nginx.conf nginx.conf` 即可。
    
3. 在 `conf.d` 这个文件夹里创建相关的配置文件，比如 `default.conf`。写自己相关的配置文件。

关于如何禁止 IP 直接访问，可以查看[这篇文章](https://tourcoder.com/disable-access-by-ip-and-port-on-docker/)。

#### 部署 Caddy server

和 nginx 一样，Caddy 是一个 server，但不一样的是，它能自动配置 https，很方便。通过 docker 部署它也很方便。

```
sudo docker run -d -p 80:80 -p 443:443 -v $PWD/Caddyfile:/etc/caddy/Caddyfile -v $PWD/caddy_data:/data --name caddy_name caddy
```

解释

这里开启了两个端口的映射 80 和 443。

$PWD 是当前目录下

Caddyfile 是 Caddy 的配置文件，需要事先在当前文件夹下写好，不然该命令会自动生成一个 Caddyfile 的文件夹。

caddy_data 是对应的数据文件夹。

caddy 是选择了 caddy 这个 image，也可以用 `caddy:版本号` 来使用对应的版本。

caddy_name 是给当前运行的容器起个名字，比如这里可以写成 caddy_container 等

#### 部署 mysql/mariadb

直接命令行部署

```
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql
```

也可以通过 `docker-compose.yml` 来定义一个，然后通过 `docker-compose up -d mariadb` 启动。

```
mariadb:
    image: mariadb:10.4
    container_name: mariadb
    ports:
       - 3306:3306
    environment:
      - MYSQL_ROOT_PASSWORD=111111
      - MYSQL_DATABASE=databasename
      - MYSQL_USER=databaseuser
      - MYSQL_PASSWORD=111111
    volumes:
      - ~/Docker/mysql/db:/var/lib/mysql
```

当然也需要进行一些初始化的内容，进入到该容器中

```
docker exec -it mysql bash
```

登录账号

```
mysql -u root -p
```

创建一个数据库

```
CREATE DATABASE IF NOT EXISTS DB_NAME DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

创建一个用户并赋予权限

```
CREATE USER 'db_username'@'%' IDENTIFIED WITH mysql_native_password BY 'db_password';
```

- 其中 % 表示从任何 IP 登录的用户，也可以写成 `'db_username'@'localhost'` 或者 ``'db_username'@'IP地址'``，如果没有写则默认是 `%`

- 如果需要更新密码，则用 `update mysql.user set password='user_password' where user='db_username'`，更新完后，需要刷新权限 `flush privileges;`。

```
grant select,delete,update,insert on db.* to db_username@'localhost' identified by 'db_username';
```

- 如果是全部权限，则是 `grant all privileges on`，赋予权限后，则使用 `flush privileges;` 刷新下权限。

- 撤销权限用 `revoke`，比如 `revoke update on` 表示撤销 update 权限，同样所有则用 `revoke all on`。

#### 部署 MongoDB

执行命令

```
docker run --name mongodb -v /root/mongodb:/data/db -p 27017:27017 -d mongo --auth
```

其中 `-v /root/mongodb:/data/db` 是将容器的内容指向宿主机器 `/root/mongodb` 下，如果需要将备份的内容也指向宿主，则在上面命令中增加 `-v /root/mongodb/backup:/data/backup`，`--auth` 表示需要验证账号密码，这就需要创建账号密码，执行命令


```
docker exec -it mongodb /bin/bash 
```

或者

```
docker exec -it mongodb mongo
```

第一个命令是进入容器后运行 bash，第二个命令是进入容器后运行 mongo，如果是第一个命令则再次输入 `mongo` 进入数据库操作界面，第二个命令是已经进入数据库操作界面。然后选择数据库 `use 数据库名`，比如给 `admin` 数据库增加用户，则执行下面的语句创建一个账户，并赋予其密码 `123456` 

```
db.createUser({user:'admin', pwd:'123456', roles:[{role:'userAdminAnyDatabase', db:'admin'}]});
```

创建完成后，可以通过 `db.auth('admin', '123456')` 检查是否能够连接。想要修改密码的话则 `db.changeUserPassword('admin','654321');`

想给某个数据库创建账户，比如给 `newdb` 创建账户，则

```
use newdb;
db.createUser({user:'uname', pwd:'upassword', roles:['readWrite']});
```

也可以

```
db.createUser({user:'uname', pwd:'upassword', roles:[{role:'readWrite', db:'newdb'}]});
```

至于赋予某个用户的权限则使用 `db.grantRolesToUser('admin', [{role:'root', db:'admin'}])`

查看数据库中的用户 `db.system.users.find()`，或则在某个数据库下使用 `show users` 查看当前库下的用户。

#### 部署 Redis

先在 Redis 的官方下载一个稳定版本的配置文件，即 redis.conf

```
wget http://download.redis.io/redis-stable/redis.conf
```

打开该文件，将 `daemonize` 后面改成 `no`，将该文件保存在某一个文件夹中，比如，`~/Docker/redis/redis.conf`。

通过命令即可创建一个 redis 的容器

```
docker run -d --name redisdemo -p 6379:6379 -v ~/Docker/redis/redis.conf:/etc/redis/redis.conf --privileged=true redis redis-server /etc/redis/redis.conf
```

还可通过命令 `docker-compose up -d` 将该容器拉起，`docker-compose.yml` 内容如下

```
version: '3'
services:
    redis:
      image: redis:latest
      container_name: redisdemo
      privileged: true
      ports:
        - "6379:6379"
      volumes:
        - ~/Docker/redis/redis.conf:/etc/redis/redis.conf 
      command: redis-server /etc/redis/redis.conf 
```

完成。

#### 帮助

有时候 Docker 会出现无法停止删除容器的情况，可以先执行命令

```
sudo systemctl restart docker.socket docker.service
```

然后就可以操作了。
