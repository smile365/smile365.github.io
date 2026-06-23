---
title: "Mac安装Android Studio教程"
heading: "Mac系统安装Android Studio及Gradle开发环境配置"
keywords: ["Mac安装Android Studio", "Android开发环境搭建", "Mac配置Gradle", "Android Studio安装教程", "Mac Java SDK安装"]
tags: ["Android Studio", "Mac", "开发环境"]
description: "详细教程指导在Mac系统上安装Android Studio、Java SDK和Gradle，搭建完整的Android开发环境。"
categories: ["code"]
date: "2022-01-11T12:08:36.108Z"
---
所需工具
- java sdk
- gradle
- android studio


下载[Android Studio](https://developer.android.com/studio)，根据[使用文档](https://developer.android.com/studio/install)安装和配置。


安装[gradle](https://gradle.org/install/)

使用 brew 安装
```
brew install gradle
```

或者下载二进制安装包安装
```bash
$ mkdir /usr/local/opt/gradle
$ unzip -d /usr/local/opt/gradle gradle-7.3.3-bin.zip
$ ls /usr/local/opt/gradle/gradle-7.3.3/
LICENSE  NOTICE  bin  getting-started.html  init.d  lib  medi
$ export PATH=$PATH:/usr/local/opt/gradle/gradle-7.3.3/bin
$ gradle -v
```