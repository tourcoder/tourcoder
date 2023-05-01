---
title: "用 koa 开发 REST API"
slug: "build-rest-api-with-koa"
author: "Bin Hua"
lastmod: 2018-08-06 07:42:25
date: 2018-08-06 07:42:25
tags: ["MongoDB", "api", "nodejs", "koa", "RESTFUL"]
---

Nodejs 特点之一是高并发，Koa2 是下一代的 Nodejs 框架。所以，我尝试写一套基于 Koa2 的 REST API。

技术选型及开发工具

- KoaJS 
- MongoDB 
- macOS 系统版本：10.13.6 
- Sublime Text 编辑器不重要，看自己喜欢 
- Terminal 终端，输入各种命令 

#### 实施步骤

- 安装基础开发环境
   
  node.js 安装 
  
  这部分内容自行搜索，我一般喜欢用的安装方式是命令行安装 
  
  ```
  nvm wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
  ```
  
  然后使用 `nvm` 来安装 `node.js`，除非有比较好的特性，不然我一般都使用 LTS 版本。 
  
  Tips: nvm 的版本会变化，你可以通过三种方式更新 nvm 的版本，   
  
  - 用最新版本的连接地址直接升级，最新地址，从这里 `https://github.com/creationix/nvm` 找。   
  - 用 git 更新，进入到 cd ~/.nvm，直接用 git 更新。   
  - 通过 zsh-nvm 来更新，项目地址 `https://github.com/lukechilds/zsh-nvm`，简单有效。   上面的三种方式都挺方便的。
  -  
 mongodb 安装及启动 
 
 ```
 brew install mongodb 
 brew services start mongodb
 ```
 
 tips: 
 
 - 可以通过 `brew services list` 或者 `ps aux | grep mongo` 来查看是否正常运行。
 - 可以通过 `cat /usr/local/var/log/mongodb/output.log` 查看日志。
 - 配置 `vi /usr/local/etc/mongod.conf`

- 编写代码

  创建一个项目 api 在终端中输入如下命令，注意终端的位置 
  
  ```
  mkdir api 
  cd api 
  npm init
  ```
  
  初始化成功后，该项目即创建成功。 
  
  安装 koa 相关的内容 
  
  ```
  npm install -S koa //安装 koa 
  npm install -S koa-router //安装 koa 中间件 
  npm install -S koa-bodyparser //用来接受 json
  ```
  
 基本代码 
 
 创建一个文件 `serv.js`，将下面代码输入进去，其实下面代码中的分号 ; 都可以去掉，但我习惯结尾有结束方式，因而保留了分号。 
 
 ```
 const Koa = require("koa"); 
 const Router = require("koa-router"); 
 const BodyParser = require("koa-bodyparser"); 
 const app = new Koa(); 
 const router = new Router(); 
 router.get("/", async function (ctx) { 	
 ctx.body = {msg: "Hello World!"} 
 }); 
 app.use(router.routes()).use(router.allowedMethods()); 
 app.listen(3000);
 ```
 
 直接执行命令 `node serv.js`，web 访问 `localhost:3000` 即可得到 `{"msg":"Hello World"}` 上面代码比较清晰，无需过多解释，其中 `async` 请看 `koa` 中的解释，而 `ctx` 是 `context` 的简写。 
 
 tips: REST 的几个动作
 
 - GET：类似于数据库中的 SELECT 
 - POST：类似数据库中的 INSERT 
 - PUT：类似数据库中的 UPDATE(完整资源) 
 - DELETE：类似数据库中的 DELETE 
 - PATCH：类似数据库中的 UPDATE(改变的属性)  
 
 这里用到了 get 动作，有时候 get 属性中有参数，形如 `localhost:3000/?currentpage=100`，则将上面代码改成 
 
 ```
 const Koa = require("koa"); 
 const Router = require("koa-router"); 
 const BodyParser = require("koa-bodyparser"); 
 const app = new Koa(); 
 const router = new Router(); 
 router.get("/", async function (ctx) { 	
 let currentpage = ctx.request.query.currentpage; 	
 ctx.body = {cpage: currentpage} 
 }); 
 app.use(router.routes()).use(router.allowedMethods()); 
 app.listen(3000);
 ```
 
 使用到了 `ctx.request.querry`，此时你访问上面的地址，即可得到 `{"cpage":"100"}`，如果 `currentpage` 这个参数不存在，那则会得到 `{}`，为了让 REST 更合理，一般会加入判断，当参数不存在则表示 `currentpage` 在第一页，这个判断可以在服务器端做，也可以在客户端做，在服务器端做，则更改上面的代码 
 
 ```
 const Koa = require("koa"); 
 const Router = require("koa-router"); 
 const BodyParser = require("koa-bodyparser"); 
 const app = new Koa(); 
 const router = new Router(); 
 router.get("/", async function (ctx) { 	
 let defaultpage = 0 	
 let currentpage = ctx.request.query.currentpage || defaultpage; 	
 ctx.body = {cpage: currentpage} 
 }); 
 app.use(router.routes()).use(router.allowedMethods()); 
 app.listen(3000);  
 ```
 
 其中 `ctx.request.query.currentpage || defaultpage` 等同于 `ctx.request.query.currentpage?ctx.request.query.currentpage:defaultpage`，先判断是否存在，存在则使用前面，不存在则使用后面，这是 C++ 中的条件操作符 `（条件表达式）？（条件为真时的表达式）：（条件为假时的表达式）`，详见推荐阅读[2]。 
 
 多个参数，形如 `localhost:3000/?currentpage=100&limit=20`，则和上面一样，添加即可
 
 ```
 router.get("/", async function (ctx) { 	
 let defaultpage = 0 	
 let currentpage = ctx.request.query.currentpage || defaultpage; 	
 let limit = ctx.request.query.limit //你也可以增加判断 	
 ctx.body = {cpage: currentpage, limit:limit} 
 });  
 ```
 
 有时候会通过 `ctx.params.rel` 的方式接受链接中的参数。 如上面的几个动作所言，除了 get 之外，我们还有 post 等其他的动作，一般让客户端发送(POST) json 串到服务器，则服务器端接受，则用到了 `koa-bodyparser`。将上面的代码改成 
 
 ```
 router.get("/", async function (ctx) { 	
 let defaultpage = 0 	
 let currentpage = ctx.request.body.currentpage || defaultpage; 	
 let defaultlimit = 1000 	
 let limit = ctx.request.body.limit || defaultlimit //你也可以增加判断 	
 ctx.body = {cpage: currentpage, limit:limit} 
 });
 ```
 
 用 POST 方式访问 `localhost:3000`，你会得到一个错误 `TypeError: Cannot read property 'currentpage' of undefined`，那是因为你没有使用 `koa-bodyparser` 这个中间件。
 
 完整代码如下 
 
 ```
 const Koa = require("koa"); 
 const Router = require("koa-router"); 
 const BodyParser = require("koa-bodyparser"); 
 const app = new Koa(); 
 const router = new Router(); 
 app.use(BodyParser()); //引入中间件，很重要 
 router.get("/", async function (ctx) {     
 let defaultpage = 0     
 let currentpage = ctx.request.query.currentpage || defaultpage;     
 let limit = ctx.request.query.limit || defaultpage;     
 ctx.body = {cpage: currentpage,limit:limit} 
 }); 
 router.post("/", async function (ctx) {     
 let defaultpage = 0     
 let currentpage = ctx.request.body.currentpage || defaultpage;     
 let defaultlimit = 1000     
 let limit = ctx.request.body.limit || defaultlimit //你也可以增加判断
 ctx.body = {cpage: currentpage, limit:limit} 
 }); 
 app.use(router.routes()).use(router.allowedMethods()); 
 app.listen(3000);  
 ```
 
 这样，get 和 post 方式完成了，其他的几个动作，基本和它们类似。 
 
- 数据库 mongoDB 

 我不止一次说过，我越来越不喜欢 mongoDB，但在和 NodeJS 相结合方面，目前看起来，只有它是最好的，Mysql 结合太吃内存了。 上面我们已经安装了 mongoDB，并且已经让它在后台运行，在项目中执行命令 `npm install -S mongodb` 将它引入到项目中来。 
 
 现在先进入 mongoDB 进行操作，终端中输入如下命令
 
 ```
 mongo //进入数据库 
 use testdb //进入 testdb 这个库，如果没有则会自动创建 
 db.users.insert({"name": "name_example"}) //在集合 users 中插入数据
 db.users.find() //查看集合 users 中的内容
 ```
 
 其中 `db.users.insert` 这里插入后会得到返回结果 `WriteResult({ "nInserted" : 1 })`，db.users.find 查询得到返回结果，比如这里是 `{ "_id" : ObjectId("5b69179505be97c64bd88d43"), "name" : "name_example" }`。 这样在 mongoDB 的 testdb 数据库的 users 这个集合中有了一条数据，现在我们通过代码将它读出来。
 
 ```
 const MongoClient = require('mongodb').MongoClient; 
 const DB_URL = "mongodb://127.0.0.1:27017/"; 
 MongoClient.connect(DB_URL, function(err, db) {     
 if (err) throw err;     
 const dbo = db.db("testdb");     
 dbo.collection("users"). find({}).toArray(function(err, result) {         
 if (err) throw err;         
 console.log(result);         
 db.close();     
 }); 
 });
 ```
 
 上面就是通过 MongoClient 将数据读出来的常规代码，得到的结果是 `[{ _id: 5b69179505be97c64bd88d43, name: 'name_example' }]`。 现在很多项目中使用 mongoose 作为数据库操作的中间件，每次看到这个名字，我都会想到加拿大鹅，😓 从 GitHub 上可以看出，它来自 Automattic，那个出了 wordpress 的公司。 除了 mongoose 之外，Automattic 还出了 monk 这个小型的 node.js 下操作 mongodb 的中间件。 
 
 具体两个是如何用的，网上的教程很多，可以自行搜索，这里大概讲解下 monk，因为够小够有意思。 
 
 在项目中安装 monk `npm install -S monk`   
 
 在 serv.js 增加如下代码，引入 monk，并且链接数据库 `testdb`
 
 ```
 const Monk = require('monk'); 
 const mongodb = Monk('localhost:27017/testdb');
 ```
 
 在调取的地方输入以下代码 
 
 ```
 router.get("/users", async (ctx) => { 	
 const user = mongodb.get('users');   	
 const userdata = await user.find({});   	
 ctx.body = userdata; 
 });
 ```
 
 访问 /users 即可得到上面一样的结果。需要注意的是，这里只是举例，很多通用的常量可以放在外面，也可以写成 module，比如也有人喜欢写成 
 
 ```
 const user = mongodb.get('users') 
 const mainuser = async ctx => {     
 const userdata = await user.find();     
 ctx.response.body = userdata; 
 } 
 router.get("/users", mainuser);  
 ```
 
 这样也可以，具体我就不一一复述。 还有其他 REST 操作动作 post，put，path，delete，基本类似，也不再一一复述。
 
 数据组成 REST 显示出来的数据应该是一个完整的数据，每个需求不一样，会导致的数据的结构不一样，一般我在设计数据结构的时候，包含几个要素。   
 
 头部信息  
 
 body 
 
 body 部分，主要分三个，code, msg, data，所以一般结构如下
 
 `{"code":"","msg":"","data":""}`  
 
 code: 表示返回的状态，有时候头部的返回不能够完全表达状态，则可以使用 code 来 
 
 msg: 表示返回的信息，一般解释说明都在里面 
 
 data: 返回的数据，有数据则返回数据，无数据则返回空 在代码中的体现如下 
 
 ```
 let temp = {}; 
 temp.code = ""; 
 temp.msg = ""; 
 temp.data = ""; 
 ctx.body = JSON.stringify(temp);
 ```
 
 
 Access Token 上面写到的接口很容易被人读取调用，这就需要用到身份验证。身份认证的东西方式很多  
 
 - `HTTP Basic`
 - `API KEY`
 - `Oauth2`
 - `JWT`   
 
 具体怎么用，看个人喜欢，我本人使用的是自己写的一个模块。 
 
 用 koa 开发 REST API 的入门文章完成，其中有什么错漏的地方，还请指正。
 
#### 推荐阅读：

[1] https://developer.github.com/v3/

[2] https://stackoverflow.com/questions/2802055/what-does-the-construct-x-x-y-mean