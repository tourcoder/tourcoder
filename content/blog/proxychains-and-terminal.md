---
title: "终端的代理"
slug: "proxychains-and-terminal"
author: "Bin Hua"
lastmod: 2018-12-24 14:28:31
date: 2018-12-24 14:28:31
tags: ["terminal", "proxy", "ProxyChains"]
---

作为一个命令行爱好者，终端 (Terminal) 的使用尤其频繁，这就难免有时候需要用到代理的时候

- SS

  这个就不用我多说了

- ProxyChains

  因为我用的是 macOS，所以可以直接通过 Homebrew 命令直接安装，Homebrew 是什么？可以看[这里](https://brew.sh/)，在终端中输入命令
  
  ```
  brew install proxychains-ng
  ```
  
  安装完成后，默认配置文件在 `/usr/local/etc/proxychains.conf`，可以将文件放到 `~/.proxychains.conf`
  
  ```
  strict_chain
  proxy_dns
  remote_dns_subnet 224
  tcp_read_time_out 15000
  tcp_connect_time_out 8000
  localnet 127.0.0.0/255.0.0.0
  quiet_mode
  [ProxyList]
  socks5  127.0.0.1 1086
  ```
  
  在 `~/.zshrc` 里设置个 alias
  
  ```
  alias proxychain="proxychains4 -f ~/.proxychains.conf"
  ```
  
  然后执行 `source ~/.zshrc` 重新加载配置，这样在终端中使用 `proxychain command` 可以访问一些有网络障碍的服务了。
  
  有兴趣的，可以去 [ProxyChains-NG](https://github.com/rofl0r/proxychains-ng.git) 官网看看，也可以通过手工编译安装实现。
  