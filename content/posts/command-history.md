---
title: "Snoopy Linux 审计日志"
keywords: ["snoopy 安装配置", "Linux history 审计", "Linux 操作记录", "snoopy 审计日志", "Linux 安全审计"]
tags: ["snoopy", "Linux审计", "命令记录"]
description: "Snoopy可以记录Linux终端的所有操作命令，本文详细介绍五种安装方式和启用步骤，实现完整的操作审计和日志追踪。"
categories: ["code"]
date: "2022-12-08T12:50:14.806Z"
series: ["blog"]
---
## 安装 snoopy

[snoopy](https://github.com/a2o/snoopy/blob/master/doc/INSTALL.md)可以记录 Linux 终端的操作记录。有 5 种安装方式。
1. 使用存储库安装
```bash
apt install -y snoopy   # Debian / Ubuntu
yum install snoopy   # RHEL / CentOS
zypper install snoopy   # SLES / OpenSUSE
```

2. 使用脚本自动安装
```bash
wget -O install-snoopy.sh https://github.com/a2o/snoopy/raw/install/install/install-snoopy.sh
chmod 755 install-snoopy.sh
sudo ./install-snoopy.sh stable
```

3. 使用二进制文件安装
如果无法正常从 github 下载文件，可以使用 releases 中的二进制文件安装  [snoopy-2.5.1.tar.gz
](https://github.com/a2o/snoopy/releases)
```bash
# 方法二
tar xf snoopy-*.gz
cd snoopy-2.5.1/
./configure --prefix=/usr/local/snoopy && make && make install

```

## 启用 snoopy
通过使用存储库安装的默认已经启用了 Snoopy 没有 snoopyctl 命令，其他方式安装可参考一下命令启用：
```bash
snoopyctl enable
snoopyctl status
# 使用二进制安装的执行以下命令启动
# /usr/local/snoopy/sbin/snoopyctl enable
# 查看是否启用（没启用需要重启）
cat /etc/ld.so.preload
# # /usr/local/snoopy/lib/libsnoopy.so
# 或者用 ldd 查看
ldd /bin/pwd
# # /usr/local/snoopy/lib/libsnoopy.so
```


Snoopy 日志路径：
CentOS：	/var/log/secure	
Debian：	/var/log/auth.log	
Ubuntu：	/var/log/auth.log	
(others)：	/var/log/messages	(potentially, could be elsewhere)
