---
title: "PowerJob 分布式任务调度"
keywords: ["PowerJob 分布式调度", "PowerJob Server 部署", "Docker 部署 PowerJob", "任务调度框架"]
tags: ["PowerJob", "分布式调度", "Docker"]
description: "在 IDEA 中运行和通过 Docker 部署 PowerJob 分布式任务调度与计算框架的完整配置教程。"
categories: ["code"]
date: "2022-12-30T09:13:22.765Z"
---
## 环境
-PostgreSQL 14
- JDK 11
- Maven 
 

## idea 运行 PowerJob Server

pg 14 不需要配置方言 [PowerJobPGDialect](https://www.yuque.com/powerjob/guidence/problem#DYCZ9)，否则会出现 [SQL Error ERROR](https://github.com/PowerJob/PowerJob/issues/509) 错误


application-daily.properties 配置文件如下：
```properties
oms.env=DAILY
logging.config=classpath:logback-dev.xml

spring.datasource.core.driver-class-name=org.postgresql.Driver
spring.datasource.core.jdbc-url=jdbc:postgresql://127.0.0.1:30132/powerjob-daily
spring.datasource.core.username=postgres
spring.datasource.core.password=xxx
spring.datasource.core.hikari.maximum-pool-size=20
spring.datasource.core.hikari.minimum-idle=5


oms.instanceinfo.retention=1
oms.container.retention.local=1
oms.container.retention.remote=-1

oms.instance.metadata.cache.size=1024
oms.accurate.select.server.percentage = 50

```

## Docker 运行 PowerJob Server

```bash
docker run -d --restart=always \
       --name powerjob-server \
       -p 7700:7700 -p 10086:10086 \
       -e TZ="Asia/Shanghai" \
       -e JVMOPTIONS="" \
       -e PARAMS="--spring.profiles.active=product \
       --spring.datasource.core.driver-class-name=org.postgresql.Driver \
       --spring.datasource.core.jdbc-url=jdbc:postgresql://localhost:5432/powerjob-product \
       --spring.datasource.core.username=postgres \
       --spring.datasource.core.password=postgres" \
       tjqq/powerjob-server:latest
```

## docker-compose 运行 PowerJob