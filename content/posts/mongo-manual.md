---
title: "mongo常用"
keywords: ["教程", "code", "it", "mongo", "常用", "createIndex", "rename", "group", "createIndex mongo", "rename group"]
tags: ["教程", "code", "it", "mongo", "常用", "createIndex", "rename", "group"]
description: "mongo更改列名$rename"
categories: ["code"]
heading: "mongo常用"
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