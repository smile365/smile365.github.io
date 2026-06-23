---
title: "Debian安装Node.js教程"
heading: "Debian 11使用NVM安装和管理Node.js多版本"
keywords: ["Debian安装Node.js", "NVM使用教程", "Node.js版本管理", "Linux安装npm", "Debian 11 Node.js"]
tags: ["Node.js", "Debian", "NVM"]
description: "在Debian 11系统上使用NVM（Node Version Manager）安装和管理多个Node.js版本的详细教程。"
categories: ["code"]
date: "2023-02-21T03:09:00.239Z"
---
## 系统环境

- debian 11 :  `cat /etc/os-release` ,[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/debian/)


## nodejs 版本选择

[Node.js](https://nodejs.org/zh-cn/) 一般每年会升级两个大版本，偶数版是生产可用的版本（LTS），具体版本生命周期可查看 [nodejs-release](https://github.com/nodejs/release#release-schedule)

mac 或者 windows 建议直接下载 [nodejs 安装包](https://nodejs.org/zh-cn/download/) 进行安装。本教程基于 debian 11 安装。

## 使用 NVM 安装 nodejs
[NVM](https://github.com/nvm-sh/nvm#installing-and-updating)  全名 Node.js Version Management ，顾名思义是一个Node.js 的版本管理工具。
```bash
ls ~/.nvm
# 官方脚本安装，需要自己配置环境变量
# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# 自动配置环境变量
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
# -bash: nvm: command not found
# source ~/.bashrc
# 或者重新打开终端


# 使用方式
nvm ls

# 使用淘宝源
export NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node/
# 安装 nodejs
nvm install node  # 最新版（当前为 19）
nvm install node --lts  # 最新长期支持版（当前为 18）
nvm install 14 # 特定版本
# 安装完默认会使用当前安装的版本
nvm use 14  # 切换版本
```

## 使用 apt 安装 nodejs
推荐使用 nvm 安装 nodejs
```bash
# 安装 nodejs 和 npm/yarn 包管理器
apt update
apt install -y nodejs npm
node -v
# v12.22.12 (2023年)
npm -v
# 7.5.2
yarn --version
# 0.32+git
```