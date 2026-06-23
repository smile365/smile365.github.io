---
title: "Conductor DAG 扩展改造"
keywords: ["Conductor DAG 限制", "Conductor 多起点工作流", "Netflix Conductor 改造", "DAG 工作流设计", "工作流对齐方案"]
tags: ["Conductor", "DAG", "工作流改造"]
description: "Netflix Conductor对DAG的支持有限，仅支持单起点单终点的对称结构，本文探讨通过拆分流程和队列方案实现多起点工作流的设计思路。"
categories: ["code"]
date: "2023-03-17T11:01:57.751Z"
---
虽然 conductor 能满足部分常见的业务场景，但因为 conductor 对 DAG 的支持有限。conductor 虽然支持 fork 、join、sub 等任务，但本质上仅支持一个节点开始，到一个节点结束。像下面的工作流 conductor 就无法实现了：
![enter description here](https://cdn.sxy21.cn/static/imgs/1679052871062.png)


更不要说多个开始节点，和多个结束节点，类似下面的图 conductor 更是没辙。

![enter description here](https://cdn.sxy21.cn/static/imgs/1679052943181.png)



conductor 的 DAG 图是一种只有一个起点和一个终点的对称的结构。


先简单考虑一种情况，如果基于 conductor 是否可以实现有两个起点，一个终点呢？

![enter description here](https://cdn.sxy21.cn/static/imgs/1679053117420.png)

假设 code 和 code3 都是由外部事件触发的，什么时候执行不知道。compression1 需要等 code1 和 code2 都执行完才往后执行。

方案一：划分成单独的流 然后使用 startWorkflow 任务启动流

![enter description here](https://cdn.sxy21.cn/static/imgs/1679053323304.png)
先拆分成三个流程，在流程 1 和流程 2 的结束增加一个自定义 task，用来判断流程 1 和流程 2 是否都执行完成。若都执行完成则启动流程 3，否则不执行任何操作。


思路似乎行得通，但是会涉及一个对齐问题。究竟是流程的实例对齐，还是流程本身对齐？

如果是实例级别对齐，相当于流程 1 每执行一次，都需要流程 2 执行一次才能执行流程 3（流程 2 也如此）。因为触发流程 1 和流程 2 的频率不一致，比如流程 1 每隔 1 分钟触发一次，流程 2 每隔 1 小时执行一次，会造成很多问题：
1. 会造成流程 1 阻塞，且阻塞的越来越多，极端一点（或者遇到黑客）会把服务器撑爆。
2. 流程 3 得到的数据缺乏实效性，流程 2 是最新的，但流程 1 是几天前的。这种情况显然不符合业务需求。

如果改成流程级别对齐呢？假设流程三永远取的是流程 1 和流程 2 最新的数据。怎么实现呢？

设计一个容量为 1 的队列（假设名称为 workflow_group_a），流程 1 和流程 2 每次执行结束都把执行的结果存入这个队列。具体实现其实用 redis 的 hash 其实就可以，field 用流程的名称 value 为当前流程的结果。

此时又面临一个问题，流程 3 往后执行的时候要不要清空 workflow_group_a 的数据？这个可能就得根据业务需求来。如果清空，那么流程 3 有可能得到的数据就会慢一个节拍。


| 1         | 2         | 3         | 4         | 5         |
| --------- | --------- | --------- | --------- | --------- |
|           | workflow1 |           | workflow1 |           |
| workflow2 |           | workflow2 |           | workflow2 |
在 2 结束的时候是 workflow2 和 workflow1 的数据。此时有两种情况。情况 1： 清空数据，那么在 3 结束的时候只有 workflow2，需要等到 4 才能触发流程 3。情况 2：不清空数据，那么在 3 结束的时候，有 workflow1 和 workflow2 可直接触发流程 3。








