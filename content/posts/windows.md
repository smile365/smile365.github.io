---
title: "Windows使用技巧"
keywords: ["Windows命令技巧", "CMD别名设置", "Windows findstr", "查看端口占用", "Windows批处理"]
tags: ["Windows", "CMD", "命令提示符"]
description: "汇总Windows命令提示符的使用技巧，包括类似Linux grep的findstr命令、端口占用查看和CMD别名设置方法。"
categories: ["code"]
date: "2018-07-20T09:32:38.774Z"
draft: "true"
series: ["blog"]
---
类似于Linux 下的grep
C:\> dir /B | findstr /R /C:"[mp]"

查看端口占用
netstat -ano | findstr 8009

新建一个批处理如：aliase.bat，双击运行。
```bat
@doskey ls=dir /b $*
@doskey st="C:\Program Files\Sublime Text 3\sublime_text.exe $*"
```

关机后下次需要重新运行一次，可以加到开机启动，新建一个hotkey.reg,双击运行。
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Command Processor]
"AutoRun"="D://sxycmd//aliase.bat"
```




参考  
- [Windows-alias给cmd命令起别名](https://www.awaimai.com/2445.html)
- [windows-alias](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt)