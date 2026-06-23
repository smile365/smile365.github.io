---
title: "Proxmox VE 虚拟机创建与磁盘管理"
keywords: ["Proxmox VE 虚拟机", "PVE 磁盘类型", "VirtIO 硬盘", "Linux 挂载大硬盘", "2TB 以上分区"]
tags: ["Proxmox VE", "虚拟机", "磁盘管理"]
description: "介绍 Proxmox VE 虚拟机创建、IDE/SATA/VirtIO 磁盘类型选择以及使用 GPT 分区挂载超过 2TB 大硬盘的教程。"
categories: ["code"]
date: "2023-02-12T08:13:02.861Z"
---
## usb 安装 pve

## 创建虚拟机
- debian
- windows 11
- alpine
- xxx

## 虚拟机磁盘类型介绍
 IDE、SATA、VirtIO、Block SCSI 
IDE 和 Block SCSI  性能低下不推荐，如果需要使用硬盘直通则使用 SATA 否则推荐使用 VirtIO



## 使用模板创建虚拟机

## 给虚拟机挂载超过 2T 的磁盘
参考[fdisk到底支不支持2T以上容量的硬盘分区](https://steemit.com/cn/@oflyhigh/-fdisk2t-2019-11-05)
```bash
root@debian11:~/docker/nas# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0  128G  0 disk 
├─sda1   8:1    0  127G  0 part /
├─sda2   8:2    0    1K  0 part 
└─sda5   8:5    0  975M  0 part [SWAP]
sdb      8:16   0    4T  0 disk 
```

sdb 为新增的磁盘
```bash
fdisk /dev/sdb
# 依次输入
m # 提示
g # 创建 GPT 类型的分区表（默认是 dos 类型，dos 类型最大支持 2T）
p # 打印分区表信息
n # 创建分区
... # 一路默认（回车）
w # 保存
```

挂载到指定目录，参考[Linux配置硬盘自动挂载](https://www.jianshu.com/p/336758411dbf)
```bash
# 格式化分区
mkfs -t ext4 /dev/sdb1
# 创建需要挂载的目录
mkdir /share
# 挂载
mount /dev/sdb1 /share
# 检查是否挂载成功 
df -h