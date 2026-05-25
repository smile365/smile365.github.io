---
title: residential-IP-fingerprint-browser
heading:  住宅 ip和指纹浏览器
date: 2026-05-24T03:13:11.331Z
tags: 
categories: ["life"]
Description:  
---

## 静态住宅 ip

| 服务商                                                                                | 价格                                                 | 说明 |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------- | ---- |
| [talordata](https://www.talordata.com/price/static-isp-proxies)                       | $6/IP/30天、$9.5/IP/60天、$13.5/IP/90天              |      |
| [iproyal](https://iproyal.com/pricing/isp-proxies/)                                   | $2.70/proxy/30 D、$2.55/proxy/60 D、$2.40/proxy/90 D |      |
| [rapidproxy](https://cn.rapidproxy.io/static-residential-proxies/pricing)             | $5/ip/30D                                            |      |
| [fluxisp](https://fluxisp.com/pricing/isp-proxy/?day=7)                               | $1/7D $4.5/30D $11/90D                               |      |
| [711proxy](https://www.711proxy.com/zh-TW/pricing/regular/static-residential-proxies) | $3.9/30D $10.5/90D                                   |      |
| [lokiproxy](https://www.lokiproxy.com/pricing/static-proxy)                           | $1.9/30D                                             |      |
| [proxy-seller.](https://proxy-seller.com/zh/isp/?region=3758)                         | $3/30D                                               |      |
**购买ip（以 lokiproxy 为例）：**
1. 注册[lokiproxy 账号](https://www.lokiproxy.com/zh-TW/signup?invite=1D7200)，选择 在 product 处选择 Static Residential Proxy ，选择需要的地区，付费即可。
2. 购买成功后点击立即使用，或者账号下选择 dashboard
3. 点击 Static Residential ，选择刚刚购买的 ip，Hostname 选择离自己近的（一般为 hk）
4. 格式选择 username:password@hostname:port ，然后点击生成链接 （Generate URL）



## 指纹浏览器

- [morelogin](https://www.morelogin.com/antidetect-browser)
- [virtualbrowser](https://virtualbrowser.cc/zh/)


### morelogin 教程

1. 安装，选择中文，然后点击创建账号。输入 邮箱、


## clash 配置

已经有订阅的情况下，打开 [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.1) 客户端，点击 订阅，右键当前使用的配置，然后选择 编辑节点，输入如下格式的节点信息，然后点击 添加前置节点（表示顺序在最前）

> socks5://帐号:密码@IP:端口#节点名称

点击 代理--链式代理，选择一个入口节点，如 香港，选择刚刚配置好的出口节点，代理模式选择全局，此时可通过 [whoer](https://whoer.net/zh)、[ipip.la](https://ipip.la/)等测试代理的 ip 信息。

> 后续可单独设置代理分组，并配置分流规则。相关教程可参考 [Clash Verge链式代理+分流--youtube 视频](https://www.youtube.com/watch?v=ajgL9OTZQvM)  

## ios shadowrocks 配置

1. 点击 + 号，选择 socks5，输入帐号、密码、IP、端口、备注， 点保存
2. 选中刚刚添加的节点，点击 i 图标， Forward 选择一个快的节点，保存。


