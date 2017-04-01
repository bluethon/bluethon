Nginx Note
===========

nginx
-----

### http配置

``` sh
server {
    listen 80;
    listen 443 ssl;
    server_name domain_or_addr;
    location / {
        proxy_pass http://localhost:8000;
    }
}
```

### uwsgi配置

sudo vim /etc/nginx/site-available/foo.com

``` conf
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

/etc/nginx/site-available/weixin.yokeneng.com

location 部分
