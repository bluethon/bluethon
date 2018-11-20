Kubernetes Note
===============

URL
---

[GCR 同步仓库](https://github.com/mritd/gcr)
[kubenetes-tools 一些工具](https://github.com/openthings/kubernetes-tools)
[kubenetes一键脚本](https://github.com/cookcodeblog/k8s-deploy)

TODO
----

``` sh
kubeadm token list
kubeadm token generate --print-join-command
kubectl get nodes
kubectl get pod --all-namespaces
# 带ip
kubectl get pod --all-namespaces -o wide
kubectl describe pod kube-flannel-ds-v0p3x --namespace=kube-system
sudo systemctl status kubelet.service
kubectl run httpd-app --image=httpd --replicas=2
kubectl get deployments
kubectl get pod -o wide
kubectl describe deployments.apps nginx-deployment
kubectl get replicasets
kubectl describe replicasets.apps nginx-deployment-d4597f7d4
kubectl describe pods
kubectl delete deployments.apps nginx-deployment
kubectl delete -f nginx.yml
# 使master也可当做Node使用
kubectl taint node k8s-master node-role.kubernetes.io/master-
# 恢复
kubectl taint node k8s-master node-role.kubernetes.io/master="":NoSchedule
kubectl get nodes --show-labels
# 编辑/查看DaemonSet
kubectl edit daemonsets.extensions --namespace kube-system kube-proxy
```

- k8s的系统组件在`kubu-system`namespace中
- kubulet是唯一不在容器中的组件, Ubuntu中通过systemd运行

CMD
---

``` shell
# 列出依赖包版本
# https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#running-kubeadm-without-an-internet-connection
kubeadm config images list
```

Note
----

### init config

> <https://godoc.org/k8s.io/kubernetes/cmd/kubeadm/app/apis/kubeadm/v1alpha3>

Install
-------

``` sh
curl -fsSL https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -
cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb [arch=amd64] https://mirrors.ustc.edu.cn/kubernetes/apt kubernetes-xenial main
EOF
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

# https://serverfault.com/a/684792/380738
cat /proc/swaps
sudo swapoff -a
sudo vim /etc/fstab
# comment swap line
```

Upgrade
-------

### Upgrade the control plane

``` sh
sudo apt update
# 必须指定名称, 因为上面设定了hold
sudo apt upgrade -y kubelet kubeadm kubectl
kubeadm version

# 显示将要升级的内容
sudo kubeadm upgrade plan
# 列出当前版本需要的image tag
kubeadm config images list
# 修改, 拉取并打官方tag
04_pull_image.sh

# 升级
sudo kubeadm upgrade apply vx.xx.x
```

### Upgrade master and node packages

``` sh
# 1. 剔除node
# in master, $NODE is node name pt-4
kubectl drain $NODE --ignore-daemonsets
# or
kubectl drain ip-172-31-85-18 --ignore-daemonsets

# 2. 安装package
sudo apt update
# 必须指定名称, 因为上面设定了hold
sudo apt upgrade -y kubelet kubeadm kubectl
kubeadm version

# 3. 手动下载image
# 显示将要升级的内容
sudo kubeadm upgrade plan
# 列出当前版本需要的image tag
kubeadm config images list
# 修改, 拉取并打官方tag
04_pull_image.sh

# 4. upgrade kubelet on each node
sudo kubeadm upgrade node config --kubelet-version $(kubelet --version | cut -d ' ' -f 2)
sudo systemctl restart kubelet.service
sudo systemctl status kubelet.service
# on maseter
kubectl uncordon $NODE
# check
kubectl get nodes
```