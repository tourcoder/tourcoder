---
title: "我的现代化的 Vibecoding 模式"
slug: "how-i-vibe-code-my-modern-ai-development-workflow"
author: "Bin Hua"
date: 2026-07-16T06:45:02Z
tags: ["vibecoding", "claude", "codex", "gemini", "yeci", "yeci-notify", "docker", "podman"]
draft: false
---

这里说现代化有点夸张了，毕竟和网友超前的 Vibe Coding 模式相比还是落后了很多，但和我以前的模式比较而言，是个很大的提升，至少能榨干 Claude/Codex 等的用量了，当然也在“榨干”我自己🤭

### 准备工作

- 一台 VPS（做好安全配置和密钥配置）

- 在 VPS 上安装好容器管理工具（我用的是 Podman，Docker 也非常优秀，但我更喜欢 Podman）

- TelegramBot（和 @botfather 对话来创建一个 telegram bot，记录下 api token）

- [YECI](https://yeci.org)（这是一个编程开发容器，内置了最新的 Claude/Gemini/Codex/Tmux/NeoVim/Git 等，开箱即用，非常方便）

### 工作流

通过 SSH/MOSH 登录到 VPS 后，进入到项目的文件夹，将 YECI 镜像拉到 VPS 本地，并基于它拉起当前项目的开发容器，比如

```
podman run -d \
--name "yeci-$PROJECT_NAME" \
--network host \
-v "$PWD":/workspace \
docker.io/tourcoder/yeci > /dev/null
```

然后进入到这个项目的开发容器里 `podman exec -it "yeci-$PROJECT_NAME" /bin/bash`，具体的 [YECI](https://yeci.org) 官网有说明。我是写了个脚本 devRun 放在 `~/.local/bin/` 下

```
#!/bin/bash

# 获取当前文件夹名作为容器标识
PROJECT_NAME=$(basename "$PWD")
CONTAINER_NAME="yeci-$PROJECT_NAME"

echo "为项目 [$PROJECT_NAME] 启动独立沙盒..."

# 检查是否已经有运行的容器
if podman ps --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
    echo "检测到现有容器，正在连接..."
    podman exec -it "$CONTAINER_NAME" /bin/bash
else
    # 新建容器
    if ! podman run -d \
      --rm \
      --name "$CONTAINER_NAME" \
      --network host \
      -v "$PWD":/workspace \
      docker.io/tourcoder/yeci > /dev/null; then
        echo "容器启动失败"
        exit 1
    fi

    # 等待容器就绪
    for i in $(seq 1 10); do
        if podman ps --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
            break
        fi
        sleep 0.3
    done

    if ! podman ps --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        echo "容器未能成功运行"
        exit 1
    fi

    echo "容器已启动，正在进入..."
    podman exec -it "$CONTAINER_NAME" /bin/bash
fi
```

每次只要在项目目录下执行 devRun 即可拉起对应的开发容器。

在开发容器里，我并没有直接执行 Claude/Codex 等命令直接拉起 code agent 来编码，因为这样的做会有个问题 -- SSH 断开会导致当前会话丢失（当前编码的 agent 就会挂掉）。我借助 yeci 内置的 tmux 来管理会话，即便 SSH 断开也不会导致当前会话丢失，再次连接上来就可以继续之前的会话。

另外，我借助了 yeci 内置 yeci-notify 和 telegram bot 解决人离开屏幕后没有时间盯住 agent，无法和它对话的痛点。根据 [yeci-notify](https://notify.yeci.org) 官网所写的 `yeci-notify init` 完成配置即可。当我人离开屏幕后，有交互的问题会被发送到绑定的 telegram bot，通过这个 bot 可以继续指导 agent 继续编码等。

![yeci-notify](https://storage.tourcoder.com/tcblog/how-i-vibe-code-my-modern-ai-development-workflow-001.jpg)

其他，我还有一些其他的操作，比如环境变量的注入等，都是容器管理器（Podman/Docker）本身的方式方法。

更多玩法可以参考:

- YECI：[yeci.org](https://yeci.org)

- YECI-NOTIFY：[yeci-notify](https://notify.yeci.org)

- Podman：[podman.io](https://podman.io)
