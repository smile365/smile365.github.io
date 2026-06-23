---
title: "wireshark使用"
keywords: ["wireshark过滤规则", "域名过滤", "http抓包", "网络分析"]
tags: ["wireshark", "教程", "网络"]
description: "学习使用Wireshark按域名过滤HTTP请求，掌握http.host和http.request等常用过滤规则的使用方法，快速提升网络抓包分析效率。"
categories: ["code"]
date: "2018-12-20T02:06:11.657Z"
draft: "true"
series: ["blog"]
---
按照域名过滤：http.host contains "http://163.com"

http.request==1
//过滤所有的http请求，貌似也可以使用http.request

参考  
- [wireshark如何按照域名过滤?](https://www.zhihu.com/question/36125941)
