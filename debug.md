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

### sudo: unable to resolve host abc

    sudo vim /etc/hosts
```
127.0.0.1       localhost
127.0.0.1       abc
```

### Unable to lock the administration directory (/var/lib/dpkg/) is another process using it?

    sudo lsof /var/lib/dpkg/lock
    kill -p <PID>

postgres
--------

### Postgresql: password authentication failed for user “<user>”

    sudo -u postgres psql
    ALTER USER <user> PASSWORD 'newPassword';
