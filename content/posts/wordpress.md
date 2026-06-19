---
title: wordpress
heading:  在 debian 12 系统上安装 WordPress 7
date: 2026-06-15T06:38:08.050Z
tags: 
categories: ["code"]
Description:  基于 WordPress 7.0+woocommerce+Flatsome 搭建电商独立站，使用 API 管理商品。安装 WPML 实现多语言和多货币，以及 RanK Math SEO。
---

## 说明

想在测试环境 debian 12 安装一套 [WordPress](https://wordpress.org/download/) 环境，用于搭建 WooCommerce 独立站进行测试。

测试环境搭建完成后可安装插件 All-in-One WP Migration 然后导入到正式环境，避免重复搭建。 
```
测试环境搭建
↓
All-in-One WP Migration 导出
↓
购买 VPS
↓
安装 WordPress
↓
导入 .wpress
↓
修改域名
↓
上线
```

## 安装 WordPress

AI 时代，让 AI 来安装吧，方法（任选其一）：

1. 安装 opencode，让 opencode 安装。
2. 让 AI 生成一个 shell 安装脚本，如 [install_wp.sh](https://github.com/smile365/blog/blob/master/install_wp.sh)

```markdown
我需要在测试环境（debian 12）安装一套 nginx+php+mariadb+wordpress 的环境，帮我写一个 install_wp.sh 脚本。要求：

- 先检查相关服务是否安装，已安装则跳过，不要重复安装 ;
- 安装完一个服务后检查是否安装成功并显示当前安装的版本，如 nginx -V ;
- 帮我安装 wp-cli，并安装 WooCommerce ；
- 然后配置好相关配置文件，并汇总显示各个服务的版本号；
- 后期需要上传文件，请修改 Nginx 和 PHP 的上传限制，改成 64MB；
- 打印本机 ip 地址，以便我输入 ip 地址即可开始 WordPress 的安装；
```


##  配置 WooCommerce

WooCommerce 是一个插件，若脚本没安装 Woo 也可以在 WordPress 插件页面搜索 WooCommerce 进行安装，同时可安装 WooCommerce PayPal  Payments、WooCommerce Stripe Payments 两个收款插件。

安装完 Woo 后点击启用。

WordPress 7.0 默认主题为 Twenty Twenty-Five 不太适合电商独立站，推荐使用主题 [Flatsome](https://demos.flatsome.com/) ，购买后（$59）后上传 zip 主题文件，并安装。

 [flatsome 主题](https://themeforest.net/item/flatsome-multipurpose-responsive-woocommerce-theme/5484319)比较贵，前期可使用免费工具：
1. [Elementor](https://wordpress.org/plugins/elementor/) 拖拽式页面构建器，免费版功能就很强，模板丰富，WooCommerce 集成度极高。
2. [Gutenberg](https://wordpress.org/gutenberg/) 原生编辑器 – WordPress 自带，配合 [Kadence Blocks](https://wordpress.org/plugins/kadence-blocks/)、GenerateBlocks 等免费插件也能搭建不错页面。
3. [Kadence 主题](https://wordpress.org/themes/kadence/) + Kadence Blocks – 轻量且性能好，导入模板即可快速建店。


若上传文件遇到`413 Request Entity Too Large`错误时，需要更改配置:
1. nginx 需要在 server { ... } 块内添加一行 client_max_body_size，例如设为 64MB;
2.  php 也需要更改成类似如下值
```ini
;文件大小
upload_max_filesize = 64M
;同上
post_max_size = 64M
;处理时间（秒）
max_execution_time = 300
```

修改方法：
```
# 找到当前 PHP 版本的配置文件
php --ini | grep "Loaded Configuration File"
# 查看当前配置在哪几行（分别在 409、703、855 行）
grep -n "upload_max_filesize\|post_max_size\|max_execution_time" /etc/php/8.2/fpm/php.ini

vim +409 /etc/php/8.2/fpm/php.ini
# 修改后输入 :703 跳转到 703 行
# 输入 :wq! 保存
# 重启 php
systemctl restart php8.2-fpm
```


## 自定义主题

- 主页修改：Flatsome -> Theme Options -> Homepage 选择 Classic Shop 
- 取消顶部栏；
- 去掉 logo 改成文字标题；
- 账户去掉[下载](https://docs.uxthemes.com/article/203-how-to-remove-downloads-from-my-account)
- 在页面找到 Front Page（主页）使用 UX Builder 编辑成自己想要的布局 
- 主题选项 定制页脚，修改 Copyright 去掉主题申明 
- 产品页面，去掉分享到社交媒体
- 修改 Refund and Returns Policy （退款和退货政策）
- Privacy Policy  隐私政策页面



## 如何导入 etsy 商品到 Woo 独立站

假设你在其他电商平台有店铺，可导入商品数据。省去一个一个手动录入的繁琐。

### Etsy 导出数据

1. 登录您的 Etsy 卖家后台（Shop Manager）。
2. 点击左侧菜单栏的 Settings（设置） > Options（选项）。
3. 切换到顶部的 Download Data（下载数据） 标签页。
4. 在 Currently for Sale Listings（当前在售商品） 区域，点击 Download CSV（下载 CSV） 按钮。
5. 系统会自动下载一个包含您所有在售商品的 `.csv` 文件（内含标题、描述、价格、库存等信息）。


### 转换数据格式

各平台有自己的数据格式，导出后的 csv 一定**没法直接导入 Woo**。需要重新调整格式。
WooCommerce 导入格式参考：[Product CSV Import Schema](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Import-Schema#csv-columns-and-formatting)

导入 VARIATION、Categories 两列经常崩溃，无法完全导入，一般仅能导入 10 个以内。一个变体就需要创建一个 SKU 编号，因此导入非常缓慢。建议先导入标题、描述、价格、库存、图片，其余的属性手动调整。

1. 列映射：TITLE-->Name,DESCRIPTION-->Description,PRICE-->Regular price,QUANTITY-->Stock
2. 合并 IMAGE1\~10 → 单个 Images 列，逗号分隔 URL，加引号包裹
3. 添加 Published 列 — 全 1
4. 添加 In stock? 列 — QUANTITY > 0 时 1，否则 0
5. 以下列不建议自动导入
   1. 添加 Type 列 — 有颜色变体的行设 variable，无变体的设 simple
   2. 拆分变体行 — 每个有颜色变体的产品需拆为：1 行父产品 + N 行子变体（每个颜色一行），子行 Type=variation，Parent=父行 SKU
   3. VARIATION 列 → Attribute 列 — VARIATION 1 NAME → Attribute 1 name，VARIATION 1 VALUES → 父行 Attribute 1 value(s)（逗号分隔），子行 Attribute 1 value(s)（单个值）
   4. 补充 SKU — 当前全部为空，必须为每个产品生成唯一 SKU（父+子变体都要）
   5. 删除 TAGS、 CURRENCY\_CODE、MATERIALS列
6. 导入后手动调整 Categories、tags、Attribute


> 可以让 AI 写格脚本来转换，或者直接把 csv 文件发给 AI，输出成所需要的格式。


在 Products -> All Products -> Import 上传处理后的 csv 文件即可导入。 Woo 会从其他平台下载图片，若图片比较多可能耗时很久。


## 使用 API 导入

使用 csv 表格导入的商品数量超过 20 个几乎会失败， 稳妥的办法是使用 [WooCommerce REST API ](https://woocommerce.com/document/woocommerce-rest-api/) 进行导入。参考 Woo 的官方文档，在 WooCommerce > Settings > Advanced > REST API 创建一个可读写的 key。让后让 AI 把 csv 格式转换成 woo 格式并通过 api 导入。

> 若其他平台的店铺已经有评论，也可以通过 API 导入到 Woo 独立站



## 创建分类 Categories

删除 flatsome 创建的实例分类，按照自己所需创建（填写 Name、Description、Slug）。

- `Slug` 推荐全部字母小写，无空格，多个单词用短横"-"链接；
- `Description` 填写后会让描述在 Shop 页面也显示内容，暂时不填写；

> 同理，也可以让 AI 通过 API 创建分类。


## 多货币

在插件商城搜索 [Currency](https://wordpress.org/plugins/search/currency/) 可以找到很多类似 [Multi-Currency](https://woocommerce.com/document/multi-currency/) 这样适合 WooCommerce 的扩展程序，可实现货币切换和实时汇率重新计算。集成[MaxMind 地理位置](https://woocommerce.com/document/maxmind-geolocation-integration/)后，还能实现根据客户的地理位置实时计算汇率和现实当地货币的价格。免费版本 12 小时更新一次汇率，对于个人独立站足够使用。

> 大多数这类插件，如 [FOX – Currency](https://wordpress.org/plugins/woocommerce-currency-switcher/#description)、[CURCY](https://wordpress.org/plugins/woo-multi-currency/#description-header) 都是只能设置两个货币免费使用，超过两个的话就要付费，大约 $34~40 美金。

## 多语言

### 免费模式

实现多语言有两个方案，或者说两个场景。一个是客户端翻译、另一个是服务端翻译。客户端翻译插件大多数是免费的，提供几乎常见的语言。翻译后的内容是浏览器实时显示的，也就是说服务端不存储翻译后的内容。在 WordPress 插件页搜索 [google translate](https://wordpress.org/plugins/search/google+translate/) ，能找到很多类似 [GTranslate](https://wordpress.org/plugins/gtranslate/)、[Automatic Translator](https://wordpress.org/plugins/auto-translate/)  等免费的翻译的插件。优点是免费，缺点自然是无法实现 SEO，比如当用户使用另一个语言搜索关键词时，搜索引擎不会显示你的内容，即使你的内容与关键词非常匹配。

### 多语言SEO

为了实现存储翻译后内容，以便搜索引擎收录，就刷要类似 [WPML](https://wpml.org/zh-hans/account/downloads/) 、 [Polylang](https://wordpress.org/plugins/polylang/)这类的服务端翻译插件。这类差距提供了一套服务器端渲染的翻译系统，该系统应具备稳定的语言URL、规范化处理、hreflang属性、站点地图集成、翻译后的元数据和翻译后的别名。

若要翻译 Woo 之类电商属性的独立站，生态最好的翻译插件当属 [WPML](https://wpml.org/zh-hans/account/downloads/) ，它可以解决多语言和多货币的问题，就是订阅费有点小贵（59欧元/年），另外它的翻译是消耗积分的，购买 [WPML](https://wpml.org/zh-hans/documentation-4/%E9%80%9A%E8%BF%87wpml%E8%87%AA%E5%8A%A8%E7%BF%BB%E8%AF%91wordpress%E5%86%85%E5%AE%B9/%E8%87%AA%E5%8A%A8%E7%BF%BB%E8%AF%91%E5%AE%9A%E4%BB%B7/) 后，将获得  90,000 个免费翻译积分额度，基本能将大多数 WordPress 网站翻译成 2-3 种语言。

使用 OTGS Installer 可自动安装 WPML 插件，或者付费后可下载插件。

WPML 包含多个功能的插件包集合，手动下载后可按需安装以下插件包：

- WPML Multilingual CMS V4.9.5, 核心翻译插件
- String Translation v 3.5.3，核心翻译组件
- WPML Multilingual & Multicurrency for WooCommerce v 5.5.6，电商独立站 多语言+多货币支持。


其他相似插件：
- [TranslatePress](https://translatepress.com/pricing/) ：免费版本无需注册，但仅能翻译一种语言。免费注册后赠送 2000 个翻译积分。付费订阅费差不多也是 99 欧元/年，感觉没有 WPML 划算；
- [Polylang for WooCommerce ](https://polylang.pro/pricing/polylang-for-woocommerce/) ： 也是 99欧元/年；


## 数据统计

为了查看访客的数量、链接收录的数量以及后期 SEO 的相关数据，接入谷歌的服务会比较方便。

- 接入 [Google Search Console](https://search.google.com/search-console/about)
- 安装 [Google Site Kit ](https://sitekit.withgoogle.com/) 插件



## 总结

如果需要搭建一个完善的电商独立站，支持多语言 SEO 及多货币自动计算汇率等功能，成本大约 $200/首年，之后 $150/每年。



### 环境和版本

| 名称        | 版本     | 说明 |
| ----------- | -------- | ---- |
| debian      | 12       |      |
| WordPress   | 7.0      |      |
| MariaDB     | 10.11.14 |      |
| PHP         | 8.2.31   |      |
| WooCommerce | 10.8.1   |      |


### 用到的服务


| 名称                            | 价格       | 说明                                                   |
| ------------------------------- | ---------- | ------------------------------------------------------ |
| WordPress 托管                  | $3/月      |                                                        |
| Flatsome 主题                   | $59/一次性 |                                                        |
| WPML 插件                       | €99/年    | 让独立站支持多语言和多币种                             |
| Rank Math SEO 插件              | 免费版     |                                                        |
| Google for WooCommerce 插件     | -          | 把商品同步到谷歌，谷歌搜索时可现实商品价格、图片、描述 |
| WooCommerce Stripe Gateway 插件 | -          | 支付网关                                               |
| All-in-One WP Migration 插件    | 免费版     | 备份整个站点，方便迁移到正式环境。                     |
