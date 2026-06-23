---
title: "Docker安装Kibana教程"
heading: "Docker安装Kibana并配置Elasticsearch密码"
keywords: ["Kibana Docker安装", "Kibana配置Elasticsearch", "Elasticsearch密码配置", "Kibana容器部署", "ELK安装教程"]
tags: ["Kibana", "Elasticsearch", "Docker"]
description: "使用Docker快速安装Kibana并配置Elasticsearch访问密码，搭建ELK日志分析平台的完整步骤。"
categories: ["code"]
date: "2022-07-22T10:31:21.628Z"
---
```bash
docker pull kibana:7.7.0
docker run -d --name kibana -p 5601:5601 kibana:7.7.0

#进入es容器内部
docker exec -it kibana /bin/bash
#修改es配置文件kibana.yml
vi /usr/share/kibana/config/kibana.yml
#添加以下内容
elasticsearch.username: "kibana"
elasticsearch.password: "*****"
#保存后退出docker容器
exit
#重启kibana
docker restart kibana
```





参考
- [kibana配置elasticsearch密码](https://blog.csdn.net/IT_road_qxc/article/details/121858843)