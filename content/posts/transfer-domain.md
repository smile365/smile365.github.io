---
title: "transfer-domain"
keywords: ["教程", "把域名从 转出到", "namesilo", "Cloudflare", "Domains", "Domain Contacts", "PayPal", "transfer domain", "transfer domain ##", "transfer"]
tags: ["教程", "把域名从 转出到", "namesilo", "Cloudflare", "Domains", "Domain Contacts", "PayPal", "transfer domain"]
description: "sxy91.com 这个博客的域名从 18 年到 26 年6月 22，在 namesilo 购买的。"
categories: ["code"]
heading: "把域名从 NameSilo 转出到 Cloudflare"
date: "2026-06-22T12:19:48.493Z"
---
## 前言

sxy91.com 这个博客的域名从 18 年到 26 年6月 22，在 namesilo 购买的。因账号里还有余额，所以开启了自动续费，今天发现到期了，域名无法访问。本来打算续费，一看价格，每年 17 美金，比 Cloudflare 还贵 7 美金，打算转出到 Cloudflare 。

> Cloudflare 的新购、续费、转入都是 10.44 美金/年。
> **📢注**：我的操作太极限了，过期的时候转出不安全，推荐至少过期前 45 天转移。

## 从 namesilo 转出域名

登录 namesilo，点击 My Account ->  Domain Manager -> 点击需要转出的域名

> 检查 Domain Contacts and Privacy 中的邮箱是否正确，确保能收到邮件（账号注册的邮箱和Domain Contacts 中预留的邮箱有可能不一致）。我就是因为没注意，结果一直以为没收到授权码。

- Domain Lock： 需要是关闭状态
- Authorization Code： 先点击 Reset Auth Code ， 然后点击 Send Email
- Domain Contacts  显示的邮箱中查找 授权码

## 把域名转入 cloudflare

1. 登录 [cloudflare](https://dash.cloudflare.com/) 在 Domains -> Transfers 添加需要转入的域名
2. 输入授权代码，确认价格，并点击继续
3. 输入联系方式和付款信息（国际信用卡或者 PayPal）
4. 银行 app 或者 PayPal 确认付款成功，cloudflare 会发送邮件提示“域名转移已经提交”
5. 之前域名填写的 Domain Contacts 中的邮箱也会收到转出请求，但千万**不要点**击邮件内的链接（看清楚哦，是在5天内点击则取消转出，不操作的话 5 天后自动完成转移）
6. Domains -> Registrations 可查看到刚刚转入的域名是 Pending Transfer 状态
7. 如果要加速转出，可以到 namesilo 的[域名转移界面](https://www.namesilo.com/account_transfers.php) ，Pending Outbound Transfers 下方有一条记录，点击 APPROVE 按钮，点击 submit，之后 namesilo 将在 15 分钟内自动向注册局提交转移申请。（若在 Pending Outbound Transfers  看不到记录，需要等 10 分钟左右）
8. 等 5 分钟左右，在 cloudflare 的 Domains -> Registration 页面即可查看到转入的域名状态为 Active


