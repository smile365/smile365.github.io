---
title: "scrapy-splash 与 scrapy-redis 的使用"
keywords: ["scrapy-splash 教程", "scrapy-redis 使用", "Python 爬虫", "动态页面抓取", "Splash 渲染引擎"]
tags: ["scrapy", "splash", "爬虫"]
description: "介绍 scrapy-splash 和 scrapy-redis 的安装与配置方法，实现动态页面爬取和分布式爬虫。"
categories: ["code"]
date: "2020-07-24T06:35:35.553Z"
---
先安装[docker](http://sxy91.com/posts/docker) 
安装并运行splash：  
```bash
docker pull scrapinghub/splash
docker run -dit -p 8050:8050 --name splash scrapinghub/splash
```

pip install scrapy-redis

运行一个测试项目
```
pip install scrapy
pip install scrapy-splash
git clone https://github.com/Python3WebSpider/ScrapySplashTest
cd ScrapySplashTest
# 修改splash地址和mongo地址
vim scrapysplashtest/settings.py
# 运行
scrapy crawl taobao
```



