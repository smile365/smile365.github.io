---
title: "Python 日志模块使用教程"
keywords: ["Python logging 模块", "Python 日志配置", "logging 基本配置", "日志格式设置"]
tags: ["Python", "日志", "logging"]
description: "介绍 Python logging 模块的基本配置方法，包括日志级别、格式化和日期格式的设置，快速实现程序日志输出。"
categories: ["code"]
date: "2018-08-07T07:34:37.512Z"
draft: "true"
---
```python
import logging

LOG_FORMAT = "%(filename)s:%(lineno)d %(levelname)s %(asctime)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO,format=LOG_FORMAT,datefmt=DATE_FORMAT)

# create logger
logger = logging.getLogger("root")

longger.info("hello")
```

参考

- [Python之日志处理（logging模块）](https://www.cnblogs.com/yyds/p/6901864.html)
- [python-logging](https://www.jianshu.com/p/feb86c06c4f4)