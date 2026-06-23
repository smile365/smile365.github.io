---
title: "个人NAS影音系统搭建"
keywords: ["NAS影音搭建", "个人媒体服务器", "黑群晖", "DLNA设置", "SMB共享", "家庭影院"]
tags: ["NAS", "影音", "群晖", "媒体服务器"]
description: "搭建黑群晖NAS影音系统，实现电视电脑手机多端播放电影并支持外挂字幕。"
categories: ["code"]
date: "2022-04-24T09:57:53.008Z"
---
## 需求
虽然目前在线看视频很方便，还有诸多不便，比如找不到想看的片源，受限于版权问题，无法在一个 app 中找到想看的。美剧、国外电影往往没有。搭建了一套黑群晖，这样可以通过远程下载想看的电影到 nas，回到家就可以用电视\手机\iPad 看 nas 里的电影。

## 电视端

小米电视自带的"高清播放器"可以自动找到内网中的NAS，以DLNA 方式连接；如果需要 SMB 方式要自行添加 NAS 的 IP 地址和 NAS 的账号密码。

DLNA 协议对于无线连接支持很好，即使是 4K 原盘也可以通过WIFI连接流畅播放，缺点是无法加载外挂字幕。

SMB 协议可以切换声道，加载外挂字幕（特效字幕），还能网络自动匹配字幕，缺点是对于无线连接支持很不好（好像最高5MB/S 左右），即使是 1080P Remux 也可能要经常缓冲。

需求：
- 支持电视、电脑、手机、平板
- 可插入 u 盘，考走文件。

## 文件拷贝
有时候需要拷贝一个电影分享给朋友，就需要能实现从 nas 拷贝到 u 盘的功能。第一个是插入 u 盘自动挂载，二、文件的浏览、搜索、复制。
步骤：
1. 实现 U 盘的自动挂载
     a. 使用 [autofs](https://linuxconfig.org/automatically-mount-usb-external-drive-with-autofs)
     b. 使用 [usbmount](https://github.com/rbrito/usbmount)（弃用，比较老，10年未更新了）
     c. [mdev](https://www.cnblogs.com/lifexy/p/7891883.html)
2. 文件管理(浏览、搜索、复制)
   a. http(s) 协议的文件管理软件，然后通过另一台设备（电脑、平板、手机）操作文件。稍微不太优雅，需要另一台设备。
   b. 使用 debian 的桌面端版本。比较优雅，稍微比服务器端版本耗费一点资源。
   c. 基于 smb 协议，使用 es文件浏览器 搜索和复制文件。插入 u 盘到 debian，手机操作。（广告多）

### autofs

```bash
apt install -y autofs
lsblk #列出设备
```

### usbmount

需要[自行编译](https://github.com/rbrito/usbmount)安装，编译成功后会在上层目录出现 [.deb](https://blog.csdn.net/wangmg0118/article/details/72026739) 安装包。

```
apt install -y git debhelper build-essential
git clone https://github.com/rbrito/usbmount.git
cd usbmount 
pkg-buildpackage -us -uc -b
# apt install -y git-buildpackage
# https://mirrors.tuna.tsinghua.edu.cn/help/debian/
cd ..
# 安装依赖
# apt -f install 
# 安装
# dpkg -i usbmount_0.0.24_all.deb
apt install -y gdebi