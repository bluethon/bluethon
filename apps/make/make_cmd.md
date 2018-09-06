Make Command
============

CMD
---

``` shell
make -n all                     # -n 预览要执行的命令
make -k all                     # 忽略错误继续
```

自动变量(Automatic Variables)
---------

    $@          指代目标, 即make foo中的foo
    $*          指代%匹配的部分

Note
----

> <https://seisman.github.io/how-to-write-makefile/overview.html>

### MakeFile中变量以`$`开头, Shell变量`$$`开头

### 每行一个进程, 所以不同行变量不传递, 多行需要写在一行, `; \`

``` Makefile
DD = fwefrgg

all:
    @CC=arm-linux-gcc; \
    echo $$CC
    @echo ${DD}
```

### 代码位置

``` Makefile
xx = xx1            # makefile code, 可以有空格
xx=xx2            # makefile code
xx=$(shell xxxxx)   # shell code
yy:
    xx=xx3    # shell code, 不允许变量赋值时两边有空格
```
