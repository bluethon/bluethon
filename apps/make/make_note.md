Make Command
============

## TODO

``` makefile
objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs
```

CMD
---

``` shell
make -n all                     # -n 预览要执行的命令
make -k all                     # 忽略错误继续
    --no-print-directory        # 不输出文件夹路径
```

自动变量(Automatic Variables)
-------

    $@          指代目标, 即`make foo`中的 foo
    $*          指代%匹配的部分

Note
----

> <https://seisman.github.io/how-to-write-makefile/overview.html>


### 忽略错误

    # 命令前加- 可以忽略失败继续执行, 另外可以make -k
    -echo 123

### 调用子make方式(使子 make 的 cd 生效)

    $(MAKE) -C <DIR> foo

### 捕获子make错误

    make || exit "$$?"

### MakeFile中变量以`$`开头, Shell变量`$$`开头

### 每行一个进程, 所以不同行变量不传递, 多行需要写在一行, `; \`

``` Makefile
DD = fw

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
