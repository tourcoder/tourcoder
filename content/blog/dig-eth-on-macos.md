---
title: "在 macOS 下玩 ETH"
slug: "dig-eth-on-macos"
author: "Bin Hua"
draft: false
date: 2018-08-20 07:43:09
tags: ["macOS", "blockchain", "eth", "以太坊"]
---

首先安装以太坊客户端 Geth

```
brew install ethereum
```

安装完成后，查看版本

```
geth version
```

接着新建文件夹，并且创建一个文件 genesis.json

```
mkdir ethtest
cd ethtest
vi genesis.json
```

输入如下内容

```
{
  "config": {
        "chainId": 10,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
  "coinbase"   : "0x0000000000000000000000000000000000000000",
  "difficulty" : "0x020000",
  "extraData"  : "",
  "gasLimit"   : "0x2fefd8",
  "nonce"      : "0x0000000000000042",
  "mixhash"    : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "timestamp"  : "0x00",
  "alloc"      : {}
}
```

初始化

```
geth --datadir datastore init genesis.json
```

启动节点

```
geth --datadir datastore --networkid 1108 console
```

其中 `--networkid 1108` 表示链的 ID 是 1108，console 表示进入控制台，此时可以在控制台中输入命令查看

```
eth.accounts //查看 eth 账户
personal.newAccount() //创建账户，需要输入密码
eth.getBalance(eth.accounts[0]) //查看账户余额
miner.start() //挖矿
```

在等待一段时间后，会得到如下结果

![](https://storage.tourcoder.com/tcblog/dig-eth-on-macos.png)

```
miner.stop() //停止挖矿
```

需要注意，在输入 `miner.stop()` 的过程中数据是不断的前滚的，所以你直接输入就好，其他不用管。