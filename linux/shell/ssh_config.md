设置
===

### 最大连接时间

    sudo vim /etc/ssh/sshd_config

``` config
# 应该只需要第三行
MaxAuthTries 20
ClientAliveInterval 120
ClientAliveCountMax 720
```

    sudo service ssh restart
