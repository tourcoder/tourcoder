---
title: "在线版的 VSCode: Code Server"
slug: "code-server-vscode-online"
author: "Bin Hua"
lastmod: 2021-07-19T11:31:48Z
date: 2021-07-19T11:31:48Z
tags: ["VSCode", "GitHub"]
---

一直没有机会获得 GitHub 的 Codespaces 权限，索性安装了个开源版本的 VSCode，项目地址是 [https://github.com/cdr/code-server](https://github.com/cdr/code-server).

### 准备工作

安装了 Debian 9.x 的服务器一台

### 安装步骤

将最新版本的 code server 下载到服务器，并解压

```
curl -OL https://github.com/cdr/code-server/releases/download/v3.11.0/code-server-3.11.0-linux-amd64.tar.gz
tar -zxvf code-server-3.11.0-linux-amd64.tar.gz
```

### 启动服务

使用比较简单，直接调用即可

```
cd code-server-3.11.0-linux-amd64
./code-server
```

运行后，可得到下面的内容

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-01.png)

直接访问是访问不了的，需要修改配置

```
vi ~/.config/code-server/config.yaml
```

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-02.png)

将 `bind-addr` 中的 `127.0.0.1` 改成 `0.0.0.0` 即可，这里的端口也可以按需要修改。

### 使用

访问 `ip:端口` 即可得到如下界面

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-03.png)

输入上面配置文件 `~/.config/code-server/config.yaml` 中的密码即可进入。

### 一些使用界面

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-04.png)

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-05.png)

![](https://storage.tourcoder.com/tcblog/code-server-vscode-online-06.png)

功能还挺多的，还真的很不错。
