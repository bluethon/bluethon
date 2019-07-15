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
  - `/sys/fs/cgroups`目录下的各资源子目录下(如`./cpu`)创建文件夹, 写入限制值
  - `tasks`文件中为PID, 指明目标
  - 限制进程在长度为`cfs_period`的一段时间内，只能被分配到总量为`cfs_quota`的 CPU 时间
  - 容器对内存等资源隔离不彻底(`/proc`不知道`Cgroups`存在), 解决方法使用`lxcfs`给容器挂载修改后的内核信息

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
# 查看aufs挂载信息, 找到对应的aufs内部ID
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
