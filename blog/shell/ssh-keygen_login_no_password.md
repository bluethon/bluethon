SSH免密码登陆
===========

``` bash
# 用ssh-keygen创建公钥(回车3次)
ssh-keygen -t rsa

# 复制公钥到ssh 访问的主机, 然后需输入密码登陆
scp -P 8888 ~/.ssh/id_rsa.pub root@192.168.1.1:~/.ssh/authorized_keys

# 然后就可正常使用
ssh root@192.168.1.1 -P 8888

```
