---
title: "MongoDB常用操作"
keywords: ["MongoDB教程", "createIndex", "rename使用", "group聚合", "MongoDB常用命令", "数据库操作"]
tags: ["MongoDB", "数据库", "教程"]
description: "总结了MongoDB创建索引、更改列名和group聚合等常用操作的使用方法。"
categories: ["code"]
date: "2018-11-07T07:37:22.875Z"
draft: "true"
series: ["blog"]
---
创建索引[createIndex](http://www.runoob.com/mongodb/mongodb-indexing.html)
```javascript
db.values.createIndex({open: 1, close: 1}, {background: true})
```

mongo更改列名[$rename](https://docs.mongodb.com/manual/reference/operator/update/rename/)
```javascript
db.students.updateMany( {}, { $rename: { "nmae": "name" } } )
```


group
```
db.user.aggregate([{$group : {_id : "$date", total : {$sum : 1}}}])
```