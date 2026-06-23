---
title: "学Python能做什么"
keywords: ["学Python用途", "Python能做什么", "Python自动化", "Python邮件发送", "Python有趣应用"]
tags: ["Python", "自动化", "编程"]
description: "用生动的例子展示学Python之后能做的有趣事情，包括自动发送邮件、刷社交应用、交易股票等实用技能。"
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