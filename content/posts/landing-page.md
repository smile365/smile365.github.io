---
title: landing-page
heading:  如何做 Landing Page
date: 2026-05-19T03:38:50.486Z
tags: 
categories: ["code"]
Description:  
---
## 前言
开发一个全新 APP 之前，为什么需要做 Landing Page？

因为当前真正需要的是：

> “验证需求 + 收集用户 + 测试转化”

而不是：

> 搭建复杂后端系统

很多独立开发者一开始就：

- VPS
- Kubernetes
- SSR
- 数据库
- 用户系统


结果：产品还没验证就浪费大量时间

这是典型过度工程。

## Landing Page 能力

1. 展示页面
- Hero
- 产品介绍
- 截图
- CTA

2. 收集邮箱
- waitlist
- beta signup

3. Analytics
 PV
 CTR
 转化率

4. 自定义域名
推荐使用一个主品牌域名+不同二级域名 / 子目录，比如：
```txt
yourbrand.com/
├── app-one/
├── app-two/
├── app-xxx/
├── blog/
```

这是目前更现实、性价比更高、也更容易长期运营的方案。若使用独立的子域名，虽然方便管理，但 SEO 权重部分独立，甚至 Google 有时视为独立站点。每个 APP 使用独立域名或者二级子域名不利于 Content + SEO + Email + Audience 的资产积累。

6. SEO 基础支持
- meta tags
- sitemap
- robots.txt


## 低成本方案选择
静态站是最佳选择

优点：
✅ 极快
✅ SEO好
✅ 免费
✅ 安全
✅ 不需要维护服务器

### 部署方案

GitHub Pages 或者 Cloudflare Pages（更推荐），因为 Cloudflare Pages：

✅ 免费
✅ 自动 HTTPS
✅ CDN
✅ 自定义域名
✅ 更现代
✅ CI/CD 简单
✅ 支持 Functions

### 表单（邮箱收集）

- Tally
- Formspree
- ConvertKit

用户提交邮箱
→ 自动存储
→ 自动邮件
→ 自动管理

完全不需要复杂后端，不需要数据库。



## 总结
- 域名：一个主域名
- 托管: Cloudflare Pages
- 表单: Tally
- 邮件: ConvertKit/Formspree
- Analytics: Plausible / Cloudflare Analytics
