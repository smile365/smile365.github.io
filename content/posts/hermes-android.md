---
title: "hermes-android"
keywords: ["教程", "Android", "Linux", "github", "在 上安装 养龙虾", "hermes android", "hermes", "U1", "hermes android ##"]
tags: ["教程", "Android", "Linux", "github", "在 上安装 养龙虾", "hermes android", "hermes", "U1"]
description: "前言 有一台坚果 U1 手机，虽然系统应用依然流畅，但内存只有 2G ，且 Android 停留在了 5.1 ，基本没什么用了。打算安装成 Linux 用来跑小龙虾。"
categories: ["code"]
heading: "在 Android 上安装 hermes 养龙虾"
date: "2026-06-06T00:54:44.028Z"
---
## 前言
有一台坚果 U1 手机，虽然系统应用依然流畅，但内存只有 2G ，且 Android 停留在了 5.1 ，基本没什么用了。打算安装成 Linux 用来跑小龙虾。

## 安装 termux

1. 手机打开开发者模式，用数据线连接电脑，使用命令 `adb devices` 查看设备；
2. 从 github 下载安装文件 [android-5-armeabi-v7a.apk](https://github.com/termux/termux-app/releases)
3. 使用命令安装 `adb install termux-xxx.apk`

可以使用 adb 命令查看手机相关信息
```bash
# 架构，32 还是 64，分别对应 arm64-v8a 和 armeabi-v7a,armeabi
adb shell getprop ro.product.cpu.abi
# 查看 Android 版本
adb shell getprop ro.build.version.release
```

## 安装 ssh

在 termux 内执行：
```bash
apt update
# 安装服务端
apt install openssh -y
# 设置密码
passwd
# 启动
sshd
# 测试连接
ssh localhost -p 8022
# 查看 ip, 192.168.1.11
ip addr |grep "inet "
```


## 安装 hermes

参考官方文档 [在 Android 上通过 Termux 运行 Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/termux)
```bash
# 替换成你的 ip
ssh 192.168.1.11 -p 8022
# 在手机上安装 hermes
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

> 安装失败了，改成红米 note8 继续尝试


Redmi note8 配置：6+64GB，Android 11

安装 termux：

1. 在设置连续点击版本号 5 次打开开发者模式，数据线连接电脑，打开 usb 调试；
2. 运行 usb 安装应用（需要登录小米账号&插入 sim 卡）；
3. 安装  `adb install termux-arm64-v8a.apk`
4. 按照上面的步骤安装 ssh 和 termux

### 错误：nodejs 安装失败

手动安装：  
```bash
# 5 分钟左右
pkg update && pkg upgrade -y
# 安装最新版 nodejs
pkg install nodejs-lts -y
```


**配置 hermes：**

1. 输入命令 `hermes setup` 选择 Full setup，配置大模型、消息渠道等；
2. 若想新增消息渠道，输入命令  `hermes setup gateway` 配置（飞书、微信、QQ 等）
3. 配置工具的时候直接跳过（大部分工具为电脑端的，无法在手机上配置）

选择 7
```txt
  Configuring 6 tool(s):
    • 🌐 Browser Automation
    • 🖱️  Computer Use (macOS)
    • 🎨 Image Generation
    • 🔊 Text-to-Speech
    • 👁️  Vision / Image Analysis
    • 🔍 Web Search & Scraping
```

然后输入命令启动
```bash 
# 检查是否安装完成
hermes doctor --fix
# 若提示配置环境变量
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
#  查看 gateway 状态
hermes gateway status
# 前台运行
hermes gateway run
# 后台运行
nohup hermes gateway run > ~/.hermes/logs/gateway.log 2>&1 &
```


## 手机上安装 debian

```bash
pkg update
pkg upgrade -y
pkg install proot-distro -y
proot-distro list
# proot-distro install debian # 默认安装最新版，即 debian 13（trixie）
# 默认命令等同于：proot-distro install debian:trixie --name debian
proot-distro install debian:bookworm # 安装特定系统 Debian 12，Debian 11 (bullseye)
proot-distro login debian # 进入 debian 系统

```

若遇到错误 Network error 可能需要代理。
```
[!] Failed to install: Network error: <urlopen error [Errno 101] Network is unreachable>
```

参考 [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/debian/) 配置镜像源，加速下载 。

1. 输入命令 `cat >/etc/apt/sources.list.d/debian.sources <<'EOF'`
2. 粘贴 DEB822 格式的内容：
3. 更新 `apt update`
4. 然后参考上面的命令安装 hermes


### 问题：WARNING gateway.run

安装完发现还是无法在消息渠道收发消息。
```
WARNING gateway.run: Feishu: lark-oapi not installed or FEISHU_APP_ID/SECRET not set
```

安装完同样遇到消息渠道也无法收发消息。

**排查过程:**

现象1：.env 配置了飞书的环境变量，但 hermes 没读取到。
```
root@localhost:~# cat /root/.hermes/.env |grep FEISHU_APP_ID
FEISHU_APP_ID=cli_xxxx
root@localhost:~# env | grep FEISHU_APP_ID # 输出为空
```
尝试：把 .env 中的所有环境变量都手动 export 一下试试
```bash
set -a
source ~/.hermes/.env
set +a   # 关闭自动导出（可选）
env | grep FEISHU_APP_ID
```

结果：env 中有环境变量依然无法正常在飞书里给 hermes 发送消息。

现象 2：自动安装了 3 个 python 环境，hermes 使用的是 3.11.15 版本
```bash
root@localhost:~# which hermes
/root/.local/bin/hermes
root@localhost:~# cat $(which hermes)
#!/usr/local/lib/hermes-agent/venv/bin/python3
# -*- coding: utf-8 -*-
import sys
from hermes_cli.main import main
if __name__ == "__main__":
    if sys.argv[0].endswith("-script.pyw"):
        sys.argv[0] = sys.argv[0][:-11]
    elif sys.argv[0].endswith(".exe"):
        sys.argv[0] = sys.argv[0][:-4]
    sys.exit(main())
root@localhost:~# which python3
/usr/bin/python3
root@localhost:~# ls -lh /usr/bin/python3
lrwxrwxrwx. 1 root root 18 Apr  9  2023 /usr/bin/python3 -> python3.11
root@localhost:~# which python
/data/data/com.termux/files/usr/bin/python
root@localhost:~# python -V
Python 3.13.13
root@localhost:~# python3 -V
Python 3.11.2
root@localhost:~# /usr/local/lib/hermes-agent/venv/bin/python3 -V
Python 3.11.15
```

确认 python 能读取到环境变量
```bash
/usr/local/lib/hermes-agent/venv/bin/python3 - <<'PY'
import os
print("APP_ID =", os.getenv("FEISHU_APP_ID"))
print("SECRET =", os.getenv("FEISHU_APP_SECRET"))
PY
```

尝试：安装 lark_oapi
```
/usr/local/lib/hermes-agent/venv/bin/pip install lark-oapi
```

重新启动 hermes （启动较慢，约 5 分钟）,可以看到能连接到飞书了。
```
[Lark] [2026-06-07 05:45:30,298] [INFO] connected to wss://msg-frontier.feishu.cn
```

在飞书发送消息给 hermes，发现报错：
```
ERROR gateway.platforms.feishu: [Feishu] Send error: Executor shutdown has been called
linux-aarch64-gnu/lib/python3.11/asyncio/base_events.py", line 524, in _check_default_executor
    raise RuntimeError('Executor shutdown has been called')
RuntimeError: Executor shutdown has been called
ERROR gateway.platforms.base: [Feishu] Fallback send also failed: Executor shutdown has been called
WARNING gateway.platforms.feishu: [Feishu] Add reaction CrossMark on om_xxxxx raised
```

是因为 gateway 没正常启动，重新启动就好了。



## 总结

1. 尝试了坚果 U1（ Android 5.1、2+32G），无法在 termux 中安装 hermes；
2. 尝试了红米 note8（Android 11、4+64G），能在 termux 中安装 hermes，无法在飞书、微信收发消息（似乎是 hermes 无法正确读取配置）；
3. 红米 note8，termux中安装了 debian，然后安装 hermes 同样遇到问题 2；是因为缺少飞书的 api，安装一下就正常了。