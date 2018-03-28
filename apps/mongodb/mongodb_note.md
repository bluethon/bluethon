Note
====

cmd
---

    show dbs;           # 显示db

    mongodump -u xiaoyu -p heheda --authenticationDatabase railway_map -d railway_map
    mongodump --gzip -h 47.104.145.108 -u xiaoyu -p heheda --authenticationDatabase railway_map -d railway_ma
    # 若导入单个数据库, 最后的目录需要指定到库级别
    mongorestore -v --gzip -h 172.19.0.2 -d railway_map -u xiaoyu -p heheda /dump/railway_map

    # 以下未验证成功
    mongorestore --uri mongodb://xiaoyu:heheda@localhost:27017/railway_map?authSource=railway_map --gzip
    docker run --rm -v /home/blue/github/docker-compose/mongo/dump/:/backup mongo bash -c 'mongorestore /backup --uri mongodb://xiaoyu:heheda@localhost:27017/railway_map?authSource=railway_map --gzip'
    mongorestore -v --gzip -d railway_map -u xiaoyu -p heheda

``` mongo
db.createUser({ 
    user: 'admin', 
    pwd: '123', 
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });

db.createUser({user:"admin",pwd:"123",roles:[{role:"userAdminAnyDatabase",db:"admin"}]});

db.createUser(
  {
    user: "xiaoyu",
    pwd: "heheda",
    roles: [ { role: "readWrite", db: "railway_map" }]
  }
)
```

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
