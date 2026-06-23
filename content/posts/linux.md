---
title: "Linux常用命令"
keywords: ["Linux命令大全", "tr命令替换", "grep正则匹配", "awk处理JSON", "jq命令行查询"]
tags: ["Linux", "命令", "shell"]
description: "收集Linux日常使用中的高频命令技巧，包括tr替换字符、grep匹配进程、awk提取JSON字段和sed定位行号等实用Shell方法。"
categories: ["code"]
date: "2019-05-19T13:28:17.845Z"
---
## tr 命令
tr命令 可以对来自标准输入的字符进行替换、压缩和删除。它可以将一组字符变成另一组字符。
1. 去除空格
```
# tr -d " "
echo "www sxy com" | tr -d " "
```


**使用grep匹配杀死多个进程**
```bash
kill $(ps aux | grep 'myapp.py' | awk '{print $2}')
```


**查看Linux发行版信息**
ls /etc/*release

**利用grep/awk/sed命令提取特定内容**

打`uid`所在的行号

`sed -n  -e '/uid/=' book.json`

统计文件的行数

`wc -l book.txt`

文件内容为一行一个json，把`user`下的`uid`提取到另一个文件

`awk '{ print $0 }' book.json | ./jq.sh -r '.user.uid' > book-uid.txt`

如果json文件不是严格正确的则

```bash
grep -o 'uid": "[0-9]*' book.json | awk -F'"' {'print $3'} > book-uid.txt
```


参考  

- [awk-filter](https://www.tecmint.com/use-linux-awk-command-to-filter-text-string-in-files/)
- [类似于sed的json行编辑器](https://stedolan.github.io/jq/)
- [使用正则匹配杀死多个进程](https://stackoverflow.com/questions/3510673/find-and-kill-a-process-in-one-line-using-bash-and-regex/3510850#3510850)