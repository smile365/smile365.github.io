---
title: "Mac双拼快速输入技术符号"
keywords: ["Mac双拼输入法", "技术符号输入", "百度输入法自定义短语", "Mac快捷键符号"]
tags: ["Mac", "双拼", "输入法"]
description: "在Mac上使用百度输入法双拼模式快速输入⌘、⌥、⇧等技术符号的自定义短语配置方法。"
categories: ["code"]
date: "2018-07-20T06:07:13.544Z"
draft: "true"
series: ["blog"]
---
mac技术符号如下：
- ⌘（command）
- ⌥（option）
- ⇧（shift）
- ⇪（caps lock）
-  ⌃（control）
-  ↩（return）
-  ⌅（enter）

安装百度输入法mac版本，在偏好设置-词库-个性短语导出短语，在导出文件的最后增加如下配置：
[Mac]
cmd=1,⌘
opt=1,⌥
shi=1,⇧
cap=1,⇪
ctl=1,⌃
rt=1,↩
et=1,⌅

然后导入刚刚编辑过的文件。

参考
- [Mac快捷键](https://support.apple.com/zh-cn/HT201236)
