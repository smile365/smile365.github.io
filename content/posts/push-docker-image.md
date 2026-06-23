---
title: "阿里云容器镜像服务使用教程"
keywords: ["阿里云容器镜像服务", "Docker 推送镜像", "阿里云 Registry", "Docker 构建推送"]
tags: ["Docker", "阿里云", "容器镜像"]
description: "详细介绍如何在阿里云容器镜像服务中创建仓库、构建 Docker 镜像并推送和拉取到 Registry 的完整步骤。"
categories: ["code"]
---
# 阿里云容器镜像服务使用教程

## 环境准备
- docker 

## 创建仓库

1. 打开[阿里云镜像服务网站](https://cr.console.aliyun.com/repository/cn-hangzhou/sxycn/jdk/details)

2. 创建仓库
本次为 jdk-agent

3. 登录阿里云Docker Registry
```bash
docker login --username=yourname registry.cn-hangzhou.aliyuncs.com
#用于登录的用户名为阿里云账号全名，密码为开通服务时设置的密码。
```


4. 构建镜像
先编辑 Dockerfile
```
FROM  openjdk:11
RUN wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```

构建
```
docker build -t jdk11-agent:1.0 .
docker images
# REPOSITORY    TAG       IMAGE ID       CREATED              SIZE
# jdk11-agent   1.0       c771ac51922a   About a minute ago   672MB
```



5. 将镜像推送到Registry
```
$ docker login --username=yourname registry.cn-hangzhou.aliyuncs.com
$ docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/sxycn/jdk-agent:[镜像版本号]
$ docker push registry.cn-hangzhou.aliyuncs.com/sxycn/jdk-agent:[镜像版本号]
# 请根据实际镜像信息替换示例中的[ImageId]和[镜像版本号]参数。
```


6. 从Registry中拉取镜像
```
$ docker pull registry.cn-hangzhou.aliyuncs.com/sxycn/jdk-agent:[镜像版本号]
```