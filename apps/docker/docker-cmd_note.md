
命令
---

### docker

``` shell
### 显示镜像列表
docker image ls

### 删除所有容器(remove all docker containers)
# -a 列出所有, 默认只列出run的, -q 仅显示id
docker rm $(docker ps -a -q)
```

### docker-compose

``` shell
# 启动
docker-compose up
# 后台启动(detached mode)
docker-compose up -d
# 查看
docker-compose ps
# 停止
docker-compose down
```
