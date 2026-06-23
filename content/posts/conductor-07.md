---
title: "Conductor Fork & Join"
keywords: ["Conductor Fork Join", "Netflix Conductor 并行任务", "DAG 并行工作流", "Conductor 工作流定义", "微服务并行编排"]
tags: ["Conductor", "Fork", "Join"]
description: "Netflix Conductor支持Fork和Join任务实现工作流的并行执行，本文通过短信、邮件和HTTP通知的实例详解配置方法。"
categories: ["code"]
date: "2023-03-17T08:13:23.993Z"
---
## conductor 支持 fork and join 工作流

假设执行问 sms 通知后，并行执行 email 通知和 http 通知

```bash
{
  "name": "notification_in_parallel",
  "description": "notification in parallel",
  "version": 1,
  "schemaVersion": 2,
  "ownerEmail": "me@sxy21.cn",
  "tasks": [
    {
      "name": "sms_notification",
      "inputParameters": {},
      "taskReferenceName": "sms_notification",
      "type": "SIMPLE"
    },
   {
    "name": "fork_join",
    "taskReferenceName": "my_fork_join_ref",
    "type": "FORK_JOIN",
    "inputParameters": {},
    "forkTasks": [
      [
        {
          "name": "email_notification",
          "taskReferenceName": "email_notification_ref",
          "type": "SIMPLE"
        }
      ],
      [
        {
          "name": "http_notification",
          "taskReferenceName": "http_notification_ref",
          "type": "SIMPLE"
        }
      ]
    ]
  }
  ]
}
```

fork 类型的任务必须有 join 任务，否则会报错：
```prolog
Fork task definition is not followed by a join task. Check the blueprint
```

在 fork_join 任务之后再增加一个 join 类型的任务即可，找到 xx ，重新恭喜工作流的定义即可。
```json