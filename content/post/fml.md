---
title: "我的翻墙服务器设置"
slug: "fml"
author: "Bin Hua"
date: 2023-05-15T23:30:08Z
tags: ["gfw", "翻墙"]
draft: false
---

我写这篇文章只是分享我是如何设置自己的 fml 服务的，~~没有将这篇文章放在我的博客是因为~~

~~1. 这篇文章可能会刺激到一些人的 G 点，不想给自己的博客找麻烦。~~

~~2. 放这里是个天然屏障，能让求知的人看到，同时也阻止了一些麻烦。~~

我几周前将这篇文章写在了自己的 GitHub 上，但今天觉得还是放回自己的博客吧。

## 准备工作

有时候，生活学习中比较糟糕的一个情况是想查的资料没法查，想用的服务被屏蔽。所以，我尝试用网上各位大牛们写的东西，组成自己的 fml 服务，让自己能在网络的世界里尽可能的自由穿行。

- VPS

  VPS 的选择有很多，我目前选择的有两家，Amazon 的 [AWS Lightsail](https://lightsail.aws.amazon.com) 和[搬瓦工 CN2 GIA](https://bandwagonhost.com/aff.php?aff=20329) 线路的 VPS。我是专机专用的原则，即将这些 VPS 仅作为代理使用。
  
  _名词解释：CN2 GIA 全称 China telecom Next Carrier Network- Global Internet Access ，其路由线路上骨干节点的 IP 均为 `59.43` 开头的。_
  
- 系统

  我主要用 Debian 的系统，习惯性升级到最新的内核和系统。
  
  **升级系统**
  
  ```
  apt update -y
  apt upgrade -y
  ```
  
  **新建用户**
  
  用默认的账户是比较危险的事情，我都会创建个新账户，同时赋予这个账户 `sudo` 的权限以及能够通过密码的方式 ssh 到这台 VPS。
  
  ```
  adduser fml
  usermod -aG sudo fml
  sed -ri 's/^#?(PasswordAuthentication)\s+(yes|no)/\1 yes/' /etc/ssh/sshd_config
  systemctl restart sshd
  ```
  
  **安装必要的软件**
  
  ```
  apt install wget curl -y
  ```
  
  **升级内核**
  
  可以通过 `uname -r` 查看当前系统的内核，现在新系统的内核一般都在 4.9+，作为代理工具，可以不升级。我只是习惯性升级到最新。操作步骤是
  
  - 在[这里](http://kernel.ubuntu.com/~kernel-ppa/mainline)找到需要用的内核，比如我选择了 4.10
  
    ```
    wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.10/http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.9/linux-image-4.9.0-040900-generic_4.9.0-040900.201612111631_amd64.deb
    ```
  
  - 下载内核文件后，执行 `dpkg -i` 命令更新，最后更新 grub 系统引导文件并重启
  
    ```
    dpkg -i linux-image-4.9.0-040900-generic_4.9.0-040900.201612111631_amd64.deb
    update-grub
    reboot
    ```
    
  **时间一致性**
  
  需要让 VPS 的时间和本地电脑的时间一致，在 root 模式下执行 `date` 或 `timedatectl` 查看 VPS 的时间，如果时间不一致，则通过 `timedatectl` 来修改时区
  
  ```
  timedatectl list-timezones
  ```
  
  查看有哪些时区，找到需要用的时区，比如我的是 `Asia/Shanghai`，通过命令
  
  ```
  timedatectl set-timezone Asia/Shanghai
  ```
  
  一般情况下，VPS 和本地时间存在时区的差异，分秒的时间几乎不差。但有时候也有出现差的情况，则用 `date -s '2012-12-11 01:01:01'` 这样修改时间，再将通过 `hwclock -w` 写入到硬件中。
  
## 基础内容

  现在阶段，我主要采用的是 [V2ray](https://www.v2fly.org) 的代理技术，因为喜欢折腾，都是自己手动安装。网上也有一些写好的脚本，建议新手使用。
  
  **一键安装脚本**
  
  在 root 模式下执行命令 `bash <(curl -s -L https://git.io/v2ray.sh)` 可以一步安装到位。至于管理，同样在 root 模式下执行 `v2ray` 即可管理。
  
  **手动安装**
  
  - 安装并配置 Caddy

    这里也可以用 Nginx，我用 Caddy 是省去签 ssl 证书。具体安装，以 Debian 为例
    
    ```
    apt install debian-keyring debian-archive-keyring apt-transport-https -y
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
    apt update -y
    apt install caddy -y
    ```
    
    更多的安装方式，看[官方文档](https://caddyserver.com/docs/install)。安装完成后，在 `/etc/caddy` 文件夹下有 `Caddyfile`，删除里面的内容，贴入以下内容
    
    ```
    your-domain-name.com {
     tls email@email.com
     handle_path /fml {
      reverse_proxy 127.0.0.1:1234
     }
    }
    ```
   
    这里的 `1234` 是 V2ray 的端口，要和 V2ray 保持一致。通过命令 `systemctl restart caddy` 重启 Caddy 即可。
   
  - 安装并配置 V2ray

    官方有很多安装方式，具体看[这里](https://www.v2fly.org/guide/install.html)，建议用官方的[安装脚本](https://github.com/v2fly/fhs-install-v2ray)。该脚本的主要脚本内容如下
    
    ```
    // 安裝和更新 V2Ray，以及 .dat 资料
    bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh)
    // 安装最新的 geoip.dat 和 geosite.dat
    bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-dat-release.sh)
    // 删除 V2ray
    bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh) --remove
    ```
    
    安装后几个文件的位置
    
    ```
    // 程序文件
    /usr/local/bin/v2ray
    // geoip 和 geosite
    /usr/local/share/v2ray/
    // 配置文件
    /usr/local/etc/v2ray/config.json
    // log 文件
    /var/log/v2ray
    // 服务文件
    /etc/systemd/system/
    ```
    
    目前配置文件是空的，需要对它进行设置，具体配置可以参考 [V2ray 的官方文档](https://v2ray.com/chapter_02/)，下面是 `Websocket + TLS` 的大致参考
    
    ```
    {
      "log": {
        "access": "/var/log/v2ray/access.log",
        "error": "/var/log/v2ray/error.log",
        "loglevel": "warning"
      },
      "inbounds": [
        {
          "port": 22002,
          "protocol": "vmess",
          "settings": {
            "clients": [
              {
                "id": "UUID",
                "level": 1,
                "alterId": 0
              }
            ]
          },
          "sniffing": {
            "enabled": true,
            "destOverride": [
              "http",
              "tls"
            ]
          },
          "streamSettings": {
            "network": "ws"
          }
        }
      ],
      "outbounds": [
        {
          "protocol": "freedom",
          "settings": {
            "domainStrategy": "UseIP"
          },
          "tag": "direct"
        },
        {
          "protocol": "blackhole",
          "settings": {},
          "tag": "blocked"
            }
      ],
      "dns": {
        "servers": [
          "https+local://dns.google/dns-query",
          "8.8.8.8",
          "1.1.1.1",
          "localhost"
        ]
      },
      "routing": {
        "domainStrategy": "IPOnDemand",
        "rules": [
                {
                    "type": "field",
                    "ip": [
                        "geoip:private"
                    ],
                    "outboundTag": "blocked"
                }
        ]
      },
      "transport": {
        "kcpSettings": {
                "uplinkCapacity": 100,
                "downlinkCapacity": 100,
                "congestion": true
            }
      }
    }
    ```

## 辅助内容

- BBR 加速

  从 Linux kernel 4.9 后，都很好的支持了 bbr，仅需要开启即可，有时候我会因为一些情况使用网上的 bbr 脚本，但我并不建议新手这么做。
  
  ```
  lsmod | grep bbr
  ```
  
  该命令用来检查是否已经启动了 bbr，如果返回结果里有 tcp_bbr 字样，则已经启动，如果没有则未启动。
  
  ```
  echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf && echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf && sysctl -p
  ```
  
  该命令用来“开启” bbr 并保存生效。
  
  ```
  sysctl net.ipv4.tcp_available_congestion_control
  sysctl net.ipv4.tcp_congestion_control
  ```
  
  上面两个命令里如果包含 bbr，则说明内核已经开启 bbr。

- Warp (原生 IP)

  目前不少服务需要用到了原生 IP，而且限制很严厉，比如 ChatGPT，Netflix 等，可以通过 Cloudflare warp 来解决这个问题。
  
  **一键安装脚本安装**
  
  网上也有大牛写了一键安装脚本，对新手来说，还是比较友好的，在 root 模式下，执行下面的命令
  
  ```
  wget git.io/warp.sh && chmod +x warp.sh
  ```
  
  下载 `warp.sh` 文件，然后运行 `./warp.sh menu` 命令逐步执行出现的菜单中的`安装 Cloudflare WARP 官方客户端`，`安装 WireGuard 相关组件`和`自动配置 WARP WireGuard 双栈全局网络`三项即可。
  
  _这里的`自动配置 WARP WireGuard 双栈全局网络`是 `IPv4` 和 `IPv6`，也可以单独选择 4 或者 6 安装。_
  
  **手动安装**
  
  首先，导入 Cloudflare 存储库的 gpg 密钥，并添加 Cloudflare 存储库，更新
  
  ```
  curl https://pkg.cloudflareclient.com/pubkey.gpg | gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/cloudflare-client.list
  apt update -y
  ```
  
  安装 Cloudflare Warp 客户端
  
  ```
  apt install cloudflare-warp -y
  ```
  
  查看是否正运行
  
  ```
  systemctl status warp-svc
  ```
  
  注册客户端，并设置为代理模式（重要）
  
  ```
  warp-cli register
  warp-cli set-mode proxy
  ```
  
  连接并让其保持永久连接
  
  ```
  warp-cli connect
  warp-cli enable-always-on
  ```
  
  可以通过命令 `warp-cli warp-stats` 查看连接是否成功，还可以通过 `warp-cli settings` 检查 Warp 的配置，查看当前代理的模式。默认情况下， socks5 监听的是 VPS 的 40000 端口，如果想修改端口可以通过命令 `warp-cli set-proxy-port 10000` 来修改，比如我这里将端口改成了 10000。
  
- 分流

  使用 Warp 后带来的一个问题是 IP 乱窜，这会让一些服务访问出现问题，比如访问 Google 时会遇到机器人识别验证的问题，还有账户归属地的有效性问题等。处理这些问题的办法很多，分流只是其中的一个方法，比较简单。分流可以在客户端进行，我这里分享下结合 `V2ray` 利用 `warp` 的 `socks` 的分流，只要修改 `config.json` 文件的内容即可。
  
  在 `config.json` 配置文件的 `outbounds` 节点增加 `socks` 规则，即
  
  ```
  {
      "protocol": "socks",
      "settings": {
          "servers": [
             {
                 "address": "127.0.0.1",
                 "port": 40000
              }
          ]
      },
      "tag":"cloudflare-warp"
  }
  ```
  
  在 `routing` 节点的 `rules` 里增加对应的规则，比如 ChatGPT 的分流
  
  ```
  {
      "type": "field",
      "domain": [
                "openai.com",
                "ai.com"
      ],
      "outboundTag": "cloudflare-warp"
  }
  ```
  
  其中 `outboundTag` 应该和上面出站的 tag 对应。这里除了 `domain` 之外，还可以用其他的规则，比如 `IP` 等，更多规则可以看[这里](https://v2ray.com/chapter_02/03_routing.html)的介绍。

- IP 被封

  IP 被封，最好的办法是更换 IP，比如 AWS Lightsail 就很容易更换 IP。还有一个办法是通过 Cloudflare 来实现，但这个办法有个致命的问题，会导致代理速度变慢。通过 Cloudflare 来解决 IP 被封的问题，要处理的地方有两处
  
  1. 在 Cloudflare 中的 DNS 中开启 IP 解析的代理，即开启小云朵。同时，将 `SSL/TLS` 设置成 `Flexible`。
  
  2. 在 VPS 中，设置网站是走 80 端口，而非 443 端口。

- 客户端

  这些年我用过很多客户端，目前是 [Surge](https://nssurge.com) 全家桶，它还是个比较强劲的开发者工具，比如有抓包等功能。不过有两个小缺点：1，目前只有 Apple 平台的，安卓、Linux 和 Windows 平台目前没有。2，对只是用来科学上网的人来说，价格不是那么亲民。
  
  **其他客户端**
  
  iPhone / iPad: [Shadowrocket]()，[Loon]()
  
  Android: [Clash for Android]()

## 说在最后

我设置自己的 fml 服务的主要目的是为了方便自己学习工作时查阅资料，更容易的使用一些服务。给自己节省大量的时间精力，丰富自己的知识眼界，仅此而已。

P.S. 这篇文章会不定期的更新。
