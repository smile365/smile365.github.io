---
title: "Elasticsearch查询语句举例"
keywords: ["Elasticsearch查询语句", "ES查询举例", "ES Docker部署", "Elasticsearch搜索语法"]
tags: ["Elasticsearch", "ES查询", "搜索引擎"]
description: "通过Docker快速部署Elasticsearch 8.10并展示常用查询语句，帮助你快速上手ES搜索功能。"
categories: ["code"]
heading: "es查询语句举例"
date: "2023-10-30T13:47:16.917Z"
---
使用 docker 运行 es
```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.4
```

配置密码

```bash
docker exec -it elasticsearch bin/elasticsearch-reset-password -u elastic
```


