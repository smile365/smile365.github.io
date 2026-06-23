---
title: "scrapy-splash与scrapy-redis的使用"
keywords: ["教程", "docker", "redis", "scrapy splash", "scrapy redis", "splash", "pip install scrapy", "scrapy"]
tags: ["教程", "docker", "redis", "scrapy splash", "scrapy redis", "splash", "pip install scrapy"]
description: "scrapy-splash"
categories: ["code"]
heading: "scrapy-splash与scrapy-redis的使用"
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



