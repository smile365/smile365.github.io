---
title: "reverse-apks-by-claude"
keywords: ["教程", "claude", "reverse apks by", "MacOS", "apk", "java", "jadx", "vineflower", "claude ##", "reverse"]
tags: ["教程", "claude", "reverse apks by", "MacOS", "apk", "java", "jadx", "vineflower"]
description: "遇到的问题 **model is not available**"
categories: ["code"]
heading: "MacOS 下使用 claude 对 apk 进行逆向分析"
date: "2026-05-11T06:01:32.934Z"
---
## 安装必要依赖

**java：** 
``` bash
java -version
# Should show version 17.x or higher</pre>
```

**jadx：**

``` bash
brew install jadx
jadx --version
```

**vineflower：**
``` bash
brew install vineflower

```

**dex2jar：**

``` bash
brew install dex2jar
d2j-dex2jar --help
```


## 安装技能


``` bash
git clone https://github.com/SimoneAvogadro/android-reverse-engineering-skill.git
claude
/plugin marketplace add ./android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
/reload-plugins

```

使用 
```bash
/decompile path/to/app.apk
```

## 遇到的问题
**model is not available**
```prolog
Please run /login · API Error: 403 This model is not available in your region.
```
在 https://openrouter.ai/ 充值了 $10 美金，结果不让用国外的模型，参考[OpenRouter 限制国内直连，已无法调用 OpenAI、Claude 和 Google 三大模型](https://linux.do/t/topic/1846933)


参考文档
- [逆向工程的依赖项](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/plugins/android-reverse-engineering/skills/android-reverse-engineering/references/setup-guide.md)