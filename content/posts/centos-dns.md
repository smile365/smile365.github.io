---
title: "centos dns配置"
keywords: ["教程", "时遇到", "未知的错误", "centos dns", "centos yum", "Could not resolve", "host", "yum", "vi", "etc"]
tags: ["教程", "时遇到", "未知的错误", "centos dns", "centos yum", "Could not resolve", "host", "yum"]
description: "因无法解析域名，需要配置域名解析服务器。"
categories: ["code"]
heading: "centos yum时遇到Could not resolve host: mirrors.aliyun.com; 未知的错误"
date: "2020-04-29T07:24:57.231Z"
---
使用`yum`命令的时候若出现
```bash
Couldn't resolve host 'mirrors.cloud.aliyuncs.com'、Could not resolve host: mirrors.aliyun.com; 未知的错误、Could not resolve host: mirrors.tuna.tsinghua.edu.cn; 未知的错误等
```

因无法解析域名，需要配置域名解析服务器。

```bash
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
```

或者编辑`vi /etc/resolv.conf`，在文末增加
```dsconfig
nameserver 8.8.8.8
nameserver 114.114.114.114
```

有疑问欢迎加入开发者交流QQ群：1003185728。