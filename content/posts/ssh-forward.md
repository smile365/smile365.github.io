---
title: "ssh-forward 端口转发"
heading: 
date: 2022-07-22T11:53:10.123Z
categories: ["code"]
tags: 
description: 
---
## SSH Port Forwarding

**SSH 端口转发**（SSH Port Forwarding），也叫 SSH 隧道（SSH Tunnel），是利用 SSH 协议建立的安全通道，将网络流量从一个端口“转发”到另一个端口或主机上。

**主要用途:**

- 加密原本明文的协议（如 Telnet、FTP、数据库连接）
- 绕过防火墙限制（如访问公司内网服务）
- 安全地暴露内网服务到外部（如微信本地调试）
- 作为 SOCKS 代理使用


## 本地端口转发（Local Forwarding）

即把本地端口通过 SSH 隧道转发到目标端口，命令为：

`-L [本地地址:]本地端口:目标主机:目标端口`

**数据流向**：
```
你的应用 → 本地端口 → SSH客户端加密 → SSH服务器解密 → 目标主机:目标端口
```

**场景**：比如远程服务器 sxy91.com 上安装了 mysql，但仅绑定了 localhost，只允许本机访问。若想调试，自己笔记本电脑无法连接到数据库，不方便调试。可使用如下命令解决：

**示例**：
```bash
# macbook 执行
ssh -L 3306:localhost:3306 root@ssh服务器
```
此时在笔记本电脑上打开 Navicat\DBeaver\DataGrip 等工具，host 写 127.0.0.1  其余照常填写即可连接到 ssh 服务器的 mysql 数据库。


### 静默转发

默认情况下 SSH 在建立隧道后会启动一个登录 shell（交互式会话）。如果只想让隧道在后台静默运行，不显示远程的终端也不需要执行任何远程命令，可以加上 **`-N`** 参数。

```bash
ssh -N -L 3306:localhost:3306 root@ssh服务器
```

- **`-N`**：告诉 SSH 不要执行远程命令（即不分配 shell、不启动任何程序）。此时 SSH 仅用于端口转发，连接建立后不会出现登录提示或命令行。

- 键入 ctrl+c 即可终止转发


### 后台转发

也可以在后面加 **`-f`** 让 SSH 在后台运行：

  ```bash
  ssh -f -N -L 3306:localhost:3306 root@ssh服务器
  ```
  
这样隧道会在后台静默维持，不会占用当前终端。如需终止转发，可以使用命令`pkill -f "ssh -f -N -L 3306:localhost:3306"`


### 配置文件转发（./ssh/cnofig）
如果转发的规则比较复杂，或者需要转发多个端口，每次敲击命令都比较麻烦，可以通过 ssh 的配置文件 ./ssh/cnofig 配制好转发规则，下次直接 ssh  test 即可。
```
Host test
    HostName 47.92.33.201
    User root
	Port 4422
    LocalForward 15432 127.0.0.1:15432
    LocalForward 16379 127.0.0.1:6379
    LocalForward 6379 sxy.redisrds.aliyuncs.com:6379
	IdentityFile ~/.ssh/id_rsa
```

## 远程端口转发（Remote Forwarding）
`-R [远程地址:]远程端口:本地主机:本地端口`

**场景**：你想让别人（或自己从外部）访问你本地的一个服务，但你没有公网 IP，而 SSH 服务器有公网 IP。

**数据流向**：
```
外部用户 → SSH服务器:远程端口 → SSH服务器加密 → 你的SSH客户端解密 → 本地主机:本地端口
```

**示例**：
```bash
ssh -R 2222:localhost:22 user@公网服务器
```
别人在公网服务器上执行 `ssh -p 2222 localhost` 就能 SSH 到你的内网机器。

### 3. 动态端口转发（Dynamic Forwarding, SOCKS）
`-D [本地地址:]本地端口`

**场景**：你想要一个加密的通用代理，浏览器或应用配置 SOCKS5 代理后，可以访问 SSH 服务器能访问的任何地址。

**数据流向**：
```
应用(配置SOCKS) → 本地端口 → SSH客户端加密 → SSH服务器解密 → 目标地址:目标端口（由应用指定）
```

**示例**：
```bash
ssh -D 1080 user@ssh服务器
```
浏览器设置 SOCKS5 代理 `localhost:1080`，所有流量通过 SSH 服务器转发。

---

## 总结

数据原理图： 
```
[你的PC]  ----(SSH加密通道)--->  [SSH服务器]  ----(明文或任意的)---->  [目标服务]
   ↑                                        ↑
本地监听端口                           能访问目标服务的网络
```

- **本地转发**：服务器是“跳板”，帮你去访问别的机器。
- **远程转发**：你的 PC 是“服务提供方”，服务器帮你把流量引回来。
- **动态转发**：目标地址由应用每次动态指定，SSH 服务器作为通用代理。

**注意事项： **

1. **SSH 连接中断，转发就失效**（可用 autossh 保持）。
2. **默认只能绑定本地端口**，绑定 0.0.0.0 需要在服务器配置 `GatewayPorts yes`（安全性降低）。
3. **只支持 TCP 协议**，无法直接转发 UDP（但可用某些工具间接实现）。
4. **性能受 SSH 加密和单连接限制**，不适合高吞吐量场景。






**参考文档：**  
- [什么是 SSH 端口转发](https://www.ssh.com/academy/ssh/tunneling/example)
- [实战 ssh 转发](https://blog.csdn.net/randyleonard/article/details/9049335)
- [SSH 隧道的反向端口转发](https://zhuanlan.zhihu.com/p/438009437)
- [轻松实现 SSH 反向隧道](https://cloud.tencent.com/developer/article/1528395)
- [SSH 反向代理和端口转发](https://www.jianshu.com/p/dafbbbe4c43b)
- [SSH/OpenSSH/PortForwarding](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding)
- [SSH Tunneling (Port Forwarding)](https://linuxize.com/post/how-to-setup-ssh-tunneling/)
- [ssh-port-forwarding](https://phoenixnap.com/kb/ssh-port-forwarding)
