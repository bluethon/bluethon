Git Set Proxy
=============

> [简化版本](http://www.mikeheijmans.com/sysadmin/2014/08/12/proxy-ssh-over-socks/)
> [完整版本](http://cms-sw.github.io/tutorial-proxy.html)

### Open a SOCKS proxy through an SSH tunnel

for ss, pass this

    ssh -f -N -D 1080 <host>

### connect using SSH

format like

    git@github.com:cms-sw/cmssw.git
    ssh://git@github.com/cms-sw/cmssw.git

vim ~/.ssh/config

``` yaml
Host github.com
    User                git
    ProxyCommand        nc -x localhost:1080 %h %p
```

### connect using HTTP(s)

    git config --global http.porxy socks5://localhost:1080
    git config --global https.porxy socks5://localhost:1080
