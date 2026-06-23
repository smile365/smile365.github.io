---
title: "Docker 运行 Node Web"
keywords: ["Docker 部署 Node.js", "Node.js 容器化", "Dockerfile 编写", "Node Web 服务", "Docker 构建镜像"]
tags: ["Docker", "Node.js", "Web开发"]
description: "将Node.js Web应用容器化部署，从编写Dockerfile和.dockerignore到构建镜像并运行容器的完整流程。"
categories: ["code"]
date: "2021-03-24T07:26:58.543Z"
---
进入 node 项目，文件结构如下：
```bash
ls
# logs  node_modules  package.json  package-lock.json  public  README.md  src  tsconfig.json
```


建立一个 `Dockerfile` 文件，内容如下：
```bash
FROM node:14.15-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . .
EXPOSE 8080 # web服务监听的端口
CMD [ "npm", "run", "dev" ]
```

建立一个 `.dockerignore ` 文件，内容如下：
```bash
.vscode
log
logs
node_modules
public
```

构建镜像
```bash
# 别忘了最后的 . 表示当前目录下
docker build -t my-web-image .
# 完成后可查看
docker images
```

运行刚刚构建好的镜像
```bash
docker run -p 49160:8080 -d my-web-image
```



参考文档  
- [对Node.js Web应用进行Docker化](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
