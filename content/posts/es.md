---
title: "es查询语句举例"
keywords: ["教程", "docker", "查询语句举例", "es"]
tags: ["教程", "docker", "查询语句举例", "es"]
description: "es查询语句举例"
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


