---
title: "Codeigniter 中集成 Jquery File Upload"
slug: "codeigniter-jquery-file-upload-integrated"
author: "Bin Hua"
lastmod: 2017-06-05 07:03:47
date: 2017-06-05 07:03:47
tags: ["jquery", "codeigniter", "php"]
---

最近在基于 PHP 的框架 Codeigniter（以下简称 CI 框架） 开发一款系统，其中用到了上传功能，考虑到用户体验等问题，采用了开源的 Jquery File Upload，如下图

![](/imgs/ci_uploader_01.png)

上传之前

![](/imgs/ci_uploader_02.png)

上传之后

**集成步骤**

- 去 Jquery File Upload 的官网（下面提供）下载最新版本

- 将 demo 中 php 文件夹下面的 UploadHandler.php 文件放入到 CI 框架中的 libraries 文件夹中

- 新建 controllers 文件，然后写入如下内容 

```
function fileupload()
{
    $this->load->library("UploadHandler");
}
```

搞定。

如果你需要对上传的文件做一些操作，比如更改文件名字，存储路径等，你可以自行修改 UploadHandler.php 文件，或者自己写类库，甚至你还可以修改 `Jquery File Upload` 的源码。

**附下载地址**

[Codeigniter 官网](https://github.com/bcit-ci/CodeIgniter)，使用的是 3.1 稳定版。

[Jquery File Upload 官网](https://github.com/blueimp/jQuery-File-Upload)，使用的是最新版。
