---
title: "处理 CURL 下载 ASCII text 问题"
slug: "solved-ascii-text-issue-when-downloading-via-curl"
author: "Bin Hua"
date: 2021-04-24T20:16:17Z
tags: ["curl", "fixed", "golang"]
draft: false
---

用  `curl -O` 下载 golang 官网的的新版本安装文件时，得到的文件类型是 `ASCII text`，原因是这里有一个 redirect，应该增加参数  `L`，即 `curl -LO https://golang.org/dl/go1.16.3.src.tar.gz`
