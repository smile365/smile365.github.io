---
title: "Auto.js获取设备信息"
keywords: ["Auto.js获取设备信息", "Auto.js获取包名", "安卓自动化脚本", "Auto.js device", "Auto.js教程"]
tags: ["Auto.js", "Android", "设备信息"]
description: "介绍Auto.js中获取手机硬件设备信息和已安装应用包名的JavaScript代码示例，包括device属性和PackageManager用法。"
categories: ["code"]
date: "2020-05-08T06:54:02.091Z"
---
获取包名、设备信息等。

```javascript
log("device:"+device.device);
log("model:"+device.model);  // MI 8
log("product:"+device.product);
log("bootloader:"+device.bootloader);
log("serial:"+device.serial);
log("sdkInt:"+device.sdkInt); // 28 = sdk 28
log("release:"+device.release); // 9 = Android 9
log("baseOS:"+device.baseOS);

function getInstallAppInfo(){
    let app_infos = context.getPackageManager().getInstalledPackages(0).toArray();
    for (let i = 0; i < app_infos.length; i++) {
        let item = app_infos[i];
        log(item.versionCode);
        log(item.packageName);
        log(item.applicationInfo.label);
        // packageName/versionName/versionCode/firstInstallTime/lastUpdateTime/longVersionCode/applicationInfo
    }
}

getInstallAppInfo();

// 14:52:40.473/D: device:dipper
// 14:52:40.473/D: model:MI 8
// 14:52:40.474/D: serial:unknown
// 14:52:40.473/D: product:dipper
// 14:52:40.474/D: sdkInt:28
// 14:52:40.475/D: baseOS:
// 14:52:40.474/D: bootloader:unknown
// 14:52:40.474/D: release:9
```