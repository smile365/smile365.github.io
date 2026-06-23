---
title: "hermes-agent"
keywords: ["教程", "hermes agent", "ghostty", "hermes", "Voice", "Images", "Files", "Threads", "hermes agent ##", "agent"]
tags: ["教程", "hermes agent", "ghostty", "hermes", "Voice", "Images", "Files", "Threads"]
description: "试用一下 hermes-agent，文档会持续更新。"
categories: ["code"]
heading: "hermes-agent"
date: "2026-06-04T11:59:28.418Z"
---
## 前言

试用一下 hermes-agent，文档会持续更新。

## hermes-agent 安装

推荐使用 [ghostty](https://ghostty.org/) 终端。

参考 [官网文档](https://hermes-agent.nousresearch.com/) 安装 hermes-agent

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

2. 启用环境变量
```bash
source ~/.zshrc
```

3. 配置

```bash
# 1. 检查是否安装完整
hermes doctor
# 2. 选择 fuall 完全配置
hermes setup
# 若选成两快速配置，可通过 ctrl+c 跳过授权登录，不使用官方的 token
# 配置消息网关，上下进行选中，空格勾选。
# 3. 使用终端对话
hermes
# 查看 gateway 状态
hermes gateway status
```

## 对话平台选择

强烈推荐**飞书**：

hermes 支持几乎市面上已有的平台，但不同平台提供的功能各不相同，具体可查看 [平台对比功能列表](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/#platform-comparison)， 同时支持 Voice/Images/Files/Threads/Reactions/Typing/Streaming 功能的平台，国内仅有 [飞书](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu) 一家（国外有 Discord/Slack/Matrix）。

除此之外 微信、元宝也是一个不错的选择，只是没有表情回复的功能。




