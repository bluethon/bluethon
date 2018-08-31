Docker-compose Note
===================

CMD
---

``` shell
pip install docker-compose              # install

docker-compose config                   # 查看设置

docker-compose up --build               # 需要重新build时(第二次有改动时)
docker-compose up -d <service>          # 仅部分启动
docker-compose down -v                  # 移除volume
docker-compose down --rmi local         # 移除image
docker-compose down --rmi all           # 移除所有compose包含image, 慎用
```
