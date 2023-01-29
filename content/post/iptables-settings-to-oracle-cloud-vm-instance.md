---
title: "甲骨文 vps 的防火墙设置"
slug: "iptables-settings-to-oracle-cloud-vm-instance"
author: Bin Hua
lastmod: 2021-05-25T13:14:36Z
date: 2021-05-25T13:14:36Z
tags: ["cloud", "oracle", "甲骨文", "IPv6"]
---

测试签发的银行卡，顺道撸了个甲骨文云的永久免费的 VPS，在上面搭建了一个饭饭服务。搭建后发现无法访问需要用到的 80/443 这两个端口。

在终端下执行命令 `telnet 域名或IP 端口`，因为在 macOS 下默认是没有 `telnet` 的可以直接安装或者使用 `nc`，即

```
nc -v domain.com port
```

得到的结果是 `nc: connectx to domain.com port 443 (tcp) failed: Connection refused`，说明端口未通。

#### 解决办法

- 先添加 ingress

    点击 vps，选择 `Primary VNIC` 下面的 `Subnet`，然后在 `Security Lists` 下选择 `Default Security List for ...`，在 `Ingress Rules` 下增加一条 Rule。

    SOURCE TYPE \- CIDR

    SOURCE CIDR \- 0.0.0.0/0

    IP PROTOCOL \- All Protocols(也可以根据自己的情况选择)

- 在 vps 中增加防火墙信息

    ```
    sudo iptables -P INPUT ACCEPT
    sudo iptables -P FORWARD ACCEPT
    sudo iptables -P OUTPUT ACCEPT
    sudo iptables -F
    ```

重启服务器即可。

### 增加 IPv6

进入所在的 oracle cloud 的节点，我的是[韩国](https://console.ap-seoul-1.oraclecloud.com)节点，其他的节点比如[日本](https://console.ap-tokyo-1.oraclecloud.com)，[美西](https://console.us-phoenix-1.oraclecloud.com)。登录后，

- 选择左上角主菜单的`网络->虚拟云网络`，选择对应的虚拟网络

- 在`资源->CIDR` 中增加 `Add IPv6 CIDR Block`，添加完成

- 在`资源->子网`中选择对应的网络，勾选`启用 IPV6 CIDR 块`，下面填写 `ee`。

- 在`资源->路由表`中选择对应的路由后面的点，选择`路由详情->添加路由规则`，增加一条 IPv6 的路由信息

  目标类型：Internet 网关
  
  目的地 CIDR：`::/0`
  
- 在`资源->安全列表`中选择对应的安全列表点击后面的点，选择`详情`，增加一条出站和一条入站规则

  目的地类型：CIDR

  目的地 CIDR：`::/0`

  IP协议：所有协议

- 选择左上角主菜单的`计算->实例`，选择服务器，在`资源->附加的 VNIC` 中选择对应的 VNIC 后面的点，选择`详情`，选择 `IPv6 地址`，然后选择`自动分配 IPv6 地址` 即可。

**服务器中设置**

使用命令 `ip addr` 查看 IPv6 是否生效，一般都是自动生效的。
