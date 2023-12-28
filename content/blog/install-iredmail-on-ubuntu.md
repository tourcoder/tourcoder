---
title: "使用 iRedmail 架设邮局系统"
slug: "install-iredmail-on-ubuntu"
author: "Bin Hua"
date: 2019-08-16 14:50:28
tags: ["Gmail", "ubuntu", "邮局系统", "iredmail", "workmail"]
draft: false
---

因为几个因素，放弃了现在购买的邮局系统，自行搭建了 iRedmail，记录下整个过程。

#### 准备

- Ubuntu 18.04

    iRedmail 会帮你安装很多东西，所以它要求是一个没有安装任何东西的全新系统。

- iRedmail 0.9.9

#### 操作

- 更新系统

    ```
    sudo apt update
    sudo apt upgrade -y
    ```
    
- 设置 `FQDN hostname`

    FQDN 全称 `fully qualified domain name`，编辑两个文件
    
    ```
    sudo vi /etc/hostname
    ```
    
    比如你的设置是 `mail.tourcoder.com`，那么这里应该是 `mail`
    
    ```
    sudo vi /etc/hosts
    ```
    
    将内容编辑成 `127.0.0.1 mail.tourcoder.com mail localhost localhost.localdomain`
    
    重启系统后，通过 `hostname -f` 查看，是否生效。
    
- 安装 iRedmail

    去其[官网](https://www.iredmail.org/download.html)下载最新版本，当前版本是 `0.9.9`
    
    ```
    wget https://bitbucket.org/zhb/iredmail/downloads/iRedMail-0.9.9.tar.bz2
    tar -zvxf iRedMail-0.9.9.tar.bz2
    cd iRedMail-0.9.9
    chmod +x iRedMail.sh
    sudo bash iRedMail.sh
    ```
    
    根据提示一步一步下去，即可。
    
- 安装 ssl

    我使用了 Let's Encrypt，因为需要用到 `git`，先安装 `git`，输入命令
    
    ```
    sudo apt-get install git-all
    ```
    
    然后安装 Let's Encrypt
    
    ```
    mkdir ~/src
    cd ~/src
    git clone https://github.com/letsencrypt/letsencrypt
    cd letsencrypt
    sudo chmod g+x letsencrypt-auto
    ./letsencrypt-auto
    ```
    
    这里会要求输入邮箱还有域名，其实也可以将最后的命令改成
    
    ```
    ./letsencrypt-auto certonly --email=hello@tourcoder.com -d mail.tourcoder.com 
    ```
    
    因为我使用的是 nginx，得到的结果是
    
    ```
    IMPORTANT NOTES:
     - Congratulations! Your certificate and chain have been saved at:
       /etc/letsencrypt/live/mail.tourcoder.com/fullchain.pem
       Your key file has been saved at:
       /etc/letsencrypt/live/mail.tourcoder.com/privkey.pem
       Your cert will expire on 2019-11-14. To obtain a new or tweaked
       version of this certificate in the future, simply run
       letsencrypt-auto again. To non-interactively renew *all* of your
       certificates, run "letsencrypt-auto renew"
     - If you like Certbot, please consider supporting our work by:

       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le
    ```
    
    用这里的地址覆盖之前自签的证书
    
    ```
    sudo cp /etc/letsencrypt/live/mail.tourcoder.com/fullchain.pem /etc/ssl/certs/iRedMail.crt
    sudo cp /etc/letsencrypt/live/mail.tourcoder.com/privkey.pem /etc/ssl/private/iRedMail.key
    ```
    
    最后重启服务
    
    ```
    sudo systemctl restart postfix
    sudo systemctl restart nginx
    sudo systemctl restart dovecot
    ```
    
到此，所有的安装都完成了，能够通过 `https://mail.tourcoder.com/mail` 是用户登录地址，管理的地址是 `https://mail.tourcoder.com/iredadmin` 是管理中心。

- 域名设置

    需要设置对应的 DNS
    
    - MX 记录

        ```
        tourcoder.com.   10    mx      mail.tourcoder.com
        ```
        
    - SPF 记录

        ```
        tourcoder.com.   3600    IN  TXT "v=spf1 mx mx:tourcoder.com -all"
        ```
        
        也可以通过 IP 地址来确定
        
        ```
        tourcoder.com.   3600    IN  TXT "v=spf1 ip4:服务器的ip -all"
        ```
        
    - DKIM 记录

        在服务器端输入 `amavisd showkeys`，不过我在 ubuntu 上提示没有，搜索了后尝试用 `amavisd-new showkeys`，会得到结果
        
        ```
        dkim._domainkey.tourcoder.com.	3600 TXT (
          "v=DKIM1; p="
          "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+xSpKRMa1ryjcaPeTh8dEjyzr"
          "KfLhh3pN9RxTckJ4U4Uds1246CVMpUnwq4/nJ3py55mDh6NIDK02mVfPPSmJJPsG"
          "ulQCUrE/H1UMsBLsynKb3BXwGeI44QdEPDe9bCRizdYALZf/WRwR6dAvgw+/kmis"
          "gGNJ5LloKim1F8GJBwIDAQAB")
        ```
        
#### 后续

搭建完成了邮局服务器，后续才是最麻烦的事情，需要想其他域名服务商"报备"

- Google 家的：[https://postmaster.google.com/](https://postmaster.google.com/)

- 微软家的：[https://sendersupport.olc.protection.outlook.com/pm/](https://sendersupport.olc.protection.outlook.com/pm/) 

- QQ 家的：[https://openmail.qq.com/](https://openmail.qq.com/)

- SPF 查询工具：[https://www.kitterman.com/spf/validate.html](https://www.kitterman.com/spf/validate.html)

基本就是这么一个操作咯。

#### 一些点

有人按我的教程成功架设了，但只能接收到邮件却发不出邮件，如果遇到这种情况，第一时间去检查 log，log 的地址为 `/var/log/maillog`，打开 log，比如下面

![](https://storage.tourcoder.com/tcblog/install-iredmail-on-ubuntu.png)

这里的 log 在说无法连接网络，其实市面上绝大部分的 vps 服务商都将 25 这个端口给封掉的，需要联系他们开启。

关于 465 端口，iRedmail 默认是不启用 465 端口的，这就需要手工开启，首先

```
sudo vi /etc/postfix/master.cf
```

将如下内容取消注释

```
smtps inet n - y - - smtpd
-o syslog_name=postfix/smtps
-o smtpd_tls_wrappermode=yes
-o smtpd_sasl_auth_enable=yes
-o smtpd_reject_unlisted_recipient=no
-o smtpd_client_restrictions=$mua_client_restrictions
-o smtpd_helo_restrictions=$mua_helo_restrictions
-o smtpd_sender_restrictions=$mua_sender_restrictions
-o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
-o milter_macro_daemon_name=ORIGINATING
```

在配置文件中开启 ssl

```
sudo vi /etc/postfix/main.cf
```

找到证书所在位置，前面增加一行 

```
smtpd_use_tls = yes
```

即

```
smtpd_use_tls = yes
smtpd_tls_key_file = /etc/ssl/private/iRedMail.key
smtpd_tls_cert_file = /etc/ssl/certs/iRedMail.crt
smtpd_tls_CAfile = /etc/ssl/certs/iRedMail.crt
smtpd_tls_CApath = /etc/ssl/certs
```

最后重启下 `systemctl restart postfix.service` 即可。