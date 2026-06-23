---
title: "PostgreSQL唯一约束冲突解决"
heading: "pg 遇到唯一性约束错误如何解决"
keywords: ["PostgreSQL唯一约束冲突", "duplicate key value", "pg_indexes查询", "数据库索引排查", "PostgreSQL错误解决"]
tags: ["PostgreSQL", "数据库", "错误排查"]
description: "PostgreSQL报错duplicate key value violates unique constraint时，通过查询pg_indexes系统表快速定位冲突索引和表的排查方法。"
categories: ["code"]
date: "2021-08-10T03:17:37.435Z"
---
报错信息
```
duplicate key value violates unique constraint "IDX_3bd1c1761646a6ec2a23c1bc11"
```

如何查是哪个表，建立的什么索引

```sql
select * from pg_indexes
WHERE indexname = 'IDX_3bd1c1761646a6ec2a23c1bc11';
```

结果如下
```sql
CREATE UNIQUE INDEX "IDX_3bd1c1761646a6ec2a23c1bc11" ON public.users USING btree (appid, openid, user_id)
```


