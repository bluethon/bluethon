Linux Shell读书笔记
==================

Chapter 1
---------

### 显示当前shell类型 - P9

    echo $0
    echo $ SHELL

### 检查当前用户是否为root(==0)

    $UID

### Fork炸弹(递归)

    :(){ :|:& };:

限制

    /etc/security/limits.conf

### 导出函数

可以像环境变量一样导出, 作用域可以扩展到子进程

    export -f <fname>

### read 读取字符 不使用回车

``` sh
# 读取n个字符, 存入变量
read -n 2 var
echo $var

# 读取密码, 无回显
read -s var

# 提示信息
read -p "Enter input:" var

# 限时输入
read -t 3 var

# 自定义结束符, 此处为`:`
read -d ":" var
```

### 返回值

true是/bin下的