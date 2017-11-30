docker
------

``` shell
docker run --name web_dev -it -p 9000:9000
    -p 3141:3141 dongweiming/web_develop:dev /bin/zsh
                                        # --name, 指定容器名称, 默认随机
                                        # -it, i：交互，t：tty
                                        # -p, 显式暴露特定端口
                                        # image:tag
                                        # /bin/zsh, 登录的默认Shell
docker start web_dev                    # 启动容器
docker attach web_dev                   # 登录

docker image ls                         # 显示镜像列表
docker images                           # 显示镜像列表(等价)
docker --version                        # 显示版本
docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
                                        # 显示容器IP

docker rm $(docker ps -a -q)            # 删除所有容器(remove all docker containers)
                                        # -a 列出所有, 默认只列出run的, -q 仅显示id

docker pull dongweiming/web_develop:dev # 下载dwm的web_develop镜像, Tag是dev
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
