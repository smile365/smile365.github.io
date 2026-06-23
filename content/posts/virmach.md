---
title: "Virmach VPS教程"
keywords: ["Virmach注册", "VPS购买教程", "Shadowsocks搭建", "CentOS配置", "便宜VPS", "VPS入门"]
tags: ["Virmach", "VPS", "教程"]
description: "本文介绍Virmach VPS的注册购买全流程，从下单选择1美元套餐到SSH登录服务器，以及CentOS系统上安装Shadowsocks的详细步骤。"
categories: ["code"]
date: "2020-02-20T07:56:16.162Z"
draft: "true"
---
注册[virmach](https://billing.virmach.com/aff.php?aff=9472&gid=1)，建议填写国内邮箱。使用代理登录virmach 的订单容易被"PENDING"待定。

登录后到vps列表页面，选择1美元一个月的套餐。

立即订购 

![order now](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582185425395.png
)


选择操作系统

选择服务器机房

同意协议

![add to cart](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582186425110.png)

付钱

![checkout](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582185909552.png)



![确认](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582186699216.png)

找到我的服务

![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582186813872.png)


找到服务器详细信息

![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582187068821.png
)

记录下ip和root密码(password)


登录服务器
![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1582187241195.png)

```bash
ssh root@ip
yes
password
```

Error: Cannot retrieve metalink for repository: epel. Please verify its path and try again

参考 [CentOS6.6安装ShadowSocks服务](https://github.com/jeezlee/www.pickerlee.com/wiki/CentOS6.6%E5%AE%89%E8%A3%85ShadowSocks%E6%9C%8D%E5%8A%A1)

```bash
cat /etc/*-release
#centos 6.10

yum install -y python-setuptools && easy_install pip
pip install shadowsocks
```