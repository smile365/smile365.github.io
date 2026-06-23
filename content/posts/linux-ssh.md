---
title: "免密登录Linux主机"
keywords: ["SSH免密登录", "Linux服务器远程连接", "SSH密钥配置", "Ed25519", "ssh-keygen教程"]
tags: ["SSH", "Linux", "密钥登录"]
description: "详细讲解如何配置SSH免密登录Linux服务器，对比RSA、DSA、ECDSA和Ed25519四种密钥算法的安全性与推荐度。"
categories: ["code"]
date: "2018-07-30T09:19:48.400Z"
---
## 安装 sshd
```
yum install -y openssl openssh-server

vi /etc/ssh/sshd_config
Port 22
PermitRootLogin yes

启动ssh服务
systemctl start sshd.service

重启网络
service network restart

设置开机启动ssh服务
systemctl enable sshd.service
```

每次在终端使用ssh链接服务器，需要输入账号、密码、端口、域名等一大堆东西，比较繁琐。若不想输入密码端口等信息，可以使用 ssh 密钥方式连接服务器。


假设Linux服务器的ip为：192.168.1.2,ssh端口：3322，以下以mac操作为例。


## 四种不同的密钥加密算法

| 文件名 | 算法类型 | 说明与推荐度 |
|--------|----------|--------------|
| `~/.ssh/id_rsa` | **RSA** | 最经典、兼容性最好。但安全性依赖密钥长度（建议≥3072位），且密钥生成和签名速度较慢。**仍可用，但已非首选**。 |
| `~/.ssh/id_dsa` | **DSA** | 老旧算法，**已被 OpenSSH 7.0+ 默认禁用**（因固定 1024 位不安全）。**不建议使用**，仅出现在历史遗留系统中。 |
| `~/.ssh/id_ecdsa` | **ECDSA** | 基于椭圆曲线，速度比 RSA 快，密钥更短。安全性依赖于所选曲线和系统随机数质量。**可用，但部分发行版/硬件支持略逊于 Ed25519**。 |
| `~/.ssh/id_ed25519` | **Ed25519** | 现代、安全、高性能的椭圆曲线算法。密钥极小，签名/验证极快。**目前最佳推荐**，所有主流系统均已支持。 |

### 核心差异总结
- **安全性排名**（高到低）：`Ed25519` ≈ `RSA(4096位)` > `ECDSA` > `RSA(2048位)` ≫ `DSA`  
- **兼容性**：`RSA` 兼容最广（老旧设备），`Ed25519` 在 2014 年后的系统普遍支持。  
- **使用建议**：**优先生成 `ed25519` 密钥**，若目标服务器极旧（如 RHEL 6）可备选 `rsa`。

### 与免密登录的关联
- 这些 `.ssh/id_xxx` 文件是**私钥**（需严格保密，权限 `600`），对应的 `.pub` 文件是**公钥**（需放到服务器 `authorized_keys`）。  



## 生成公钥和私钥

使用[ssh-keygen](https://blog.csdn.net/u013227473/article/details/78989041)生成密钥：`ssh-keygen -f ~/.ssh/id_rsa_sxy`
> 可以使用 -C 添加注释，如： `ssh-keygen -f ~/.ssh/id_rsa_sxy -C "sxy21cn@qq.com" `

```bash
ssh-keygen -t ed25519 -C "你的备注（如邮箱）"
```