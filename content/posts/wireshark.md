---
title: "wireshark使用"
keywords: ["教程", "code", "it", "wireshark"]
tags: ["教程", "code", "it", "wireshark"]
description: "按照域名过滤：http.host contains \""
categories: ["code"]
heading: "wireshark使用"
date: "2018-12-20T02:06:11.657Z"
draft: "true"
series: ["blog"]
---
按照域名过滤：http.host contains "http://163.com"

http.request==1
//过滤所有的http请求，貌似也可以使用http.request

参考  
- [wireshark如何按照域名过滤?](https://www.zhihu.com/question/36125941)
