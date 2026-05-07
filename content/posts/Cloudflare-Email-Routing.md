---
title: Cloudflare-Email-Routing
heading:  基于Cloudflare实现无限量邮箱
date: 2026-05-07T02:58:03.148Z
tags: 
categories: ["code"]
Description:  
---
## 前言
根据 [cloudflare](https://www.cloudflare.com/developer-platform/products/email-routing/) 官方文档的介绍：

> **Cloudflare 电子邮件路由** 它可以让你为你的域名创建任意数量的自定义邮件地址，**免费**地将邮件转发到你已有的任何收件箱（如 gmail、QQ邮箱）。


实际功能远不止于此：

*   **灵活的“目标配置”**：一条路由规则可以将一个自定义地址映射到一个目标邮箱地址，或是转发给 Email Worker。

*   **强大的“Catch-all”规则**：这是一个王牌功能，开启后所有未匹配的邮件（如`netflix@...`, `service@...`等）都会自动转发。这意味着**理论上的无限别名**。

*   **与Worker集成（进阶核心）**：这是Cloudflare Email Routing真正强大的地方，也是体现高级玩法的关键。

    *   **工作流自动化**：你可以编写Email Worker来处理入站邮件，实现自动分类、解析、存储或丢弃。

    *   **数据持久化**：可以将邮件附件存储到 **R2 对象存储**，将其元数据保存在 **D1 数据库**中。

    *   **AI集成**：配合 **Workers AI**，可以创建AI智能客服，自动读取邮件并回复。

*   **从“收”到“发”：Email Sending 弥补了短板**：

    *   **以前 Email Routing 只能“收”不能“发”**：在回复邮件时，你原有的邮箱（如Gmail）需要额外配置SMTP代发，过程繁琐且影响送达率。

    *   **现在有 Email Sending 公测了**：Cloudflare推出了**邮件发送服务**。开发者可以在Workers里调用它，通过REST API发送邮件。这被称为 **"complete bidirectional email"** (完整的双向邮件)。


## 这玩意有什么用呢？


对于做独立站/个人网站/博客或者一人公司的小伙伴来说，这玩意简直是必须。


 1. 比如我的独立站建议有如下几个邮箱：
 
| 邮箱 | 用途 |
| --- | --- |
| support@ | 客服 |
| hello@ | 品牌联系 |
| orders@ | 订单 |
| refund@ | 售后 |
放在以前，需要专门搭建一个邮箱服务器，或者购买 saas 服务提供商的邮箱服务。成本最贵，还不好用。得不停登录不同的邮箱查收邮件。

使用 **Email Routing** 后可以把以上邮箱地址全都转发到我的 QQ 邮箱。对于订单类的邮件，甚至可以配置一个 Worker，收到邮箱直接微信提醒或者飞书提醒，都不用打开邮箱。

2. 再比如注册一些服务的时候，需要验证邮箱，但又害怕暴露自己真实邮箱。或者仅仅为了用邮箱注册新账号，薅羊毛。


## 开通步骤


1. 打开：[Cloudflare Dashboard](https://dash.cloudflare.com/?utm_source=chatgpt.com)
2. 进入：Domains --> overview --> 域名 --> Email --> Email Routing
3. 点击： Get started
4. 填写 Custom address：比如 support
5. 填写 Destination： 比如 my@qq.com 
6. Destination 邮箱地址会收到一封 Verify 邮件，需要点击 **Verify email address**
7. Configure your DNS
若你的域名解析使用的是 Cloudflare 那么，直接点击 **Add records and enable** 即可创建 DNS 解析，否则需要参考 Cloudflare 给的记录自行创建域名解析。


## Routing rules：Catch-All

如果你不想配置多条转发规则，或者害怕客户输错自己的邮箱地址，可直接开启 **Catch-All** 功能，把所有未匹配的邮件地址都转发到特定邮箱。

1. 点击： Edit catch-all address
2. Action： 选择 Send to an email
3. Destination：选择刚刚验证过的邮箱






