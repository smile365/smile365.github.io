---
title: "mac-shell-error"
keywords: ["教程", "mac shell error", "mac", "command+c command+v", "shell", "error"]
tags: ["教程", "mac shell error", "mac", "command+c command+v"]
description: "mac 终端 粘贴复制出现异常字符，前后出现多余字符 00~ 01~ command+c command+v"
categories: ["code"]
heading: "mac-shell-error"
date: "2022-09-14T12:44:47.594Z"
draft: "true"
---
mac 终端 粘贴复制出现异常字符，前后出现多余字符 00~  01~  command+c  command+v

```bash
printf '\e[?2004l'
```
