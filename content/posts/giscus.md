---
title:  博客接入Giscus
heading: hugo 博客接入Giscus 无后端评论系统
date: 2026-06-23T15:54:54.903Z
tags: ["hugo","giscus"]
categories: ["code"]
Description:  Hugo 博客引入 Giscus 评论系统简易教程
---

## 前言

此博客之前接入的评论是 [valine](https://valine.js.org/quickstart.html) 无后端评论系统（数据基于 LeanCloud） ，我最近发现 valine 已经在 24 年停止了更新。 且 LeanCloud 公告显示：LeanCloud 服务将于 2027 年 1 月 12 日关闭。 打算把博客的评论系统迁移到 [giscus](https://github.com/giscus/giscus)

giscus 是利用 GitHub Discussions 实现的评论系统，无需数据库，也是一个无后端的评论系统，数据直接存储在 github。缺点是评论的时候需要使用 github 登录，无法实现匿名评论。


## 为什么选择 giscus

基于 github 的评论系统经历了从 Issues 到 Discussions 的发展:

```
第一代：Gitalk （Issues）, 于 2021 年停止更新
      ↓
第二代：Utterances （Issues）, 于 2022 年停止更新 
      ↓
第三代：Giscus （Discussions）, 2026年6月依然在更新
```

| 系统       | 技术                                                             |
| ---------- | ---------------------------------------------------------------- |
| Gitalk     | OAuth Callback+Client ID+Client Secret+GitHub API + GitHub Issue |
| Utterances | GitHub App + GitHub Issue                                        |
| Giscus     | GitHub App + GitHub Discussions                                  |
虽然 [Utterances](https://utteranc.es/) 比 [Gitalk](https://github.com/gitalk/gitalk) 更好，但两者的存储都是基于 Issue，造成了如下问题：
1. Issue 不是评论系统，它本来是用于 Bug Tracker；
2. 仓库被污染，每篇文章都生成一个 Issue ，且没有原生 Reaction；

后来 GitHub 开发了 Discussions，专门用于 Q&A、论坛、讨论、社区交流，因此 Giscus 应运而生，解决了以上问题。



## 博客接入 giscus 步骤

### 启用 Discussions

1. 打开 GitHub 仓库 -> Settings -> General
2. 勾选 Features 下面的 Discussions
3. 点击 [giscus app ](https://github.com/apps/giscus) 选择博客所在仓库进行安装
4. 到 [giscus 官网 ](https://giscus.app/zh-CN) 填写仓库地址，
5. Discussion 分类选择 General
6. 特性建议勾选：启用主帖子上的反应(reaction)、懒加载评论


### 修改主题

增加配置项
```toml
[params.giscus]
  repo = "smile365/smile365.github.io"
  repo_id = "xxx"
  category_id = "xxxx"
```


找到主题的单页布局文件，比如 `themes/wehuth/layouts/_default/single.html` , 在想让评论出现的位置添加以下`<script>`标签，内容如下：
```html
    <script src="https://giscus.app/client.js"
        data-repo="{{ $.Site.Params.giscus.repo }}"
        data-repo-id="{{ $.Site.Params.giscus.repo_id }}"
        data-category="{{ $.Site.Params.giscus.category }}"
        data-category-id="{{ $.Site.Params.giscus.category_id }}"
        data-mapping="{{ default "pathname" $.Site.Params.giscus.mapping }}"
        data-strict="{{ default "0" $.Site.Params.giscus.strict }}"
        data-reactions-enabled="{{ default "1" $.Site.Params.giscus.reactions_enabled }}"
        data-emit-metadata="{{ default "0" $.Site.Params.giscus.emit_metadata }}"
        data-input-position="{{ default "bottom" $.Site.Params.giscus.input_position }}"
        data-theme="{{ default "preferred_color_scheme" $.Site.Params.giscus.theme }}"
        data-lang="{{ default "zh-CN" $.Site.Params.giscus.lang }}"
        data-loading="{{ default "lazy" $.Site.Params.giscus.loading }}"
        crossorigin="anonymous"
        async>
    </script>
```


使用命令预览

```bash
hugo server -D -t wehuth --bind=127.0.0.1 --baseURL=http://127.0.0.1:1313
```