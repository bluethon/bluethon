Docker-compose Note
===================

CMD
---

``` shell
pip install docker-compose              # install

docker-compose config                   # 查看设置

docker-compose up --build               # 需要重新build时(第二次有改动时)
docker-compose up -d <service>          # 仅部分启动
```
