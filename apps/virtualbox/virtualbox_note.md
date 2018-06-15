Vbox Note
=========

Share Folder
------------

### win to linux

> <http://serverfault.com/a/674975/380738>

win set share folder

in linux do below

``` bash
#!/bin/bash
# 修改默认挂载点
sudo VBoxControl guestproperty set /VirtualBox/GuestAdd/SharedFolders/MountDir /home/blue/programs/
sudo VBoxControl guestproperty get /VirtualBox/GuestAdd/SharedFolders/MountDir

# 修改默认前缀
sudo VBoxControl guestproperty get /VirtualBox/GuestAdd/SharedFolders/MountPrefix
sudo VBoxControl guestproperty set /VirtualBox/GuestAdd/SharedFolders/MountPrefix ""

# 增加用户到组
sudo adduser <user> vboxsf
```
