---
title: "URL正则表达式"
keywords: ["URL正则表达式", "RFC 1738", "URL编码", "网址匹配正则", "正则表达式教程", "JavaScript正则"]
tags: ["正则", "URL", "RFC"]
description: "本文总结了符合RFC 1738标准的URL正则表达式，包含完整网址和相对网址的正则匹配模式，以及URL编码和百分号编码的参考资料。"
categories: ["code"]
date: "2018-07-27T02:05:03.386Z"
draft: "true"
---
网络标准RFC 1738规定：
"只有字母和数字[0-9a-zA-Z]、一些特殊符号"$-_.+!*'(),"[不包括双引号]、以及某些保留字，才可以不经过编码直接用于URL。"

全网址
`(https?://)?([-\w]+\.)+[-\w]+(/[-\w\.'&=+$#%]+)*`

相对网址
(\.\./[-\w]*)*(\./)?[-\w\.'&=+$#%]+

参考
- [正则表达式](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions)
- [关于URL编码](http://www.ruanyifeng.com/blog/2010/02/url_encoding.html)
- [百分号编码](https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)
