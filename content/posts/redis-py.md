---
title: "redis-py使用教程和自动解码"
keywords: ["教程", "python", "redis", "自动解码", "客户端", "使用 连接", "redis py", "uri"]
tags: ["教程", "python", "redis", "自动解码", "客户端", "使用 连接", "redis py", "uri"]
description: "redis-py使用教程"
categories: ["code"]
heading: "python的客户端redis-py使用uri连接redis使用教程"
date: "2020-07-28T09:22:46.180Z"
---
安装
```bash
pip install redis
```

```python
import redis
# 'redis://:密码@host:端口/数据库db'
uri = 'redis://:password@127.0.0.1:6379/0'
r = redis.from_url(uri)
r.ping()
```