Alpine Linux
============

Note
----

### 时区

``` docker
FROM alpine:3.6
RUN apk add --no-cache tzdata
ENV TZ Asia/Shanghai
```

    date
    export TZ='Asia/Shanghai'
    date
