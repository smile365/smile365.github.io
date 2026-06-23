---
title: "Redis布隆过滤器配置"
heading: "Redis配置布隆过滤器Bloom Filter完整教程"
keywords: ["Redis布隆过滤器", "Bloom Filter Redis", "RedisBloom安装", "Redis模块加载", "Redis缓存优化"]
tags: ["Redis", "布隆过滤器", "RedisBloom"]
description: "介绍如何在Redis中安装和配置RedisBloom布隆过滤器模块，通过配置文件和命令行两种方式加载。"
categories: ["code"]
date: "2019-08-06T07:12:55.203Z"
draft: "true"
---
下载并编译
```bash

git clone https://github.com/RedisBloom/RedisBloom.git redisbloom
cd redisbloom
make
mkdir -p /opt/redismodules/
mv redisbloom.so /opt/redismodules/

# Assuming you have a redis build from the unstable branch:
redis-server --loadmodule /opt/redismodules/redisbloom.so

#查看默认配置 
awk -F: '/^[^#]/ {print}' /etc/redis.conf
```

使用配置文件加载
`vim /etc/redis.conf`
```conf
loadmodule /opt/redismodules/redisbloom.so
```

使用命令行加载
`redis-cli`
```shell
MODULE LOAD /opt/redismodules/redisbloom.so
```


参考  

- [ReBloom](https://oss.redislabs.com/redisbloom/Quick_Start/)
- [redisbloom-py](https://github.com/RedisBloom/redisbloom-py)
- [Redis的BloomFilter](https://redislabs.com/blog/rebloom-bloom-filter-datatype-redis/)
- [redis-module](https://segmentfault.com/a/1190015976157)
- [redis-modules-hub](https://redislabs.com/community/redis-modules-hub/)
- [Redis 高级主题之布隆过滤器(BloomFilter)](https://juejin.im/post/5cfd060ee51d4556f76e8067)