---
title: "定期自动备份 GitHub 上的代码到你私人 vps"
slug: "automatically-sync-your-code-on-github-to-your-vps-on-a-regular-basis"
author: "Bin Hua"
date: 2024-10-09T07:47:07Z
tags: ["github", "git", "gitlab"]
draft: false
---

之前在推上说过担心 GitHub 上代码丢失，写了个脚本定期自动将自己的代码从 GitHub 上同步到自己的 vps，这里记录分享下。原则上说，这个方法也适用了其它的 git 服务。

### 实现的思路

简单和直接是我的追求，所以我抛除了做系统写配置的方式。直用一个脚本+定时器(cron) 来解决问题。

整个目录结构有三层

第一层是 github_backup，表示来自 GitHub 的

第二层是 github 上的 orgname/username

第三层是 orgname/username 名下的 repo

这里有点麻烦的是，需要手动操作现将每个 repo 从 GitHub 上拉到本地的 vps。然后让脚本遍历这些 repo，自动 git pull 更新。

### 脚本

这是 python 的脚本

```
import os
import subprocess
from pathlib import Path

# github_backup 文件夹的路径，自定义
GITHUB_BACKUP_PATH = '/github_backup'

def run_command(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    else:
        print(result.stdout.strip())
    return result

def git_pull_in_branch(repo_path, branch):
    result = run_command(f"git checkout {branch}", cwd=repo_path)
    if result.returncode == 0:
        run_command("git pull", cwd=repo_path)

def pull_all_branches(repo_path):
    result = run_command("git branch --list", cwd=repo_path)
    if result.returncode == 0:
        branches = result.stdout.splitlines()
        branches = [branch.strip().replace('* ', '') for branch in branches] 
        for branch in branches:
            git_pull_in_branch(repo_path, branch)

def process_repository(repo_path):
    if os.path.exists(os.path.join(repo_path, '.git')):
        print(f"Processing repository: {repo_path}")
        result = run_command("git fetch --all", cwd=repo_path)
        if result.returncode == 0:
            pull_all_branches(repo_path)
    else:
        print(f"Not a valid git repository: {repo_path}")

def process_backup_directories(base_path):
    base = Path(base_path)
    for second_level_dir in base.iterdir():
        if second_level_dir.is_dir():
            for repo_dir in second_level_dir.iterdir():
                if repo_dir.is_dir():
                    process_repository(str(repo_dir))

if __name__ == "__main__":
    process_backup_directories(GITHUB_BACKUP_PATH)
```

### 定时器

用定时器去定时运行即可，cron 的设置可以翻看我博客的另外一篇博文「[Linux 下利用 crontab 自动备份](https://tourcoder.com/auto-backup-on-linux/)」

### 后续

这里抛砖引玉，期待各位玩出更多的花样。