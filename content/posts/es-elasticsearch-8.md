---
title: "Elasticsearch 8 REST API使用指南"
keywords: ["Elasticsearch 8 REST API", "ES Document APIs", "ES单文档操作", "ES批量操作", "ES查询指南", "Elasticsearch 8.10教程"]
tags: ["Elasticsearch", "REST API", "ES接口", "搜索引擎"]
description: "详细介绍Elasticsearch 8.10的REST API使用方式，包括单文档和多文档操作的增删改查示例。"
categories: ["code"]
heading: "Elasticsearch 8.10 REST API使用指南"
date: "2020-05-09T06:42:21.580Z"
---
## 前言
es 官方文档藏的很深。如果点击"定价"旁边的"文档"是找不到的。正确路径是从 Platform -> Elasticsearch -> 文档 -> Overview -> Elasticsearch 8.10 -> What is Elasticsearch?  

或者直接搜索 [elasticsearch guide 8](https://www.elastic.co/guide/en/elasticsearch/reference/8.10/elasticsearch-intro.html)


## REST API
主要看 [Document APIs](https://www.elastic.co/guide/en/elasticsearch/reference/8.10/docs.html#docs)

单文档 APIs
- Index： 新增/保存
- Get：获取
- Delete：删除
- Update：更新


多文档 APIs：
- Multi get：获取多个
- Bulk：批量
- Delete by query：
- Update by query：
- Reindex：

## 例子

Multi get `get /index_name/_mget?_source_excludes=input,rawJSON,output`
```json
{
    "docs":[
        {"_id":"4d74d20d-da12-45bf-a5e5-a4640dcee50b"}
    ]
}
```






