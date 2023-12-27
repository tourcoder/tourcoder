---
title: "Go 语言中的 GO111MODULE 和 Go Get"
slug: "go111module-and-go-get-in-golang"
author: "Bin Hua"
lastmod: 2021-07-26T12:13:24Z
date: 2021-07-26T12:13:24Z
tags: ["golang", "gomodule"]
---

Go 语言在 1.11 中加入了 Go Module 作为官方包管理形式，因而不同的设置会导致执行 `go get` 下载第三方包时，包将下载到工作区的根目录下的不同的文件夹中，引用也会不一样。

在终端中输入命令 `go env` 查看 go 语言环境中的 `GO111MODULE`，有三种状态

- `GO111MODULE=""`

  默认情况，可以理解为是自动模式，Go 命令行会根据当前目录来决定是否启用 module 功能。这种情况下可以分为两种情形
  
  - 当前目录在 `$GOPATH/src` 之外且该目录包含 `go.mod` 文件
  
  - 当前文件在包含 `go.mod` 文件的目录下面

  当 module 功能启用时，`$GOPATH` 在项目构建过程中不再担当 import 的角色，但它仍然存储下载的依赖包，保存于 `$GOPATH/pkg/mod`。
  
- `GO111MODULE="off"`

  可以通过 `go env -w GO111MODULE=off` 设置生效，此时的 Go 命令行不支持 module 功能，沿用旧版本通过 vendor 目录或者 `$GOPATH` 模式来寻找依赖包。通过 `go get` 下载的第三方包都会被下载到 `$GOPATH/src` 这个文件夹中，同时会在 `pkg` 这个文件夹中生成对应的文件，同样用上面的 Gin 举例，得到的目录结构如下图
  
  ![](https://storage.tourcoder.com/tcblog/go111module-and-go-get-in-golang-002.png)

  此模式下，可以在 源码中直接通过 `import` 引入这个包，比如新建文件 `hello.go`，加入下面代码
  
  ```
  package main
  import "github.com/gin-gonic/gin"
  func main() {
	  r := gin.Default()
	  r.GET("/ping", func(c *gin.Context) {
		  c.JSON(200, gin.H{
			  "message": "pong",
		  })
	  })
	  r.Run() // 监听并在 0.0.0.0:8080 上启动服务
  }
  ```
  
  执行命令 `go run hello.go`，则启动项目，没有错误。

- `GO111MODULE="on"`

  可以通过 `go env -w GO111MODULE=on` 设置生效，此时的 Go 命令行会使用 modules，并不会去 `$GOPATH` 目录下查找。通过 `go get` 下载的第三方包都会被下载到 `$GOPATH/pkg` 这个文件夹中。比如下载 Go 的 web 开发框架 Gin，`go get github.com/gin-gonic/gin` 得到目录结构如下图
  
  ![](https://storage.tourcoder.com/tcblog/go111module-and-go-get-in-golang-001.png)
  
  和上面方式一样，创建新文件 `hello.go` 并加入上上面的代码，执行 `go run hello.go`，则会提示错误
  
  ```
  hello.go:3:8: no required module provides package github.com/gin-gonic/gin: go.mod file not found in current directory or any parent directory; see 'go help modules'
  ```
  
  正确的操作方式是 `go mod init 随意的名字/建议是项目名`，以本项目为例，`go mod init project_name` 会得到提示
    
    ```
    go: creating new go.mod: module project_name
    go: to add module requirements and sums:
	go mod tidy
    ```
    
    同时生成了一个 `go.mod` 的文件，初始内容为
    
    ```
    module project_name

    go 1.16
    ```
    
    以后它的内容将会被 `go toolchain` 全面掌控。`go toolchain` 会在各类命令执行时修改和维护 `go.mod` 文件，比如 `go get`、`go build`、`go mod` 等命令。
    
    `go.mod` 提供了四个命令：

    - module 语句指定包的名字（路径）

    - require 语句指定的依赖项模块

    - replace 语句可以替换依赖项模块

    - exclude 语句可以忽略依赖项模块
    
    回到本文，此时引入要使用的第三方包，比如这里的 Gin，即 `go get github.com/gin-gonic/gin`，此时 `go.mod` 文件里会自动增加内容，并且还生成了一个 `go.sum` 文件
    
    `go.mod` 文件的内容
    
    ```
    module hello

    go 1.16

    require (
	github.com/gin-gonic/gin v1.7.2 // indirect
	github.com/go-playground/validator/v10 v10.8.0 // indirect
	github.com/golang/protobuf v1.5.2 // indirect
	github.com/json-iterator/go v1.1.11 // indirect
	github.com/mattn/go-isatty v0.0.13 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.1 // indirect
	github.com/ugorji/go v1.2.6 // indirect
	google.golang.org/protobuf v1.27.1 // indirect
	gopkg.in/yaml.v2 v2.4.0 // indirect
    )
    ```
    
    
    `go.sum` 文件的内容
    
    ```
    github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
    github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
    github.com/gin-contrib/sse v0.1.0 h1:Y/yl/+YNO8GZSjAhjMsSuLt29uWRFHdHYUb5lYOV9qE=
    github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
    ```
    
    此时再去执行 `go run hello.go` 则会启动项目，一切正常。
    
    更多 `go mod` 的用法可以看 `go mod help`。
