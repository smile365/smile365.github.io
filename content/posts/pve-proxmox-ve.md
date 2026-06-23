---
title: "Proxmox VE 企业级虚拟化平台教程"
keywords: ["Proxmox VE 安装", "PVE 系统教程", "裸机安装 Proxmox", "Win11 虚拟机 PVE", "PVE 清华源配置"]
tags: ["Proxmox VE", "虚拟化", "安装教程"]
description: "从裸机安装 Proxmox VE 7.2 系统开始，涵盖 Win11 虚拟机创建、virtio 驱动安装和清华镜像源配置的完整教程。"
categories: ["code"]
heading: "裸机安装 Proxmox VE - pve 系统 7.2-1"
date: "2022-09-06T06:33:45.328Z"
---
## 安装 pve 系统
通过 u 盘启动安装 [Proxmox VE](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) 系统。

通过官网下载 iso 镜像 [proxmox-ve_7.2-1.iso](https://www.proxmox.com/en/downloads/category/iso-images-pve),推荐先下载 BitTorrent 然后通过迅雷等 bt 工具下载，国内下载 pve 系统特别慢。或者通过[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/proxmox/)镜像站下载


下载后放入已经制作好的 ventoy 的 u 盘中，插入电脑，设置 bios 从 u 盘启动。安装系统的时候建议插上网线，不然装完系统配置网络比较麻烦。


## win11 系统

准备工具（登录 pve 然后点击从 URL 下载）：

- 下载驱动 [virtio-win-0.1.208-1.iso](https://foxi.buduanwang.vip/pan/proxmox-edge/%E9%A9%B1%E5%8A%A8/)
- 下载系统镜像 [zh-cn_windows_11_business_editions_x64_dvd.iso](https://foxi.buduanwang.vip/pan/proxmox-edge/ISO/)
- 或者 ed2k[迅雷](https://sysin.org/blog/windows-11/#%E2%AC%87%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80)下载   [zh-cn_windows_11.iso](ed2k://|file|zh-cn_windows_11_business_editions_x64_dvd_f5f6bcbd.iso|5413181440|88CA1AE28F5F8A238647561B5C00E511|/)



参考 [安装教程](https://www.gordon2000.com/2021/10/pvewindows-11-step-by-step.html),

如果没有到安装界面是因为没有配置启动项，或者启动项配置错误。通过 PVE 重启虚拟机，然后按 F2 进入 bois 设置启动项为 CD-ROM 即可。可参考[视频教程](https://www.bilibili.com/s/video/BV16L4y1B7F3)

然后搜索激活工具 [HEU KMS Activator](https://github.com/zbezj/HEU_KMS_Activator/releases) 或者 AAct Portable 进行激活。


## 配置清华镜像源

参考教程[Proxmox 软件仓库镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/proxmox/)
```bash
cp /etc/apt/sources.list /etc/apt/sources.list.bak
echo deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware > /etc/apt/sources.list
echo deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware >> /etc/apt/sources.list
echo deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware >> /etc/apt/sources.list
echo deb https://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware >> /etc/apt/sources.list

cat /etc/apt/sources.list 

# 
echo deb https://mirrors.tuna.tsinghua.edu.cn/proxmox/debian/pve bookworm pve-no-subscription > /etc/apt/sources.list.d/pve-no-subscription.list
```

配置 替换 CT Templates 的源:
```bash
cp /usr/share/perl5/PVE/APLInfo.pm /usr/share/perl5/PVE/APLInfo.pm_back
sed -i 's|http://download.proxmox.com|https://mirrors.tuna.tsinghua.edu.cn/proxmox|g' /usr/share/perl5/PVE/APLInfo.pm
# 需要重启才生效
# reboot
```