---
title: "好玩的免费API接口推荐"
heading: "有哪些好玩的免费API接口及创意编程项目思路"
keywords: ["免费API接口推荐", "Golang截屏API", "OCR文字识别API", "API创意项目", "邮箱发送API"]
tags: ["API", "Golang", "创意编程"]
description: "分享好玩的免费API接口及创意编程项目思路，用Golang截屏结合OCR文字识别自动发送唯美壁纸到邮箱。"
categories: ["code"]
date: "2021-03-11T03:42:43.170Z"
---
你缺的不是接口，而是一个好玩的 idea 。

来，出个考题。

假设只用这两个接口
- 发送邮箱接口
- 文本识别接口

能做出什么好玩的东西？

女朋友是文青，喜欢唯美的句子和壁纸。

刚好有一台闲置的 Windows ，锁屏后会自动播放锁屏画报。类似于这样：
![](https://gitee.com/smile365/blogimg/raw/master/sxy91/1615436033621.png)

能不能写个程序，每天截一张图用邮箱发给她呢？

来用 golang 语言,几行代码搞定截屏
```golang
func Capture2base64() string{
    rect := screenshot.GetDisplayBounds(0)
    if *scale != 1 {
        rect.Max = rect.Max.Mul(*scale)
    }

    var img image.Image
    img, err := screenshot.CaptureRect(rect)
    if err != nil {
        fmt.Printf("failed to capture display: %v\n", err)
        return ""
    }
    if *scale != 1 {
        img = resize.Resize(uint(img.Bounds().Dx()/(*scale)), 0, img, resize.Lanczos3)
    }

    buf := new(bytes.Buffer)
    err = jpeg.Encode(buf, img, nil)
    return base64.StdEncoding.EncodeToString(buf.Bytes())

}
```

对于一个追求完美的人，只发图片没有图上的文案怎么能行。

用文字识别 api 把唯美的句子提取出来，调用 api 这种事，Python 擅长：
```python
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

def request(url, data):
    ''' 调用 OCR  api 
    '''