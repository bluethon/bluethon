Cmd Note
=========

template
--------

### note

``` django
&copy;                  # 图标
{% now 'Y' %}           # 年
{% lorem %}             # 占位字符
<a role="button">       # 语义强调?
{% url 'foo' 'bar' %}   # view name + param
```

py
---

### Set environ

    export DEBUG=on
    unset DEBUG

### use the template with `startproject`

使用自定义模板生成新项目

**注意模板使用{{ secret_key }}**

    django-admin.py startproject <foo> --template=project_name

### use Gunicorn and set output to console

    gunicorn hello --log-file=-

### django.contrib.staticfiles

加入`INSTALLED_APPS`, 引入

    {% static %}
    collectstatic       # shell命令

### ch3 generate static file

    python prototypes.py build
    cd _build
    python -m http.server 9000
