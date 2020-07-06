#### 前戏

```js
启动Mongodb    mongod  -- dbpath "数据库目录"
默认端口是 27017
redis  默认端口 9527 
mysql 默认端口 3306
django 默认端口 8000
```

#### 概念

```js
mysql    		mongodb
数据库			  数据库
表			   collections
列			   field
row				documents
```

#### 命令

```js
(1) 查看所有存在磁盘上的数据库  : show dbs
(2) 查看当前数据库存在磁盘上的数据表 : show tables 
(3) use 数据库  创建数据库 或切换数据库
########使用了不能存在的对象即创建对象##########


// 数据库的增删改查

// 查
db.user.find()  查看所有
db.user.findOne({})  查看符合条件的第一个   

// 增加
db.user.insertOne({})
db.user.insertMany([{},{}])

#  改
// 添加field  如果写条件就过滤出符合条件的记录添加一个字段,如果不写过滤条件,就都加字段
db.user.update({id:1}, 
    {$set:{'hobby':['收集杯子',"喝茶"]}}, 
)
// 如果不存在的字段就创建字段, 如果字段存在就更新
db.user.update({"id":1}, 
    {$set:{"age":28}}, 
    
)

# 删
// 全部删除
db.user.remove({"name":"yuan"})
// 删除第一条符合条件的数据
db.user.deleteOne({name:"yuan"})
// 删除所有符合条件的数据
db.user.deleteMany({name:'yuan'})



# $all（只有都包含才会显示）
> db.c5.insert({name:’zhangsan’,age:[1,2,3,4,5,9,10]});
WriteResult({ “nInserted” : 1 })
> db.c5.insert({name:’lisi’,age:[2,4,7,9,10]});
WriteResult({ “nInserted” : 1 })
> db.c5.insert({name:’wangwu’,age:[4,7,8,16,24]});
WriteResult({ “nInserted” : 1 })
> db.c5.find({age:{$all:[4,7,9]}});
{ “_id” : ObjectId(“543e20c5e2c90313035e7d06”), “name” : “lisi”, “age” : [ 2, 4, 7, 9, 10 ] 
> 

# $in(只要有包含1个就显示)
> db.c5.find();
{ “_id” : ObjectId(“543e2098e2c90313035e7d05”), “name” : “zhangsan”, “age” : [ 1, 2, 3, 4, 5, 9, 10
] }
{ “_id” : ObjectId(“543e20c5e2c90313035e7d06”), “name” : “lisi”, “age” : [ 2, 4, 7, 9, 10 ] }
{ “_id” : ObjectId(“543e20ece2c90313035e7d07”), “name” : “wangwu”, “age” : [ 4, 7, 8, 16, 24 ] }
>db.c5.find({age:{$in:[1,2,3]}});
{ “_id” : ObjectId(“543e2098e2c90313035e7d05”), “name” : “zhangsan”, “age” : [ 1, 2, 3, 4, 5, 9, 10
] }
{ “_id” : ObjectId(“543e20c5e2c90313035e7d06”), “name” : “lisi”, “age” : [ 2, 4, 7, 9, 10 

// 数学比较符
    $gt : 大于db.user.find({"age":{$gt:73}})                                 $gte : 大于等于
    $lt : 小于
    $lte: 小于等于
    $eq: 等于
    : 也是等于
                                                                          
```

##### $修改器

```js
db.user.find({})
// 强制修改 $set
db.user.update({age:12}, {$set:{"age":28}}
)

// 暴力删除字段 ,hobby  后面的1  是固定写法
db.user.insert([{"id":1,name:"yuan"},{name:"yuan"}])
db.user.updateOne({"name":"yuan"},{$unset:{"hobby":1}})

// 引用增加  在原有值的基础上增加 
db.user.updateMany({"name":"yuan"},{$inc: {"id":1}}
)

```

##### array 修改器

```js

// array  修改器

db.user.find({})

// $push  增加元素
db.user.updateOne({name:'yuan'}, 
    {$push:{"hobby":"haha"}}, 
)

// $pull 删除元素
db.user.updateOne({name:'yuan'}, 
    {$pull:{"hobby":"haha"}}, 
)


// pushAll   迭代添加 相当于extends

db.user.updateOne({
    'name':"yuan"
}, 
    {$pushAll:{"hobby":['hecha','beizi']}}
   
)


// $pop  默认删除最后一条  
// -1 删除第一个         1  删除最后一个
db.user.update({"name":"yuan"}, 
    {$pop:{"hobby":-1}}, 
    { multi: false, upsert: false}
)
```

##### $ 字符











