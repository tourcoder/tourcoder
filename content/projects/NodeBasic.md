---
title: "NodeBasic"
slug: "NodeBasic"
summary: "The node docker file with basic functionality"
author: "Bin Hua"
date: 2023-11-20T09:54:58+08:00
tags: ["node", "Docker", "Open Source"]
draft: false
---

The node docker file with basic functionality

### Why I created this

![compare](https://user-images.githubusercontent.com/535675/182006100-8ba27fed-4817-48c5-8476-3da0f0464dd5.png)

I found that even the alpine version of the node docker image is over 100M, but NodeBasic is less than 55M.

### How to use nodebasic

Use as base image in Dockerfile

- From Docker Hub

  ```
  FROM tourcoder/nodebasic
  ```

- From GitHub 

  ```
  FROM docker.pkg.github.com/tourcoder/nodebasic/nodebasic:latest
  ```

Download `Dockerfile` in this repo, and run

```
docker build -t nodebasic .
```

[Open Source on GitHub](https://github.com/tourcoder/nodebasic)

[Release on Docker Hub](https://hub.docker.com/r/tourcoder/nodebasic)