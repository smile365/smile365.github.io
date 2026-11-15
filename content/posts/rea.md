---
title: rea
heading:  
date: 2026-10-13T02:42:09.145Z
tags: 
categories: ["code"]
Description:  
---


> REA（rea-agents）是一个 MCP 服务 + CLI，用于逆向分析二进制文件、应用和运行时行为。
> 官方来源：[morluto/rea](https://github.com/morluto/rea) · [rea.tools](https://rea.tools/) · npm 包 [rea-agents](https://www.npmjs.com/package/rea-agents)。请只从这些官方渠道安装。

## 1. 环境要求

| 组件    | 要求                    |
| ------- | ----------------------- |
| Node.js | ≥24.22.1 或  ≥26.12.1 |
| npm     | 随 Node.js 提供         |

检查版本：

```bash
node --version   # 例如 v24.22.3
```

版本不满足时用 nvm 升级：

```bash
nvm install 24 && nvm alias default 24
```

## 2. 安装 CLI

```bash
npm install --global rea-agents
```

如需运行时分析，进程捕获等 Frida 功能（npm 默认拦截其安装脚本）：

```bash
npm install -g --allow-scripts=frida rea-agents
```

验证：

```bash
rea --version    # 例如 6.9.0
rea doctor       # 就绪检查：node/host 应为 healthy
```

## 3. 注册到智能体（MCP）

交互式（选择要配置的智能体并确认）：

```bash
npx rea-agents setup
```

或非交互式指定智能体：

```bash
rea setup --all-detected --yes          # 所有检测到的智能体
rea setup --client claude_code --yes    # 仅 Claude Code
rea setup --all-detected --dry-run      # 只预览变更，不修改
```

完成后**重启智能体**即可在对话中直接使用 REA。不注册 MCP 也可以直接用终端命令（见第 5 步）。

## 4. 原生分析引擎（可选）

静态分析 JavaScript/Electron、.NET、APK 资源、GGUF 等**不需要**原生引擎；只有深入分析原生二进制（伪代码/汇编）才需要其中之一：


| 引擎 | 性质 | 支持情况 | 在 REA 中的接入方式 |
| --- | --- | --- | --- |
| Ghidra | 美国国家安全局（NSA）开源的逆向框架，免费 | 架构支持最全（x86/x64、ARM、MIPS 等），带 C 伪代码反编译器 | 设置 GHIDRA_INSTALL_DIR 指向解压后的 Ghidra 12.x（≥12.1）目录 |
| Hopper | 商业软件（Cryptic Apps），macOS 生态里最常用的平价选择 | macOS/Linux，x86/x64、ARM/ARM64，反汇编 + 伪代码 | rea setup --install-hopper --yes 可由 REA 代装，或设 HOPPER_LAUNCHER_PATH |
| IDA Pro | Hex-Rays 出品的行业标准商业工具，昂贵，需自行购买许可 | 架构支持最广、反编译质量公认最强（Hex-Rays） | 设 REA_IDA_MCP_CONFIG，指向你已有的 IDA MCP 注册 |
| Kuna | Apache-2.0 开源静态反编译器，单个可执行文件，轻量新工具 | 仅 ELF 和 thin Mach-O（x86-64 / AArch64 / ARM），不支持 PE/fat Mach-O，REA 官方验证版本 1.990 | 设 REA_KUNA_COMMAND 指向 kuna 可执行文件；REA 不会帮你下载安装 |


```bash
rea setup --install-hopper --yes   # 安装 Hopper（需确认许可）
```

或使用已有安装：`GHIDRA_INSTALL_DIR`（Ghidra 12.x）、`REA_IDA_MCP_CONFIG`（IDA）、`REA_KUNA_COMMAND`（Kuna）。用 `rea doctor` 查看哪些已就绪。

## 5. 使用

在智能体中直接提问：

```text
弄清 Notes 应用的搜索功能如何工作，展示证据，并为我的项目实现类似功能。
```

或用终端分析已解包的 JS/Electron 应用：

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

## 6. 更新与卸载

```bash
rea update                          # 更新 CLI（Bun 需 ≥1.2.17）
npx rea-agents@latest setup         # 更新智能体注册和 skill，然后重启智能体
```

## 常见问题

- **`rea doctor` 提示 missing_analysis_engine**：仅影响原生二进制分析，静态分析不受影响，按需配置第 4 步。
- **npm 缓存 EACCES**：`sudo chown -R $(id -u):$(id -g) ~/.npm`，或临时用 `npm install --cache ~/.npm-rea-cache`。
- **遇到错误**：先 `rea update`，再重启智能体重试；仍有问题到 [GitHub Issues](https://github.com/morluto/rea/issues) 反馈。

更多文档：[安装与设置](https://rea.tools/zh-CN/) · [CLI 指南](https://rea.tools/zh-CN/guides/)
