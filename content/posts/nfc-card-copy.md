---
title: "门禁卡复制教程"
keywords: ["NFC门禁卡复制", "MifareClassicTool", "UID卡复制", "门禁卡模拟", "NFC复制"]
tags: ["NFC", "门禁卡", "Mifare"]
description: "使用安卓手机和 MifareClassicTool 复制门禁卡的详细步骤，包括密钥文件编辑和 UID 写入操作。"
categories: ["code"]
date: "2022-01-06T12:45:14.795Z"
---
手机打开 nfc 开关

下载软件[MifareClassicTool](https://xiakele.lanzouq.com/i67Ccygn7rc)

点击编辑/新建密钥文件,右上角加号,随便起个名字如：my.key

粘贴下面的内容
```bash
# chuncheng-360b4cfe-key
E4C2245A84AA
# defulat key
ffffffffffff
# others 
```

参考文档 

- [安卓手机NFC模拟门禁卡（设置UID）的一种方法](https://cloud.tencent.com/developer/article/1423314)
- [高通 NXP NFC（PN547PN548） 移植流程 android6.0](https://cloud.tencent.com/developer/article/1351970)
- [修改手机的UID模拟门禁卡](https://www.jianshu.com/p/763662e8f104)
- 