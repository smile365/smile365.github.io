---
title: "Grafana安装与配置"
keywords: ["grafana安装", "grafana配置", "grafana反向代理", "grafana邮件告警", "nginx反向代理"]
tags: ["Grafana", "监控", "Nginx"]
description: "在 CentOS 上安装 Grafana 并配置 Nginx 反向代理和邮件报警服务，实现监控面板的域名访问和告警通知。"
categories: ["code"]
date: "2019-09-02T08:39:36.785Z"
draft: "true"
---
```bash
yum install grafana
systemctl start grafana-server
systemctl enable grafana-server
```

编辑配置文件：`vim /etc/grafana/grafana.ini`,配置反向代理和邮件报警服务。

```ini
#反向代理
[server]
domain = localhost
root_url = http://192.168.1.133/grafana/

#邮件提醒
[smtp]
enabled = true
host = smtp.exmail.qq.com:25
user = songxueyan@sxy91.com
password = yourpassword
from_address = songxueyan@sxy91.com
skipVerify = true
```

nginx配置对应上面的`root_url`

```nginx
  location /grafana/ {
     proxy_pass http://localhost:3000/;
  }
```


参考

- [grafana-docs](https://grafana.com/docs/)