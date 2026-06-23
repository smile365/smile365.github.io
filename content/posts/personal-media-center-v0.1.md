---
title: "家庭媒体中心v0.1"
keywords: ["Docker搭建媒体中心", "Samba文件共享", "Transmission下载", "Docker Compose配置", "家庭NAS搭建"]
tags: ["媒体中心", "Samba", "Transmission"]
description: "使用Docker Compose搭建家庭媒体中心v0.1版本，集成Samba文件共享服务和Transmission下载工具。"
categories: ["code"]
date: "2023-09-02T05:47:42.629Z"
---
## 需求
- 手动下载
- 可拷贝
- 可 smba 观看


## docker-compose

```yaml
---
version: "3"
services:
  samba:
    image: crazymax/samba
    container_name: samba
    volumes:
      - "/etc/samba:/etc/samba"
      - "/etc/docker/samba:/data"
      - "/share:/share"
    environment:
      - "TZ=Asia/Shanghais"
      - "SAMBA_LOG_LEVEL=0"
    ports:
     - 445:445
    restart: always


  transmission:
    image: lscr.io/linuxserver/transmission
    container_name: transmission
    restart: unless-stopped
    volumes:
      - /etc/docker/transmission:/config
      - /share/downloads:/downloads
    ports:
      - 30307:9091
      - 30308:51413
      - 30308:51413/udp
```



```conf
# vi /etc/samba/smb.conf
# cat /etc/samba/smb.conf grep | multi
# cat /etc/samba/smb.conf grep | aio
# server multi channel support=yes
aio read size=1
aio write size=1

[data]
  comment = server data
  path = /share
  browseable = yes
  writable = yes
# 增加下面配置则为公开访问，无需账号密码
  public=yes
  writable = yes
  create mask=0775
  directory mask=0775
  available = yes
```
