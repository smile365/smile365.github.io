---
title: "Claude Code 安装指南"
keywords: ["Claude Code 安装", "MacOS Claude Code", "CC Switch 配置", "Claude 国产模型", "Claude CLI 安装"]
tags: ["Claude Code", "安装教程", "MacOS"]
description: "详细介绍Claude Code的安装方法，包括官方安装包、脚本安装和Homebrew三种方式，以及cc-switch工具配置国产模型的完整步骤。"
heading: "MacOS 下 Claude Code 安装与使用国产模型"
categories: ["code"]
date: "2026-05-11T05:22:31.210Z"
---
## 安装

### 1、使用官方安装包
目前 Claude Code 也提供了桌面版，可在以下地址下载：<https://claude.com/download>


### 2、使用官方脚本安装（推荐）

官方提供了一键安装脚本，根据你的系统选择对应的命令执行：

**macOS、Linux、WSL：**

``` bash
sudo sh -c 'curl -fsSL https://claude.ai/install.sh | bash'
```

添加环境变量， **zsh**：
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
添加环境变量， **bash**：

``` bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```


**Homebrew:**

``` bash
brew install --cask claude-code
```



**安装完成后，验证是否安装成功：**

``` bash
claude --version
```

如果终端输出了版本号（如 `2.1.138`），说明安装成功:


## 安装 cc-switch


前往 [GitHub Releases: https://github.com/farion1231/cc-switch/releases/latest](https://github.com/farion1231/cc-switch/releases/latest) 下载对应平台的安装包并安装。
