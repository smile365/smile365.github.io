---
title: "Auto.js日志与调试"
heading: "Auto.js如何在手机上显示日志和调试信息"
keywords: ["Auto.js显示日志", "手机调试信息", "Auto.js console", "Auto.js日志输出", "Auto.js调试教程"]
tags: ["Auto.js", "日志", "调试"]
description: "Auto.js在手机上显示日志和调试信息的详细教程，包括console.show()使用方法、日志级别颜色区分和输出到文件。"
categories: ["code"]
date: "2020-04-29T01:26:59.943Z"
---
autojs的文档没有pdf格式可供下载，只能去看网页版官方文档地址：`https://hyb1996.github.io/AutoJs-Docs`。文档支持Auto.js 4（免费版）和auto.js pro7（收费版）两个版本。作者hyb1996还没来得及写Auto.js 8.0 pro的文档，如果你用的是auto.js pro8只能自己研究。

我目前用的是autojs 7.0 pro，官网已经不支持下载。如果需要老版本和最新版本可以到这里[下载Auto.js app](https://www.sxy91.com/posts/autojs/)


使用autojs写脚本的时候，最需要的就是调试信息，不然无法知道出错的信息。一般打印日志的方法是log、print、console等。但在手机上如何显示呢。

下面的autojs命令代码支持autojs 4.1.0和auto.js pro7。

```javascript
// 会在手机显示一个控制台，打印的信息会在手机端显示（需要开启悬浮窗权限）
// autojs在手机端显示调试信息，也就是日志
console.show();
//autojs打印日志调试信息的各种方法
log("如何用autojs打印白色的日志");
print("这个日志也是白色的");
console.verbose("这个调试信息是灰色的");
console.info("autojs的日志变绿色了");
console.warn("蓝色的调试信息");
console.error("红色的调试信息");
//还支持吧日志信息输出到文件
console.setGlobalLogConfig({
    "file": "/sdcard/autojs-log.txt"
});
```

如果需要在auto.js连接电脑进行调试，请参考教程[Auto.js如何连接电脑上的VS Code插件](https://www.sxy91.com/posts/autojs/)


有疑问欢迎加入AutoJs的交流QQ群提问：`1003185728`。

参考文章

- [Auto.js自动打开QQ群的方法教程](https://www.sxy91.com/posts/autojs-qq-group/)