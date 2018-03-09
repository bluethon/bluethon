Config
======

config
------

``` sh
Host *
  # allow local -> server1 -> server2
  # use local private key to server 2
  ForwardAgent yes
  # avoid Too many authentication failures
  # explicitly provided private key.
  IdentitiesOnly yes

Host github.com
  HostName github.com
  Port 22
  # ProxyCommand=nc -X 5 -x localhost:1080 %h %p
  User git
  IdentityFile ~/.ssh/id_rsa_github

  # PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa_bitbucket.pub

```

sshd config
-----------

### 最大连接时间

    sudo vim /etc/ssh/sshd_config

``` config
# 应该只需要第三行
MaxAuthTries 20
ClientAliveInterval 120
ClientAliveCountMax 720
```

    sudo service ssh restart
