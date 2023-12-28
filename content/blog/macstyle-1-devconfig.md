---
title: "MacStyle 之环境配置"
slug: "macstyle-1-devconfig"
author: "Bin Hua"
date: 2016-08-10 06:49:45
tags: ["macOS", "Git"]
draft: false
---

**Git** 版本控制环境

**MAMP** PHP 环境开发配置

**Node.js** Nodejs 的开发环境

**Oh My Zsh** Shell 环境

**CocoaPods** Xcode 第三方开发工具包管理，其中用到 RubyGems 镜像，官方镜像被墙，可考虑用淘宝镜像(http://ruby.taobao.org)

**Homebrew** The missing package manager for OS X，这是它的 slogan，已经说得很清楚了

至于怎么配置，怎么弄，上面的官方网址都有说明。

补充

**Terminal**

- Screenshot

    ![](https://storage.tourcoder.com/tcblog/macstyle-1-devconfig-01.png)

- Theme

    基于 Homebrew 主题修改，可以从[这里](https://raw.githubusercontent.com/tourcoder/dotfiles/master/Homebrew.terminal)下载我的文件，双击直接安装，在安装前，请先下载下面的字体，先安装字体。

- Font

    我使用的字体情况是 `InputMono Thin  14pt`

    你可以去[官网](http://input.fontbureau.com/download)下载最新版本。

- Ohmyzsh

    Ohmyzsh 的主题是基于 af-magic 这款主题修改，具体操作如下

    - Enter folder with command cd ~/.oh-my-zsh/themes
    
    - Run command vi simple.zsh-theme
    
    - The code in simple.zsh-theme 

        ```
        # simple.zsh-theme

        if [ $UID -eq 0 ]; then NCOLOR="red"; else NCOLOR="green"; fi
        local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"

        # primary prompt
                        PROMPT='$FG[237]------------------------------------------------------------%{$reset_color%}
        $FG[032]%~\
        $(git_prompt_info) \
        $FG[105]%(!.#.»)%{$reset_color%} '
        PROMPT2='%{$fg[red]%}\ %{$reset_color%}'
        RPS1='${return_code}'
        # color vars
        eval my_gray='$FG[237]'
        eval my_orange='$FG[214]'
        
        # git settings
        ZSH_THEME_GIT_PROMPT_PREFIX="$FG[075]($FG[078]"
        ZSH_THEME_GIT_PROMPT_CLEAN=""
        ZSH_THEME_GIT_PROMPT_DIRTY="$my_orange*%{$reset_color%}"
        ZSH_THEME_GIT_PROMPT_SUFFIX="$FG[075])%{$reset_color%}"
        ```
        
    - Run command `vi ~/.zshrc`, change the `ZSH_THEM`E to `ZSH_THEME="simple"`

2019 年已经使用 iTerm2，我只做了最简单的配置，看[这里](/iterm-manual/)。

本文最后编辑时间：2019-01-10 10:00
