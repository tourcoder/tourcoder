---
title: "搭建 Docker 私有仓库"
slug: "create-your-own-docker-registry"
author: "Bin Hua"
lastmod: 2020-07-18 05:39:20
date: 2020-01-13 04:25:46
tags: ["docker", "registry", "self-hosted"]
---

安全起见，不想用 Docker Hub 的私有服务，也不想用 GitHub 的 Docker registry，那么剩下的办法就是自建。挺好，Docker 提供了这方面的内容。

先下载 registry

```
docker pull registry
```

然后启动一个 registry 的容器

```
docker run -d -p 5000:5000 --restart=always --name=registryman -v $PWD/registrydata:/var/lib/registry registry
```

这样就是搭建完成了。

测试下过程，先下载一个 `nginx`

```
docker pull nginx:latest
```

然后通过 `docker images` 查看该 nginx 镜像的 `image ID`，我这里的 `image ID` 是 `231d40e811cd`，修改该镜像的 tag

```
docker tag 231d40e811cd server_ip:5000/nginx
```

将该镜像上传到该私有的 registry

```
docker tag 231d40e811cd server_ip:5000/nginx
```

等待完成后即可。

其中需要注意的是，push 是强制 https 的，如果要通过 http 进行 push 的话，不同的系统有不同的处理办法

在 macOS 下

点击 Docker 的图标，进入设置

![dockerregistry00](/imgs/create-your-own-docker-registry-00.png)

在 `Insecure registries` 中输入私有 registry 的地址，如上图，保存重启。

在 Debian 下

修改 `/etc/default/docker`，增加一行，如下图

![dockerregistry01](/imgs/create-your-own-docker-registry-01.png)

修改 `/lib/systemd/system/docker.service`，增加一行，更新一行，如下图

![dockerregistry02](/imgs/create-your-own-docker-registry-02.png)

重启服务

```
sudo systemctl daemon-reload;
sudo service docker restart
```

有时候会需要一个 web 页面更方便的查看相关的内容，则可以使用 `docker registry web`，先拉取

```
docker pull hyper/docker-registry-web
```

运行一个 web 的容器

```
docker run -it -p 8080:8080 --restart=always --name registryWeb --link registryman -e REGISTRY_URL=http://server_ip:5000/v2 -e REGISTRY_NAME=localhost:5000 hyper/docker-registry-web
```

直接访问即可。