Kubernetes Note
===============

URL
---

[GCR 同步仓库](https://github.com/mritd/gcr)
[kubenetes-tools 一些工具](https://github.com/openthings/kubernetes-tools)
[kubenetes一键脚本](https://github.com/cookcodeblog/k8s-deploy)

    # k8s.gcr.io
    gcr.mirrors.ustc.edu.cn/google-containers

CMD
---

``` shell
# 列出依赖包版本
# https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#running-kubeadm-without-an-internet-connection
kubeadm config images list
```

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
# 查看deployments过程
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

# 以下三层递进底层, 命名可以看出关系
# 查看deployment
kubectl get deployments.apps <name> -o wide
# 查看replicaset
kubectl get replicasets.apps -o wide
# 查看pod
kubectl get pods -o wide

# 加入版本记录
kubectl apply -f httpd.v2.yml --record
# 查询滚动升级历史记录
kubectl rollout history deployment httpd
# 回滚历史版本到v1
kubectl rollout undo deployment httpd --to-revision=1

# 获取secret
kubectl get secrets mysecret
# 查看/编辑详细的base64
kubectl edit secrets mysecret

# 显示cli连接秘钥
kubectl config view --flatten

# install helm
brew install kubernetes-helm
# install Tiller
helm init --upgrade -i registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.11.0 --stable-repo-url https://kubernetes-charts.proxy.ustclug.org
# 查看所有charts
helm search
# 仓库链接
helm repo list
# 增加/更改仓库
helm repo add <name> <url>
# 删除仓库
helm repo remove <name>

# Error: no available release name found
# 增加权限
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'

# 安装
helm install <name>/<chart>
# -n release名字
# --namespace <namespace>(默认`default`)
# `ReleaseName-ChartName`
helm list
helm delete <release>
helm upgrade <release> stable/mysql -f 166_myvalues_upgrade.yml
helm history <release>
helm rollback <release> <version>

# 创建空模板
helm create <name>
# 校验
helm lint <name>
# 预览安装yamlf
helm install --dry-run --debug <name>

helm install ./foo.tgz
helm install <dir>
# 打包自己的chart
helm package <chart-dir>
# cd charts dir
helm repo index myrepo --url <url>
# 生成index.yaml
# cp charts dir to serve
# helm add repo <my-charts>

# download
helm fetch <chart>

# reset(on each node)
sudo kubeadm reset
# clean iptable manually
sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X

# migrate from old init yaml
sudo kubeadm config migrate --old-config k8s-adm.yml
# show default init config(master)
sudo kubeadm config print init-defaults

# get user `admin` token for dashboard
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin | awk '{print $1}')

# monitor(NodePort)
kubectl apply -f "https://cloud.weave.works/k8s/scope.yaml?k8s-version=$(kubectl version | base64 | tr -d '\n')&k8s-service-type=NodePort"
```

YAML
----

- k8s的系统组件在`kubu-system`namespace中
- kubulet是唯一不在容器中的组件, Ubuntu中通过systemd运行

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

Note
----

### Network Policy(172)

当设置`replicas`, 如果`ingress`CIDR仅设置`Node`级别, 则使用`<nodeIP>:<port>`
方式访问到其他`Node`上的`Pod`, 会访问不到, 需要同时设置`Pod`级别的`ingress`

### PersistentVolume

- nfs创建后, 如果挂载是在`/nfsdata`, 则使用时`<ip>/`即为前面根目录, 不加`/nfsdata`
- 使用时需要提前创建`nfs`下的目录, 否则Pod无法启动

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

Initialization
--------------

> <https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/>
> <https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file>

``` bash
### on master
# refer to change init.yml
# ! podSubnet need choose a network first !
sudo kubeadm config print init-defaults
sudo kubeadm init -f init.yml
# copy kubeadm join xxx

# make kubectl work for your non-root user
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

### on join node
# paste
sudo kubeadm join xxx

# Installing a pod network add-on
# https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network
# choose one(below for flannel)
kubectl apply -f xxxx/kube-flannel.yml

### on master
kubectl get nodes

### on local
mkdir $HOME/.kube
ssh <server> "kubectl config view --flatten" > config
kubectl get nodes
```

Upgrade
-------

> <https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/>

### Upgrade the control plane

``` sh
# 1 On master node, upgrade kubeadm
sudo apt-mark unhold kubelet kubeadm && \
sudo apt update && sudo apt upgrade -y kubelet kubeadm && \
sudo apt-mark hold kubelet kubeadm

# 2 Verify
kubeadm version

# 3 显示将要升级的内容
sudo kubeadm upgrade plan
# kubeadm upgrade apply 如果出现多次要依次升级(如果升级失败, 执行此处)

# 4 列出当前版本需要的image tag
kubeadm config images list
# 指定查看版本对应images(可选, 失败尝试)
kubeadm config images list --kubernetes-version=v1.xx.x

# 5 修改, 拉取并打官方tag
04_pull_image.sh

# 6 升级
sudo kubeadm upgrade apply vx.xx.x
```

### Upgrade master and node packages

``` sh

### on master
# 1. 剔除node
# in master, $NODE is node name pt-4
# master节点必须加 --ignore-daemonsets
# master上依次剔除所有节点
kubectl drain $NODE --ignore-daemonsets
# or
kubectl drain ip-172-31-85-18 --ignore-daemonsets

### on each node
# 2. 安装package
sudo apt-mark unhold kubelet kubeadm && \
sudo apt update && sudo apt upgrade -y kubelet kubeadm && \
sudo apt-mark hold kubelet kubeadm
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
