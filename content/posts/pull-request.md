---
title: "为 GitHub 开源项目贡献代码"
keywords: ["GitHub Pull Request 教程", "开源项目贡献代码", "Git fork PR 流程", "GitHub 协作开发"]
tags: ["GitHub", "Pull Request", "开源"]
description: "通过 fork、clone、关联上游仓库和提交 Pull Request 的完整流程，学习如何为 GitHub 开源项目贡献代码。"
categories: ["code"]
date: "2022-04-15T11:25:18.427Z"
---
## 什么是 pr（pull request）
参考 [Pull Request 的命令行管理](http://www.ruanyifeng.com/blog/2017/07/pull_request.html)

>"Pull Request 是 github 的一种通知机制。你修改了他人的代码，将你的修改通知原来的作者，希望他合并你的修改，这就是 Pull Request。"



## 一、fork 原作者的项目
假设 someone 有个项目 demo

由于没有对 demo 的直接 push 权限，我们需要先对 demo 库进行 fork，然后从自己的地址 clone。
```bash
git clone git@github.com:yourname/demo.git
someone
```


## 二、与原作者仓库进行拉取和推送关联
为了保证我的代码和原作者实时同步（原作者的改动我们也能拉取，我们的修改也能推送到原作者仓库），需要进行 关联。

clone 项目到本地后，进入 demo 目录，添加一个新的推送地址，取名叫 upstream（代表原作者的仓库） 。
```bash
cd ~/demo
git remote add upstream git@github.com:someone/demo.git
```

使用 `git remote -v` 查看此时有两个推送和拉取地址。
```
origin	git@github.com:username/demo.git (fetch)
origin	git@github.com:username/demo.git (push)
upstream	git@github.com:someone/demo.git (fetch)
upstream	git@github.com:someone/demo.git (push)
```
## 三、切换 dev 分支

根据原作者的说明，一般需要在 dev 分支进行修改和提交 pr。

先查看远程仓库里有哪些分支 `git branch -r`
```
  origin/HEAD -> origin/master
  origin/develop
  origin/master
  upstream/develop
  upstream/master
```


切换到 develop 分支，并跟踪远程分支。

git checkout --track origin/develop