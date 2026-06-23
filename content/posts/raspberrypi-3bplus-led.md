---
title: "树莓派 3B+ 点亮 LED 继电器"
keywords: ["树莓派 GPIO 控制", "RPi.GPIO LED 闪烁", "树莓派 3B+ 引脚", "Python GPIO 编程"]
tags: ["树莓派", "GPIO", "LED"]
description: "在树莓派 3B+ 上使用 Python RPi.GPIO 库控制 LED 闪烁，包含 GPIO 引脚排列和 BCM 编码模式的教程。"
categories: ["code"]
date: "2024-01-10T13:44:20.343Z"
---
## 前言

  查看树莓派版本
```bash
cat /proc/cpuinfo |grep Model
# Model		: Raspberry Pi 3 Model B Plus Rev 1.3
```

查看操作系统
```bash
cat /etc/os-*
# Raspbian 12
```

如果是树莓派 os ，可以通过 `pinout` 命令输出[引脚排列](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio-pinout)。
![enter description here](https://cdn.sxy21.cn/static/imgs/1704894807177.png)



检查 [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/install/) 是否安装（树莓派系统已经默认安装）。
```python
import RPi.GPIO as GPIO
import time
#注意BOARD和BCM编码的不同，这里设置的是BCM编码
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
#闪5次
for i in range(5):
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(21,GPIO.LOW)
    time.sleep(1)
#建议每次退出时都用cleanup设置GPIO引脚为低电平状态
GPIO.cleanup()

```