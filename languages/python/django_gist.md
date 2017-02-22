Django常用代码片段
================

### 获取model中field的verbose_name

``` python
model._meta.get_field(field_name).verbose_name
```

Template
--------

### 模板中使用数组

``` python
array.0
array.1
```
