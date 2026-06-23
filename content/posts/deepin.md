---
title: "Deepin 深度操作系统配置"
keywords: ["Deepin 配置指南", "深度操作系统", "SSH 服务开启", "xrdp 远程桌面", "Linux 常用软件"]
tags: ["Deepin", "SSH", "Linux桌面"]
description: "介绍Deepin 20.9操作系统中SSH远程连接和xrdp远程桌面的开启方法，帮助用户快速配置国产Linux操作系统。"
categories: ["code"]
date: "2023-08-25T19:16:05.490Z"
---
## 版本信息
- deepin:  20.9

系统自动安装了 ssh（需要启动），xrdp（默认启动）

## 开启 ssh
参考[官方文档](https://wiki.deepin.org/en/System_Management/Service_Management/SSH_service)，注意此系统的 ssh 服务直接叫 ssh 不是 sshd。
```bash
sudo systemctl start ssh
# sudo apt-get install openssh-server
# sudo /etc/init.d/ssh start
```


## 开启远程桌面 xrdp

参考 [xrdp](https://github.com/deepin-community/xrdp)


## 常用软件

### 微信
基于 Windows


## 参考资料

