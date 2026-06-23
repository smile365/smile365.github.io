---
title: "使用 pyenv 安装和管理 Python 版本"
keywords: ["pyenv 安装", "pyenv Python 版本管理", "Debian 安装 pyenv", "多版本 Python 管理"]
tags: ["pyenv", "Python", "版本管理"]
description: "在 Debian 12 系统中使用 pyenv 安装和管理多个 Python 版本，解决因版本差异导致的 API 模块兼容性问题。"
categories: ["code"]
date: "2025-06-04T03:24:55.365Z"
---
## 前言

开发了一个 python 后端 api，其中用到了阿里云 python sdk 。
```python
send_sms_verify_code_request = dypnsapi_20170525_models.SendSmsVerifyCodeRequest(
            sign_name='云渚科技验证服务',
            template_code='100001',
            phone_number='12345678911',
            template_param='{"code":"##code##"}'
        )
```

本地运行完全没问题。但是部署到 debian 12 服务器就报错：
```bash
module 'alibabacloud_dypnsapi20170525.models' has no attribute 'SendSmsVerifyCodeRequest'
```

尝试了半天没解决，对比后发现 python 版本不一样，我本地是 3.10.12，线上的 python 是 3.11.2。怀疑是版本不同引发的问题。决定使用 pyenv 管理不同版本的 python。


## 安装 pyenv

[pyenv 官方](https://github.com/pyenv/pyenv/?tab=readme-ov-file#installation)推荐使用脚本安装

```bash
<pre>curl -fsSL https://pyenv.run | bash</pre>
```

国内访问 github 受限，经常安装失败，会报错：
```bash
Cloning into '/root/.pyenv'... fatal: unable to access 'https://github.com/pyenv/pyenv.git/': GnuTLS recv error (-110): The TLS connection was non-properly terminated.
```

可以通过镜像站安装，如 [gh-proxy.com](https://gh-proxy.com)
```bash
rm -rf /root/.pyenv
curl -fsSL  https://gh-proxy.com/github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```


## 设置 pyenv 环境变量

通过在 ~/.bash_profile 文件中添加以下代码自动加载 pyenv：
```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init - bash)"
```

通过在 ~/.bashrc 文件中添加以下代码自动加载 pyenv-virtualenv