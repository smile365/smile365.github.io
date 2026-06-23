---
title: "PostgreSQL 新手入门教程"
keywords: ["PostgreSQL 安装", "CentOS 7 PostgreSQL", "PostgreSQL 教程", "psql 使用", "数据库入门"]
tags: ["PostgreSQL", "教程", "CentOS"]
description: "在 CentOS 7 上通过 RPM 包安装 PostgreSQL 11，配置远程访问并导入千万级测试数据的完整教程。"
categories: ["code"]
date: "2019-06-04T08:13:00.474Z"
---
使用[官网的rpm](https://www.postgresql.org/download/linux/redhat/)包在centos7下安装PostgreSQL 11
```shell
yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum -y install postgresql11-server
/usr/pgsql-11/bin/postgresql-11-setup initdb
systemctl enable postgresql-11
systemctl start postgresql-11
sudo -u postgres psql -c "SELECT version();"
```

创建角色和数据库: `sudo -u postgres psql`  
```sql
CREATE ROLE sxy LOGIN PASSWORD 'sxy';
create database sxydb;
grant all privileges on database sxydb to sxy;
```

开启远程访问和登录方式 
```bash
#允许所有内网网段通过密码方式登录数据库
echo -e "host \t all \t all \t 192.168.31.0/24 \t md5" >> /var/lib/pgsql/11/data/pg_hba.conf
echo "listen_addresses = '*'" >> /var/lib/pgsql/11/data/postgresql.conf
sudo systemctl restart postgresql-11
psql -h 127.0.0.1 -d sxydb -U sxy -W
```

> 登录方式可参考：[pg_hba.conf](https://www.postgresql.org/docs/9.3/auth-pg-hba-conf.html) 
若提示`psql: could not connect to server: 拒绝连接
	Is the server running on host "xxx" and accepting
	TCP/IP connections on port 30000?`
  可使用`p`参数指定端口：`psql -h 127.0.0.1 -p 5432 -d sxydb -U sxy -W `
  

导入某2千万数据测试
```sql
CREATE TABLE persons
(
  Name character varying(50),
  CtfId character varying(18),
  Gender character varying(50),
  Address character varying(100),
  Mobile character varying(50),
  Tel character varying(50),
  EMail character varying(50),
  Nation character varying(50)
);
\COPY persons FROM '/home/persons.csv' DELIMITER ',' CSV HEADER;
```

32G内存8核cpu，建议修改[postgresql.conf](https://github.com/digoal/blog/blob/master/201611/20161121_01.md)的如下配置项  `vim /var/lib/pgsql/11/data/postgresql.conf`
```