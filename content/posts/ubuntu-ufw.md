---
title: "Ubuntu防火墙UFW使用教程"
heading: "Ubuntu使用UFW查看端口和配置防火墙规则"
keywords: ["Ubuntu防火墙配置", "UFW使用教程", "Ubuntu开放端口", "Linux防火墙", "iptables"]
tags: ["Ubuntu", "UFW", "防火墙"]
description: "Ubuntu系统自带的UFW防火墙配置工具使用教程，详解如何查看端口状态和配置防火墙规则。"
categories: ["code"]
date: "2021-07-28T05:02:44.701Z"
---
Ubuntu 随附了一个称为 UFW（非复杂防火墙）的防火墙配置工具。 UFW是用于管理iptables防火墙规则的用户友好型前端，其主要目标是使管理防火墙规则更容易，或者名称不复杂。


查看防火墙状态
```bash
ufw status
# inactive 禁用状态
# active 启用状态
```

若果发现防火墙是关闭状态，但部分端口还是无法访问，那可能是用了云服务器的[虚拟防火墙](https://developer.aliyun.com/article/767328)，需要登录到云服务器的控制台去开启。


