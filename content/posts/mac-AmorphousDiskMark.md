---
title: "Mac硬盘U盘测速AmorphousDiskMark"
keywords: ["Mac硬盘测速", "AmorphousDiskMark教程", "固态硬盘速度测试", "MacBook磁盘性能", "移动硬盘测速"]
tags: ["Mac", "硬盘测速", "AmorphousDiskMark"]
description: "使用AmorphousDiskMark在Mac上测试各类存储设备的读写速度，包括2230固态、M2 MacBook Air和移动硬盘的真实性能数据对比。"
categories: ["read"]
date: "2022-11-23"
series: ["blog"]
---
## 参考文档
- [SD 卡速度等级](https://www.kingston.com.cn/cn/blog/personal-storage/memory-card-speed-classes)

## 2230 固态
- 硬盘盒：ITGZ  m.2 JMS583  2230 硬盘盒 （66 元）
- 2230 固态： 镁光 2230 512G （某鱼 245 元）格式化成 [APFS](https://evestorm.github.io/posts/33677/)格式
- 读：1029 MB/s
- 写：1031 MB/s

![enter description here](https://cdn.sxy21.cn/static/imgs/1669186717752.png)

## 2019 年 mac air 自带硬盘 
- 读：1306 MB/s
- 写：131 MB/s （可能是我存储不够了）
 
![enter description here](https://cdn.sxy21.cn/static/imgs/1669187655393.png)

感觉写入特别低，可能是我们硬盘满了，只剩 6G 可用空间。删除了一些文件，剩余空间 15G，再次测试。

![enter description here](https://cdn.sxy21.cn/static/imgs/1669188907356.png)

提升还是挺明显的，但写入依旧没到 1000 MB/s，难道还是剩余空间不够？


## 2022 年 MacBook air（m2）
![enter description here](https://cdn.sxy21.cn/static/imgs/1699433989471.png)

## 移动固态硬盘
海康威视 T9 PRO 1024GB
![enter description here](https://cdn.sxy21.cn/static/imgs/1699435584169.png)

换成苹果原装充电线，变成了读写 36MB 上下。
![enter description here](https://cdn.sxy21.cn/static/imgs/1699437718691.png)


## usb2.0 的 u 盘
对比一下我 usb2.0 的 u 盘
- 读：20 MB/s
- 写：4 MB/s 

![enter description here](https://cdn.sxy21.cn/static/imgs/1669190236680.png)


这速度不能忍，拷贝一个 1 G 的文件进去要 3 分多钟，而 2230 固态只需要 1 秒。

## 2014 年希捷 1T HDD
对比 2014 年买的希捷 1T HDD（机械） 移动硬盘
- 读：31 MB/s
- 写：65 MB/s 
