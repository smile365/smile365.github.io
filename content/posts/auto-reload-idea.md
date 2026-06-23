---
title: "IDEA热部署配置"
heading: "IntelliJ IDEA Mac版Spring Boot热部署配置"
keywords: ["IDEA热部署配置", "Spring Boot热加载", "IntelliJ热部署", "Mac IDEA devtools", "Java热部署"]
tags: ["IDEA", "热部署", "Spring Boot"]
description: "详细介绍IntelliJ IDEA 2022.3.2 Mac版本下Spring Boot Devtools热部署的配置步骤和依赖添加方法。"
categories: ["code"]
date: "2023-02-16T05:33:39.140Z"
---
## 添加依赖
```xml
<!--热部署依赖，生产环境、应用被打成jar包后，自动失效-->
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-devtools</artifactId>
	<optional>true</optional>
</dependency>
```

## 打开 settings
快捷键：Command + ，
![enter description here](https://cdn.sxy21.cn/static/imgs/1676525901618.png)

![enter description here](https://cdn.sxy21.cn/static/imgs/1676526063793.png)



![enter description here](https://cdn.sxy21.cn/static/imgs/1676526118622.png)