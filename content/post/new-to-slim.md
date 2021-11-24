---
title: "Slim 初体验"
slug: new-to-slim
author: Bin Hua
lastmod: 2020-08-13 09:10:14
date: 2017-11-02 07:18:23
tags: [php", "slim"]
---

最近喜欢上了 Slim 这个小型的 PHP 框架，用它写 RESTFUL API 感觉好极了。官方地址：[Slim Framework](https://www.slimframework.com/)，Github 上的[开源地址](https://github.com/slimphp/Slim)。

根据官网的说明，建议使用 [Composer](https://getcomposer.org/) 来安装，具体步骤如下

- 安装 Composer，如果你已经安装好，这步略过（具体怎么安装 Composer，请去[这里](https://getcomposer.org/)查看）

- 然后用 Slim-skeleton 安装，执行命令 

```
php composer.phar create-project slim/slim-skeleton [your-project-name]
```

等待完成，因为一些因素，速度会慢一点。

进入到创建好的文件夹，执行命令

```
php -S localhost:8080
```

用浏览器访问 `localhost:8080`，就能看到具体的内容，至于更多的参数用法，请自行去查询。

下面是一个 API 的简单示例

```
<?php
require 'vendor/autoload.php';
$app = new Slim\App();
$app->get('/article', function ($request, $response, $args) {
    return $response->write("You visit article");
});
$app->get('/article/{id}', function ($request, $response, $args) {
    return $response->write("You visit artile" . $args['id']);
});
//$app->post, $app->put, $app->delete 等是类似的写法
$app->run();
```

这会我体验下来，和我之前用的 CI 比较起来，它更为直接轻便，还是值得一用的。