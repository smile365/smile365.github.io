---
title: "Docker 安装 MongoDB"
keywords: ["Docker 安装 MongoDB", "MongoDB 容器部署", "Docker MongoDB 教程", "MongoDB 数据持久化"]
tags: ["Docker", "MongoDB", "数据库"]
description: "使用Docker快速部署MongoDB数据库，支持自定义版本选择、数据持久化挂载和端口映射配置。"
categories: ["code"]
date: "2018-11-02T07:16:11.158Z"
---
使用默认配置后台运行最新版：
```bash
# 安装
docker run -p 47017:27017 --name sxymongo  -d mongo
# 进入容器
docker exec -it sxymongo  /bin/sh
# 连接 mongo
mongosh
```

使用其他版本和配置数据路径：
```bash
mkdir -p ~/mongo/data
chcon -Rt svirt_sandbox_file_t ~/mongo
docker run -p 47017:27017 --name daxindb -v /home/daxin/mongo/:/data/db -d mongo:3.4 --replSet "rs0"
```

官方文档：
https://docs.docker.com/samples/library/mongo/#mongoversion

参考：http://www.runoob.com/docker/docker-install-mongodb.html
