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
kubectl get jobs.batch
kubectl logs <job>

# job(restartPolicy: Never)失败会一直创建新的Pod, (restartPolicy: OnFailure)则会重启同一Pod
# job的completions和parallelism默认为1

# show all api versions
kubectl api-versions

# 获取cron job
kubectl get cronjobs.batch
# 获取实际的每次jobs
kubectl get jobs.batch

kubectl get services
kubectl describe services httpd-svc

# look dns
kubectl get deployments.apps --namespace kube-system

kubectl run --generator=run-pod/v1 alpine --rm -it --image alpine /bin/sh
# 查看域名
nslookup httpd-svc.default
# 同namespace可以省略
nslookup httpd-svc
# 查看所有命名空间
kubectl get namespaces
```

- k8s的系统组件在`kubu-system`namespace中
- kubulet是唯一不在容器中的组件, Ubuntu中通过systemd运行

YAML
----

``` yaml
apiVersion: batch/v1
apiVersion: batch/v1beta1
kind: Job
kind: CronJob
spec:
  # 并发
  parallelism: 2
  # 总数
  completions: 6
  schedule: "* * * * *"
restartPolicy: Never
restartPolicy: OnFailure

---
apiVersion: v1
kind: Service
metadata:
  name: httpd-svc
spec:
  # 开启节点端口
  type: NodePort
  selector:
    run: httpd
  ports:
    - protocol: TCP
      # 节点
      nodePort: 30000
      # ClusterIP
      port: 8080
      # Pod
      targetPort: 80
```

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