---
title: "pyppeteer 简明教程"
keywords: ["pyppeteer 爬虫", "Python 无头浏览器", "pyppeteer 教程", "自动化 Chrome", "pyppeteer 微博"]
tags: ["pyppeteer", "爬虫", "Python"]
description: "pyppeteer 是 Puppeteer 的 Python 实现，可自动化控制无头 Chrome 浏览器，涵盖安装测试与会话关闭问题的解决方法。"
categories: ["code"]
heading: "爬虫神器 pyppeteer 的使用教程方法"
date: "2019-07-01T02:11:34.220Z"
---
Puppeteer它是一个Node库，提供了一个高级的API来控制DevTools协议上的无头版Chrome，可以自动化控制浏览器运行。pyppeteer是python版的实现。

centos7安装[pyppeteer](https://miyakogi.github.io/pyppeteer/)
==

```sh
yum -y install chromium
python3 -m pip install pyppeteer
```

测试  
==
```python
import asyncio
from pyppeteer import launch

async def main():
	browser = await launch()
	page = await browser.newPage()
	await page.goto('https://sxy91.com')
	await page.screenshot({'path': 'sxy.png'})
	await asyncio.sleep(30)
	title = await page.title()
	print(title)

asyncio.get_event_loop().run_until_complete(main())
```

会话关闭的解决办法
==
20秒不操作后会话关闭，会出现错误:`Session closed. Most likely the page has been closed`  
pyppeteer的开发团队似乎比较忙，还没修复。可参考[pyppeteer#159](https://github.com/miyakogi/pyppeteer/pull/160/files),修改源码`pyppeteer/connection.py`，替换第44行源码。
```git 
self._ws = websockets.client.connect(
- self._url, max_size=None, loop=self._loop)
+ self._url, max_size=None, loop=self._loop,ping_interval=None, ping_timeout=None)
```

使用pyppeteer自动发送微博的例子
```python
import asyncio
from pyppeteer import launch

home_url = 'https://weibo.com/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

img = '/Users/songyangcong/Pictures/6781573623694_.pic.jpg'

async def sendimg(path,headless=False,devtools=False):
	browser = await launch(executablePath=path,headless=headless,devtools=devtools,userDataDir='./tmp/userdata',args=['--no-sandbox','--disable-infobars'])