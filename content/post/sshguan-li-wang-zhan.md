---
title: "SSH管理网站"
slug: "sshguan-li-wang-zhan"
author: "Bin Hua"
lastmod: 2020-08-13 08:52:59
date: 2011-04-06 06:31:24
tags: [ssh", "shell", "cmd"]
---

今天家里的21端口又莫名其妙的被封了，懒得动，又不想去公司，所以，研究了下SSH管理网站

进入命令 `ssh user@ip -i id_rsa`  (可以省略为  ssh user@ip)，回车后会提示你输入 `yes or no`，输入完整的 yes，回车后会要求你输入密码，输入密码，OK，你可以开始管理你的站点了
附带一些常用命令和信息

- Linux文件管理命令

    ```
    $ls 列出当前文件夹下所有内容

    $ls -o 列出当前文件夹中所有内容，含详细信息，但不列出group

    $ls -l 同上，含group信息

    $ls -a 列出当前文件夹中所有内容，包含以”.”开头的文件

    $ls -t 按更改时间排序

    $ls -v 按版本先后排序

    $cd [dir] 进入文件夹

    $pwd 显示当前路径

    $mkdir [dir] 新建文件夹

    $chmod [Mode] [dir]，其中Mode形如”755″或”777″等。

    $chmod [Mode] [file]

    $chmod -R [Mode] [dir]，递归形式，即将目标文件夹内所有文件均改变权限

    $rm [file] 删除文件/文件夹

    $rm -f [file] 强行删除，忽略不存在的文件，无提示

    $rm -r [file] 递归删除所有内容

    $cp [options] [source] [destination] 拷贝，其中[options]可以为-f（强行拷贝）或-r（递归拷贝），常用-a选项来复制整个目录树，常用于备份或者复制安装程序

    $mv [options] [source] [destination] 重命名或移动，[options]常用：-f（强行移动/重命名）, -i（移动/重命名前尝试）, -u（更新）
    ```
    
- wget下载

    ```
    $wget http://weburl/file.zip
    ```
    
- 解压缩
    
    ```
    $unzip [options] [file] 解压.zip文件
    $tar [options] [file] 解压.tar, .tar.gz等文件
    ```
    
    其中 [options] 用法：
    
    ```
    -c 生成新的备份，并同时覆盖旧的备份文件

    -x 从备份文件中解压缩

    -t 列出备份文件内的文件目录

    -v 显示所有被操作文件列表

    -f 在指定位置生成备份

    -u 将不存在于备份中的文件，或将已经被更改的文件加入该备份中。
    ```
    
    举例说明：

    ```
    tar cvf filename.tar //制作备份

    tar cvf tarfile.tar .//filename /将filename的文件备份到tarfile.tar里面

    tar tvf filename.tar //列出tar文档的内容

    tar xvf filename.tar //从tar文档中导出文件

    tar zxpvf filename.tar.gz //从tar.gz文档中导出文件

    tar zxvf filename.tar.gz //同上

    tar xvf tarfile.tar ./filename //导出tar文件中的单个文件
    ```

- 备份WP博客举例：其中博客所在目录为blog

    打包博客目录 `tar cvf blogbackup.tar.gz blog`

    删除备份文件 `rm blogbackup.tar`
