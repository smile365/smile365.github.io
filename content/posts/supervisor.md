---
title: "Supervisor进程管理"
keywords: ["Supervisor教程", "进程管理工具", "Linux进程守护", "Supervisor配置", "Python进程管理"]
tags: ["Supervisor", "Linux", "运维"]
description: "Supervisor进程管理工具的安装和配置教程，通过配置INI文件实现对后台进程的守护和自动重启管理。"
categories: ["code"]
date: "2019-04-29T08:29:53.151Z"
draft: "true"
series: ["blog"]
---
安装
```shell
yum -y  install supervisor
systemctl enable supervisord
vim /etc/supervisord.d/myprogram.ini
```

配置文件myprogram.ini内容
```ini
[program:db2db]
directory=/root/project
command=/usr/bin/python db2db.py
stderr_logfile=/root/project/err.log
```

重启
```shell
systemctl restart supervisord
supervisorctl
```

参考  
- [supervisor](http://supervisord.org/installing.html)