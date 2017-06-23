Github Repo Pangolin Note
==========================

cmd
---

``` shell
bin/index.js server -p 11000 -l 11001       # server listen 11001, 通信11000
bin/index.js client -r host:11000 -l 8000   # client listen 8000, 通信11000

```

Install
-------

    git clone https://github.com/bluethon/pangolin.git
    npm install                 # 本地安装
    sudo npm install -g         # 全局安装
