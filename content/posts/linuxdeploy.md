---
title: "安卓手机运行Linux系统"
keywords: ["Linux Deploy教程", "安卓手机装Linux", "旧手机变服务器", "坚果手机刷机", "Linux on Android"]
tags: ["LinuxDeploy", "安卓", "刷机"]
description: "利用Linux Deploy在旧安卓手机上安装Linux系统将其变身为服务器，涵盖Root权限获取和各型号坚果手机的刷机方法。"
categories: ["code"]
heading: "使用Linux Deploy在安卓手机上运行Linux服务器"
date: "2023-07-23T22:13:00.474Z"
---
## 前言

旧手机没用了，旧物利用一下。

## 前提条件
1. 一台安卓手机
2. 刷机获取 root 权限


## 安装超级用户管理程序



## 安装 linuxdeploy

下载[linuxdeploy.app](https://github.com/meefik/linuxdeploy/releases) 到手机安装即可





## 坚果手机刷机方法
- 锤子坚果YQ601+YQ607机型：可使用Kingroot手机获取完整ROOT权限
- 锤子坚果Pro：使用工程线，进入高通9008模式，刷入第三方recovery，获取ROOT
- 锤子坚果Pro2：借助高通9008工程线进入线刷模式，刷recovery，然后ROOT
- 锤子坚果Pro2S：使用降级包，降级手机系统，直接解锁BL，再次刷入twrp，最终获取ROOT
- 锤子坚果R1：刷入系统降级包，，直接解锁BL，最好刷入twrp，最终获取ROOT权限
- 锤子坚果3：使用工程线进高通9008模式，线刷第三方twrp刷入ROOT包
- 锤子坚果M1/L：高通9008模式，线刷第三方recovery，最终刷入ROOT包


## 参考
- [用Linux Deploy让安卓手机成为Linux服务器](https://blog.luvying.com/archives/linux-deploy)
