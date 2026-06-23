---
title: "Conductor 自定义 Worker"
keywords: ["Conductor 自定义 Worker", "Conductor Java SDK", "Netflix Conductor 开发", "Spring Boot Conductor", "微服务 Worker 实现"]
tags: ["Conductor", "Worker", "Java SDK"]
description: "基于Netflix Conductor的Java SDK实现自定义Worker，详细讲解Spring Boot项目配置和Worker接口的实现步骤。"
categories: ["code"]
date: "2023-03-17T07:16:30.731Z"
---
## 基于 Java sdk 实现自定义 worker

hello world

### 依赖
- 已经搭建完成 conductor-server
- 有 conductor-ui


### 新建 spring-boot 项目引入依赖

```xml
<dependency>
    <groupId>com.netflix.conductor</groupId>
    <artifactId>conductor-client-spring</artifactId>
    <version>3.3.6</version>
</dependency>
<dependency>
    <groupId>com.netflix.conductor</groupId>
    <artifactId>conductor-common</artifactId>
    <version>3.3.6</version>
</dependency>
<dependency>
    <groupId>com.netflix.conductor</groupId>
    <artifactId>conductor-client</artifactId>
    <version>3.3.6</version>
</dependency>
```


### 配置 conductor

在  application.yml 中配置 conductor-server 的 api 地址

```yaml
conductor:
  worker:
    pollingInterval: 2
  client:
    rootURI: http://127.0.0.1:8080/api/
    threadCount: 2
```


 ### 实现一个 worker
 比如开发一个邮件通知的 worker。写一个Java 类并实现 Worker 接口中的 getTaskDefName 和 execute 方法即可。
 ```java
 public class EmailWorker implements Worker {
    @Override
    public String getTaskDefName() {
		// 返回 worker 的名字（唯一标识）