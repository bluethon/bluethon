错误笔记
=======

ssh
---

### no route to host

服务端没有连网

### Could not open a connection to your authentication agent

<http://stackoverflow.com/a/17848593/4757521>

    eval `ssh-agent -s`
    ssh-add


ubuntu
------

### mount exfat

    sudo apt-get install exfat-fuse exfat-utils

postgres
--------

### Postgresql: password authentication failed for user “<user>”

    sudo -u postgres psql
    ALTER USER <user> PASSWORD 'newPassword';
