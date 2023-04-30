---
title: "macOS 下使用 GPG"
slug: gpg-on-macos
author: "Bin Hua"
lastmod: 2020-08-13 09:38:12
date: 2019-10-04 11:45:51
tags: ["macOS", "git", "GitHub", "加密", "homebrew", "gpg", "GNU"]
---

GPG 是 GNU Privacy Guard 的简称，又名 GnuPG 是一种加密软件，它是 PGP 即 Pretty Good Privacy 的替代物，因为 PGP 不开源不免费，所以 GPG 使用还是比较广泛。在 macOS 下使用也比较方便。

#### 安装 GPG

在 macOS 下通过 Homebrew 来安装

```
brew install gpg
```

在一段时间的等待后，安装即完成了，我当前使用的版本是 `gnupg 2.2.17`。

#### 使用 GPG，生成公钥和私钥

在终端下执行命令

```
gpg --full-generate-key
```

会让你选择

![](/imgs/gpg_01.png)

一般选择默认 1，可以根据自己的需求来选择其他的选项

然后会让选择长度，也是默认 2048，可以根据自己的需求来选择其他的选项

然后选择有效去，也是默认 0，可以根据自己的需求来选择其他的选项，会有一个确认的过程，整个过程如下图

![](/imgs/gpg_02.png)

然后会要求输入名字，Email 地址以及 COMMENT，最后确认

![](/imgs/gpg_03.png)

此时会要求输入密码和再次确认密码，如下图

![](/imgs/gpg_04.png)

完成后，即可得到结果

![](/imgs/gpg_05.png)

#### 显示和导出公钥和私钥

```
gpg --list-keys //查看所有keys
gpg --list-public-keys //查看所有公钥
gpg --list-secret-keys //查看所有私钥
```

![](/imgs/gpg_06.jpg)

通过第一条命令查询后得到的结果，其中虚线上面一条是公钥文件及其保存地址，该文件是一个二进制形式存储的文件，虚线下面的内容是

pub 后是公钥的特征，包含 2048 位，指纹字符串以及生成的时间，该字符串最后十六位即长密钥 ID。其中括号中 S 表示 Signing 即签名，E 表示 Encrypting 即加密，C 表示 Certificating 即认证。

uid 后是用户的个人信息

sub 后是子密钥特征，格式和公钥部分大致相同，包含 2048 位和生成时间。

上面看到的都是精简的内容，如果要看到完整的内容，通过如下命令

```
gpg --armor --export <邮箱或者指纹字符串或者长密钥 ID> //查看完整的公钥
gpg --armor --export-secret-keys <邮箱或者指纹字符串或者长密钥 ID> //查看完整的私钥
```

其中在查看私钥的时候，会提示输入之前要求输入的密码，输入正确的密码即可。

为了方便，可以将导出成文件，则执行命令

```
gpg --armor --output publickeyfile.txt --export <邮箱或者指纹字符串或者长密钥 ID> //导出公钥
gpg --armor --output privatekeyfile.txt --export-secret-keys <邮箱或者指纹字符串或者长密钥 ID> //导出私钥
```

更多使用帮助，可以通过命令 `gpg --help` 查看。

#### 应用

公钥在很多场景中可以得到应用，比如收发加密邮件，GitHub 的 Commit 加密等。

- GitHub 的 Commit 加密

  访问 [https://github.com/settings/keys](https://github.com/settings/keys), 点击右侧的 `New GPG keys`，将公钥输入进去，**注意是公钥，不是私钥**，得到的结果如下图。
  
  ![](/imgs/gpg_07.png)
  
  本地电脑设置密钥，我习惯了用终端，这里就介绍下终端下的设置
  
  ```
  git config --global gpg.program $(which gpg)
  git config --global user.signingkey <长密钥 ID>
  git config --global commit.gpgsign true //让每次 commit 自动要求签名，如果不增加则需要 git commit -S -m "内容"，每次加上 -S 参数。
  ```
  
  但是在 `git commit` 的时候总会遇到问题
  
  ```
  error: gpg failed to sign the data
  fatal: failed to write commit object
  ```
  
  在搜索后找到了解决方案，见[这里](https://community.atlassian.com/t5/Bitbucket-questions/can-t-commit/qaq-p/719732)，大致说下过程
  
  在终端中执行一下几个命令
  
  ```
  brew upgrade gnupg  # This has a make step which takes a while
  brew link --overwrite gnupg
  brew install pinentry-mac
  echo "pinentry-program /usr/local/bin/pinentry-mac" >> ~/.gnupg/gpg-agent.conf
  killall gpg-agent
  echo "test" | gpg --clearsign  # on linux it's gpg2 but brew stays as gpg
  ```
  
  当执行最后一步成功时会有一个弹窗要求输入密钥的密码，输入密码即可。完成 `git commit` 后可以通过命令 `git log --show-signature -1` 查看是否已经签名。
  
  ![](/imgs/gpg_08.png)
  
  上图是在 GitHub 上的效果图，其实两个都是带有签名的，但有一个却显示 `Unverified`，其原因是这一条 `commit` 的 `user.email` 不是 GPG 生成的密钥中的 email 地址。
  
  ![](/imgs/gpg_09.png)
  
  对由网页端操作进行认证，使用 GitHub 的密钥，如上图，先导入
  
  ```
  curl https://github.com/web-flow.gpg | gpg --import
  ```
  
  用自己的密钥再信任它
  
  ```
  gpg --sign-key 4AEE18F83AFDEB23
  ```
  
  完成。