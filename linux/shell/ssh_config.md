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

### 运行root登录

    sudo vim /etc/ssh/sshd_config

``` ssh
PermitRootLogin yes
```

### 多 Github deploy keys

> https://www.justinsilver.com/technology/github-multiple-repository-ssh-deploy-keys/


``` shell
# create
ssh-keygen -t rsa -f ~/.ssh/id_rsa_repo1 -C https://github.com/username/foo
# test key
ssh -i /home/username/.ssh/id_rsa_repo1 git@github.com
```

**alias host**

``` config
Host repo1 github.com
  Hostname github.com
  IdentityFile /home/username/.ssh/id_rsa_repo1

Host repo2 github.com
  Hostname github.com
  IdentityFile /home/username/.ssh/id_rsa_repo2
```

    git clone git@repo1:username/repo1.git

### 最大连接时间

    sudo vim /etc/ssh/sshd_config

``` config
# 应该只需要第三行
MaxAuthTries 20
ClientAliveInterval 120
ClientAliveCountMax 720
```

    sudo service ssh restart
