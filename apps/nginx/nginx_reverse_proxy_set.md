Nginx反向代理设置小记
===================

> 作为反向代理的Nginx记为Nginx-Reverse(NR), 作为静态资源的Nginx记为Nginx-Static(NS)

> [主力Nginx教程(推荐)](https://openresty.org/download/agentzh-nginx-tutorials-zhcn.html)

Note
----

### location ^~ <reg>

匹配开头为`reg`的URI, 在其他正则匹配前优先匹配

### 使用`map`创建自定义变量

``` nginx
map $http_mode $MODE {
    default "PRD";
    ~.      $http_mode;
}
```

如果http header中mode有值(`~.`匹配), 则`$MODE`值等于该值, 否则默认为`PRD`

### Nginx内置绑定变量

> <https://moonbingbing.gitbooks.io/openresty-best-practices/content/openresty/inline_var.html>

### Docker Openresty(Nginx包含echo模块)

> <https://github.com/openresty/docker-openresty>

### `try_files`命令执行顺序

> <https://openresty.org/download/agentzh-nginx-tutorials-zhcn.html#02-NginxDirectiveExecOrder11>

    try_files $uri $uri/index.html =404;

依次尝试前N-1项文件是否存在, 否则无条件内部跳转第N项, 即使DEBUG模式输出为try, 实际行为仍然是内部跳转

### 目录与文件

Nginx识别URI为目录和文件看末尾是否包含`/`, 文件末尾无`/`

### 将所有非静态文件末尾重定向到带`/`路由

> <https://stackoverflow.com/a/3912675/4757521>

``` nginx
server {
    rewrite ^([^.]*[^/])$ $scheme://$http_host$1/ permanent;
}
```

坑
---

### NS正常配置读取不到NR自定义的`http header`

NR转发部分配置如下

``` nginx
location / {
    proxy_pass http://example.com;
    proxy_set_header MODE 'TEST';
    proxy_set_header INDEX_HOST 'example.com:8080';
}
```

理论上NS上使用`http_index_host`即可读取到上述自定义header, 但Nginx默认要求自定义header不能使用下划线命名, 导致NS会丢弃这些自定义header, 避免此问题的方法如下:

- 使用`foo-bar`, 避免`foo_bar`(我选用此项)
- 配置中http部分 增加`underscores_in_headers on`
- `ignore_invalid_headers on;`

### Chrome报`invalid_redirect`

> [重定向Doc](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Redirections)

重定向链接没有包含`$scheme`, 即`http://` or `https://`
