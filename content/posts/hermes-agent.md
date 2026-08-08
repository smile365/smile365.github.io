---
title: hermes-agent
heading:  
date: 2026-06-04T11:59:28.418Z
tags: 
categories: ["code"]
Description:  
---

## 前言

试用一下 hermes-agent，文档会持续更新。环境为 MacBook air （m2），OS 为 macos Tahoe Version 26.5。

## hermes-agent 安装

推荐使用 [ghostty](https://ghostty.org/) 终端。

参考 [官网文档](https://hermes-agent.nousresearch.com/) 安装 hermes-agent（需要 Python 3.11 ）。若不想使用  uv 安装的版本，可使用  [pyenv]({{< relref "mac-python3.md" >}}) 安装和管理多个 python 版本。

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

若遇到错误 `Permission denied` 错误，是因为 uv 没有权限创建自己的 Python 安装目录。
```txt
→ Python 3.11 not found, installing via uv...
error: failed to create directory
/Users/sxy/.local/share/uv/python
Permission denied (os error 13)
```
可查看相关目录的所有者为 root ，一般是之前运行命令用了 sudo
```
ls -ld ~/.local
ls -ld ~/.local/share
```

修改所有者和权限即可重新安装 hermes
```
# 改所有者
sudo chown -R "$USER":"$(id -gn)" ~/.local
# 改权限
chmod -R u+rw ~/.local
```


## 对话平台选择

强烈推荐 [飞书](https://open.feishu.cn/app)

hermes 支持几乎市面上已有的平台，但不同平台提供的功能各不相同，具体可查看 [平台对比功能列表](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/#platform-comparison)， 同时支持 Voice/Images/Files/Threads/Reactions/Typing/Streaming 功能的平台，国内仅有 [飞书](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu) 一家（国外有 Discord/Slack/Matrix）。

除此之外 微信、元宝也是一个不错的选择，只是没有表情回复的功能。


可以打开飞书开放平台，创建机器人，然后填入 App ID 和 App Secret ,或者使用 hermes 提供的一键扫码自动创建机器人模式。


### cli 工具选择

```txt
   [✓] 🔍 Web Search & Scraping  (web_search, web_extract)
   [✓] 🌐 Browser Automation  (navigate, click, type, scroll)
   [✓] 💻 Terminal & Processes  (terminal, process)
   [✓] 📁 File Operations  (read, write, patch, search)
   [✓] ⚡ Code Execution  (execute_code)
   [ ] 👁️  Vision / Image Analysis  (vision_analyze)  [no API key]
   [ ] 🎬 Video Analysis  (video_analyze (requires video-capable model))
   [ ] 🎨 Image Generation  (image_generate)
   [ ] 🎬 Video Generation  (video_generate (text/image/reference))
   [ ] 🎬 BFL FLUX 3 Video  (bfl_flux3_*)
   [ ] 🐦 X (Twitter) Search  (x_search (requires xAI OAuth or XAI_API_KEY))
   [✓] 🔊 Text-to-Speech  (text_to_speech)
   [✓] 📚 Skills  (list, view, manage)
   [✓] 📋 Task Planning  (todo)
   [✓] 💾 Memory  (persistent memory across sessions)
   [ ] 🧩 Context Engine  (runtime tools from the active context engine)
   [✓] 🔎 Session Search  (search past conversations)
   [✓] ❓ Clarifying Questions  (clarify)
   [✓] 👥 Task Delegation  (delegate_task)
   [✓] ⏰ Cron Jobs  (create/list/update/pause/resume/run, with optional attached skills)
   [ ] 🏠 Home Assistant  (smart home device control)  [no API key]
   [ ] 🎵 Spotify  (playback, search, playlists, library)
   [ ] 🤖 Yuanbao  (group info, member queries, DM)
   [✓] 🖱️  Computer Use (macOS/Windows/Linux)  (background desktop control via cua-driver)
 → [ ] 🔌 A2A  (A2A (Agent-to-Agent) protocol v1.0 support for Hermes Agent — both directions of the open Linux Foundation standard for inter-agent communication.
OUTBOUND (client too
```


### 浏览器自动化选择

```
(○) Local Browser [★ recommended · free] — Headless Chromium, no API key needed
→ (●) Camofox [free · local] — Anti-detection browser (Firefox/Camoufox)
(○) Skip — keep defaults / configure later
```

### TTS 选择

```
→ (●) Microsoft Edge TTS [★ recommended · free] — Good quality, no API key needed [active]
   (○) Google Gemini TTS [preview] — 30 prebuilt voices, controllable via prompts
   (○) KittenTTS [local · free] — Lightweight local ONNX TTS (~25MB), no API key
   (○) Piper [local · free] — Local neural TTS, 44 languages (voices ~20-90MB)
   (○) Skip — keep defaults / configure later
 ```
 
### 搜索提供商

```
   (○) Firecrawl Self-Hosted [free · self-hosted] — Run your own Firecrawl instance (Docker)
   →  (●) Brave Search (Free) [free] — Free-tier API key — 2k queries/mo, search only.
   (○) DuckDuckGo (ddgs) [free · no key · search only] — Search via the ddgs Python package — no API key (pair with any extract provider)
   (○) SearXNG [free · self-hosted] — Free, privacy-respecting metasearch. Point SEARXNG_URL at your instance.
   (○) xAI Web Search (Grok) [paid] — Agentic web search via Grok's web_search tool — uses xAI Grok OAuth or XAI_API_KEY.
   (○) Skip — keep defaults / configure later
```
   
   
   

### 启用环境变量
```bash
source ~/.zshrc
```

其他配置

```bash
# 查看 gateway 状态
hermes gateway status
# 查看 gateway 帮助（启动方式）
hermes gateway -h
# 前台运行
# hermes gateway run
# 后台运行
# hermes gateway start
# 配置网关
# hermes gateway setup

# 检查是否安装完整
hermes doctor
# 选择 fuall 完全配置
hermes setup
# 若选成两快速配置，可通过 ctrl+c 跳过授权登录，不使用官方的 token
# 配置消息网关，上下进行选中，空格勾选。
# 3. 使用终端对话
hermes

```

