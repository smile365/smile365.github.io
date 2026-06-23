---
title: "树莓派无外设安装使用教程"
keywords: ["树莓派无屏安装", "树莓派自动连 Wi-Fi", "树莓派开启 SSH", "Raspberry Pi OS 烧录", "无头树莓派"]
tags: ["树莓派", "Raspberry Pi", "无头安装"]
description: "无需鼠标键盘和显示器，在烧录树莓派系统时直接配置 Wi-Fi 和 SSH，实现远程连接和使用的完整教程。"
categories: ["code"]
heading: "树莓派最新安装和使用教程（无需鼠标键盘显示器等外设）"
date: "2019-07-02T10:35:01.080Z"
---
## 前言
Mac OS 的触摸板非常好用，基本告别了鼠标键盘。买了个 树莓派，笔记本用的是 WIFI 网络，手上也没有鼠标、键盘、网线、显示器，如何在没有鼠标键盘的情况下，安装树莓派系统和并自动配置 WIFI 和 SSH 呢。

可以在烧录树莓派系统的时候就指定 WIFI 名称和密码，并打开 SSH 开关，这样就可以通过远程连接树莓派，无需鼠标键盘和显示器，以下是详细教程：


#### 安装系统
Raspberry Pi OS（原为Raspbian）是为树莓派基于Debian开发的操作系统。到官网下载[Raspberry Pi Imager](https://www.raspberrypi.org/software/)这个安装工具并安装到电脑上，然后选择需要烧录的 sd 卡和需要烧录的系统，工具会自动下载 Raspberry Pi OS ，并烧录到 sd 卡上，只需要简单 3 步。工具下载 os 比较慢，可以到清华源下载 [Raspberry Pi OS](https://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os-images/raspios_armhf/images/)

![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1610547292645.png)

#### 配置 WIFI
若果没有鼠标、键盘、显示器、网线，只有一个 wifi ，烧录的时候可以把 wifi 密码直接写入 sd 卡，让树莓派启动时自动连接 wifi。

在SD卡的根目录下添加一个名为 wpa_supplicant.conf的文件，然后在该文件内添加以下的内容 ： 
```bash
country=CN  
update_config=1  
ctrl_interface=DIR=/var/run/wpa_supplicant     GROUP=netdev
network={
  ssid="WIFI名"
  psk="WIFI密码"
}
# 别漏了双引号“”
```

#### 启用 SSH

ssh 默认关闭，只需在 SD 的根目录新建一个名为 ssh 文件即可开启 ssh

![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1610548512219.png)


#### 找到树莓派 ip

先查自己电脑 ip
```bash
ifconfig |grep "inet "
	inet 127.0.0.1 netmask 0xff000000 
	inet 192.168.1.21 netmask 0xffffff00 broadcast 10.3.1.255
```

写一个 [shell 脚本](https://sxy91.com/posts/ping-ip/) ping 一下 ip 或者扫描一下 22 端口。编写 ip_ping.sh 内容如下：
```bash
#!/bin/bash
ip=192.168.1
port=22
for ((i=2;i<=254;i++))
do
{
        curl $ip.$i:$port -m 3 2>&1 | grep -q "SSH" && echo "$ip.$i:$port yes"