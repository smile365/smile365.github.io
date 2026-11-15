---
title: 在macOS上安装rea并反编译一个网站
heading:  
date: 2026-10-13T02:42:09.145Z
tags: 
categories: ["code"]
Description:  
---


> [REA](https://github.com/morluto/rea/blob/main/docs/readme/README_zh.md#%E5%8F%AF%E4%BB%A5%E5%88%86%E6%9E%90%E4%BB%80%E4%B9%88)（rea-agents）是一个 MCP 服务 + CLI，用于逆向分析二进制文件、应用和运行时行为。

## 1. 安装 nodejs

Node.js	≥24.22.1 或  ≥26.12.1


检查版本：

```bash
node --version   # 例如 v24.22.3
```

版本不满足时用 nvm 升级：

```bash
nvm install 24 && nvm alias default 24
```

## 2. 安装 rea-agents CLI

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

卸载：

```bash
rea update                          # 更新 CLI（Bun 需 ≥1.2.17）
npx rea-agents@latest setup         # 更新智能体注册和 skill，然后重启智能体
```

## 3. 注册到智能体（MCP）

交互式（选择要配置的智能体并确认）：

```bash
# 可多选
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


## 6.网页分析

[REA Browser Observation 定位：](https://github.com/morluto/rea/blob/main/docs/guides/web/browser-observation.md?utm_source=chatgpt.com)：**Passive Reverse Engineering（被动逆向分析）**。

它通过 Chrome DevTools Protocol（CDP）连接一个已经运行的浏览器，不负责替你点击、输入或控制浏览器，而是采集浏览器现有页面的证据。主要能力包括：

| REA 能力                 <a class="xsj_anchor xsj_anchor_range xsj_anchor_range_start" name="xsj_1794736750074"></a> | 在 web 分析中的用途                        |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `list-browser-targets`                                                                                               | 找到浏览器页面                             |
| `inspect-web-page`                                                                                                   | 分析 DOM、Accessibility Tree、脚本、资源等 |
| `observe-web-session`                                                                                                | 记录你操作网页期间的页面事件               |
| `analyze-web-bundle`                                                                                                 | 静态分析网页加载的 JS Bundle               |
| `capture-web-screenshot`                                                                                             | 保存当前网页的视觉状态                     |
| `compare-web-captures`                                                                                               | 对比不同操作前后的页面结构变化             |
尤其值得注意的是：

- REA 不执行被捕获的 JavaScript 源码，而是静态解析。
- 网络和 Console 观察从 REA Attach 后才开始，不包含此前的历史活动。
- 可以通过观察窗口记录你手动操作时发生的页面变化。
- 可以输出 DOM、脚本、资源、网络元数据等不同维度的 Evidence。

这意味着它更适合做有明确实验步骤的交互研究，而不是一次性抓取整个飞书应用。

### 网页逆向实验

1. **使用独立的 `profile` 启动 chrome**（macOS 示例）：

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/rea-feishu-profile" \
  "https://www.example.com"
```



然后进行第一次检查：

```
rea inspect-web-page \
  http://127.0.0.1:9222 \
  TARGET_ID \
  --observation-ms 1000 \
  --include-accessibility-text \
  --include-script-sources \
  --json > 01-detailed-inspection.json
```

观察：

- 页面包含多少个 Frame。
- 对应什么 DOM 结构。
- 元素具有属性。
- 是否由多个独立容器组成。
- 是否存在独立的工具栏、浮动菜单、侧边栏。
- Accessibility Tree 暴露了哪些角色和交互元素。
- 加载了哪些 JS、CSS、字体及其他资源。

这里有一个容易忽略的细节：

**REA 默认的 DOM 观察不是完整 HTML 导出。**

它保留 DOM 节点结构、节点类型、属性名称等信息，但默认不会保留普通 DOM 文本和属性值。Accessibility 的名称和描述也需要显式开启。因此，
需要更丰富的信息时，可以通过 `include` 命令选择性开启。

注意: 脚本内容、Accessibility 文本等可能包含文档或应用敏感信息。使用自己创建的测试文档，不要随意把真实业务文档、客户信息或登录凭证放进分析产物。

**2. 分析 JavaScript Bundle**

这是 REA 非常有价值的一部分。

```
rea analyze-web-bundle \
  http://127.0.0.1:9222 \
  TARGET_ID \
  --json > 02-bundle-analysis.json
```

可研究以下内容：

| 分析对象                | 研究目的            |
| ------------------- | --------------- |
| Bundle / Chunk 依赖关系 | 找出相关代码包      |
| Vendor fingerprints | 判断使用了哪些第三方技术    |
| JS 模块关系             | 了解模块之间的组织方式     |
| Source Map          | 尝试获得原始模块路径和源码   |
| 路由候选                | 区分主要页面和其他业务页面 |
| 资源加载情况              | 找到字体、图标、样式等  |

如果有必要，再研究 Source Map。

注意：不要一开始就试图把所有 JS Bundle 都读完。遇到大型系统可能很大。



