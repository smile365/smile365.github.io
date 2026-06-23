---
title: "redis-py使用教程"
keywords: ["redis-py使用教程", "python连接redis", "redis uri连接", "redis自动解码", "redis python客户端"]
tags: ["redis-py", "python", "redis"]
description: "详细介绍Python的redis-py客户端库的使用方法，包括通过URI连接Redis和自动解码配置。"
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