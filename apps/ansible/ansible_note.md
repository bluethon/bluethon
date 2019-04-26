Ansible Note
============

CMD
---

``` sh
ansible-galaxy init /path/to/role       # 初始化一个role
                                        # https://galaxy.ansible.com/docs/contributing/creating_role.html
```

PlayBook
--------

``` sh
ansible-playbook
    -f 10                               # parallelism 10
    --syntax-check                      # 语法检查
    playbook.yml --list-hosts           # 预检查影响哪些host
    --verbose                           # see details
```

### include_role, tags 不执行

> <https://github.com/ansible/ansible/issues/30882#issuecomment-479214591>

``` yml
# 1
- include_tasks:
    file: whatever.yml
    apply:
      tags:
        - tag_for_included_tasks
  tags:
    - tag_for_include
# 2
- include_tasks:
    file: whatever.yml
    apply:
      tags:
        - tag_for_included_tasks
  tags:
    - always
```

### local execute

> <http://willthames.github.io/2018/07/01/connection-local-vs-delegate_to-localhost.html>

``` yml
# 1, 切换连接, 最合适
# https://docs.ansible.com/ansible/latest/plugins/connection/local.html
# 在task中指定
connection: local
# 在var中指定
ansible_connection: local
# 2, 切换指定执行的server, localhost是特例
delegate_to: localhost
# 3, 不推荐
local_action: <shell>

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

### 循环复制template文件

> <https://serverfault.com/a/640139/380738>

`fileglob`默认找的是`files`路径下的文件

``` yml
- name: deploy api compose
  template:
    src: '{{ item }}'
    dest: '{{ path }}/{{ item | basename | regex_replace("\.j2$","") }}'
  with_fileglob:
    - '{{ role_path }}/templates/*.j2'
    - '{{ role_path }}/templates/.*.j2'
```
