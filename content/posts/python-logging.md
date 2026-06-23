---
title: "python日志"
keywords: ["教程", "logging", "python", "日志", "python logging"]
tags: ["教程", "logging", "python", "日志", "python logging"]
description: "Python之日志处理（logging模块） - python-logging"
categories: ["code"]
heading: "python日志"
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