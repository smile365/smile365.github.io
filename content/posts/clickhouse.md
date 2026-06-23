---
title: "ClickHouse 入门教程"
keywords: ["ClickHouse 安装", "ClickHouse 配置", "ClickHouse 入门", "列式数据库", "OLAP 数据库"]
tags: ["ClickHouse", "数据库", "OLAP"]
description: "ClickHouse是一个开源列式数据库，本教程详细介绍在CentOS 7上安装配置ClickHouse的完整步骤及基础使用方法。"
heading: "ClickHouse 入门教程：安装配置与性能测试"
categories: ["code"]
date: "2020-03-12T03:06:50.536Z"
---
ClickHouse 是一个开源列式数据库，由俄罗斯排名第一的搜索引擎公司 Yandex 开发，主要用于线上分析处理（OLAP）。该系统允许分析实时更新的数据，以高性能著称。ClickHouse 官网地址：[clickhouse.tech](https://clickhouse.tech)

ClickHouse 的主键不具有唯一性，其使用场景比较适合在并发低，需要实时分析大规模数据的业务场景中。

在 centos 7 安装 ClickHouse 过程如下：

`CentOS 7`换成[清华的镜像](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)或者[阿里云的镜像](https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.3e221b11XBR0VU)

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
sed -i -e '/mirrors.cloud.aliyuncs.com/d' -e '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/CentOS-Base.repo
sed -i -e '/mirrors.cloud.aliyuncs.com/d' -e '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/CentOS-Base.repo
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
yum makecache
```

> 若出现`Couldn't resolve host 'mirrors.cloud.aliyuncs.com'`、`Could not resolve host: mirrors.aliyun.com; 未知的错误`、`Could not resolve host: mirrors.tuna.tsinghua.edu.cn; 未知的错误`等，运行`echo "nameserver 8.8.8.8" >> /etc/resolv.conf` 即可。


安装 [ClickHouse](https://clickhouse.tech/#quick-start)
```bash
yum install -y yum-utils
rpm --import https://repo.yandex.ru/clickhouse/CLICKHOUSE-KEY.GPG
yum-config-manager --add-repo https://repo.yandex.ru/clickhouse/rpm/stable/x86_64
yum install -y clickhouse-server clickhouse-client

```

修改[服务器配置项](https://clickhouse.tech/docs/en/operations/server_settings/settings/#server_settings-listen_host)，监听内网ip和配置数据目录。
`vim /etc/clickhouse-server/config.xml`
```xml
<listen_host>192.168.1.135</listen_host>
<path>/var/lib/clickhouse/</path>
<tmp_path>/var/lib/clickhouse/tmp/</tmp_path>
```

修改[用户配置项](https://clickhouse.tech/docs/en/operations/settings/query_complexity/#settings_max_memory_usage),调整可用最大内存。
`vim /etc/clickhouse-server/users.xml`
```xml
<max_memory_usage>20000000000</max_memory_usage>
```

启动服务器和客户端
```bash
systemctl start clickhouse-server
clickhouse-client -h 192.168.1.135

# 如果开启远程连接
# 防火墙打开端口
firewall-cmd --add-port=9000/tcp
