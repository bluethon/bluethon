MongoDB in docker Note
======================

> https://blog.igevin.info/posts/docker-mongo-auth/

### create Docker Compose

``` dockerfile
version: '2'
services:
  mongo:
    # restart: always
    container_name: 'mongo'
    image: mongo:3.2
    command: [--auth]
    ports:
      - "27017:27017"
    volumes:
      - /data/db
```

### up

    docker-compose up -d
    docker-compose ps

### create admin

    #               容器名 cmd   `admin`数据库
    docker exec -it mongo mongo admin

``` js
db.createUser({ 
    user: 'mongo-admin', 
    pwd: 'admin-initial-password', 
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
```

退出

### 创建指定数据库的用户

    # start mongo
    docker exec -it mongo mongo admin
    # auth
    db.auth("mongo-admin","admin-initial-password")
    # change db
    use test

``` js
db.createUser(
  {
    user: "gevin",
    pwd: "gevin",
    roles: [ { role: "readWrite", db: "test" },
             { role: "readWrite", db: "test2" } ]
  }
);
```
