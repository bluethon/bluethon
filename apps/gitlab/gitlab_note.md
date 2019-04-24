GitLab
======

## DEBUG

### Problem accessing /project/Jenkins_Project_name/. Reason: 404

> <https://github.com/jenkinsci/gitlab-plugin/issues/533#issuecomment-302443098>

Jenkins和Gitlab不能使用相同域名(仅端口不一样不行), 否则需要使用IP

### gitlab runner x509 error(SSL certificate problem: unable to get issuer certificate)

runner中挂载根证书(此处使用的是`let's encrypt`生成的fullchain.cer)

``` yml
- /var/gitlab/config/ssl/fullchain.cer:/etc/gitlab-runner/certs/ca.crt
```

---

## Config

### allow same server(localhost) webhook

> /admin/application_settings/network

    Outbound requests / Allow requests to the local network from hooks and services

### Backup

> <https://docs.gitlab.com/omnibus/settings/backups.html#creating-backups-for-gitlab-instances-in-docker-containers>

``` sh
# Backup application:
docker exec -t <your container name> gitlab-rake gitlab:backup:create
# Backup configuration and secrets:
docker exec -t <your container name> /bin/sh -c 'umask 0077; tar cfz /var/opt/gitlab/backups/$(date "+etc-gitlab-\%s.tgz") -C / etc/gitlab'
```

### gitlab-runner注册

> <https://docs.gitlab.com/runner/register/index.html#one-line-registration-command>

``` sh
docker run --rm -t -i -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register \
  --non-interactive \
  --executor "docker" \
  --docker-image alpine:3 \
  --url "https://gitlab.com/" \
  --registration-token "PROJECT_REGISTRATION_TOKEN" \
  --description "docker-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false"
```

## 安装

### ansible

> <https://github.com/jonashackt/gitlab-ci-stack>

### Dockerfile

``` Dockerfile
version: '3'

services:
  gitlab:
    image: 'gitlab/gitlab-ce:latest'
    restart: always
    hostname: 'gitlab.example.com'
    environment:
      TZ: 'Asia/Shanghai'
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://gitlab.example.com:<port>'
        gitlab_rails['time_zone'] = 'Asia/Shanghai'
        gitlab_rails['gitlab_shell_ssh_port'] = 9022
        nginx['custom_gitlab_server_config'] = 'error_page 497 https://$$host:9080$$request_uri;'
        # 指定证书(证书要使用带CA的)
        nginx['ssl_certificate'] = '/etc/gitlab/ssl/fullchain.cer'
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
