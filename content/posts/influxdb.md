---
title: "InfluxDB安装与使用教程"
heading: "InfluxDB时序数据库从安装到Python操作完整教程"
keywords: ["InfluxDB安装教程", "InfluxDB使用入门", "时序数据库教程", "InfluxDB Python操作", "InfluxDB SQL查询"]
tags: ["InfluxDB", "时序数据库", "教程"]
description: "从安装到使用的InfluxDB时序数据库完整教程，涵盖数据库创建、保留策略、连续查询和Python集成操作。"
categories: ["code"]
date: "2019-08-27T07:56:11.769Z"
---
使用[influxdata](https://docs.influxdata.com/influxdb/v1.7/introduction/installation/)的源进行安装

```shell
cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF

yum -y install influxdb
systemctl start influxdb
# 进入infulx
influx -precision rfc3339
```

创建数据库

```sql

#创建数据库
create database "sxydata"

-- 建立一个保留时间1周的默认数据保留策略（RP）
CREATE RETENTION POLICY "seven_days" ON "sxydata" DURATION 1w REPLICATION 1 DEFAULT

-- 建立一个保留时间4周的数据保留策略
CREATE RETENTION POLICY "one_month" ON "sxydata" DURATION 4w REPLICATION 1 


-- 连续查询（CQ）聚合1小时的数据,使用默认RP
CREATE CONTINUOUS QUERY "cq_Adata_1h" ON "sxydata"
BEGIN
  SELECT sum(*) INTO "Adata_1h" FROM "Adata" GROUP BY *,time(1h) tz('Asia/Shanghai')
END

-- CQ连续查询 聚合1天的数据，使用one_month的RP
CREATE CONTINUOUS QUERY "cq_1day" ON "sxydata"
BEGIN
  SELECT sum("sum_repeat") as "repeat",sum("sum_total") as "total" INTO "sxydata"."one_month"."sum_1day" FROM "sum_source_1h" GROUP BY *,time(1d) tz('Asia/Shanghai')
END

-- 查看连续查询
SHOW CONTINUOUS QUERIES

-- 删除连续查询
DROP CONTINUOUS QUERY "cq_sum_1h" ON "sxydata"

-- 查看measurements(类似于表)