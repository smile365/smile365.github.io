# smile365.github.io

宋洋葱的个人博客 [blog](sxy91.com) , 基于 hugo 部署，主题为：微信公众号风格的 [wehugo](https://github.com/smile365/wehuth) 主题

## 如何给文章打标签

| 字段         | 单片文章数量 | 定义   | 用途 | 举例 |
| ---------- | -------- | ------- | ----- | ----------------- |
| categories |  1        | 栏目     | 文章最大分类     | 生活、代码、读书、其他               |
| tags       |   1~5      | 具体主题标签  | 文章讲什么     |  hugo、hugo theme            |
| keywords   | 3~8       | SEO关键词  | 用户怎么搜     |               | hugo install, hugo github pages 
| series     | 1  | 系列文章    | 需要分好几篇讲清除同一个事情    | AI教程1、AI教程2、AI教程3             |


## 如何引用同项目内文章

不同目录
```
[GitHub Pages 部署指南]({{< relref "posts/github-pages.md" >}})
```

相同目录
```markdown
参考：[文章B]({{< relref "article-b.md" >}})
```


## 推荐的 Front Matter

```markdown
---
title: "文章标题"
date: 2026-06-23
lastmod: 2026-06-24              # 最后修改时间，影响 article:modified_time
publishDate: 2026-06-23          # 发布日期，用于 article:published_time
description: "文章摘要，会出现在搜索结果和社交分享中"  # 强烈推荐
tags: ["hugo", "theme"]          # 用于 OG article:tag、站内关联、关键词
categories: ["技术"]              # 用于 OG article:section
author: "宋洋葱"                  # 覆盖站点默认作者
slug: "custom-url"               # 自定义 URL 别名
weight: 10                       # 列表排序权重
heading: "展示用标题"              # 与 title 不同时可设置
aliases: ["/old-url"]            # 旧 URL 301 重定向
toc: false                       # 禁用目录
enableReadingTime: false         # 禁用阅读时间估算
---
```