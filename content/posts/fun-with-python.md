---
title: "学 Python 都用来干嘛的？"
keywords: ["生活", "Python", "学 都用来干嘛", "fun", "with"]
tags: ["生活", "Python", "学 都用来干嘛"]
description: "学 Python 都用来干嘛的？"
categories: ["life"]
heading: "学 Python 都用来干嘛的？"
date: "2020-02-14T07:39:08.895Z"
draft: "true"
---
3行代码自动发送邮件?

```python
import yagmail
yag = yagmail.SMTP('your@qq.com', '授权码','smtp.qq.com',465)
yag.send(to = 'sxy9103@qq.com', subject = '微信搜索「下课了」试试', contents = ['这是软广', '不对，是硬广。下面是我的靓照','./gaoqing.png'])
```


自动左划右划？

自动发送微博

自动交易股票？

生成炫酷的朋友圈



