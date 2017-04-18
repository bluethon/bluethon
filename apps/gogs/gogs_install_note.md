gogs install
============

### gogs

``` sh
wget -qO - https://deb.packager.io/key | sudo apt-key add -
echo "deb https://deb.packager.io/gh/pkgr/gogs $(lsb_release -cs) pkgr" | sudo tee /etc/apt/sources.list.d/gogs.list
sudo apt-get update
sudo apt-get install gogs
```

### nginx

    sudo vim /etc/nginx/site-available/gogs.conf

``` conf
server {
    listen 80;
    server_name example.com;
    # 增大单文件上传大小
    client_max_body_size 200M;

    location / {
        proxy_pass http://localhost:6000;
    }
}
```

    sudo ln -s /etc/nginx/site-available/gogs.conf /etc/nginx/site-enabled/gogs.conf

### 首次启动设置环境

``` ini
; App name that shows on every page title
APP_NAME = Gogs
; The name of the system user that runs Gogs
RUN_USER = gogs
; Either "dev", "prod" or "test"
RUN_MODE = prod

[server]
PROTOCOL               = http
DOMAIN                 = example.com
ROOT_URL               = http://example.com/
HTTP_ADDR              = 0.0.0.0
HTTP_PORT              = 6000
; Disable SSH feature when not available
DISABLE_SSH            = false
; Whether use builtin SSH server or not.
START_SSH_SERVER       = false
; Domain name to be exposed in SSH clone URL
SSH_DOMAIN             = %(DOMAIN)s
; Port number to be exposed in SSH clone URL
SSH_PORT               = 22
; Network interface builtin SSH server listens on
SSH_LISTEN_HOST        = 0.0.0.0
; Port number builtin SSH server listens on
SSH_LISTEN_PORT        = %(SSH_PORT)s
; Root path of SSH directory, default is '~/.ssh', but you have to use '/home/git/.ssh'.
SSH_ROOT_PATH          = 
OFFLINE_MODE           = false
DISABLE_ROUTER_LOG     = false

[repository]
; Root path for storing repositories's data, default is "~/<username>/gogs-repositories"
ROOT                        = /home/gogs/gogs-repositories

[repository.upload]
; Maximum size of each file in MB
FILE_MAX_SIZE = 50

[database]
; Either "mysql", "postgres" or "sqlite3", you can connect to TiDB with MySQL protocol
DB_TYPE  = mysql
HOST     = 127.0.0.1:3306
NAME     = gogs
USER     = root
PASSWD   = passwd

[log]
ROOT_PATH  = /opt/gogs/log
```
