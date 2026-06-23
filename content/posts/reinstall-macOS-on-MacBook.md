---
title: "MacBook重装macOS"
keywords: ["MacBook重装系统", "macOS重装教程", "WinPE Mac", "忘记密码重装Mac", "MacBook刷机"]
tags: ["MacBook", "macOS", "重装系统"]
description: "在忘记密码的情况下将安装了Windows的MacBook重装为macOS系统的详细教程，包括WinPE制作和启动方法。"
categories: ["read"]
heading: "How to reinstall macOS on a 2017 12‑inch MacBook"
date: "2026-06-04T04:10:33.971Z"
---
## 前言

接了一个装小龙虾(openclaw)的单子。电脑是 2017 款的 12 英寸  MacBook，安装了双系统（windows+macos），双系统的密码都忘记了。说如果可以的话看看硬盘里没有重要文件，实在看不了就重装。

在没开启 BitLocker 设备加密的电脑上完全可以用 WinPE 进行系统维护，查看设备上的文件。

> PE 是 Windows 预安装环境(Windows Preinstallation Environment)的简称,可以把它理解为一个装在U盘里面的迷你系统。

> **📢注：** Intel 芯片的 Mac 可以安装 windows 或者 WinPE，但 Apple 芯片的（如 M1以上系列）Mac 电脑不支持原生启动 x86 版 Windows，因此无法使用 WinPE 进行系统维护。


## winPE 制作

操作环境：Windows11 64位系统

### U盘启动工具：ventoy
[ventoy](https://www.ventoy.net/cn/doc_disk_layout.html)  是一款强大的 U盘启动工具。ventoy 会把 U 盘分成 2 个分区，它使用了一小部分存储（约 33MB）作为启动引导，剩下的空间（最大的）相当于普通 u 盘，可再次格式化。只需要把 ios 等系统镜像文件放到 U盘任意目录，安装时 ventoy 会扫描 U盘内支持安装的系统镜像，并使用列表显示支持安装的系统。

**安装 ventoy**

ventoy 仅支持在 windows、Linux 操作系统下安装，暂不支持 MacOS。

1. 下载 [ventoy](https://www.ventoy.net/cn/download.html) 并解压；
2. u 盘插入 windows 电脑 ，点击 Ventoy2Disk.exe ，分区类型选择 GPT，点击安装；
3. 把需要安装的系统镜像文件（如 [Hikari_PE.iso](https://www.ventoy.net/cn/distro_iso/winpe.html)）拷贝到 U盘内即可；

> 硬盘分区表有 MBR 与 GPT 两种，MBR（Master Boot Record，主引导记录）已经过时了，诞生于1983年 IBM PC时代。Mac 电脑仅支持GPT（GUID Partition Table）GUID 分区表，属于 UEFI 标准，大约2005年以后开始流行。


### PE工具：edgeless

[edgeless](https://wiki.edgeless.top/v2/guide/burn.html) 是一款强大而优雅的半开源PE工具，极简且没有广告，制作 PE 时可通过独有的插件系统选择所需的功能。

1. 下载 [Edgeless Hub](https://down.edgeless.top/) 解压后运行 edgeless-hub.exe 点击'制作启动盘'；
2. 跳过 ventoy 的安装（直接右上角关闭），确认 U 盘后 edgeless 会自动下载所需文件，并拷贝到 U盘目录。


## MacBook 启动 WinpE

因 WinPe 没有 mac 硬件相关的驱动，因此 Intel 芯片的 Mac 电脑虽然可以运行 WinPE，但无法使用触控板和键盘，因此需要单独配一套键盘和鼠标（蓝牙有线均可）才能操作。

1. 按住开机键 2 秒后，立刻安装 Option 键，等待出现硬盘选择界面；
2. 插入 U盘，此时应该出现 EFI Boot 选项，选中后回车；
3. 自动进入 ventoy 引导，然后选择 WinPE 系统；
4. 此时可以查看 Mac 电脑本身硬盘内的文件；

> 若第 2 步无法显示 EFI Boot 选择，大概率是 U 盘启动没制作正确，需要检查是否是 GPT 分区。

## 重装 mac 成 macos

之前是双系统，要求重新安装成 macos 单系统，苹果电脑本身就有  Internet Recovery 模式，即使忘记密码也能重装系统。

1. 关机后，按住 Option + Command + R 并开机，看到旋转的地球图标即可松手；
2. 连接 WiFi（或通过拓展坞连接有线）；
3. 进入  Internet Recovery 后选择 磁盘工具，此时可以看到两个分区；
4. 顶部打开"显示所有设备"，点击 APPLE SSD xxx ，选择"抹掉（Erase）"；
5. 名称可以填 Macintosh HD，或者随意，其他保持默认；
6. 确认后回到 Internet Recovery 界面，选择重装系统即可，根据网速大概 30 分钟到 2 小时即可安装完成。

> Apple 芯片（M系列）进入恢复模式的方法为：关机状态下，长按电源键，看到"正在载入启动选项"后，点击"选项"并按提示连接 Wi-Fi 即可。









