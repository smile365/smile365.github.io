---
title: "使用Hugo创建个人博客"
heading: "使用Hugo从零搭建个人博客站点：安装到主题配置"
keywords: ["Hugo搭建博客", "Hugo安装教程", "静态博客生成器", "Hugo主题配置", "Hugo入门教程"]
tags: ["Hugo", "博客", "静态网站"]
description: "详细教程教你使用Hugo静态站点生成器在CentOS或Mac上安装并创建个人博客，从安装到主题配置一步到位。"
categories: ["code"]
date: "2018-07-04"
---
### 安装

Centos 系统安装方法：
```sh
yum-config-manager --add-repo https://copr.fedorainfracloud.org/coprs/daftaupe/hugo/repo/epel-7/daftaupe-hugo-epel-7.repo
yum -y install hugo
hugo version
```

Mac 系统[安装](https://gohugo.io/getting-started/quick-start/)方法：
使用 
```sh
# 安装
brew install hugo
# 测试
hugo version
```

如果 安装不成功，可以直接[下载](https://github.com/gohugoio/hugo/releases)二进制文件[安装](https://discourse.gohugo.io/t/script-to-install-latest-hugo-release-on-macos-and-ubuntu/14774)
下载并解压后。
```
# 改成可运行
chmod +x hugo
# 放到用户目录
mv hugo /usr/local/bin/
# 测试
hugo version
```

之后的创建站点、使用主题、添加内容、启动等都可以从[quick-start](https://gohugo.io/getting-started/quick-start/)查看到。

debian 系统[安装方法](https://gohugo.io/installation/linux/#debian)
```bash
apt install -y hugo
```

## 创建 blog
1. 参考 [官方教程](https://gohugo.io/getting-started/quick-start/#create-a-site)初始化一个 blog
```bash
# 找一个文件夹
mkdir -p /usr/share/www
cd /usr/share/www && hugo new site myblog
cd myblog
git init
# 配置主题
git submodule add https://gitee.com/smile365/wehuth.git themes/wehuth

# 配置文件
cp themes/wehuth/exampleSite/config.toml .
```