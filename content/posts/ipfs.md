---
title: "IPFS分布式文件系统教程"
heading: "IPFS星际文件系统从入门到Spring Boot集成"
keywords: ["IPFS使用教程", "IPFS Docker安装", "IPFS Java集成", "分布式文件系统", "星际文件系统"]
tags: ["IPFS", "分布式存储", "教程"]
description: "IPFS星际文件系统完整使用教程，涵盖概念介绍、Docker安装部署以及Spring Boot项目集成IPFS存储。"
categories: ["code"]
date: "2022-07-25T16:46:23.029Z"
---
## IPFS 介绍

星际文件系统（InterPlanetary File System，缩写为IPFS）是一个旨在实现文件的分布式存储、共享和持久化的网络传输协议。该技术诞生于 2014 年，由协议实验室（Protocol Labs）创建，IPFS 整合了最先进的网络技术，如（BitTorrent、DHT、Git、SFS等）。

## IPFS 用途
参考
- [24个IPFS应用项目](https://www.163.com/dy/article/GJPIJU3O0552EI9F.html)
- [使用案例](https://zh.wikipedia.org/wiki/%E6%98%9F%E9%99%85%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F#%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B)
- [玩转 ipfs](https://zhuanlan.zhihu.com/p/93803533)

## 安装
参考 [在 docker 中安装 ipfs](https://docs.ipfs.tech/install/run-ipfs-inside-docker/#set-up)

Start a container running ipfs and expose ports 4001 (P2P TCP/QUIC transports), 5001 (RPC API) and 8080 (Gateway):

```bash
docker pull ipfs/kubo
docker run -d --name ipfs -p 4001:4001 -p 4001:4001/udp -p 8080:8080 -p 5001:5001 ipfs/kubo
docker logs -f ipfs

docker exec ipfs ipfs swarm peers

```

或者使用 docker-compose 安装

```yaml
version: '3'

services:
  ipfs:
    image: ipfs/kubo
    restart: always
    ports:
      #- "4001:4001"  # P2P TCP/QUIC transports
      #- "8080:8080"  # Gateway
      - "5001:5001"   # RPC API
```

## 在 spring boot 项目使用 ipfs 存储 Java 对象

当做序列化存储的后端。

创建一个 Java spring boot 项目，引入依赖
```xml
    <dependency>
        <groupId>com.github.ipfs</groupId>
        <artifactId>java-ipfs-api</artifactId>
        <version>v1.4.0</version>
    </dependency>