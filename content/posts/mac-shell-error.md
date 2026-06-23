---
title: "Mac终端粘贴异常字符解决"
keywords: ["Mac终端粘贴乱码", "shell复制粘贴异常", "command+c command+v 异常字符"]
tags: ["Mac", "终端", "shell"]
description: "解决Mac终端粘贴复制时出现00~和01~等异常字符的问题，一条命令即可修复。"
categories: ["code"]
date: "2022-09-14T12:44:47.594Z"
draft: "true"
---
mac 终端 粘贴复制出现异常字符，前后出现多余字符 00~  01~  command+c  command+v

```bash
printf '\e[?2004l'
```
