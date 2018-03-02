Dockerfile Note
===============

``` Dockerfile
# 继承的镜像:tag
FROM python:3

# 构建者
MAINTAINER bluethon

# 执行命令并构建新的镜像层
RUN echo '[global]' >> pip.conf && \
    echo 'index-url = https://pypi.douban.com/simple' >> pip.conf

# 切换目录
WORKDIR ~/web_develop

# 复制文件(当前磁盘目录 to 容器内目录)
COPY . .

# 设置容器启动后默认执行的命令及参数
# CMD能够被 docker run 后的参数覆盖
# 必须使用双引号
CMD ["python", "./chapter3/section1/hello.py"]

```
