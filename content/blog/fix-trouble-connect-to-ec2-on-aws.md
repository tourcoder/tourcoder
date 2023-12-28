---
title: "AWS ec2 实例连接的问题"
slug: "fix-trouble-connect-to-ec2-on-aws"
author: "Bin Hua"
date: 2019-03-18 08:09:00
tags: ["aws", "ec2"]
draft: false
---

相信不少人被 aws ec2 连接的问题给折腾得够呛，每每看到 `Permission denied (publickey,gssapi-keyex,gssapi-with-mic)` 这句话，头都要大了。搜索了下，各种答案，但没有一个有效的。

这里提供一些解决的办法和思路，注意，不一定能够 100% 解决这个问题，要知道连 AWS 官方都没有一个靠谱的办法 :(

#### 解决思路

- 查看你的用户名是否正确

    AWS 中创建实例时，选择不同的系统他的用户名也会不一样，比如我常用的 centOS 系统，它的用户名是 centOS，ubuntu 系统是 ubuntu，Amazon Linux 系统是 ec2-user，debian 系统是 admin 或者 root，还有其他的系统用户名可以去 aws 搜索看看。
    
- 权限问题

    如果不是上面用户名错误，那么权限问题就占了很大的比例。权限问题分两个，一个是在本地，一个是在服务器端。
    
    - 本地

        本地的 pem 文件，运行命令 `chmod 400 key.pem` 更改权限，然后再尝试是否连接得上。
        
    - 服务器端

        服务器端 key 的权限问题，运行下面几个命令，注意，不同的服务器，这里的 username 会不一样，我是在 centos 上解决的，所以这里是 centos
        
        ```
        chmod 600 /home/centos/.ssh/authorized_keys
        chmod 700 /home/centos/.ssh
        chmod 700 /home/centos
        ```
        
        一般这里的权限设置后，问题就会解决，我自己就是这样解决的。
        
- pem 文件问题

    确保本地的 pem 文件是完整的，不是错误的。
    
经过以上方式基本能解决这个让人头疼的问题，如果你有什么其他解决方式的，欢迎告诉我。