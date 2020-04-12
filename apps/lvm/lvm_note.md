LVM Note
========

CMD
---

``` sh
fdisk -l

sudo fdisk /dev/sdb
# create partition
# type 8e

# create a physical volume
sudo pvcreate /dev/sdb
# show volume group
sudo vgdisplay
# Extend volume group
sudo vgextend vg-name /dev/sdb

# re-size non swap partition
# # -r resize lv
sudo lvresize -r -L -8G /dev/mapper/lv-xxx
# or
sudo resize2fs /dev/mapper/xxxx-home

### Resize Swap Partition
# Resize swap
sudo lvresize -L 8G /dev/mapper/xxxx-swap_1
# Turn off swap
sudo swapoff -a
# Remake swap
sudo mkswap /dev/mapper/xxxx-swap_1
# Turn on swap again
sudo swapon -a
```
