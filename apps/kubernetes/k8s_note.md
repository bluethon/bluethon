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