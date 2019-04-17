# 继承的镜像:tag
FROM python:3

LABEL maintainer='bluethon j5088794@gmail.com'

ENV FLASK_APP=manage.py \
    FLASK_CONFIG="production" \
    APP_PORT=9000 \
    PROJECT_DIR=/app

RUN sed -i 's/[[:alpha:]]*.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update \
    && apt-get install -y --no-install-recommends cron \
    && rm -rf /var/lib/apt/lists/*

# 执行命令并构建新的镜像层
RUN pip install -r /tmp/requirements.txt -i https://pypi.douban.com/simple

# 切换目录
WORKDIR $PROJECT_DIR

# 复制文件(当前磁盘目录 to 容器内目录)
COPY . .

# cron
RUN echo '0  2  *  *  *    flask daily' | crontab -

EXPOSE $APP_PORT

# 运行容器时，可以指定--restart always选项。
# 这样的话，容器崩溃时，Docker守护进程(docker daemon)会重启容器。
# 对于需要长时间运行的容器，这个选项非常有用。
# 但是，如果容器的确在运行，但是不可(陷入死循环，配置错误)用怎么办？
# 使用HEALTHCHECK指令可以让Docker周期性的检查容器的健康状况。
# 我们只需要指定一个命令，如果一切正常的话返回0，否则返回1。
# 对HEALTHCHECK感兴趣的话，可以参考这篇博客
# https://blog.newrelic.com/2016/08/24/docker-health-check-instruction/
HEALTHCHECK CMD curl --fail http://localhost:$APP_PORT || exit 1

# fix permission deny
# > https://github.com/composer/docker/issues/7#issuecomment-370086150
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]

# 设置容器启动后默认执行的命令及参数
# CMD能够被 docker run 后的参数覆盖
# 必须使用双引号
# 数组形式
CMD ["python", "./chapter3/section1/hello.py"]
CMD ["flask", "run"]
CMD gunicorn -c ./instance/gunicorn_config.py manage:app
