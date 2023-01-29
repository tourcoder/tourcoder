---
title: "如何创建一个 Go Mod"
slug: "how-to-create-a-public-go-mod"
author: Bin Hua
lastmod: 2021-07-27T21:31:17Z
date: 2021-07-27T21:31:17Z
tags: ["gomod", "howto"]
---

写并发布一个 Go Mod 还是挺方便的。

### 编写并发布

比如本次要写的 mod 名称为 `gomoddemo`，文件是 `gomoddemo.go`，其代码如下

```
package gomoddemo

import "fmt"

/***
 *
 * go mod demo
 *
 ***/

func PrintHelloTo (name string) string {

   return fmt.Sprintf("Hello, %s", name)

}
```

初始化 `go.mod` 文件

```
go mod init github.com/tourcoder/gomoddemo
```

这里用 `github.com/tourcoder/gomoddemo` 是因为该 mod 会存放在 GitHub 上。执行后得到结果 `go: creating new go.mod: module github.com/tourcoder/gomoddemo`，查看 `go.mod` 为如下内容

```
module github.com/tourcoder/gomoddemo

go 1.16
```

将这两个文件 push 到 GitHub 上对应的库中，即 https://github.com/tourcoder/gomoddemo 的仓库里即可。但需要注意的是为了很好的版本控制，建议通过 tag 来进行版本的控制，即在该仓库上执行

```
git tag v0.0.1
git push --tags
```

这样就有了一个 `0.0.1` 版本的 mod 了。

### 使用

和使用其他的库一样的方式使用该库 `go get github.com/tourcoder/gomoddemo`，然后在代码中 `import` 即可。比如这个 mod 的调用 `test.go` 的代码如下

```
package main
import (
        "fmt"
        "github.com/tourcoder/gomoddemo"
)

func main() {
        fmt.Println(gomoddemo.PrintHelloTo("tourcoder"))
}
```

运行 `go run test.go` 即可得到结果 `Hello, tourcoder`。
