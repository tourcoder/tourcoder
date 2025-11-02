---
title: "使用 Cloud SQL Auth Proxy 助力客户端连接 GCP Cloud SQL PostgreSQL"
slug: "cloud-sql-auth-proxy-connect-gcp-postgresql"
author: "Bin Hua"
date: 2025-11-02T07:08:06Z
tags: ["Google Cloud", "Cloud SQL Auth Proxy", "PostgreSQL"]
draft: false
---

### 原由

之前在 macOS 上都用客户端通过 IP 方式直接连接 Cloud SQL PostgreSQL，但这里会有几个问题

1. 操作麻烦：比如需要将当前客户端所在的 IP 添加到 Cloud SQL 实例的「已获授权的网络」里，每次 IP 变化，每次都要增加更新。如果嫌弃麻烦，也可以用下面的高风险的方式。

2. 安全风险：如上面所说到的，将 `0.0.0.0/0` 增加到实例的「已获授权的网络」，这也就意味着这个 Cloud SQL 实例将对整个互联网开放，任何知道实例公共 IP 地址的人都可以尝试连接。

心血来潮，尝试下 Cloud SQL Auth Proxy 这个解决方案，它可以不需要将本地的 IP 添加到实例的「已获授权的网络」里，更不需要 `0.0.0.0/0`，但能方便在本地通过客户端连接 Cloud SQL 实例。

下面是记录折腾过程

### 折腾过程

#### 安装必备的工具

0. 终端

	下面的操作都要在终端中进行，终端即 Terminal，系统自带。

1. 安装 gcloud CLI

	有 homebrew 的，在终端中直接通过 `brew install google-cloud-sdk` 命令安装即可。我讨厌 homebrew 的臃肿，所以手动安装了，安装的文档参考 [GCP 的官方文档](https://docs.cloud.google.com/sdk/docs/install?hl=zh-cn)。

2. 安装 Cloud SQL Auth Proxy

	关于它的介绍，可以看[这里](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy?hl=zh-cn)，这里以 macOS 为例

	```
	curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.18.2/cloud-sql-proxy.darwin.amd64
	```

	在终端中执行上面命令即可完成安装，执行 `chmod +x cloud-sql-proxy` 命令给刚下载的脚本执行权限

#### 连接

1. 初始化 gcloud CLI 并设置应用默认凭证 (ADC)

	在终端中执行下面的命令

	```
	gcloud init
	```

	完成基础配置，比如选择 project，设置地区（选择错了，可以通过 `gcloud config set compute/region NAME` 来更改）


	```
	gcloud auth application-default login
	```

	登录并授权，完成 ADC 配置，请确保选择的账户具有 Cloud SQL 客户端权限。

2. 运行 Cloud SQL Auth Proxy

	在终端中回到 `cloud-sql-proxy` 所在的位置，执行 `./cloud-sql-proxy "INSTANCE_CONNECTION_NAME"`，成功后得到结果

	```
	2025/11/02 14:52:43 Authorizing with Application Default Credentials
	2025/11/02 14:52:45 [foobar] Listening on 127.0.0.1:5432
	2025/11/02 14:52:45 The proxy has started successfully and is ready for new connections!
	```

3. 第三方数据库管理软件

	我使用的是 TablePlus，在数据库地址这块填写上面的 127.0.0.1，端口是 5432，用户名，数据库，密码等保持不变，即可成功连接。