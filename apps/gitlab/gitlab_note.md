GitLab
======

TODO
-----

<https://docs.gitlab.com/omnibus/docker/>

<https://docs.gitlab.com/omnibus/docker/#after-starting-a-container>

articles
---------

[安装+持续集成](http://www.jianshu.com/p/7a0d6917e009)

安装
----

### 中文版

> <https://hub.docker.com/r/twang2218/gitlab-ce-zh/>

``` sh
# 安装docker
# 创建环境
pyvenv venv
# 安装docker-compose
source venv/bin/activate
pip docker-compose
# 创建配置文件
vim docker-compose.yml
```

Dockerfile

``` yaml
version: '3'
services:
  gitlab:
    image: 'twang2218/gitlab-ce-zh:8.17.3'
    restart: unless-stopped
    hostname: 'gitlab.example.com'
    environment:
      TZ: 'Asia/Shanghai'
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://gitlab.example.com'
        gitlab_rails['time_zone'] = 'Asia/Shanghai'
        # 需要配置到 gitlab.rb 中的配置可以在这里配置，每个配置一行，注意缩进。
        # 比如下面的电子邮件的配置：
        # gitlab_rails['smtp_enable'] = true
        # gitlab_rails['smtp_address'] = "smtp.exmail.qq.com"
        # gitlab_rails['smtp_port'] = 465
        # gitlab_rails['smtp_user_name'] = "xxxx@xx.com"
        # gitlab_rails['smtp_password'] = "password"
        # gitlab_rails['smtp_authentication'] = "login"
        # gitlab_rails['smtp_enable_starttls_auto'] = true
        # gitlab_rails['smtp_tls'] = true
        # gitlab_rails['gitlab_email_from'] = 'xxxx@xx.com'
    ports:
      - '80:80'
      - '443:443'
      - '22:22'
    volumes:
      - config:/etc/gitlab
      - data:/var/opt/gitlab
      - logs:/var/log/gitlab
volumes:
    config:
    data:
    logs:
```

启动

    docker-compose up -d

停止

    docker-compose down

### docker

``` sh
docker pull gitlab/gitlab-ce

```
