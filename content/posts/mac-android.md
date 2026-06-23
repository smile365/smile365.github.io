---
title: "Mac搭建安卓开发环境"
keywords: ["Mac搭建Android开发环境", "Android Studio安装", "macOS安卓开发", "Java8配置", "Android SDK"]
tags: ["Android", "Mac", "开发环境"]
description: "在Mac电脑上搭建Android开发环境的完整步骤，包括安装Java8、Android Studio、命令行工具及常见问题的解决方法。"
categories: ["code"]
date: "2018-07-22T13:38:58.727Z"
series: ["blog"]
---
先安装构建工具和java8
```
brew cask install java8
brew install ant
brew install maven
brew install gradle
```

然后到官网下载[Android studio](https://developer.android.google.cn/studio/)

如果出现unable to access android sdk add-on list，直接点击取消，之后会自动下载(可能需翻墙)。



参考
- [官方文档](https://developer.android.com/studio/install?hl=zh-cn)
- [ANDROID学习之路](http://stormzhang.com/android/2014/07/07/learn-android-from-rookie/)
- [androiddevtools](http://www.androiddevtools.cn/)
- [Android SDK 使用国内镜像](https://blog.csdn.net/zdw_wym/article/details/74942772)
- [镜像地址](https://www.jianshu.com/p/53080a8cbc95)
- [谷歌中国](https://developer.android.google.cn/)
- [Mac-Setup-Guide4OCD](https://github.com/macdao/ocds-guide-to-setting-up-mac)
- [brew和brew-cask的区别](https://www.zhihu.com/question/22624898)
- [idea-android-brew-mac](https://www.soupwaylee.com/2017/09/02/android-setup.html)
