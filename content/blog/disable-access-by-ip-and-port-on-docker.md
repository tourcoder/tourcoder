---
title: "Docker 中禁止 IP 和端口访问"
slug: "disable-access-by-ip-and-port-on-docker"
author: "Bin Hua"
lastmod: 2019-12-27 05:59:42
date: 2019-12-27 05:59:42
tags: ["docker", "nginx"]
---

先说两个概念

1. Docker 的容器是一个独立的个体，每一个容器可以理解成是一个独立的 VPS

2. 每个容器可以单独的运行，可以单独的被访问

#### 准备工作

一台安装了 Docker 及相关工具的机器，其 IP 地址是 `123.123.123.123`，默认所有的端口都是开放的，可访问的。

这里用 nginx 作为代理，部署一个网站，监听的端口为 `3000`，网站镜像已经完成，叫 `webapp`

#### 操作步骤

一般情况下，我们可能会这样部署（为了更好的阐明情况，这里使用了 `docker run` 的方式）

部署该网站

```
docker run -d -p 3000:3000 --name myWebapp webapp
```

此时不需要通过 nginx 作为代理，即可以通过 `ip:port` 的方式访问到该网站，即 `http://123.123.123.123:3000`。

但我想实现的是禁止通过 IP 端口这种方式访问，那在 nginx 中设置禁止 IP 访问就好了，即启动一个 nginx 的容器，配置下 conf 文件，即

```
docker run -d -p 80:80 --name myNginx -v $PWD/conf.d:/etc/nginx/conf.d nginx
```

然后在配置文件 `default.conf` 中增加

```
server {
    listen 80;
    return 404;
}
```

这样的确是禁止了 IP 直接访问，但在访问 `ip:port` 的时候，依旧能够被访问到，所以上面的做法是错误的！

原因就是本文开头说到的两个概念，80 端口的访问被绑定在了 nginx 上，所以当访问 IP 时，nginx 会根据配置返回 404， 但在访问 `ip:port` 时，和 nginx 一点关系没有，它是直接访问已经创建的 `myWebapp` 这个容器。

所以正确的做法是

-  部署网站时，无需将端口暴露出来

    ```
    docker run -d --name myWebapp webapp
    ```
    
- 将网站容器的名字关联到 nginx 的容器

    ```
    docker run -d -p 80:80 --link myWebapp:myWebapp --name nginxman -v $PWD/conf.d:/etc/nginx/conf.d nginx
    ```
    
- 在 nginx 的配置文件中，通过该网站容器名字对网站的容器进行代理操作

    ```
    server {
        listen 80;
        server_name tourcoder.com;
        location / {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header HOST $http_host;
            proxy_set_header X-NginX-Proxy true;
            proxy_pass http://myWebapp:3000;
            proxy_redirect off;
            proxy_set_header X-Real-PORT $remote_port;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```
    
此时，只可以通过 nginx 中配置的域名来访问该网站，通过 `ip:port` 将无法访问到该网站。

至于如何用 `docker-compose.yml` 来写，可以去看 docker 的帮助说明。

上面的方法在多站点的时候会遇到问题，更为科学的配置方式是通过 `docker network` 来配置，依旧用上面的例子来说明

先创建一个网络

```
docker network create network-name
```

可以通过 `docker network ls` 查看网络的情况，这里也可以通过参数给设置网络的 IP 等，具体可以通过 `docker network --help` 查看命令，也可以访问 `docker network` 的[官方资料](https://docs.docker.com/engine/reference/commandline/network/)。

然后基于该网络创建 `nginx` 的容器

```
docker create --name myNginx --network network-name -p 80:80 nginx:latest
```

如果像上面已经创建了一个 nginx 的容器，则将它关联到该网络

```
docker network connect network-name myNginx
```

和上面一样，不暴露端口的部署网站，并将该网站关联到该网络

```
docker network connect network-name myWebapp
```

最后也还是和上面一样配置的 `nginx config` 文件即可。