Ansible Note
============

CMD
---

PlayBook
--------

``` sh
ansible-playbook
    -f 10                               # parallelism 10
    --syntax-check                      # 语法检查
    playbook.yml --list-hosts           # 预检查影响哪些host
    --verbose                           # see details
```

### command/shell

- 返回值需要为0
  - 忽略返回值
    - ignore_error: True
- 可换行, 直接回车
- 变量使用(vars)
  - {{ var }}

### notify/handler

- 如果是多通知任务, 按`handler`定义顺序, 而不是`notify`中写的顺序
