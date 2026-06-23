---
title: "Netflix Conductor 教程"
keywords: ["Netflix Conductor", "微服务编排引擎", "工作流引擎", "Conductor 教程", "DAG工作流"]
tags: ["微服务", "Conductor", "工作流", "编排引擎"]
description: "Netflix Conductor 微服务编排引擎的使用教程，涵盖工作流定义、任务编排、Worker 实现及 Docker 部署。"
categories: ["code"]
heading: "Netflix-Conductor 微服务编排引擎使用教程"
date: "2023-01-09T09:16:21.901Z"
---
## 相关组件

- Elasticsearch
- Conductor Server
- Conductor UI （可选）
- Redis （可选）
- PostgreSQL （可选）

参考 [概述](https://conductor.netflix.com/devguide/running/docker.html#alternative-persistence-engines)

## 本地运行


## docker 运行
参考 [官方文档](https://conductor.netflix.com/gettingstarted/docker.html)

端口
- 8080，API 界面，/swagger-ui/index.html  查看 api
- 5000， UI 界面。


## 使用 Conductor

1. 定义任务

2. 定义工作流（编排任务）
 把一堆任务按照 DAG 组成一个工作流

3. 启动工作流

4. 实现 worker


### 系统任务

### 自定义任务
自定义任务（[Worker Tasks](https://conductor.netflix.com/how-tos/Workers/build-a-java-task-worker.html)）由应用程序实现，并在与 Conductor 不同的环境中运行。工作线程任务可以用任何语言实现。这些任务通过 REST/gRPC 与指挥服务器通信，以轮询任务并在执行后更新其状态。

使用 Clojure、C#、Go、Java、Python 的 [Conductor SDK](https://conductor.netflix.com/gettingstarted/client.html)可以开发的自己 worker，实现注册/更新工作流和任务定义、启动新工作流、获取工作流的执行状态、轮询任务、执行后更新任务结果、获取任务状等。


## 参考文档 
- [Netflix Conductor 入门 Example](https://www.jianshu.com/p/d30dbc681a11)
- [conductor-github](https://github.com/Netflix/conductor)
- [conductor-doc](https://conductor.netflix.com/gettingstarted/local.html)
- [DAG](https://conductor.netflix.com/reference-docs/directed-acyclic-graph.html)
- [conductor-api](https://conductor.netflix.com/apispec.html)
- [工作流引擎对比](https://www.jdon.com/workflow/Airflow-vs-Azkaban-vs-Conductor-vs-Oozie-vs-Amazon-Step-Functions.html)
