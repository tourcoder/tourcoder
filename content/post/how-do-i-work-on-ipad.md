---
title: "我是如何在 iPad 上工作的"
slug: "how-do-i-work-on-ipad"
author: "Bin Hua"
lastmod: 2020-07-14 02:05:26
date: 2019-12-24 06:56:22
tags: ["远程工作", "GitHub", "iPad"]
---

拉了下统计，发现今年所写的代码中有 17% 的量是在 iPad 上完成的，比我之前想的要多。除此了写代码之外，其他也有不少工作是在 iPad 上完成的，比如邮件，文字之类的工作。

#### 硬件

2020 年我将设备换成了 iPad Pro 和专属的妙控键盘，感受是重，打字难受，完全提不起在上面写代码的兴趣，也基本告别用它来写代码。

~~iPad：iPad 2019 款，没有买单独的支架，就是买了个能支撑的保护套。~~

~~键盘：因为 iPad 我基本只是在家才会使用，所以并没有买便携式的折叠键盘，而用的是自己一直在用的 Magic Keyboard，毕竟都是 Apple 家的东西，体验没话说。~~

耳机：Airpod
    
#### 主要软件

Termius：我一直是 Termius 的用户，但我比较反感它在后来的版本中推出了账户体系。
    
Safari: 主要浏览器，备用浏览器是 Firefox
    
MindNode：思路图/脑图的工具
    
Cloud Storage：现在主要用 iCloud 自带的存储，怎么说呢，这并不是一个值得信任的产品。Apple 把整个 iCloud 做得挺烂，总是莫名其妙的丢东西，出现奇奇怪怪的问题。本来一直用 Google Drive，但因 Google Drive 并不支持 MindNode 的文件格式，而我非常依赖 MindNode，所以花钱买了更高容量的 iCloud 存储。试过微软家的 onedrive，但总感觉自己和它八字不合，但 iCloud 总是莫名其妙的丢文件，这点超级烦躁。
    
#### 开发情况

这一年写后端底层的东西比较多，更倾向于在 Linux 上开发，我的操作方式是

在 Google Cloud 上买了一个双核 4G 内存的 VM，在该 VM 上配置了开发需要的环境等，然后通过 SSH 登录到 VM 上进行开发，其实不只是在 iPad 上，在电脑上我也基本是连接接到 VM 上做开发。

我很少在 iPad 上进行本地开发，本地操作的内容多为文字性的东西以及脑图等，内容存储在 iCloud Storage 中。

iPad 分屏作用很大，尤其是在开发中需要看一些文档时。现在虽然有好的文档应用，但它们的分屏适配不行。

#### 感受

待电：待电时间绝对的棒，一天工作下来，毫无压力，基本几天才用充一次电
    
便携性：虽然我是在家才会用，但可以想一下，出门只要拿着它和一个便携式键盘，同一个出门要带着电源的电脑比，哪个好？
    
缺点：功能单一，工具少
   
#### 开发机

上面说到我很多时候都是在一台部署在 Google Cloud 上的 VM 进行开发的，那么这台机器具体是个什么情况呢？

**名字**

没错，我是那种无聊到会给自己每一台设备都起一个名字的人，开发机也不例外，它的名字是 spurs。在 debian 里更改名字

```
vi /etc/hosts
```

将里面默认的计算机名改成 spurs

```
vi /etc/hostname
```

将里面默认的计算机名也改成 spurs，重启即可。

**系统及基础配置**

系统使用的是 Debian 9，基础配置如下

以 root 用户登录后，执行命令

```
apt update -y
apt upgrade -y
```

更新下系统，先开启 ssh 开机启动 `update-rc.d ssh enable`。

```
adduser tourcoder
usermod -aG sudo tourcoder
```

增加一个用户，并将其拉入到 sudo 组，检查是否在 sudo 组里，通过命令

```
cat /etc/group|grep 组名
```

也可以通过 `cat /etc/group` 直接查看组，也可以通过

```
cat /etc/passwd|grep tourcoder
```

查看具体的某一个用户的情况，或者 `cat /etc/passwd` 查看用户情况。

需要注意的是 Google Cloud 的 VM 需要开启密码登录验证，执行下面的命令

```
vi /etc/ssh/sshd_config
```

将文件里的 `PasswordAuthentication no` 中的 `no` 改成 `yes`，然后重启 `service sshd restart`。

需要注意的是，我图省事，使用了密码登录的方式，其实应该是通过密钥登录方式才更安全。设置密钥的方式如下，在用户的根目录下执行命令

```
ssh-keygen
```

会要求输入保存地址，默认即可，同时建议输入一个密码

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/tourcoder/.ssh/id_rsa):
Created directory '/home/tourcoder/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/tourcoder/.ssh/id_rsa.
Your public key has been saved in /home/tourcoder/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Q9Uu6OacubPJAf689mxPtvhAqgwDmSBwzLg7ePNEtzQ tourcoder@spurs
The key's randomart image is:
+---[RSA 2048]----+
|.+.       ..     |
|o.o      .  .    |
|o.      .. .     |
|o. o. E.. . .    |
|..+. o.+S ..     |
|+ o.....o+       |
| o +o .+oo. o    |
|    .+ =B+.= .   |
|      o.OB+o+    |
+----[SHA256]-----+
```

此时会在 `~/.ssh/` 下有一个生成两个文件 `id_rsa` 和 `id_rsa.pub`，将公钥 `id_rsa.pub` 安装

```
cat id_rsa.pub >> authorized_keys
```

更改权限

```
chmod 600 authorized_keys
chmod 700 ~/.ssh
```

如上所说，将 `/etc/ssh/sshd_config` 中的 `PasswordAuthentication` 改成 `no`，有时候可能需要设置

```
RSAAuthentication yes
PubkeyAuthentication yes
```

但也有的系统不需要，最后重启下即可 `sudo service sshd restart`。将 `id_rsa` 下载到本地计算机，执行 `ssh -i id_rsa tourcoder@server_ip` 即可登录，如果之前生成密钥时输入了密码，这里会要求输入密码 `Enter passphrase for key 'id_rsa':`，输入密码即可。

**安全和防火墙**

禁用 root 远程登录，这点很重要。

```
vi /etc/ssh/sshd_config
```

将 `PermitRootLogin` 后面的 `yes` 改成 `no`，最后重启 `sshd` 服务

```
service sshd restart
```

在防火墙方面，除了 Google Cloud 的一套之外，在里面我安装了 `ufw`，主要是它更简单好用

```
apt install ufw
```

一些常用的命令

```
ufw enable //开启 ufw
ufw status //查看状态
ufw allow applicationname //允许某个应用通过
ufw app list //查看允许的应用
```

我的开发机只允许了三个端口 `http`，`https` 和 `ssh`，即

```
ufw allow 80
ufw allow 443
ufw allow ssh
```

如上面所说，我使用的是密码方式通过 SSH 登录，就会存在一个 SSH 被暴力破解的问题存在，Google Cloud 本身有一套运行机制防止被暴力破解，但我还是使用了 `fail2ban` 这个工具，其官网是 [https://www.fail2ban.org/](https://www.fail2ban.org/) ，它会监控多个系统的日志文件并根据检测到的任何可疑的行为自动触发不同的防御动作，先安装

```
sudo apt install fail2ban -y
```

配置监狱文件，一般参考 `jail.conf` 文件新建自己的文件

```
cd /etc/fail2ban
sudo cp jail.conf jail.local
sudo vi jail.local
```

修改其中的

```
bantime = 86400 // 禁止 24 小时
banaction = ufw // 使用 ufw 允许的
```

重启 fail2ban，使其生效

```
sudo service fail2ban restart
```

查看是否生效

```
sudo fail2ban-client ping
```

会得到返回 `Server replied: pong`，其中 `fail2ban-client` 也可以进行一些操作，比如上面的刷新配置可以用 `sudo fail2ban-client reload`，具体的自行执行命令 `sudo fail2ban-client --help` 查看。

注意，在 Debian 中 fail2ban 是自动开机启动的，在其他系统中可能会需要手动开启开机启动，执行命令 `sudo systemctl enable fail2ban`。

**更改端口并开启**

处于安全考虑，我更改了 ssh 的登录端口，不使用默认的 22 端口

```
vi /etc/ssh/ssh_config
vi /etc/ssh/sshd_config
```

取消上面两个文件中的 `PORT` 前面的 `#`，将 22 换成自己想使用的端口，比如我用了 2299，重启

```
service sshd restart
```

接着开启该端口，用上面 `ufw`，则运行 `ufw allow 2299`，如果是用 `iptables`，则

```
//如果是关闭端口，将下面的 INPUT 换成 OUTPUT
iptables -I INPUT -p tcp --dport 2299 -j ACCEPT
```

保存该文件 `service iptables save`，但这个保存并不是持续保存，重启会失效，可以通过 `iptables-persistent` 来保存，先安装

```
apt install iptables-persistent -y
```

然后保存，并使规则生效

```
netfilter-persistent save
netfilter-persistent reload
```

通过命令 `netstat -an | grep 2299` 检查端口是否已经开启，也可以通过 `nmap` 命令在外部检查，命令为 `nmap -p 端口 IP`。另外 `nmap` 的命令很多，比如 `nmap IP` 就可以查看某个 IP 开放的端口，其他高级应用自行搜索。

最后通过 `ssh -p 2299 user@ip` 检查是否可以登录了。


**定期检查**

我会定期检查开发机的成功登录情况

```
cat /var/log/auth.log |  grep Accepted
```

如果发现不是自己的 IP，说明被黑了。

**软件**

编辑器：我使用的是 vim，一款比较传统的编辑器，刚开始的时候并不适应，现在习惯了，效率也就上来了。VSCode 现在提供了远程连接服务器编程功能，很棒，具体说明看[这里](https://code.visualstudio.com/docs/remote/ssh#_getting-started)，只是目前还不支持 iPad。
    
Docker：因为配置一个服务器有时候真的很烦，而 Docker 让我不那么烦了。
    
Git：基本就这些内容，没那么复杂。

尽管这么完善，但有一些开发还是在本地电脑进行的，比如 iOS 应用，对这些工具我的看法是简单直接点，不搞事。

**补充**

我在 GitHub 上写了一份配置，具体看[这里](https://github.com/TOURCODER/nerd)
