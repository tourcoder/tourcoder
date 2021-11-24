---
title: "Days of Golang (更新中)"
slug: days-of-golang
author: Bin Hua
lastmod: 2020-08-13 09:44:18
date: 2020-01-03 07:53:26
tags: ["Google", "Golang", "go"]
---

计划着今年把 Golang 好好的再撸一遍，我以前学习开发语言的方法是手册，基础知识点看一遍，然后直接看别人的代码，从简单的到难的。但这次我想换个方法，跟着网上的视频教程学习一次。

### 教学视频

在 YouTube 上发现「韩顺平 Go 语言零基础教程」似乎不错，观看地址点[这里](https://www.youtube.com/playlist?list=PLmOn9nNkQxJFWlwItS-iI3C-4jeARUNjq)


### 学习计划及时间安排

这个系列的视频一共有 389 个，每个视频时长不等，粗略按每个视频 30 分钟计算，一共 11670 分钟，194.5 个小时。

我的学习计划是平均每天学习 2 个小时，即需要 97.25 天，满打满算取个整，需要 98 天，如果是在一年内的话，基本平均每三天要学习 2 个小时。

### 笔记

我会把每次的学习做一份笔记，整理成博文发出来，方便分享以及自己以后再回头学习。

### 第一天学习笔记

**学习内容**

本次学习了该系列教程的第 001 - 014

**知识点整理**

Golang 是由 Google 开发的一门静态强类型、编译型、并发型，并具有垃圾回收功能的编程语言，更多的介绍看 Golang 在维基百科上的[介绍](https://zh.wikipedia.org/wiki/Go)。
    
Go 既有静态编译语言的安全和性能，又有动态语言开发维护的高效。
    
Go 的包用于组织程序结构，Go 的一个文件都要归属于一个包，不能单独存在。
    
Go 中，内存自动回收垃圾，不需要开发人员管理。
    
Go 并发性是其一个比较重要的特点，它从语言层面就支持并发；goroutine，轻量级线程实现大并发处理，高效利用多核；基于 CPS(Commiunicating Sequential Processes) 并发模型的实现。

Go 吸收了管道通信机制，形成 Go 特有的管道通过管道，可以实现不同的 goroute 之间的饿相互通信。

Go 函数可以返回多个值

```
func sumAndSub(n1 int, n2 int)(int, int) {
    sum := n1 + n2
    sub := n1 - n2
    return sum, sub
}
```

Go 中还有一些创新性功能，比如欺骗 (slice)，掩饰执行 (defer)。


**开发工具和环境安装**

开发工具多种多样，挑自己顺手的即可。

访问 [golang.org](https://golang.org)，选择自己系统的平台，下载对应的包安装即可。

我本人使用的是 macOS，日常开发机器用的是 Debian，则

- macOS 下安装

    **通过 Homebrew 安装**
    
    具体的安装方式可以看之前些的文章，[https://tourcoder.com/macos-manual/](/macos-manual/)。
    
    **直接用 pkg 文件安装**
    
    官网直接下载 pkg 文件，双击安装即可。
    
- Debian 下安装

    查看系统的版本 `uname -a`，我使用的是 `x86_64` 即 64 位的 Debian 9 的系统，选择 64 位 Linux 下的 Go 压缩包下载。
    
    ```
    https://dl.google.com/go/go1.13.5.linux-amd64.tar.gz
    ```
    
    最好检查下哈希值
    
    ```
    sha256sum go1.13.5.linux-amd64.tar.gz
    ```
    
    查看得到的哈希值和下载该压缩包的地方，Google 所提供的哈希值是否一致。
    
    ```
    tar -zvxf go1.13.5.linux-amd64.tar.gz
    ```
    
    解压压缩文件，然后将解压后的文件夹 `go` 移动到它所建议的目录地址 `/usr/local`，即
    
    ```
    sudo mv go /usr/local
    ```
    
    编辑 `~/.profile` 文件进行环境设置
    
    ```
    vi ~/.profile
    ```
    
    在文末增加内容
    
    ```
    export GOPATH=$HOME/work
    export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
    ```
    
    如果将 go 文件夹移到了其他目录位置，而非 `/usr/local` 下，比如主目录中，则这里的内容为
    
    ```
    export GOROOT=$HOME/go
    export GOPATH=$HOME/work
    export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
    ```
    
    刷新生效
    
    ```
    source ~/.profile
    ```
    
    输入 `go version` 出现版本号即表示安装配置完成，查看环境变量的命令 `go env`。

其它安装方式，可以用 glv 安装最新版本的 golang 环境，地址：[http://github.com/tourcoder/glv](http://github.com/tourcoder/glv)。
    
这里基本是第一天学习的内容，都是一些基础概念和常规的安装配置，很容易上手。

### 第二天学习笔记

**学习内容**

本次学习了该系列教程的第 015 - 019

**知识点整理**

一贯作风，写一个 `hello world` ，在写之前先解释下目录结构，Golang 做了一些目录结构的规定，具体看 [How to Write Go Code ](https://golang.org/doc/code.html#Workspaces)。

一般 GOPATH 下需要建立三个目录

```
bin - 存放编译后生成的可执行文件
    
pkg - 存放编译后生成的包文件
    
src - 存放项目源码
```

而在 src 文件夹下，每个 package 都有一个单独的文件夹（与 package 同名）将同名字的 package 文件（package.go）包含起来。

继续写 `hello world`，创建一个文件 `hi.go`，将相关代码写入里面

```
package main
import "fmt"

func main() {
    fmt.Println("hello world")
}
```

如第一天学习笔记里面提到的 `Go 的一个文件都要归属于一个包，不能单独存在`，这里代码第一行就是表示一个包。

第二行表示引入另外一个包，然后这个文件就可以使用所引入包所包含的函数内容了，比如这里用到了 `fmt` 包中 `Println` 这个函数。

`func main()` 可以理解为是定义入口函数。

执行 `go build hi.go` 进行编译，即可得到一个 `hi` 文件，这是一个可执行的二进制文件。其中在 windows 下是 `hi.exe`，直接执行即可得到 `hello world`，在 macOS 和 Linux 下是 `hi`，直接运行 `./hi` 即可得到 `hello world`。

在用 `go build` 做编译的时候，生成的文件的默认文件名是当前 go 文件的文件名，可以通过参数修改，比如 `go build -o hello hi.go` 生成的文件就是 `hello`。

也可以通过 `go run hi.go` 运行，但其速度要比编译后的要慢，可以在调试程序的时候使用，并不建议在生产力环境下使用。

`go build` 和 `go run` 是有区别的。`go build` 后的文件可以运行在没有 Golang 环境的机器中，因为在做编译时已经将执行依赖的包文件打包进入编译后的文件中了，并且该可执行文件大了很多。`go run` 需要在有 Golang 环境的机器中才可以运行。

Go 源码文件是以 go 为扩展名。

Go 严格区分大小写。

Go 应用程序的执行入口是 main() 函数。

Go 方法是由一条条语句组成，每条语句的结尾不需要加分号表示结束，不加分号的时候不可以将多条语句写在同一行，但如果加了分号则可以将多个语句写在同一行，但**不建议**这么做。

Go 中 import 到的包或者定义的变量没有被使用到，代码编译不能通过。

Go 中大括号要成对出现，缺一不可。
