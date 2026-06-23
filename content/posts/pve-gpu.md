---
title: "Proxmox VE 显卡直通教程"
keywords: ["PVE 显卡直通", "GPU 直通虚拟机", "Proxmox GPU 透传", "NVIDIA 显卡直通"]
tags: ["Proxmox VE", "显卡直通", "GPU"]
description: "在 Proxmox VE 7.2 上配置 NVIDIA GT 1030 显卡直通到虚拟机的详细步骤及硬件环境要求。"
categories: ["code"]
heading: "pve 显卡直通"
date: "2023-04-14T09:26:22.517Z"
draft: "true"
---
## 前言


## 环境

硬件环境：
- CPU	INTEL E5-2696v4
- 主板	华南 X99-F8 
- 固态硬盘	海康威视C2000PRO 2TB SSD M.2
- 机械硬盘	希捷 16T
- 内存	三星 32G 2133MHz
- 电源	长城 G6 全模组 650W
- 显卡	微星 gt1030 AERO ITX 2G d4
- 机箱	撒哈拉 C360 ATX 中塔背线机箱
- 散热	杂牌 X99 CPU散热器

软件环境：
- Virtual Environment 7.2-3


查看显卡 ID
```
# 
lspci -nn |grep NVIDIA
# VGA NVIDIA  rev a1
03:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP108 [GeForce GT 1030] [10de:1d01] (rev a1)
# 10de:1d01
```