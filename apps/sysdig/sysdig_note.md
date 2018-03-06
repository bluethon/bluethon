Sysdig Note
===========

Install
-------

``` shell
curl -s https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public | sudo apt-key add -
sudo curl -s -o /etc/apt/sources.list.d/draios.list http://download.draios.com/stable/deb/draios.list
sudo apt update
sudo apt install sysdig
```

Use
---

    sudo sysdig
    sudo csysdig
