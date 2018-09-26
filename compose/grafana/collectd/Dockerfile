FROM alpine:latest

RUN sed -i 's#http://dl-cdn.alpinelinux.org#https://mirrors.ustc.edu.cn#g' /etc/apk/repositories
RUN apk add --no-cache collectd collectd-disk py3-pip
RUN pip3 install envtpl -i https://pypi.douban.com/simple

COPY collectd.conf.tpl /etc/collectd/collectd.conf.tpl

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD collectd -f
