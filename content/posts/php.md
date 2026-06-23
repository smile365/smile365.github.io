---
title: "Debian安装PHP和Composer"
keywords: ["Debian安装PHP", "Composer安装教程", "PHP扩展安装", "VSCode PHP开发", "PHP开发环境配置"]
tags: ["PHP", "Composer", "Debian"]
description: "在Debian系统上安装PHP和Composer依赖管理工具，并配置VSCode进行PHP开发的完整教程。"
categories: ["code"]
date: "2023-03-08T05:39:21.528Z"
---
## 安装 php
```bash
apt update
# apt upgrade -y
apt install -y php-fpm

# 安装 php 扩展, 一般都是 php-扩展名
apt install -y php-curl php-json php-openssl
```

## 安装 composer
php 使用 [composer](https://getcomposer.org/root) 作为依赖管理工具
```bash
# 安装依赖
apt install -y wget php-cli php-zip unzip
# 下载安装程序
wget -O composer-setup.php https://getcomposer.org/installer
# 安装
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer

# 使用
composer -V
composer self-update  # 升级 composer
composer install # 安装依赖
```

## 在 vscode 中开发 php
安装扩展 
- Intelephense
- dubug

## 问题
1. git clone fatal: 无法访问 gnutls_handshake() failed: TLS 链接非正常地终止了
```bash
git config --global https.proxy 'socks5://192.168.2.1:7891'
```


## 参考文档
- [-install-php-on-debian-11](https://www.myfreax.com/how-to-install-php-on-debian-11/)
- [升级 debian](https://www.iplayio.cn/post/8400576791)
- [保持 debian 最新](https://www.debian.org/doc/manuals/debian-faq/uptodate.zh-cn.html)
- [vscode-php](https://zhuanlan.zhihu.com/p/359984466)
- [git clone 代理](https://blog.51cto.com/frytea/3348716)
- [install-and-use-composer](https://linuxize.com/post/how-to-install-and-use-composer-on-debian-10/)
- [install-composer](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-debian-11)
- [VS Code PHP 配置](https://zhuanlan.zhihu.com/p/359984466)
