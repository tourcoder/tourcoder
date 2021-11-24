---
title: "Ghost中文安装指南"
slug: ghost-install-manual
author: Bin Hua
lastmod: 2020-07-06 16:53:47
date: 2016-10-11 06:52:16
tags: ["ghost", "blog", "vultr"]
---

“哥，你的博客好漂亮啊，是最近写的吗？”，同事猛不丁的对我嚷嚷起来。

“不是，这个博客是我在一个开源的博客程序上更改的。”，我头也不抬的忙着手上的事情。

“那你帮我也弄一个呗！”，同事凑了过来看着我。

“你去我的 Github 上看吧，教程我分享了”。

同事立刻访问我的 Github 地址，找到了那篇教程。

Ghost 是一个 Markdown 格式的博客程序，使用 Node.js 编写，目前开源在 [Github](http://github.com/tryghost/ghost) 上。

**服务器的选择**

为了方便安装该博客，建议购买国外的 VPS，比如 vultr。点[这里](https://www.vultr.com/?ref=6870749)链接购买，注册即可得到 $10。

**如何安装？**

2019 年更新：下面不用看了，可以通过 Docker 直接一步安装

```
sudo docker run -d --name tcblog -p 3000:2368 -v ~/tcblog/content:/var/lib/ghost/content ghost
```

网上有很多的安装教程，这里我说下在 Ubuntu 上如何安装。

- 更新系统

    ```
    #sudo apt-get update
    #sudo apt-get upgrade
    ```
    
- 安装 Node.js 环境

    ```
    # apt-get install g++ make python python-software-properties
    # add-apt-repository ppa:chris-lea/node.js
    # apt-get update
    # apt-get install nodejs
    ```
    
    Update: 2017-09-01: 从1.0版本后，有了更简单的安装方式，去[官网](https://docs.ghost.org/docs/install)查看

- 下载并安装 Ghost
    
    ```
    # cd
    # wget https://ghost.org/zip/ghost-latest.zip
    # unzip ghost-latest.zip -d ghost
    # cd ghost
    # npm install --production
    ```
    
- 配置 Ghost 监听本机所有 IP，修改 127.0.0.1 为 0.0.0.0

    ```
    # vi config.js
    
    server: {
        host: '0.0.0.0',
        port: '2368'
    }
    ```
    
- npm 启动 Ghost，默认端口是 2368，启动后可通过 http://ip:2368 访问。

    ```
    #npm start
    ```
    
- 让 Ghost 程序自动在后台启动运行，则可以通过脚本加到 Upstart 里。

    ```
    # vi /etc/init/ghost.conf
    start on startup
    script
      cd /path/ghost
      npm start
    end script
    ```
    
    这样就可以方便的通过 `service ghost start/restart/stop` 对 Ghost 进行操作了。

- 还可以使用 PM2 和 forever 这两个利器进行管理使用。

    - forever 方式

        在博客根目录下安装 forever

        ```
        npm install forever
        ```
        
        将 forever 加入到 bashrc 中

        ```
        echo "export PATH=/你博客的根目录/node_modules/forever/bin:$PATH" >> ~/.bashrc
        source ~/.bashrc
        ```
        
        让 ghost 用 forever 启动

        ```
        NODE_ENV=production /你博客的根目录/node_modules/forever/bin/forever start index.js
        ```

- 去掉端口 2368 的方式

    去掉端口可以通过 ngixn 或着 apache。

    - Apache

        安装 Apache 后，修改 apache2.conf 文件，在下面加入

        ```
        LoadModule proxy_module /usr/lib/apache2/modules/mod_proxy.so
        LoadModule proxy_http_module /usr/lib/apache2/modules/mod_proxy_http.so
        ```

        载入 module。然后创建对应的配置文件。

        ```
        <VirtualHost *:80>
            ServerName domain.com
            #ServerAlias blog.domain.com
            ProxyRequests off
            ProxyPass / http://127.0.0.1:2368/
            ProxyPassReverse / http:/127.0.0.1:2368/
        </VirtualHost>
        ```

    - Nginx

        安装 Nginx 后，创建对应的配置文件

        ```
        server {
                listen 0.0.0.0:80;
                server_name domain.com;
                access_log /var/log/nginx/domain.com.log;
                location / {
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header HOST $http_host;
                        proxy_set_header X-NginX-Proxy true;
                        proxy_pass http://127.0.0.1:2368;
                        proxy_redirect off;
                }
        }
        ```

        就这样，完成!

照着这篇教程，一会功夫，同事架设好了自己的博客，这会，他正缠着我给他写个漂亮的主题。