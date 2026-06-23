---
title: "KVM远程管理方案"
keywords: ["KVM远程管理", "IPMI功能", "远程控制电脑", "PiKVM", "树莓派远程管理"]
tags: ["KVM", "IPMI", "远程管理"]
description: "介绍如何利用开源方案给普通PC实现类似IPMI的远程KVM管理功能，支持远程开关机、BIOS操作和操作系统安装。"
categories: ["code"]
heading: "给普通PC实现IPMI远程管理功能"
date: "2023-10-28T08:47:11.754Z"
---
## 前言
一些概念
- IPMI，[Intelligent Platform Management Interface](https://www.bilibili.com/video/BV1FQ4y1f7iT/)
- KVM，Keyboard Video Mouse
- USB
- USB OTG



介绍 ipmi，用途。

## 思路
网络
屏幕
键盘
USB 设备

桥接，搭一座桥

视频输出（HDMI） ---> 视频输入
USB 接口 <----> 软件模拟出 USB HUB （任意类型的 USB 设备）----



## 解决方案

- 至少两个 USB 的设备。一个「从属设备」模式，接收视频数据，显示界面。一个「主设备」模式，模拟鼠标键盘，发送鼠标键盘信号。也就是说，至少需要一个支持 OTG 功能的 USB。这种 USB 一般直接接入 CPU，让 CPU 直接发送命令，而不是接入 USB 集线器，当做设备给 CPU 读取。 
- HDMI 采集卡。
- 可运行 KVM 软件的硬件。

## 软件
- [Open IP-KVM](https://github.com/Nihiue/open-ip-kvm)
- PiKVM 

## 硬件
可以运行 armbian 或者 openwrt ，且带 OTG USB 的硬件都可以
- 树莓派(zero)/[香橙派](https://www.bilibili.com/read/cv21169636/)/R2S
- 电视盒子
- 斐讯 n1
- 随身WiFi


## 下载 os
从 [nanopi-r2s-rk3328.img.bz2
](https://github.com/Yura80/os) 下载


## 给电脑开机有什么办法
- 按开机键
- [WOL](https://zhouyuqian.com/2020/04/04/Linux-Wake-on-Lan/) 信号（需主板支持，大部分主板）
- IPMI（需主板支持，仅服务器主板）
