---
title: "搭建K8s集群"
keywords: ["K8s搭建", "Kubernetes安装", "KubeSphere教程", "CentOS K8s集群", "KubeKey"]
tags: ["Kubernetes", "K8s", "KubeSphere", "容器化"]
description: "使用KubeKey在CentOS上快速搭建Kubernetes集群和KubeSphere的详细步骤。"
categories: ["code"]
date: "2022-10-27T02:16:05.490Z"
---
1. 使用清华源
```bash
# 备份
cp -r /etc/yum.repos.d /etc/yum.repos.bak
# 对于 CentOS 8
sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
         -e 's|^#baseurl=http://mirror.centos.org/$contentdir|baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos|g' \
         -i.bak \
         /etc/yum.repos.d/CentOS-*.repo
```

2. 使用 [kubesphere](https://kubesphere.io/zh/docs/quick-start/all-in-one-on-linux/) 的 kk 安装 kubernetes
```bash
yum install -y socat conntrack ebtables ipset
export KKZONE=cn
curl -sfL https://get-kk.kubesphere.io | VERSION=v2.2.2 sh 
# -s 不显示进度信息，silent
# -f 不显示错误信息，fail
# -L 相当于自动 302 跳转，location 
./kk create cluster --with-kubernetes v1.22.10 --with-kubesphere v3.3.0 --container-manager containerd -y
# 检测安装
kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l 'app in (ks-install, ks-installer)' -o jsonpath='{.items[0].metadata.name}') -f
```





