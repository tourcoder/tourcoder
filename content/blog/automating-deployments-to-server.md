---
title: "利用 Git Hooks 自动部署到服务器"
slug: "automating-deployments-to-server"
author: "Bin Hua"
lastmod: 2018-02-12 07:28:14
date: 2018-02-12 07:28:14
tags: ["git", "GitHub"]
---

使用自动部署的原因很多，我们主要是因为人手关系，还有就是希望开发人员专注于代码的开发，提升代码质量，而非被这些机械式的事情浪费大量时间。

**注意点**

这里只是搭建一个简单的自动部署功能，起到抛砖引玉的作用，网上也有一些收费的很不错的自动部署的服务，欢迎去购买。

再次强调两点：

1. 下面的教程内容并不建议你使用在生产力环境里；
 
2. 自动部署之前应该需要有严格的测试过程。

**知识点**

Git Hooks，俗称钩子，关于它的官方文档 [Git Hooks](https://git-scm.com/docs/githooks)。

**开始**

为了方便，本次教程服务器和客户端部分都在我本地的电脑上。

- 服务器部分

    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-01.png)

    新建 server 文件夹作为服务器端，在服务器端里创建一个自动部署的目录 `autodeploy`，使用 `git init --bare` 初始化，查看这个目录你会发现，它将 `.git` 的内容显示出来了。它和 `git init` 的区别是它显示的是 `.git` 中的内容，而 `git init` 是初始化一个常规仓库，并且将 `.git` 作为一个隐藏的文件夹在这个仓库里的。

    `blogdata` 是服务器上需要被自动部署到的地方，进入这个文件夹，将自动部署的内容克隆过来，执行命令 `git clone ~/desktop/server/autodeploy posts`，完成后查看，`posts` 存在了，自动部署的内容将会被自动部署在 `posts` 这个文件夹里。
    
    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-03.png)

    进入到 `autodeploy/hooks` 这个文件夹，执行命令 `vi post-receive`，创建一个文件，在文件中输入上面的内容，完成编辑保存。
    
    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-02.png)

    赋予 `post-receive` 文件执行权限，到这里，自动部署的服务器部分基本完成了。
    
- 开发端（开发者）

    和日常开发一样，并没有什么特别的地方
    
    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-04.png)

    创建一个文件夹，用 `git init` 初始化，添加远程库，注意这里要添加的是自动部署的库，添加完成后查看。
    
    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-05.png)
    
    日常开始，添加内容，比如添加了 `test.md` 文件，然后 `push` 到服务器端。
    
    ![](https://storage.tourcoder.com/tcblog/automating-deployments-to-server-06.png)

    进入到服务器端查看，会发现，已经自动部署到对应的文件夹了。
    
**写在最后**

如前面所说这只是一个指导教程，不应该如此简单的应用于生产力环境，切记。

**更新**

刚才有人问如果是用 GitHub 那么该怎么操作呢？这里抛砖引玉的简单说明下，基本步骤如下：

- GitHub 上创建项目

    进入 `Setting->Webhooks` 新建一个 `Webhook`，如下图  其中 `Which events would you like to trigger this webhook?` 这里的内容你可以根据自己的需要进行配置，填好后提交即可。
    
- 服务器部分，添加你的回调的文件，我这里用的是 PHP，文件名：`autodeploy.php`
    
    ```
    <?php 
    $getBody = file_get_contents("php://input"); 
    if (empty($getBody)) {     
        echo "fail"; 
    } else {     
        $content = json_decode($getBody, true);     
        echo $content["ref"]; 
    } 
    ```
    
    代码只是显示提交的分支，自己可以根据自己的需求定制这里的内容。
   
- 把一些开发好的内容提交到 GitHub 后，在 `Setting->Webhooks` 下查看 `Recent Deliveries`，即可以看到你的提交是否已经触发并发送到服务器了。这里 `Body` 部分就是返回的信息。 

