# 深入剖析Kubenetes

## 05 容器基础1: 进程

> 容器, 特殊的进程

- 容器技术的核心功能, 就是通过约束和修改进程的动态表现, 从而为其创造出一个'边界'
  - Cgroup, 制造约束
  - Namespace, 修改进程视图
    - PID Namespace, 其只是系统创建线程的系统调用`clone()`的可选参数(Linux的线程是用进程实现的)
    - Mount Namespace
    - User Namespace
    - Network Namespace
    - etc

## 06 容器基础2: 隔离与限制

- 敏捷和高性能是优势
- 隔离的不彻底
  - 只是特殊进程, 多个容器间使用相同宿主机内核(这也是为什么win和Mac不能用docker)
  - Linux内核中, 很多资源和对象是不能Namespace化的, 典型如时间
- Linux Cgroups(Linux Control Group), 限制进程组使用的资源上限
  - `/sys/fs/cgroups`目录下的各资源子目录(如`./cpu`)下创建文件夹(如./docker), 写入限制值
  - `tasks`文件中为PID, 指明目标
  - 限制进程在长度为`cfs_period`的一段时间内，只能被分配到总量为`cfs_quota`的 CPU 时间
  - 容器对内存等资源隔离不彻底(`/proc`不知道`Cgroups`存在), 解决方法使用`lxcfs`给容器挂载修改后的内核信息
- Docker参数
  - `--cpu-period`, can not be less than 1ms (i.e. 1000)
  - `--cpu-quota`
  - `-m`, 内存限制, 如`100M`

## 07 容器基础3: 镜像

- 容器镜像: 即rootfs(根文件系统), 如Ubuntu18.04
- 容器层修改只读内容: `Copy-on-write`, 从上到下一次查找, 找到后复制到容器层, 然后修改

### Docker核心原理

- 启用Linux Namespace配置
- 设置指定的Cgroups参数
- 切换进程的根目录(优先使用`pivot_root`, 不支持用`chroot`)

> pivot_root是把整个系统切换到一个新的root目录，而移除对之前root文件系统的依赖，这样你就能够umount原先的root文件系统。而chroot是针对某个进程，而系统的其它部分依旧运行于老的root目录

### 联合文件系统（Union File System）

- 又叫UnionFS, 将多个不同位置的目录联合挂载(Union Mount)到同一目录下
- Ubuntu之前默认`aufs`, 现在使用`overlay2`(省略了fs后缀), Linux内核集成

``` sh
# 查看aufs挂载信息(mnt), 找到对应的aufs内部ID
cat /proc/mounts | grep aufs
xxxxxxxxxxxxxxxxxxxxxxxxxxxxx,si=xxxxx
# 查看被联合挂载的各层信息
cat /sys/fs/aufs/si_xxxxxxxxxxx/br[0-9]*
/var/lib/docker/aufs/diff/xxxxx     # 可读写层(rw)
                                    # Init层(ro+wh)
                                    # 只读层(ro+wh)
```

### aufs

- 只读层
  - rootfs最下面的几层, ro+wh(readonly+whiteout)
- 可读写层
  - 最上面一层, rw, 在没有写入文件前, 目录空
  - 删除文件, 创建`.wh.<name>`文件, 联合挂载后, 原文件被遮挡(即消失), 即whiteout(白障)
- Init层
  - 以`-init`结尾的层, 专门用来存放`/etc/hosts`等内容
  - 其原属于镜像只读, 但是需要启动时修改满足功能, 但是不希望docker commit提交此类修改, 所以单独挂载

### overlay2

/var/lib/docker/overlay2

- `LowerDir`, 镜像层
- `UpperDir`, 容器层, 创建文件后, 出现在此目录
- `MergedDir`, 容器挂载点, lower和upper联合挂载后, 作为root提供给容器
- `WorkDir`, 用于实现`Copy-on-write`

## 08 容器基础4: 容器

``` sh
# 查看容器PID
docker inspect --format '{{ .State.Pid }}' <conID>
# 查看容器Namespace
ls -l /proc/<pid>/ns
```

### ENTRYPOINT

- 和CMD都是容器进程启动所必需的参数
- 完整执行格式`ENTRYPOINT CMD`
- 默认提供隐含值, `/bin/sh -c`, 最后执行`/bin/sh -c "python abc.py"`, CMD即为ENTRYPOINT的参数

### docker exec

原理, 创建进程通过加入容器已有的namespace

- 通过`open()`系统调用打开Namespace
- 把文件描述符`fd`交给`setns()`使用
- `setns`执行后当前进程就加入了ns

### Volume

- 联合挂载在`/mnt/`下, 即`rootfs` ready
- 在执行chroot前, 挂载指定目录到`mnt`下对应目录
- 挂载时容器进程(dockerinit)已创建, Mount Namespace已生效, 挂载只在容器内可见, 保证隔离性不会被Volume破坏
  - 此处的容器进程, 是Docker创建的一个容器初始化进程(dockerinit), 不是应用进程(ENTRYPOINT+CMD)
  - dockerinit会负责完成根目录准备, 挂载设置和目录, 配置hostname等
  - 最后, 通过`execv()`系统调用, 让应用进程取代自己, 成为PID=1的进程
- 使用绑定挂载(bind mount)机制
  - 实际是一个`inode`替换过程, 绑定相当于修改'指针'指向
  - `inode`, 存放文件的'对象'
  - `dentry`, 目录项, 访问inode的'指针'

![bind-mount](./k8s/bind-mount.png)

### '全景图'

![all-view](./k8s/docker-top-view.png)

## 09 Kubernetes的本质

### 全局架构

![global](./k8s/k8s-architecture.png)

- Master(控制节点)
  - `kube-apiserver`, API服务
  - `kube-scheduler`, 调度
  - `kube-controller-manager`, 容器编排
  - `Etcd`, 集群的持久化数据, 由`kube-apiserver`处理后存入
- Node(计算节点)
  - `kubelet`, 负责同容器运行时(如Docker)交互
    - 依赖`CRI`远程调用接口, (Container Runtime Interface), 接口定义了容器运行的核心操作
    - 容器运行时(Docker)通过`OCI`与Linux交互
    - 通过`gRPC`协议与`Device Plugin`插件交互, 管理GPU等宿主机物理设备
    - `CNI`(Container Networking Interface), 网络插件, 配置容器网络
    - `CSI`(Container Storage Interface), 存储插件, 持久化存储

### 核心功能全景图

![全景图](./k8s/k8s-func-panorama.png)

- 最主要的设计思想是, 从更宏观的角度, 以统一的方式来定义任务之间的各种关系, 并且为将来支持更多种类的关系留有余地
- 编排, 按照用户的意愿和整个系统的规则, 完全自动化地处理容器间的各种关系
- 容器间关系
  - `Pod`, 之中的容器共享一个Network Namespace, 同一组数据卷
  - `Service`, 作为Pod的代理入口(Portal), 代替Pod对外暴露一个固定的网络地址
  - `Deployment`, 多实例管理器, 一次启动多个应用实例
  - `Secret`对象, 保存在Etcd中的键值对数据, 容器启动时, 以Volume方式挂载到容器内
- 应用运行形态
  - `Job`, 一次性任务
  - `DaemonSet`, 每个宿主机上只运行一个副本的守护进程服务
  - `CronJob`, 定时任务
- 使用方式:　声明式API，对应的以下对象为API对象
  - 通过一个'编排对象', 比如Pod Job CronJob等, 描述管理的应用
  - 在为它定义一些'服务对象', 比如Service Secret Horizontal-Pod-Autoscaler等, 负责具体的平台级功能

## 10 kubeadm

- kubeadm init
  - 检查是否可以部署(Preflight Checks)
  - 生成Kubernetes对外提供服务所需的各种证书和对应的目录
    - 除非专门开启'不安全模式', 默认都需要HTTPS
    - 证书位置, Master下`/etc/kubernetes/pki`
    - 项目证书ca.crt和私钥ca.key
    - kubelet进行streaming操作, 需要通过访问kube-apiserver, 使用的证书`apiserver-kubelet-client.crt`和`xx.key`
    - 可以拷贝现有证书到该目录下, 使kubeadm跳过生成步骤
  - 生成其他组件访问kube-apiserver所需的配置文件
    - `/etc/kubernetes/xxx.conf`
      - admin.conf
      - controller-manager.conf
      - kubelet.conf
      - scheduler.conf
    - 记录Master节点服务器地址, 监听端口, 证书目录等
  - 为Master组件生成Pod配置文件(Static Pod), kubelet启动后会自动检查, 加载所有的Pod YAML, 运行
    - `/etc/kubernetes/manifests`
    - kube-apiserver
    - kube-controller-manager
    - kube-scheduler
  - 生成Etcd的Pod YAML
  - Master容器启动后, kubeadm检查localhost:6443/healthz检查, 等待完全加载
  - 生成`bootstrap token`
  - 将ca.crt等Master节点信息, 通过ConfigMap方式(cluster-info)保存在Etcd中, 工后续部署Node使用
  - 安装默认插件
    - kube-proxy[必装], 提供集群的服务发现
    - DNS[必装], DNS解析
- kubeadm join
  - 使用token, 获取证书(CA文件), 用来和apiserver交互, 获取cluster-info内的信息
- 配置kubeadm的部署参数
  - `kubeadm init --config kubeadm.yml`
  - 修改配置文件

## 11 从0搭建k8s集群

- 默认情况下, Master节点不允许运行用户的Pod
- 通过Taint(污点)/Toleration机制
- 原理, 某节点打上Taint, 所有Pod都不能在该节点上运行, Pod有'洁癖'
- 除非个别Pod声明自己能'容忍'该'污点', 即声明了Toleration, 才能在该节点运行
- 加污点, `kubectl taint nodes node1 foo=bar:NoSchedule`
- Taint只对之后调度的Pod生效, 不影响之前的
- 删除键为xx的污点, `kubectl taint nodes --all node-role.kubernetes.io/master-`, 末尾加`-`
- 云原生, 即Kubernetes原生

## 12 部署一个应用

``` yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.8
        ports:
        - containerPort: 80
        volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: nginx-vol
      volumes:
      - name: nginx-vol
        emptyDir: {}
```

- YAML文件, 在k8s中, 即为一个API Object(API对象)
- `Deployment`, 是一个定义多副本应用的对象
- Pod模板(spec.template)
- Pod就是k8s世界里的应用, 而一个应用, 可以由多个容器组成
- 控制器模式(controller pattern), 使用API对象(Deployment)管理另一种API对象(Pod)的方法
- `Metadata`字段, API对象的'标识', 即元数据, 也是k8s中找到这个对象的主要依据
  - 最主要是`Labels`字段, 一组kv格式的标签(如`app: nginx`)
  - 使用Labels字段过滤被控制对象
  - 过滤规则定义`spec.selector.matchLabels`, 即`Label Selector`
  - `Annotations`, 与Labels格式/层级完全相同, 用来携带内部信息(k8s自身使用), 大部分是自动添加
- API对象定义, 2部分
  - Metadata, 存放对象的元数据, 所有API对象, 基本一致
  - Spec, 属于该对象独有的定义, 用来描述其要表达的功能
- 过滤命令, `kubectl get pods -l app=nginx`, 命令行中, 标签使用`=`, 而不是`:`
- describe的`Events(事件)`中包含详细信息, debug时有用
- 全程推荐使用`kubectl apply -f x.yml`, k8s根据YAML内容自动具体处理
- 如果实例只有一个, 推荐`replicas=1`的Deployment, 而不是单独的Pod, 因为前者在Node挂掉后仍可调度到其他Node

## 13 为什么需要Pod

- Pod是k8s项目的原子调度单位
- 实现原理
  - 只是逻辑概念
  - 内部所有容器, 共享一个Network Namespace, 并且可以声明共享一个Volume
  - 首先创建Infra容器, 其他通过Join Network Namespace加入
    - 特殊容器
    - 汇编编写
    - 永远处于暂停状态
    - `k8s.gcr.io/pause`
- 产生的效果
  - 内容容器可以直接localhost通信
  - 一个Pod只有一个IP, 即Network Namespace的
  - Pod的生命周期只跟Infra容器一致, 与真实绑定的内部容器无关
- 同理, Volume定义设计在Pod层级, 这样内部容器都可以挂载, 共享内容
- 实例(Sidecar模式)
  - webpack打包内容和Nginx, 即可一个Pod两个容器
  - 打包容器定义为`Init Container`
  - 在Pod中, 所有`Init Container`定义的容器, 都会比`spec.containers`定义的用户容器先启动
  - `Init Container`容器会按顺序逐一启动
- Sidecar指在一个Pod中, 启动一个辅助容器, 完成一些独立于主进程之外的工作
- 理解Pod的本质: Pod实际扮演的是传统基础设施的'虚拟机', 容器则是虚拟机内的用户程序

## 14 深入解析Pod对象1

- 凡是调度/网络/存储, 以及安全相关的属性, 都是Pod级别的
- 部分重要字段
  - `NodeSelector`, 供用户将Pod和Node进行绑定的字段
  - `NodeName`, 有值, 表示被调度过了, 一般由调度器负责设置, 但可自行设置用于debug等
  - `HostAliases`, 定义`/etc/hosts`内容
- 跟容器Linux Namespace相关的属性, 也是Pod级别
- Pod中容器要共享宿主机的Namespace, 也是Pod级别, 如共享主机网卡等
- Containers相关字段
  - `ImagePullPolicy`, 拉取镜像策略
  - `Lifecycle`, 定义容器生命周期相关的Hook
- Pod生命周期(.Status)
  - `Pending`, 已提交k8s, 保存etcd, 但没有成功创建, 如调度有问题
  - `Running`, 成功调度, 至少有一个在运行
  - `Succeeded`, 运行完毕退出, 常见于一次性任务
  - `Failed`, 至少一个容器不正常(非0)退出, 需要debug, 如Pod的Events和日志
  - `Unknown`, 异常状态, Pod的状态不能持续被kubelet汇报给kube-apiserver, 怀疑主从通信问题

## 15 深入解析Pod对象2

- `Projected Volume`, 特殊Volume, 投射数据卷
  - 为容器提供预先定义好的数据, 从容器角度看, Volume内的信息是被k8s'投射'(Project)进入容器的
- 种类
  - Secret
    - 作用, 把Pod想要访问的加密数据, 存放到Etcd中, 使用时挂载
    - 数据必须是base64转码(echo -n 'xxx' | base64)
    - Etcd更新, Pod内也会更新(kubelet定时维护, 有时延), 注意重试和超时逻辑
  - ConfigMap
    - 保存不加密的配置信息
    - `kubectl get configmaps xxx -o yaml`导出
  - Downward API
    - 让Pod里的容器直接获取到Pod API对象本身的信息
    - 只能获取Pod里容器启动前确定下来的(比如PID不能获取)
  - ServiceAccountToken
    - ServiceAccount, k8s内置的`服务账户`, 允许权限分配, 授权信息和文件, 保存在其绑定的特殊Secret对象(即父级别的SAToken)内
    - 默认'服务账户'(default Service Account), 默认挂载, 可以describe查看
    - `InClusterConfig`, 把k8s客户端以容器运行在集群内, 使用默认服务账户自动授权的方式
    - 可以关闭, 默认不挂载
- 健康检查与恢复
  - `Probe`(探针), 在Pod里定义, kubelet根据其返回值决定容器状态
    - `livenessProbe`, 检查容器是否正常
      - HTTP
      - TCP
      - exec
    - `readnessProbe`, 检查是否可以被Service服务访问, 不影响生命周期
  - 恢复机制(restartPolicy)
    - `Always`, 任何情况下, 只要容器不在运行态, 就自动重启(删除创建), 默认
    - `OnFailure`, 异常退出才重启
    - `Never`, 从不重启
  - 恢复策略和Pod状态
    - 只要Pod的restartPolicy指定的策略允许重启异常的容器(如Always), Pod就保持Running, 并进行重启, 否则Failed
    - 对于包含多容器的Pod, 只有里面所有容器都异常退出, Pod才进入Failed, `READY`字段显示正常的个数
- Pod字段自动填充(PodPreset)
  - 只会在Pod API对象被创建前追加到对象上, 不会影响Pod的控制器(即Deployment不受影响)
  - 如果有多个PodPreset, 合并修改, 冲突字段不修改

## 16 编排, 控制器模式

- Pod API对象是对容器进一步抽象和封装
- 控制器组件
  - `kube-controller-manager`
  - 集合目录, <https://github.com/kubernetes/kubernetes/tree/master/pkg/controller>
- 遵循统一的编排模式: 控制循环(control loop)
  - 实际状态A(k8s集群)
  - 期望状态B(用户YAML)
  - if A==B()
  - skip
  - else
  - 执行操作, 调整为B
- 对比状态的操作: 调谐(Reconcile), 过程: 调谐循环(Reconcile Loop) or 同步循环(Sync Loop)
- 用一种对象(控制器)管理另一种对象(Pod)
- 被控对象定义: PodTemplate(Pod模板)
- 组成, 上半部分的控制器定义和下半部分的被控制对象的模板, [图片](./k8s/pod-template.png)
- 当前API对象的`Metadata`中`ownerReference`保存着拥有者(Owner)信息

## 17 水平扩展和收缩

### Deployment

- Deployment
  - 两层控制器
  - 实际控制的是ReplicaSet对象(保存各版本对象), ReplicaSet对象控制Pod对象
  - 通过RS个数描述应用版本
  - 通过RS属性(如replicas)保证Pod副本数量
- 水平扩展/收缩(horizon scaling out/in)
  - D控制修改RS的Pod个数
- 滚动更新
  - D控制多个RS, 调节其Pod个数, 交替逐一升级
  - 只有处于AVAILABLE的Pod才是最终状态
  - 查看状态, `kubectl rollout status deployment/<name>`
  - 更新策略由`RollingUpdateStrategy`指定
  - `kubectl set image`可以更新镜像
  - 控制RS历史版本数量, `spec.revisionHistoryLimit`, 为0不能回滚

## 18 StatefulSet: 拓扑状态

- 有状态应用(Stateful Application)
- 无状态应用(Stateless Application)
- 应用状态抽象
  - 拓扑状态, 多实例间不对等, 依次启动, 网络标识一致
  - 存储状态, 多实例分别绑定不同存储数据
- 核心功能, 通过记录应用状态, 在Pod重新创建时, 为新Pod恢复状态
- Service访问方式
  - VIP(Virtual IP), 分配虚拟IP
  - DNS, 分配特定DNS
    - Normal Service, DNS解析结果为VIP, 后续流程如VIP流程
    - Headless Service, DNS解析结果直接为Pod的IP
      - 绑定DNS记录格式`<pod-name>.<svc-name>.<namespace>.svc.cluster.local`
- `spec.serviceName`增加表示此功能
- 内部Pod被删除后, 重新创建网络身份完全相同的Pod(DNS解析对应关系一致), 保证Pod网络标识的稳定性
- 固定了Pod的拓扑状态(如节点启动顺序), 按照Pod的`名称+编号`方式

## 19 StatefulSet: 存储状态

- StatefulSet的控制器直接管理Pod
- 通过Headless Service, 为Pod 编号, 在DNS服务器生成同编号DNS记录
- 为每个Pod分配并创建同编号PVC
- StatefulSet是特殊的Deployment(为每个Pod编号), 使每个Pod集群唯一
- 使用PV和PVC实现
- `volumeClaimTemplates`为每个Pod声明PVC
- Pod删除重建都会挂载对应的同一个PVC(Bound状态)
