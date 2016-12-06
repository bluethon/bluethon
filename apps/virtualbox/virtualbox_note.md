Vbox Note
=========

Share Folder
------------

### win to linux

> <http://serverfault.com/a/674975/380738>

win set share folder

in linux do below

``` sh
# 修改默认挂载点
sudo VBoxControl guestproperty set /VirtualBox/GuestAdd/SharedFolders/MountDir /home/blue/programs/

# 修改默认前缀
sudo VBoxControl guestproperty get /VirtualBox/GuestAdd/SharedFolders/MountPrefix
sudo VBoxControl guestproperty set /VirtualBox/GuestAdd/SharedFolders/MountPrefix ""
```
