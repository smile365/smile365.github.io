---
title: EdgeOne
heading:  基于EdgeOne Makers免费部署后端api项目
date: 2026-11-25T08:56:22.683Z
tags: 
categories: ["code"]
Description:  基于腾讯免费 EdgeOne 服务，部署一套完全免费的后端 api 项目
---

## 前言

以前一直白嫖 cloudflare 的免费服务，最近使用了一段时间的 EdgeOne 发现不错，也有免费额度。


## 关于 Edge Functions 

EdgeOne 支持两种 [Functions](https://makers.edgeone.link/document/pages-functions-overview)：Edge Functions 和 Cloud Functions

两种都可以用于实现后端 API。Edge Functions 相当于运行在离用户最近的一台仅支持 V8 引擎（仅可运行 javascript 代码）的服务器上，可以拦截用户的请求，然后进行简单处理（使用 js 处理）。

```
浏览器  ← 获取 HTML/CSS/JS 并渲染
   │ HTTP
   ▼
EdgeOne 边缘节点
   ├─ 静态文件      → CDN 直接返回（与函数路由冲突时静态优先）
   └─ Edge Functions → 可选拦截：鉴权 / 限流 / 改写 / 重定向 / 直接吐 JSON
      └── fetch 子请求   → Cloud Functions / 外部 API / 源站
```

Cloud Functions 则相当于后端开发常见的 Node.js、Python、Go 等环境，可以使用各种复杂的 web 框架和第三方依赖包。


## 关于 EdgeOne Makers

一个 EdgeOne Makers 项目可以同时有 public/edge-functions/cloud-functions/agents/ 目录，也可以只有 edge-functions，本次后端 api 比较简单，没有静态资源，仅返回 json 数据。

```
my-project/
├── public/                          # 静态文件路径（由 edgeone.json: outputDirectory 参数指定的目录会部署到 cdn 节点，发给用户浏览器执行）
│   ├── index.html
│   └── assets/
├── edge-functions/                   # V8 环境，离用户最近的腾讯云服务器执行
│   └── gate/						  # 匹配请求→ /gate/*
│       └── [[default]].js            # 仅能运行 js 代码
├── cloud-functions/                  # Node.js、Python、Go 后端环境
│   └── api/						  # 匹配请求→ /api/*
│       └── [[default]].[py/js/ts/go] # 后端代码 
└── edgeone.json # 配置文件（非必须）
```


`edge-functions` 下的 js 与 public 下的 js 不同，此目录下的 js 用户看不见，仅能处理 http 请求并响应。

## 真实项目

### 需求

对着手机说：“小爱同学，打开车库大门”，发送一个请求给服务器实现开门。

iPhone 用户可以通过 iOS 快捷指令，实现 siri 开门（或者一键开门）

### 原理

车库大门是定做的，可以手机联网控制。我逆向了这个app，找到了开门的“办法”（当然只能开自己的门）。开门的本质就是发送一个 http 请求给服务端。

实现思路：快捷指令通过 post 把用户名密码发送到 api/open.js , js 把数据与 env 中的比对，通过后则调用大门厂商的登录接口，成后获取 token 后调用厂商的开门接口。


### 项目目录

本次使用 [EdgeOne CLI](https://makers.edgeone.link/document/edgeone-cli) 来初始化 EdgeOne Makers 项目， cli 也比较方便本地开发和测试。

```
my-project/
├── edge-functions/     # V8 环境
│   └── api/			# 匹配请求 → /api/*
│       └── open.js     # 匹配请求 → /api/open 执行开门逻辑
└── .env                # 环境变量（账号密码），在 .gitignore 中忽略
```


伪代码
```javascript
// 默认值（常量）
const DEFAULTS = {
    API_BASE: 'https://api.mydoor.cn',
    API_APIS_DOMAIN: 'apis'
};
// env 中的 key
const REQUIRED_KEYS = [
    'USERNAME', 'PASSWORD', 'DOOR_PUNIT_ID', 'DOOR_SN', 'AES_KEY', 'AES_IV', 'SECRET',
];

/** 读取并校验配置；缺失必需项时抛出可读错误。 */
export function loadConfig(env) {
    return {
        username: String(env.USERNAME),
        password: String(env.PASSWORD),
        punitId: Number(env.DOOR_PUNIT_ID),
        sn: String(env.DOOR_SN),
    };
}

// 开门逻辑，匹配 HTTP Methods (POST)
export async function onRequestPost(context) {
    let cfg = loadConfig(context.env);
    let form;
    const raw = await context.request.text();
    form = new URLSearchParams(raw);
    const username = (form.get('username') || '').trim();
    const password = form.get('password') || '';
    const [usernameOk, passwordOk] = await Promise.all([
        constantTimeEqual(username, cfg.username),
        constantTimeEqual(password, cfg.password),
    ]);
    let result = result = await sendCall(call, cfg);
    let ok = isSuccess(result, cfg) && result.data && Number(result.data.state) ===
    return jsonResponse(200, {
        ok: ok,
        credential: credential.mode,
        door: cfg.doorName,
        target: {
            punitId: cfg.punitId,
            sn: cfg.sn
        },
        seq,
        request: {
            path: cfg.openDoorPath,
            url: call.url,
            method: 'POST'
        },
        upstream: dryRun ? {
            ecode: 'DRY_RUN',
            msg: 'no upstream request sent'
        } : result,
    });
}

```


参考官方步骤 [绑定 Git 仓库](https://makers.edgeone.link/document/importing-a-git-repository)后，下次 push 代码即可自动部署。

> 注：为了方便绑定自定义域名，登录腾讯云的账户最好与要绑定域名的账户一致，切域名托管在腾讯云。方便自动绑定域名。
