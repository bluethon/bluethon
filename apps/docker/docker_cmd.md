docker cmd
==========

CMD
---

``` shell
docker run
    dongweiming/web_develop:dev /bin/zsh
    --name <con name>                   # 指定容器名称, 默认随机
                                        # image:tag
    -i                                  # 与容器内容STDIN交互
    -t                                  # 指定一个终端(tty)
    -d                                  # detach 后台运行
    -e A=a                              # 环境变量
    -p <hostP>:<conPort>                # 显式暴露特定端口, 重复-p可绑定多端口
    -v `pwd`/dist:/app/dist             # 映射文件
    -w /path/to/workdir                 # 设定默认目录
    --rm                                # 一次性

docker pull bluethon/foo:bar            # 拉取镜像
docker start web_dev                    # 启动容器
docker system df                        # 占用存储大小
docker info                             # docker系统信息(可查看镜像地址)!
docker logs <container>                 # 查看容器输出(run -d后台运行时)
    - t                                 # 时间戳
    - f                                 # 持续
docker ps [-a]                          # 查看容器状态
docker ps -a --format="table {{.Names}}\t{{.Image}}\t{{.RunningFor}}\t{{.Status}}\t{{.Ports}}"
docker ps | less -S                     # 解决显示换行问题

docker stop $(docker ps -f label=type=fe)
                                        # 组合命令停止某容器
docker stop $(docker ps -a -q)          # 停止所有容器
docker rm $(docker ps -a -q)            # 删除所有容器(remove all docker containers)
                                        # -a 列出所有, 默认只列出run的, -q 仅显示id

docker cp <conId>:/path/within/con /host/path/target
                                        # 从容器内拷贝文件到主机上

docker images                           # 显示镜像列表(等价)
docker image ls                         # 显示镜像列表
docker image prune                      # 删除dangling镜像(虚悬, <none>)
docker image rm [option] <image1> [<image2> ...]
                                        # 删除本地镜像
docker rmi $(docker images | grep '^<none>' | awk '{print $3}')
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
                                        # 删除<none>的镜像
docker images | awk '$2~/<tag>/{print $1":"$2}'
                                        # 通过正则(~)查找tag列($2)的镜像

docker --version                        # 显示版本
docker config
docker stats                            # 容器整体运行状态
docker system prune                     # 系统清理
    --filter until=240h                 # 清除10天前数据, 单位(h, m, s)

docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
                                        # 显示容器IP
docker inspect --format '{{ .Id }}' <container name>
                                        # 获得容器完整ID
docker inspect -f "{{ .RestartCount }}" <con-id>
                                        # 容器重启次数
docker inspect -f "{{ .State.StartedAt }}" <con-id>
                                        # 上次重启时间
docker inspect -f \
   '{{range $index, $value := .Config.Env}}{{$value}} {{end}}' container_name
                                        # 打印环境变量(空格)
docker inspect -f \
    '{{range $index, $value := .Config.Env}}{{println $value}}{{end}}' \
    <name>
                                        # 打印环境变量(多行)
docker inspect -f "{{ .HostConfig.RestartPolicy }}" <name>
                                        # 重启策略(restart policy)
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
                                        # IP

docker volume create <vol>              # 创建数据卷
docker volume inspect <vol>             # 查看数据卷信息
docker volume ls                        # 查看所有数据卷
docker volume prune                     # 清除无主的数据卷
    --filter "label!=keep"              # 通过标签过滤, 不等于keep, ls中不适用

docker attach <container>               # 进入容器(退出后容器停止)
docker exec -it <container> bash        # 进入容器(退出后容器不停止) 推荐

docker container rm <container>         # 删除容器
    -f                                  # 结束运行状态的容器(发送SIGKILL信号)
docker container prune                  # 清除所有终止状态额容器

docker build -t <name>[:<tag>] <path>   # 根据Dockerfile构建镜像
    -t                                  # tag
    -f <file>                           # 指定Dockerfil

docker network create <name>            # 创建网络
docker network inspect <name>           # 查看网络内的信息, 主机IP等

docker save -o foo.tar <image:tag>      # 离线保存镜像为文件(丢失分层)
docker save <image:tag> | pv | pigz > f.tgz
                                        # 导出为压缩包
docker load -i f.tgz                    # 导入压缩包
```

Note
----

### RUN vs CMD

> <https://ibm.co/2BR8Yqr>

CMD和ENTRYPOINT推荐使用Exec格式, 因为指令可读性更强, 更易理解
RUN则两种都可以

Shell格式

- `<instruction> <command>`
- 底层调用`/bin/sh -c <command>`
- 变量会被解析

Exec格式

- `<instruction> ["executable", "param1", "param2", ...]`
- 直接调用`command`
- 变量不会被解析

### docker-compose

``` shell
docker-compose up                       # 启动
docker-compose up -d                    # 后台启动(detached mode)
docker-compose ps                       # 查看
docker-compose down                     # 停止
docker-compose down -v                  # 删除volumes
docker-compose down --rmi <local/all>   # 删除images
```

### docker ps

    # table for title
    docker ps --format "table {{.ID}}\t{{.Labels}}"

    Placeholder     Description
    .ID
    .Image
    .Command
    .CreatedAt      标准时间
    .RunningFor     Elapsed time since the container was started.(多少天前)
    .Ports
    .Status
    .Size
    .Names
    .Labels
    .Label          Eg: '{{.Label "com.docker.swarm.cpu"}}'
    .Mounts
    .Networks
