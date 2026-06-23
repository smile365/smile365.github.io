---
title: "Homebrew安装与国内镜像配置"
keywords: ["Homebrew安装", "brew国内镜像", "Mac包管理工具", "清华镜像源", "brew配置教程"]
tags: ["brew", "macOS", "镜像配置"]
description: "详细介绍Homebrew的安装步骤以及如何配置清华等国内镜像源，加速软件包下载和更新。"
categories: ["code"]
heading: "brew"
date: "2023-04-25"
draft: "true"
---
## 安装 brew 
使用国内安装

## 配置国内镜像
1. 配置[清华 brew 镜像](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/)


```bash
# bash 环境 ~/.bash_profile
# zsh 环境
vi ~/.zshrc
# 在 ~/.zshrc 追加内容：
export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_PIP_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
```