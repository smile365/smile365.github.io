---
title: "只安装redis-cli"
keywords: ["只安装redis-cli", "redis客户端安装", "redis-cli安装教程", "mac安装redis-cli", "linux安装redis-cli"]
tags: ["redis-cli", "redis", "安装"]
description: "详细介绍如何在macOS、Linux、CentOS等系统上只安装redis-cli客户端而不安装redis-server服务端的方法。"
categories: ["code"]
heading: "如何只安装redis-cli，mac|windos|centos|linux"
date: "2020-04-09T05:48:31.427Z"
---
有时候我们只想用redis-cli客户端，但不想在电脑上安装redis-server服务端。下面是单独安装redis-cli的教程方法。

仅仅安装redis-cli

mac 
```bash
brew tap ringohub/redis-cli
brew update && brew doctor
brew install redis-cli
```

通用平台，[先安装go](http://sxy91.com/posts/golang)

```bash
go get -u -v github.com/holys/redis-cli 
```

linux 自行编译
```bash
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make redis-cli
sudo cp src/redis-cli /usr/local/bin/
redis-cli -h 127.0.0.1-p 6379 ping
```



参考

- [install-redis-cli-only](https://stackoverflow.com/questions/21795340/linux-install-redis-cli-only)