---
title: Claude-Code
heading:   MacOS 下 Claude Code 安装与使用国产模型
date: 2026-05-11T05:22:31.210Z
tags: 
categories: ["code"]
Description:  
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

如果终端输出了版本号（如 `2.1.138`），说明安装成功:


## 安装 cc-switch


前往 [GitHub Releases: https://github.com/farion1231/cc-switch/releases/latest](https://github.com/farion1231/cc-switch/releases/latest) 下载对应平台的安装包并安装。

选择 claude 图标，点击添加配置按钮。
![enter description here](https://cdn.sxy21.cn/static/imgs/1778478575269.png)


## 使用

```bash
mkdir ~/projects/my-project-1 
cd ~/projects/my-project-1
claude

```

## 参考文档

- [Claude Code 安装-runoob](https://www.runoob.com/claude-code/claude-code-install.html)
- [cc-switch 安装-runoob](https://www.runoob.com/ai-agent/cc-switch.html)