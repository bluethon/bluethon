错误笔记
=======

ssh
---

### no route to host

服务端没有连网


mount exfat

    sudo apt-get install exfat-fuse exfat-utils

postgres
--------

### Postgresql: password authentication failed for user “<user>”

    sudo -u postgres psql
    ALTER USER <user> PASSWORD 'newPassword';
