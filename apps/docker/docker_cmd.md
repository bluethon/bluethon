docker cmd
----------

``` shell
docker run --name web_dev -it -p 9000:9000
    -p 3141:3141 dongweiming/web_develop:dev /bin/zsh
                                        # --name, 指定容器名称, 默认随机
                                        # -it, i：交互，t：tty
                                        # -p, 显式暴露特定端口
                                        # image:tag
                                        # /bin/zsh, 登录的默认Shell
    -d                                  # daemon 后台运行
docker start web_dev                    # 启动容器

docker image ls                         # 显示镜像列表
docker image rm [option] <image1> [<image2> ...]    # 删除本地镜像

docker images                           # 显示镜像列表(等价)
docker --version                        # 显示版本
docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
                                        # 显示容器IP

docker rm $(docker ps -a -q)            # 删除所有容器(remove all docker containers)
                                        # -a 列出所有, 默认只列出run的, -q 仅显示id

docker pull dongweiming/web_develop:dev # 下载dwm的web_develop镜像, Tag是dev

docker volume create <vol>              # 创建数据卷
docker volume inspect <vol>             # 查看数据卷信息
docker volume ls                        # 查看所有数据卷
docker volume prune                     # 清除无主的数据卷

docker logs <container>                 # 查看容器输出(run -d后台运行时)

docker attach <container>               # 进入容器(退出后容器停止)
docker exec -it <container> bash        # 进入容器(退出后容器不停止) 推荐

docker container rm <container>         # 删除容器
    -f                                  # 结束运行状态的容器(发送SIGKILL信号)
docker container prune                  # 清除所有终止状态额容器

docker build -t <name>[:<tag>] <path>   # 根据Dockerfile构建镜像
            -t                          # tag
```

Note
----

### RUN vs CMD

> https://ibm.co/2BR8Yqr

CMD和ENTRYPOINT推荐使用Exec格式, 因为指令可读性更强, 更易理解  
RUN则两种都可以

Shell格式

- <instruction> <command>
- 底层调用 /bin/sh -c <command>
- 变量会被解析

Exec格式

- <instruction> ["executable", "param1", "param2", ...]
- 直接调用<command>
- 变量不会被解析

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
