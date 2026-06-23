---
title: "CentOS 7安装MongoDB"
keywords: ["CentOS安装MongoDB", "MongoDB安装教程", "yum安装MongoDB", "MongoDB配置", "Linux安装数据库"]
tags: ["MongoDB", "CentOS", "安装"]
description: "在CentOS 7上通过yum配置阿里源安装MongoDB 4.0并启用安全认证。"
categories: ["code"]
date: "2018-08-13T02:55:14.439Z"
---
**配置软件的安装源**


```shell
#1、备份
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

#2、下载新的CentOS-Base.repo 到/etc/yum.repos.d/CentOS 7
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

#3、之后运行yum makecache生成缓存
yum makecache
```

在[mongo官网](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)找到repo源,并添加`vi /etc/yum.repos.d/mongodb-org-4.0.repo`

把地址改为阿里的：
```ini
[mongodb-org-4.0]
name=MongoDB Repository
#baseurl = https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/ 
baseurl=https://mirrors.aliyun.com/mongodb/yum/redhat/7Server/mongodb-org/4.0/x86_64/
#gpgcheck=1
gpgcheck=0
enabled=1
#gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
```
> 奇数版本为开发版(如3.5)，不建议生产环境使用

**安装及启动**  
```
yum install -y mongodb-org
```
编辑配置文：`vi /etc/mongod.conf` 

件建议修改日志文件路径/数据存储路径/端口/及启用密码。
 
```yaml
systemLog:
  path: /var/log/mongodb/mongod.log
storage:
  dbPath: /var/lib/mongo 
net:
  port: 47017 #监听端口
  bindIp: 0.0.0.0
security:
  authorization: enabled #启用安全认证
```

启动服务（不能使用systemctl启动）：`mongod -f /etc/mongod.conf`
