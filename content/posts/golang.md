---
title: "Golang简明入门教程"
keywords: ["golang入门", "go语言安装", "go mod配置", "centos安装go", "mac安装go"]
tags: ["Golang", "Go", "编程入门"]
description: "Go 语言的快速入门指南，涵盖 CentOS 和 Mac 系统的安装方法、Go Modules 配置以及第一个 Hello World 项目的创建。"
categories: ["code"]
date: "2019-07-26T05:45:19.158Z"
---
centos


```bash
yum -y install go
go version
```

[或者通过压缩包安装](https://golang.google.cn/dl/)  
```bash
# 下载
wget https://golang.google.cn/dl/go1.14.5.linux-amd64.tar.gz
# 解压
tar -C /usr/local -xzf go1.14.5.linux-amd64.tar.gz
# 配置环境变量
vim /etc/profile
# 尾部增加如下内容：
export PATH=$PATH:/usr/local/go/bin
# 重新打开一个shell即可
```


mac

[下载golang安装包](https://golang.google.cn/doc/install),或者使用brew
```bash
brew install go
```

配置镜像
```bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```

```bash
mkdir test && cd test
go mod init hello

```

在test目录下新建文件`hello.go`
```go
package main

import "github.com/astaxie/beego"

func main() {
    beego.Run()
}
```

运行`go run hello.go`



参考  

- [install](https://golang.google.cn/doc/install)
- [goproxy.cn](https://github.com/goproxy/goproxy.cn)
- [go mod](https://zhuanlan.zhihu.com/p/60703832)