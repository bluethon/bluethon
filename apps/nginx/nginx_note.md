Nginx Note
===========

cmd
---

    nginx -t                                # 验证配置
          -T                                # 验证并输出
          -c nginx.conf -t                  # 指定文件验证
          -s reload                         # 重新加载配置

    docker kill -s HUP <container name>     # 重载配置
    docker restart <container name>         # 重启

configuration
-------------

    # 可以放在http/server/locaiton任意地方
    # Nginx: 413 Request Entity Too Large Error and Solution
    client_max_body_size 2M;            # 单文件大小上限

docker-compose
--------------

### debug

> https://github.com/docker-library/docs/tree/master/nginx#running-nginx-in-debug-mode

``` yaml
web:
  image: nginx
  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
  command: [nginx-debug, '-g', 'daemon off;']

  # 读取环境变量
  environment:
      ENV_FOO: ENV_FOO
      ENV_BAR: ENV_BAR
  command: >
    sh -c "envsubst \"`env | awk -F = '{printf \" $$%s\", $$1}'`\"
    < /etc/nginx/conf.d/web.template
    > /etc/nginx/conf.d/default.conf &&
    nginx -g 'daemon off;'"
```

nginx
-----

### http配置

``` nginx
server {
    listen 80;
    listen 443 ssl;
    server_name domain_or_addr;

    # 404 定位到 /
    error_page 404 /;

    # = 精确匹配, 加速
    location = / { 
        index index.html;
    }

    # 最后匹配(无视位置) /
    location / {
        proxy_pass http://localhost:8000;
    }
}
```

### uwsgi配置

sudo vim /etc/nginx/site-available/foo.com

``` nginx
upstream foo {
    # 使用文件socket
    server unix:///tmp/foo.sock;
}
server {
    listen 80;
    server_name domain_or_addr;
    location / {
        include uwsgi_params;

        # 3 ways
        uwsgi_pass foo; # 上面upstream
        uwsgi_pass unix:/tmp/foo.sock;
        uwsgi_pass localhost:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

sudo ln -s /etc/nginx/site-available/foo.com /etc/nginx/site-enable/foo.com

### 重启

    sudo service nginx restart
    sudo nginx -s reload
