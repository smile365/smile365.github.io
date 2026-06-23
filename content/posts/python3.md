---
title: "使用 pyenv 安装 Python 2"
keywords: ["pyenv 安装 Python 2", "apt 安装 python", "Debian 多版本 Python", "pyenv 使用教程"]
tags: ["pyenv", "Python", "安装"]
description: "在 Debian 系统上通过 pyenv 安装 Python 2 及多个版本，配置环境变量并解决 GnuTLS 网络下载错误的完整教程。"
categories: ["code"]
date: "2023-02-21T05:55:25.875Z"
---
## 使用 apt 安装 python
```bash
apt update
apt install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt install python3.9
python3.9 --version
```


## 使用 pyenv 安装 python

[pyenv](https://github.com/pyenv/pyenv#automatic-installer)
```bash
# 安装依赖
apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
# 下载 pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# 配置环境变量
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
# 生效
exec "$SHELL"
```
使用方式
```bash
pyenv install --list  # 查看所有可安装的版本
pyenv install 3.9 # 安装指定版本
pyenv rehash # 安装新版本后rehash一下
pyenv uninstall 3.5.2 # 删除指定版本
pyenv global 3.6.5 # 指定全局版本
pyenv global 3.6.5 2.7.14 # 指定多个全局版本, 3版本优先
pyenv local 3.5.2 #指定当前目录版本
```

## 安装 pip

## 配置 pip 镜像源


## 安装 miniconda


## 遇到的问题


1. GnuTLS recv error
GnuTLS recv error (-110): The TLS connection was non-properly terminated.