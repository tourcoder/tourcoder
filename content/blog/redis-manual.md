---
title: "Redis 学习笔记"
slug: "redis-manual"
author: "Bin Hua"
lastmod: 2019-01-11 03:51:15
date: 2019-01-11 03:51:15
tags: ["redis", "笔记"]
---

Redis 可以理解为缓存数据库

### macOS

#### 安装

Redis 有多种安装方式

- 手动安装

    进入到 redis 官网，找到下载到源文件(最好使用稳定版)，然后执行命令即可，我当前看到的稳定版本是 5.0.3
    
    ```
    wget http://download.redis.io/releases/redis-5.0.3.tar.gz
    tar -zvxf redis-5.0.3.tar.gz
    mv redis-5.0.3 redis
    cd redis
    make
    make install
    ```

- macOS 下 Homebrew 安装

    Homebrew 的介绍看[这里](https://brew.sh)，在终端中输入
    
    ```
    brew install redis
    ```
    
    即可完成安装，安装的位置
    
    ```
    /usr/local/bin //命令工具
    /usr/local/etc //redis.conf 所在
    ```
    
#### 启动

可以通过命令 `ps aux | grep redis` 查看 redis 服务是否已经启动。

- Homebrew 启动

    ```
    brew services start redis
    ```
    
    即可在后台运行 redis 服务。
    
- 手动启动

    ```
    /usr/local/bin/redis-server /usr/local/etc/redis.conf
    ```

    在前台启动 redis 服务，启动后效果如下
    
    ![](/imgs/redis-manual-01.png)
    
#### bin 文件夹下命令工具

- redis-server: Redis服务器

- redis-cli: 命令行客户端

- redis-benchmark: Redis的性能测试工具

- redis-check-aof: AOF文件修复工具

- redis-check-dump: RDB文件检测工具

- redis.conf: Redis的配置文件

### CentOS 下

#### 安装

直接通过 `yum` 来安装，但一般需要先增加 epel-release 库，并更新

```
sudo yum install epel-release -y
sudo yum update -y
```

然后直接安装

```
sudo yum -y install redis
```

#### 启动

```
sudo systemctl start redis
```

#### 其他命令

- systemctl start redis.service #启动redis服务器

- systemctl stop redis.service #停止redis服务器

- systemctl restart redis.service #重新启动redis服务器

- systemctl status redis.service #获取redis服务器的运行状态

- systemctl enable redis.service #开机启动redis服务器

- systemctl disable redis.service #开机禁用redis服务器

#### 配置

编辑文件 `vi /etc/redis.conf`

```
#bind 127.0.0.1
```

注释掉表示允许远程访问

```
#requirepass foobared
```

去掉注释，更改成你的代码

```
daemonize no
```

将 `daemonize` 从 `no` 改成 `yes`，可后台启动。

### Debian 下

```
sudo apt update -y
sudo apt install redis-server -y
sudo systemctl status redis-server //检查是否运行
```

#### 配置

```
sudo vi /etc/redis/redis.conf
```

将里面的 `supervised no` 改成 `supervised systemd`，然后重启 `sudo systemctl restart redis`

至于其他的看上面 centos 部分，还有一个重名的问题，可以自行搜索。