---
title:  copilot pro 悄悄限制了 claude 相关模型调用
heading:  
date: 2026-06-26T23:09:06.976Z
tags: 
categories: ["code"]
Description:  
---
## 前言
持续订阅了 copilot pro 一年半套餐，因为它可以调用 claude 相关模型。前两天发现 claude 模型突然不在 model 选项里了，怎么找都没有。

Copilot 之前就强行把用户未到期的订阅从"按请求数计费"切换成了"按 token 消耗计费"，引发了大量用户不满和吐槽。

不过改成按量计费我倒是理解，按次 copilog 确实亏的太多了，成本承受不住。但这次直接不通知就把 PRO 订阅的可用模型全换成低级模型，连通知都没有，吃相太难看了。

搜索了一圈好像没人遇到我这种问题，难道是触发了风控？

## 问题排查

我订阅了 copilot pro 套餐，官网 https://github.com/features/copilot/plans 写着 pro 可以使用如下 Claude 的大模型：
```text
Pro
$10 per month
Get started
Anthropic Claude Haiku 4.5
Anthropic Claude Sonnet 4
Anthropic Claude Sonnet 4.5
Anthropic Claude Sonnet 4.6
```

但是我使用 vscode 中的  copilot 或者 copilot cli 或者 https://github.com/copilot 这个网页聊天，都无法使用 Claude 相关模型。

我把相关 IDE、cli 版本升级到最高，退出后重新登录，确认是个人 Pro 生效到你当前 GitHub 账号，

在 vscode 的 copilot 窗口显示内容如下：

```
搜索模型
Auto  10% discount
Gemini 3.1 Pro (Preview)
GPT-5.4 
Claude Opus 4.8 升级
Claude Sonnet 4.6 升级
GPT-5.5 升级
```
鼠标放到“升级”提示：升级到 GitHub Copilot Pro+以使用最佳模型。

在网页版 copilot chat 显示如下内容:

```text
Most powerful at complex tasks
GPT-5.5 Pro+
GPT-5.4
GPT-5.3-Codex
Claude Opus 4.8 Pro+
Claude Opus 4.7 Pro+
Claude Opus 4.6. Max
```

在 cli 终端输入 model 查看可用模型如下：
```
Auto
GPT-5.4 (default)
GPT-5.3-Codex
GPT-5.4 mini
GPT-5 mini
GPT-4.1
Gemini 3.1 Pro (Preview)
Gemini 3.5 Flash
MAI-Code-1-Flash
```

pro 套餐我持续订阅了大约一年多，且订阅层级从未发生过变更。我在 https://github.com/settings/billing 页面也能看到我订阅的是 Copilot Pro $10.00 per month 。

在 AI usage 页面能看到如下内容：
```markdown
Included credits    Copilot Pro
417/1,500 Al credits
Resets in 4 days on Jun 30, 2026


| Model | Included credits | Included usage | Additional credits | Additional usage |
| :--- | :--- | :--- | :--- | :--- |
| Claude Sonnet 4.6 | 233.99 | $2.34 | 0 | $0.00 |
| GPT-5.4 | 178.99 | $1.79 | 0 | $0.00 |
| Auto: GPT-5.3-Codex | 4.02 | $0.04 | 0 | $0.00 |

```


我半个月前还使用了相关 Claude 模型，似乎是升级后就无法使用了。我确保我的订阅还在有效期内，但依旧无法使用官网宣传中 pro 可用的 claude 模型。

## 提交工单

在 github 的支持页面 [support.github.com](https://support.github.com/tickets/personal/0) 提交了一份 Subject 为 **Copilot Pro account cannot access Claude models despite active subscription** 的工单，内容如下：

```markdown
Hello GitHub Support,

I'm a Copilot Pro subscriber ($10/month) and my subscriptionis active.
According to the official plan page (https://github.com/features/copilot/plans), Copilot Pro includes access to AnthropiC Claude
models, including:
- Claude Haiku 4.5
- Claude Sonnet 4
- Claude Sonnet 4.5
- Claude Sonnet 4.6

I have used Claude models normally until about two weeks ago. However, now I can no longer access any Claude modelson:
- VS Code (Copilot Chat)
- GitHub Copilot Web (https://github.com/copilot)
- GitHub Copilot CLI (copilot CLI)

All Claude models show "Upgrade to Copilot Pro+" or are not listed at all, even though I am on the Pro plan.

However, my Al usage page (https://github.com/settings/billing/ai_usage) shows that I have already used Claude Sonnet 4.6:  233.99 credits used/included

This confirms that my account has access to Claude modelsand the usage is being tracked,but the three client experiences are not allowing me touse them.

Could you please help me check the status of my account and enable access to Claude models again?

Thank you!
```

