---
title: "Mongoose 学习笔记"
slug: study-mongoose
author: "Bin Hua"
lastmod: 2020-07-18 06:10:57
date: 2018-08-22 07:45:57
tags: ["nodejs", "mongodb", "笔记", "mongoose"]
---

之前写的用 [koa 开发 REST API](/build-rest-api-with-koa)，有提到过这个总让我想起加拿大鹅的中间件，索性好好学习一下。

**准备工作**

- 安装好 `mongodb`，并新建一个数据库 `testdb` 
 
- 新建一个工程，并初始化 `npm init` 

- 安装 `mongoose npm install mongoose`

**连接数据库**

新建文件 serv.js，并输入一下代码

```
const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/testdb");
let db = mongoose.connection;
db.on("error", function (error) {
    console.log("fail--->" + error);
});
db.on("open", function () {
    console.log("connected");
});
```

执行该文件 node serv.js，可以得到正确或错误的信息。

注意：如果你的 mongodb 版本较高，则会出现下面的警告

```
DeprecationWarning: current URL string parser is deprecated, and will be removed in a future version. To use the new parser, pass option { useNewUrlParser: true } to MongoClient.connect.
```

解决办法，只要将

```
mongoose.connect("mongodb://127.0.0.1:27017/testdb");
```

改成

```
mongoose.connect("mongodb://127.0.0.1:27017/testdb", {useNewUrlParser: true});
```

即可。

**Schema，Model和Entity**

- Scheme

    可以理解为表结构，可以写成
    
    ```
    const mongoose = require("mongoose");
    let tempSchema = new mongoose.Schema({
    name : {type:String},
    age  : {type:Number, default:0},
    password: {type:String}
    });
    ```
    
    也可以写成
    
    ```
    const mongoose = require('mongoose');
    let tempSchema = new mongoose.Schema;
    tempSchema.add({ name:'String', age:'Number', password:'String'});
    ```
    
- Model

    可以理解为数据库操作层，主要是对数据库层面的操作，其实就是对数据库中的集合（表）进行操作，比如结合刚才创建的 Schema，创建一个 Model
    
    ```
    let db = mongoose.connect("mongodb://127.0.0.1:27017/testdb");
    let tempModel = db.model("tempCollection", tempSchema);
    ```
    
    需要注意，这里的 tempCollection 就是集合，如果该集合在数据库中存在，则将内容保存在里面，如果不存在，则会自动创建，并且再将内容保存在里面。
    
- Entity

    由 Model 创建的实体，同样结合上面的数据
    
    ```
    var tempEntity = new tempModel({
       name : "tcoder",
       age  : 100,
       password: "123456"
    });
    console.log(tempEntity.name);
    ```
    
    结果将得到 tcoder，Entity 使用 save 来保存数据，即 tempEntity.save()。
    
    这样最终完整的代码
    
    ```
    const mongoose = require("mongoose");
    mongoose.connect("mongodb://127.0.0.1:27017/testdb", {useNewUrlParser: true});
    let db = mongoose.connection;
    let tempSchema = new mongoose.Schema({
        name : {type:String},
        age  : {type:Number, default:0},
        password: {type:String}
    });
    let tempModel = db.model("tempCollection", tempSchema);
    let tempEntity = new tempModel({
        name : "tcoder",
        age  : 1,
        password: "123456"
    });
    tempEntity.save(function(error,data){
      if(error){
         console.log("error :" + error);
      }else{
         console.log(data);
      }
    });
    ```
    
    执行代码，将会得到结果，进入到数据库中检查
    
    ```
    >use testdb
    switched to db testdb
    >db.tempCollection.find()
    { "_id" : ObjectId("5b7d104487a4a795f30984ea"), "age" : 1, "name" : "tcoder", "password" : "123456", "__v" : 0 }
    ```
    
**数据库的几个操作：增删改查**

- 增

    增加的操作，在前面的代码中已经实现，使用了 Entity 的 save 功能，即可将内容保存到 mongodb 中。
    
    ```
    let tempEntity = new tempModel({
        name : "tcoder",
        age  : 1,
        password: "123456"
    });
    tempEntity.save(function(error,data){
      if(error){
         console.log("error :" + error);
      }else{
         console.log(data);
      }
    });
    ```
    
    也可以用 Model 中的 create 功能来实现。
    
    ```
    tempModel.create({ name:"newname", age:2}, function(error,data){
    if(error) {
            console.log(error);
        } else {
            console.log(data);
        }
    });
    ```
    
    进入数据库中查询，可以发现该条数据也保存在数据库中了，如果同时增加多条信息，则可以通过数组方式增加，即
    
    ```
    tempModel.create([{ name:"newname", age:2},{ name:"new2", age:30 }{ name:"test2", age:3 },{ name:"new3", age:4 }], function(error,data){
        if(error) {
            console.log(error);
        } else {
            console.log(data);
        }
    });
    ```
    
- 删除

    和 sql 不一样，这里使用的是 remove 这个来进行资源的删除，其格式是 Model.remove(条件,回调);

    ```
    let condition = {name : 'tcoder'};
    tempModel.update(condition, function(error){
        if(error) {
            console.log(error);
        } else {
            console.log('Deleted');
        }
    });
    ```
    
    运行将会提示删除，当集合中没有满足条件的数据时，还是会出现删除成功的提示。

- 修改/更新

    使用 Model 的 update 进行更新，其格式是 Model.update(条件,更新对象,回调); 如找到 name 是 tcoder 的用户，将他的密码改成 654321，则代码如下

    ```
    let condition = {name : 'tcoder'};
    let updatecontent = {$set : {password :"654321"}};
    tempModel.update(condition, updatecontent, function(error){
        if(error) {
            console.log(error);
        } else {
            console.log('Updated');
        }
    });
    ```

    运行将会更新成功，因为是更新，它本身并没有创建数据的功能，所以当集合中没有满足条件的数据时，还是会出现更新完成的提醒。
    
- 查询

    在 mongodb 中使用 find 命令来操作 db.tempCollection.find({})，其中 find 中可以有参数，如果没有写入参数，则表示查询所有的内容。而在 mongoose 中也是类似的概念，结合上面的 Model 进行操作。

    ```
    tempModel.find({},function(error,data){
        if(error) {
            console.log("error :" + error);
        } else {
            console.log(data);
        }
    });
    ```
    
    比如我们要查询 name 为 t 的用户，则在 find 中加入参数 {name:"t"} 即

    ```
    tempModel.find({name:"t"},function(error,data){
        if(error) {
            console.log("error :" + error);
        } else {
            console.log(data);
        }
    });
    ```
       
    运行，则得到结果是不存在的，因为的确是没有这条数据，将 t 改成 tcoder 即可得到数据。

    注意：因为版本的问题，这里也会出现一个警告 DeprecationWarning: collection.find option [fields] is deprecated and will be removed in a later version.，更多看下面推荐阅读[1]。

    有时候会对一些内容进行过滤，则格式为 Model.find(查询条件, 过滤条件, 回调);，比如下面一段代码
    
    ```
    let filterCondition = {name:1}
    tempModel.find({}, filterCondition, function(error,data){
        console.log(data)
    })
    ```

    表示显示所有的数据，但只显示这些数据的 name 这一部分。因为 _id 是自动显示的，所以在结果中会出现 name 和 _id 两个。如果不想显示 _id，则将其设置为 0，即上面的条件可以更改为

    ```
    let filterCondition = {name:1, _id:0}
    ```
    
    即可只显示 name 的内容，需要注意的是，name 后面的数字 1 可以是任何一个非空的数字，但不可以是 0，如果是 0，则程序会报错 undefined。而一些数据没有一些键值，这个不会产生影响。
    
    Model.findOne(查询条件, 回调) 则是查询第一条符合条件的数据

    ```
    tempModel.findOne({age:1}, function(error, data){
       console.log(data)
    });
    ```
    
    注意这里是第一条数据。

    Model.findById(查询的_id, 回调) 是根据 _id 查询一条数据，用法如下

    ```
    tempModel.findById('5b7d1f2a44e00f98705fda67', function(error, data){
        console.log(data)
    });
    ```

**查询中的条件符号**

`$gt` 大于 (>)，格式为 `{"age":{"$gt":1}}`

`$gte` 大于等于 (>=)，格式为 `{"age":{"$gte":1}}`

`$lt` 小于 (<)，格式为 `{"age":{"$lt":1}}`

`$lte` 小于等于 (<=)，格式为 `{"age":{"$lte":1}}`

`{"age":{"$gt":1,"$lt":2}` 则表示大于 1 小于 2

`$ne` 不等于 (!=)，格式为 `{name:{$ne:"tcoder"}}`

和上面结合的多个条件则形如 `{name:{$ne:"tcoder"}, age:{"$lte":1}}`

`$in` 包含，格式为 `{age:{$in:[1,2]}}`，表示包含 1 和 2 的，也可以是单独一个

`$or` 或者，满足一个条件即可，格式为 `{"$or":[{"name":"tcoder"},{"age":1}]}`，这里的条件应该是数组形式

`$exists` 是否存在，格式为 `{age:{$exists:true}}`，查看所有 age 存在的文档

所有的条件的查询格式如下
    
    ```
    let condition = "待查询的状态"
    tempModel.find(condition,function(error,data){
      console.log(data)
    });
    ```

**游标**

有时候查询结果的数量庞大，会需要对结果进行操作，这就要用到 limit 函数，格式为 `Model.find(查询条件,过滤条件（可为 null ）,{limit函数体}, 回调);`，比如要查询 10 条数据，则

```
tempModel.find({},null,{limit:10},function(error,data){
    console.log(data);
});
```

和 limit 有同样作用的是 skip 函数，但不同的是，如果数量少于 skip 的数量，则不会显示内容

```
tempModel.find({},null,{skip:2},function(error,data){
    console.log(data);
});
```

既然要处理多个结果中的一部分内容，势必就需要用到排序功能，sort 函数就是用来做排序的，格式和上面差不多，`Model.find(查询条件,过滤条件,{sort函数体},回调)`，比如要按 age 升序排列

```
tempModel.find({},null,{sort:{age:1}},function(error,data){
    console.log(data);
});
```

其中 1 表示是升序，-1 表示是降序。

**mongoDB 操作**

- 导入文件夹

    ```
    mongorestore -d db_name 文件夹目录 // 文件夹里是文件
    ```
    
- 删除数据库

    ```
    use db_name; // 选择要删除的数据库
    db.dropDatabase()
    ```

**推荐阅读**

[1] https://github.com/Automattic/mongoose/issues/6880

[2] https://mongoosejs.com/docs/guide.html