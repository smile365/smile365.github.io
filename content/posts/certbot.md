---
title: "cerbot-on-debian11"
keywords: ["教程", "cerbot on debian11", "certbot", "openresty"]
tags: ["教程", "cerbot on debian11", "certbot", "openresty"]
description: "打开 certbot 官网，按照教程安装。"
categories: ["code"]
heading: "cerbot-on-debian11"
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