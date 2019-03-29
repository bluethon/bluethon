Ansible Note
============

CMD
---

    ansible-playbook --syntax-check                     语法检查
    ansible-playbook playbook.yml --list-hosts          预检查影响哪些host

PlayBook
--------

### command/shell

- 返回值需要为0
  - 忽略返回值
    - ignore_error: True
- 可换行, 直接回车
- 变量使用(vars)
  - {{ var }}
