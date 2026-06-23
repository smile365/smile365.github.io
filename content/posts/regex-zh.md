---
title: "正则匹配中日韩文"
keywords: ["正则匹配中文", "正则匹配日文", "正则匹配韩文", "python正则", "Unicode编码区间"]
tags: ["正则", "python", "Unicode"]
description: "使用Python正则表达式匹配中文、日文和韩文，基于Unicode编码区间实现中日韩文的判断与提取。"
categories: ["code"]
heading: "python判断是不是韩语日语和中文"
date: "2019-11-06T09:52:57.390Z"
---
项目中需要用python判断某段文本是不是韩语日语，可以用python正则表达式来解决。

首先得知道UTF-8(Unicode)编码区间如下：
- u0800-u4e00 (日文)
- u4e00-u9fa5 (中文)
- uac00-ud7a3 (韩文)


所以python匹配中日韩文的正则如下：

```python
import re
p = re.compile('[ࠀ-龥가-힣]')
text = '''
这是简体中文,這是繁體中文
这是日文,これは日本語です
这是韩文,한국 사람입니다
'''
print(p.findall(text))
```

参考文档：

- [最新正则匹配手机号](https://sxy91.com/posts/regex-for-phone-number/)