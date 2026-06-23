---
title: "InfluxDB+Grafana搭建监控系统"
heading: "使用InfluxDB和Grafana解决数据统计与服务器监控报警"
keywords: ["InfluxDB Grafana监控", "服务器监控报警", "Grafana数据统计", "时序数据可视化", "Grafana告警配置"]
tags: ["InfluxDB", "Grafana", "监控报警"]
description: "使用InfluxDB和Grafana搭建数据统计与服务器监控报警系统，解决99%的运维监控需求。"
categories: ["code"]
date: "2019-09-03T07:19:42.179Z"
draft: "true"
---
```sql
SELECT sum("sum_total") as "total" , sum("sum_repeat") as "repeat",  sum("sum_total") -  sum("sum_repeat")  as "unique"   FROM "sum_source_1h" where time > now() - 8d GROUP BY time(1d)  tz('Asia/Shanghai')
```