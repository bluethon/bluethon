错误笔记
=======

Makefile
--------

### makefile:2: *** missing separator. Stop

Makefile只能用tab, 不能使用4个space

> https://stackoverflow.com/a/16945143/4757521

    cat -e -t -v  makefile_name

supervisor
----------

### socket error

服务没有启动

    sudo service supervisor start

------------------

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

### Failed to connect to bus: No such file or directory

> https://askubuntu.com/a/999123/537695

    sudo apt install --reinstall dbus

### Python locale error: unsupported locale setting

    export LC_ALL="en_US.UTF-8"
    export LC_CTYPE="en_US.UTF-8"
    sudo dpkg-reconfigure locales

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

zsh
---

### zsh: no matches found: thunderbird*

    unsetopt no_match

> <http://askubuntu.com/a/481591/537695>
