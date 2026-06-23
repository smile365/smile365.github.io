---
title: "Docker安装PostgreSQL"
keywords: ["Docker安装PostgreSQL", "PostgreSQL docker-compose", "Docker运行PostgreSQL", "数据库容器化", "PostgreSQL配置"]
tags: ["PostgreSQL", "Docker", "数据库"]
description: "使用Docker和docker-compose快速安装部署PostgreSQL数据库，包含配置文件创建、启动和初始化数据库的完整步骤。"
categories: ["code"]
date: "2023-06-27T22:13:00.474Z"
---
## 准备工作

1. 创建配置文件
```yaml
version: "3"
services:
  pg:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    restart: always
    ports:
      - 5432:5432

```

 2. 启动
```bash
# 使用 dc 命令代替 docker compose （下同）
 dc up -d pg
```

 3. 创建数据库
 ```bash
dc exec -it pg psql -U postgres
CREATE DATABASE mydatabase;
# 列出数据库
\l
 ```