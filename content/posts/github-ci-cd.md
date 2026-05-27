---
title:  github-ci-cd
heading:  基于 GitHub Actions 实现自动部署（CI/CD）
date: 2026-05-27T12:24:38.406Z
tags: 
categories: ["code"]
Description:  
---

## 前言
基于  python 给几个 app 开发了对应的后端 api，每次改完代码部署都比较繁琐：

1. 要先手动把代码拷贝到服务器，比如使用 scp/rsync 命令或者使用 shell 脚本；
2. ssh 到服务器，然后停止服务，或者重启服务

使用 GitHub Actions 可以简化这一过程，实现推送代码即可自动部署（CI/CD），它运行的原理如下：

```
本地开发
   ↓
git push
   ↓
GitHub Actions
   ↓
SSH 登录 VPS
   ↓
执行 deploy.sh
```

也就是 GitHub Actions 具有登录服务器，然后执行 shell 脚本的能力，只需要在 deploy.sh 写好部署的逻辑即可，以下是实现教程。

## 生成 ssh 公钥

1. 生成 github 登录服务器所需的密钥

在自己的个人电脑（不是服务器）执行命令：

```bash
# 查看是否有同名的密钥，避免覆盖
ls -lh ~/.ssh/*.pub
# 生成密钥，-t 为签名算法，-C 为备注， -f 为文件名
ssh-keygen -t ed25519 -C "github-actions" -f ~/.ssh/github-actions
```


2. 把公钥加到服务器（server）

```
# -p 为端口，若为 22 可省略；root 为用户名；server 为 ip 或域名
ssh-copy-id -p 3322 -i ~/.ssh/github-actions.pub  root@server
```
3. 测试免密登录
```bash
ssh -i ~/.ssh/github-actions root@server
```
4. 避免每次都指定密钥、用户名、端口。

在文件 `~/.ssh/config`中配置 ssh 所需的信息：
```bash
Host p1
    HostName 8.8.8.8
    User root
    Port 3322
    IdentityFile ~/.ssh/github-actions
```

之后仅需使用命令 `ssh p1` 即可登录服务器。

##  github 添加公钥

找到需要集成 CI/CD 代码仓库的[项目主页](https://github.com/smile365?tab=repositories)，依次点击 Settings/Secrets and variables/Actions/New repository secret


| No  | name        | Secret       |
| --- | ----------- | ------------ |
| 1   | VPS_HOST    | ip 或域名    |
| 2   | VPS_USER    | root         |
| 3   | VPS_SSH_KEY | 粘贴私钥内容 |
> xxx

## 配置cicd

在仓库的根目录创建如下文件 .github/workflows/deploy.yml ， 内容如下：

```yaml
name: Deploy Imgtool

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to VPS
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            /opt/deploy-myapp.sh
```

参数解释：
- - branches 为触发的分支，到仓库主页查看，有的为 master ，有的为 main
