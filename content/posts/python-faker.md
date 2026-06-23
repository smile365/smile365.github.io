---
title: "Python 使用 Faker 生成假数据"
keywords: ["Faker 生成测试数据", "Python 假数据生成", "Faker 中文数据", "Python 造数据"]
tags: ["Faker", "Python", "测试数据"]
description: "使用 Python Faker 库自动生成姓名、地址、手机号等随机测试数据，并批量生成 30 万用户信息的实战案例。"
categories: ["code"]
date: "2021-01-20T02:37:09.448Z"
---
## 前言
[faker](https://faker.readthedocs.io/en/master/)可以生成非常真实的随机数据，通过它的[提供者](https://faker.readthedocs.io/en/master/providers.html)，可以生成诸如姓名、地址、ip、公司名、银行卡号、邮编、ISBN、时间、手机号、职业等等数据。通过本地话配置可支持设置不同的语言和地区。

另一个相似的工具是 [mimesis](https://github.com/lk-geimfari/mimesis)

## 安装

```bash
pip install faker
```

## 使用

### 简单使用
```python
from faker import Faker
# 设置语言
fake = Faker('zh_CN')

print(fake.name())
print(fake.random_int(0, 100))
print(fake.random_number(digits=10))

print(fake.lexify(text='测试字符串：????', letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
```

### 真实案例
请使用 python3 的 Faker 模块生成一个 30 万的用户信息，并写入名为 users30w.json 的文件，然后使用 post 请求把 用户信息发送到 localhost:8080/save/users 。

```python
# pip3 install Faker requests
from faker import Faker
import json
import requests

# 创建 Faker 实例
fake = Faker()

# 生成用户信息
users = []
for i in range(300000):
    user = {
        "id": fake.uuid4(),
        "userPoolId":"64916f78cc768114483d9924",
        "status": "Activated",
        "email": fake.email(),
        "username": fake.user_name(),
        "nickname": fake.name(),
        "gender": fake.random_element(["M", "F", "U"])
    }
    #print(f'{i}:{user["id"]}')