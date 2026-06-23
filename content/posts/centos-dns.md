---
title: "CentOS DNS配置教程"
keywords: ["CentOS DNS配置", "yum无法解析域名", "Could not resolve host", "resolv.conf配置", "Linux网络配置"]
tags: ["CentOS", "DNS", "yum"]
heading: "CentOS yum报错Could not resolve host的DNS解决方法"
description: "解决CentOS使用yum时出现Could not resolve host报错的方法，通过配置DNS域名解析服务器即可修复网络连接问题。"
categories: ["code"]
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