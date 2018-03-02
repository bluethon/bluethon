Note
====

cmd
---

    show dbs;           # 显示db

install
-------

``` shell
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb [ arch=amd64 ] https://mirrors.tuna.tsinghua.edu.cn/mongodb/apt/ubuntu xenial/mongodb-org/stable multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-stable.list
sudo apt-get update
sudo apt-get install -y mongodb-org

```

docker run
----------

启动

    # -v 挂载本地目录
    # -d daemon
    docker run --name <name> -p 27017:27017 -v /data/db:/data/db -d mongo

命令行

    # mongo是启动命令行的shell命令
    docker exec -it <name> mongo
