Moving /var, /home to separate partition
========================================

Knowledge
---------

LVM 全称为Logical Volume Management，它是Linux环境下对磁盘分区进行管理的一种机制，它通过在硬盘和分区上建立一个抽象的逻辑层，来屏蔽分区大小，磁盘空间给用户 带来的困难。在LVM中，可以将多个磁盘分区组做成一个存储池，管理员可以在此存储池上随意创建逻辑卷组，再mount到相应的挂载点上去，从而达成动态 增加磁盘空间的目的。例如上边的这个例子，当/home分区不够大时，可把磁盘的一部分空间mount到/home上去，这样的话，就可以实现零当机时间 来调整磁盘了。

在开始LVM配置之前，先简述几个基本概念和术语：

1 - 物理存储介质：

指的是物理的硬盘，在/dev目录下看到的sda，sdb，sdc，hda，hdb，hdc等。

2 - 物理卷（Pisical Volume）：

指的是物理硬盘上的分区或逻辑上与磁盘分区具有相同功能能的设备，是LVM的基本存储块，但和分区来比，却包含了与LVM管理相关的参数。这个就是前面讲的存储池。

3 - 卷组（Volume Group）：
LVM的卷组类似于物理硬盘，卷组上边可以建立多个虚拟的“分区”，LVM卷组由一个或多个物理卷组成。

4 - 逻辑卷（Logical Volume）：

LVM的逻辑卷类似于非LVM系统中的硬盘分区，在逻辑卷上边可以建立文件系统，用于mount到不同的挂载点，提升分区空间——这是真正跟用户打交道的部分。

5 - PE （Physical Extent）

每一个物理卷被划分为一个个的基本存储单元，每一个PE都具有唯一的编址（这个东西类似于物理硬盘上的磁盘地址）。PE的大小默认为4MB。

6 - LE（Logical Extent）

每一个逻辑卷也被划分为一个个的基本存储单元，每一个LE也具有一个唯一的编址。在同一个卷组中，LE和PE的大小是相等的。

综上所述，进行一个总结就是，一个或者多个物理硬盘上都可以划分出一个或者多个LVM分区，然后这些分区可以组成一个物理卷（PV），形成一个存储池。用 户把这个存储池划分出来一个或者多个LV，挂载到不同的分区上去使用，这个就是LVM的基本原理，也是建立LVM的过程。

结合上边那个例子，如果要为/home和/var分区增加空间，则要有如下步骤：

1. 给服务器装上2块新硬盘

2. 把新硬盘进行分区，并标记为LVM分区

3. 把2块新硬盘上的LVM分区合并起来，组成一个新的物理卷（PV）

4. 把物理卷划分成两个逻辑卷（LV）：名字分别是home和var

5. 在这两个逻辑卷上建立文件系统

6. 把这两个逻辑卷挂载到/home和/var上去

CMD
---

> <https://unix.stackexchange.com/a/131318/181922>

``` bash
# 1. 安装软件
agi lvm2

# 2. 查看硬盘
sudo fdisk -l

# 3. 分区
sudo fdisk /dev/sdb

# 3.1 创建LVM分区
# 参数命令 n/p/1/enter/enter/t/8e/w

# 3.2 创建物理卷PV(Physical Volume)
sudo pvcreate /dev/sdb1
pvdisplay
# if rm
sudo pvremove /dev/sdb1

# 3.3 创建逻辑卷组VG(Volume Group)
# 如果多个 后面添加(sdc1)
sudo vgcreate vg1 /dev/sdb1 /dev/sdc1
# add disk
sudo vgextend vg1 /dev/sdd1
# rm
sudo vgremove vg1
# ls
sudo vgdisplay
# or
sudo vgscan

# 3.4 创建逻辑卷LV(Logical Volume)
sudo lvcreate --name var_ext --size 100G vg1
sudo lvdisplay
sudo lvremove /dev/vg1/var_ext
# 如果是全用, 按G输入会报错, 因为实际差若干M
# 可以先分99%, 剩下扩展
# -r resizefs, 调整lv大小后调整文件系统, 有数据时必加!!!
# -r必加, 已经又错误一次(2020-01-26)
sudo lvextend -r -L [+]1020M /dev/vg1/var_ext
# 减少
sudo lvreduce -r -L -4G /dev/vg1/var_ext   # 减少4G
sudo lvreduce -r -L 4G /dev/vg1/var_ext    # 减到4G!!!
# rename
sudo lvrename vg1/var_ext var_ext1
# 调整大小
lvresize

# 3.5 格式化
sudo mkfs.ext4 /dev/vg1/var_ext

# 4. mount to /mnt
sudo mkdir /mnt/var
sudo mount /dev/vg1/var_ext /mnt/var

# 5 singer-user mode, 防止他人写入, 单用户不必需
sudo init 1

# 6 backup data in var only(not the /var directory itself)
cd /var
# -x, one file system
# 比如/proc的文件系统就和/var不一样, 就不会复制, 当然/proc不在/var下, 仅举例
sudo cp -ax . /mnt/var

# 7 rename
cd /
sudo mv var var.old

# 8 new dir
sudo mkdir var

# 9 umount
sudo umount /dev/vg1/var_ext

# 10 remount
sudo mount /dev/vg1/var_ext /var

# 11 auto mount
sudo vim /etc/fstab

/dev/vg1/var_ext    /var    ext4    defaults 0   0

# 12 return multitasking mode
sudo init 5
```
