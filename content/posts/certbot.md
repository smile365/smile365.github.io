---
title: "Debian 11安装Certbot教程"
keywords: ["Certbot安装教程", "Debian 11 SSL证书", "Let's Encrypt", "Nginx SSL配置", "snap安装certbot"]
tags: ["Certbot", "SSL", "Debian"]
description: "在Debian 11上通过snap安装Certbot，配合Nginx或OpenResty自动获取和配置Let's Encrypt免费SSL证书。"
categories: ["code"]
date: "2023-05-31"
draft: "true"
---
1. 先安装 [openresty](https://gitee.com/smile365/blog/blob/master/openresty.md)

2. 安装 certbot

打开 [certbot](https://certbot.eff.org/instructions?ws=nginx&os=debianbuster) 官网，按照教程安装。

```bash
apt install snapd
snap install core; 
snap refresh core;
apt remove certbot
snap install --classic certbot

certbot --nginx
```