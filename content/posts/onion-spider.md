---
title: "暗网爬虫 - 洋葱网络数据抓取"
keywords: ["暗网爬虫", "Tor网络", "洋葱路由", "Python Tor代理", "暗网数据抓取"]
tags: ["暗网", "Tor", "爬虫", "Python"]
description: "在 CentOS 和 macOS 上配置 Tor 代理，使用 Python 通过 SOCKS5 代理抓取洋葱网站（.onion）数据的教程。"
categories: ["life"]
date: "2019-12-19T10:24:00.095Z"
draft: "true"
---
centos安装tor
```bash
yum -y install tor
# 编辑配置文件
vim /etc/tor/torrc
# 启动
# systemctl start tor
```

mac安装tor
```bash
mac brew install tor
# 拷贝配置文件
cp /usr/local/etc/tor/torrc.sample /usr/local/etc/tor/torrc
# 编辑配置文件
# vim /usr/local/etc/tor/torrc
#启动
tor
```

配置文件的其他项
```
Socks5Proxy 127.0.1.1:1080 # 使用ss代理的地址和端口
CookieAuthentication 1         # 开启cookies
```

python测试代码
```python
proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
not_evil = "http://hss3uro2hsxfogfq.onion/"
data = requests.get(not_evil,proxies=proxies).text
print(data)
```


参考


- [requests-proxy](https://stackoverflow.com/questions/43682909/connect-to-onion-websites-on-tor-using-python)
- [Centos-7配置与使用SS-tor环境](https://zhizhebuyan.com/2017/07/12/Centos-7%E9%85%8D%E7%BD%AE%E4%B8%8E%E4%BD%BF%E7%94%A8SS-tor%E7%8E%AF%E5%A2%83/)
