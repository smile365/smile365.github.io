---
title: "VSCode入门教程"
keywords: ["VSCode入门", "VSCode代码片段", "Python模板", "编辑器教程", "VSCode配置", "代码片段设置"]
tags: ["VSCode", "教程", "Python"]
description: "本文介绍VSCode的入门使用方法，教你如何创建Python代码片段模板，自定义用户代码片段提高编码效率，适合初学者快速上手Visual Studio Code。"
categories: ["code"]
date: "2019-12-04T08:13:10.397Z"
draft: "true"
---
创建python模板

```json
{
	"python file": {
		"scope": "python",
		"prefix": "py",
		"body": [
			"#!/usr/bin/env python",
			"# -*- coding: utf-8 -*-",
			"# @Date    : ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE} ${CURRENT_HOUR}:${CURRENT_MINUTE}:${CURRENT_SECOND} ",
			"# @Author  : songxueyan (sxy9103@gmail.com)",
			"# @Link    : https://sxy91.com",
			"# @Description : ",
			"",
			"$1",
		],
		"description": "new python file"
	}
}
```

参考  

- [vscode的代码片段](https://code.visualstudio.com/docs/editor/userdefinedsnippets)