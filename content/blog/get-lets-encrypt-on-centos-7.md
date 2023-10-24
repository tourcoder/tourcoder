---
title: "CentOS 7 下签发 Let's Encrypt https 证书"
slug: "get-lets-encrypt-on-centos-7"
author: "Bin Hua"
lastmod: 2019-02-09 15:15:00
date: 2019-02-09 15:15:00
tags: ["ssl", "centos", "https", "let's encrypt"]
---

在当今网络世界，HTTPS 是必备的，但 SSL 证书买起来比较贵，多亏 Let's Encrypt 提供了免费的证书，地址是：[https://letsencrypt.org/](https://letsencrypt.org/) 希望大家可以去捐赠他们。

安装 Let's Encrypt 有软件和手工申请两种方式，另外这里还可以通过服务商申请就不介绍了。我自己是自己写了个脚本程序来处理的，本文介绍的是一个开源的项目 Certbot。

**通过 Certbot 客户端申请**

- 安装 epel 软件源 
	
    ```
    sudo yum install epel-release
    ```
    
- 安装 certbot 和 certbot 的 nginx 插件 
	
    ```
    yum install certbot-nginx
    ```
    
- 获取证书 
	
    ```
    certbot --nginx
    ```
    
基本到这里就完成了，不过这里有个问题就是如果你的 `nginx` 不是直接 `yum install` 安装，而是通过源码安装，则在最后一步会有问题，需要将地址指向 `sbin/nginx`。

也可以先配置 `nginx` 文件

```
server {			
    listen 80;			
    server_name domain.com;			
    root /usr/local/domain.com;			
    index index.html index.htm;		
}
```
    
然后执行命令
	
```
certbot certonly --webroot -w /usr/local/domain.com -d domain.com -m admin@domain.com --agree-tos
```
    
完成后即可得到结果，证书保存的位置是 `/etc/letsencrypt/live/domain.com/`

此时配置 nginx 的 config 文件
```
server {
    listen 443 ssl;
    server_name domain.com;
    root /usr/local/domain.com;
    index index.html index.htm;
    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    ssl_session_timeout 1d;ssl_session_cache shared:SSL:50m;
    ssl_session_tickets on;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128:AES256:AES:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK';
}
```
    
- PFS

    在配置 nginx 的时候会有一个 PFS 的选项，关于 PFS 的解释，请看下面的相关阅读第二条目

    - 生成 PFS 键值
	
        ```
        mkdir /usr/local/ssl/private/ -p		
        cd /usr/local/ssl/private/		
        openssl dhparam 2048 -out dhparamfile.pem
        ```
    
    - 在 nginx 中使用
		
        ```
        ssl_dhparam /usr/local/ssl/private/dhparamfile.pem;
        ```

**通过手工申请**

省略

**有效期**

因为该证书是有有效期的，90 天为有效期，所以应该在 90 天到期前进行更新，简单的命令即可

```
certbot renew --dry-run //更新证书
certbot renew --quiet //静默方式
```

不想手工签发的可以通过 cron 脚本来设置更新，记得更新完后重启 nginx。

**相关阅读**

- https://wiki.mozilla.org/Security/Server_Side_TLS

- https://en.wikipedia.org/wiki/Forward_secrecy