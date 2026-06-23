---
title: "Orange Pi Zero3 GPIO教程"
keywords: ["Orange Pi Zero3 GPIO", "OPi.GPIO安装", "wiringOP-Python教程", "Python控制LED", "Orange Pi引脚控制"]
tags: ["Orange Pi", "GPIO", "LED"]
description: "介绍在Orange Pi Zero3上安装OPi.GPIO和wiringOP-Python库，通过Python控制GPIO引脚点亮LED的完整过程。"
categories: ["code"]
date: "2024-01-12T15:28:25.319Z"
---
## 安装 OPi.GPIO

中文版系统走百度网盘，下载巨慢无比，简易在英文版官网 [orangepi-os](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-Zero-3.html) 



1. 参考官网安装 [OPi.GPIO](https://opi-gpio.readthedocs.io/en/latest/install.html)
```bash
ssh orangepi@192.168.0.107
pip -V
sudo apt install -y python3-pip
# 3.4+
sudo pip3 install --upgrade OPi.GPIO
#sudo pipx install OPi.GPIO
##sudo apt-get install pipx
cat /etc/os-*
# Armbian 23.08.0-trunk jammy
# Ubuntu 22.04 (Jammy Jellyfish)

# Orange Pi 1.0.2 Bookworm
# Debian 12 (bookworm)
```



2. 使用官方 [demo 代码](https://opi-gpio.readthedocs.io/en/latest/api-documentation.html#outputs) 测试 
```python
# Orange Pi Zero3（1GB）
import OPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.cleanup()  
# 在程序结束时进行清理，否则会报 UserWarning: Channel 12 is already in use
```

上面的代码在我尝试了 orangepi 官网的如下系统： 
- Orangepizero3_1.0.2_debian_bookworm_server_linux6.1.31.img （❌）
- Orangepizero3_1.0.2_debian_bullseye_server_linux6.1.31.img  （❌）
- [raspberry-pi-os](https://github.com/leeboby/raspberry-pi-os-images?tab=readme-ov-file)  （❌）

都报错：
```bash
OSError: [Errno 22] Invalid argument

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/orangepi/pi.py", line 3, in <module>
    GPIO.setup(12, GPIO.OUT)
  File "/usr/local/lib/python3.9/dist-packages/OPi/GPIO.py", line 482, in setup
    sysfs.direction(pin, direction)
  File "/usr/local/lib/python3.9/dist-packages/OPi/sysfs.py", line 56, in direction
    fp.write("out")
OSError: [Errno 22] Invalid argument
```

最后使用如下系统可以成功运行：
- Orangepizero3_1.0.0_debian_bullseye_server_linux5.4.125.img 🆗️

看官方说是不维护了 😭
![enter description here](https://cdn.sxy21.cn/static/imgs/1705122708523.png)

翻看官方 [Orange_Pi_Zero_3 操作手册](http://www.orangepi.cn/orangepiwiki/index.php/Orange_Pi_Zero_3#Orange_Pi_Zero_3.E7.9A.84.E6.8E.A5.E5.8F.A3.E8.AF.A6.E6.83.85.E5.9B.BE) 说是要用 [wiringOP-Python](http://www.orangepi.cn/orangepiwiki/index.php/Orange_Pi_Zero_3#wiringOP-Python.E7.9A.84.E5.AE.89.E8.A3.85.E6.96.B9.E6.B3.95)



## 安装 wiringOP-Python

参考官网[wiringOP-Python](https://github.com/orangepi-xunlong/wiringOP-Python)
```bash
sudo apt-get update
sudo apt-get -y install git swig python3-dev python3-setuptools
git clone --recursive https://github.com/orangepi-xunlong/wiringOP-Python -b next
cd wiringOP-Python
python3 generate-bindings.py > bindings.i
sudo python3 setup.py install

```





## 引脚排列
查看[Orange Pi Zero3 引脚图](http://www.orangepi.cn/orangepiwiki/index.php/Orange_Pi_Zero_3)

![enter description here](https://cdn.sxy21.cn/static/imgs/1705119321710.png)
[BOARD 编码](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_3#Instructions_for_using_the_5v_pin_in_the_26pin_or_13pin_interface_of_the_development_board_to_supply_power)如下：

![enter description here](https://cdn.sxy21.cn/static/imgs/1705119377730.png)

或者使用  `gpio readall`
![enter description here](https://cdn.sxy21.cn/static/imgs/1705122603042.png)


## 点亮 led

1. led 接线
- 13 号引脚接 led 正极，任意一个 GND 接 led 负极。

2. 代码
```python
import wiringpi
from wiringpi import GPIO; wiringpi.wiringPiSetup()
import time
LED_PIN = 7
wiringpi.pinMode(LED_PIN, GPIO.OUTPUT)
wiringpi.digitalWrite(LED_PIN, GPIO.LOW)
#闪5次
for i in range(5):
	print("GPIO.HIGH")
	wiringpi.digitalWrite(LED_PIN, GPIO.HIGH)
	time.sleep(1)
	print("GPIO.LOW")
	wiringpi.digitalWrite(LED_PIN, GPIO.LOW)
	time.sleep(1)

wiringpi.digitalWrite(LED_PIN, GPIO.LOW)
```

3. 也可以使用 [gpiod](https://pypi.org/project/gpiod/) (ipKVM 所使用的库) 库来点亮 led，代码如下：

```python

import time
import gpiod

# 根据具体板卡的LED灯连接修改使用的Chip和Line,没有LED可以自行外接
LINE_OFFSET = 69

chip0 = gpiod.Chip("0", gpiod.Chip.OPEN_BY_NUMBER)

gpio0_b0 = chip0.get_line(LINE_OFFSET)
gpio0_b0.request(consumer="gpio", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

print(gpio0_b0.consumer())

try:
    for i in range(5):
        gpio0_b0.set_value(1)
        time.sleep(0.5)
        gpio0_b0.set_value(0)
        time.sleep(0.5)
finally:
    gpio0_b0.release()
```


## 电脑开关机
基于 [fruity-pikvm](https://github.com/jacobbar/fruity-pikvm?tab=readme-ov-file) 项目实现，看文档作者在 OrangePi Zero 2 的 ubuntu_jammy 系统上完成了测试，保险起见把系统镜像改成 Orangepizero3_1.0.0_ubuntu_jammy_server_linux5.4.125 。


```bash
apt install -y vim

```







## 参考文献
- [基于PiKVM制作M1 Mac Mini KVM](https://blog.cyyself.name/pikvm-m1-mac-mini/)
- 