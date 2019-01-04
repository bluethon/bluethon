#!/bin/bash

if condition
then
    cmd;
elif condition; then
    cmd;
else
    cmd;
fi

# 算术比较(中括号间需要空格, 否则会识别为`[`开头的命令)

v=0
[ $v -eq 0 ]    # 等于0
[ $v -ne 0 ]    # 不等于
[ $v -gt 0 ]    # 大于
[ $v -lt 0 ]    # 小于
[ $v -ge 0 ]    # 大于等于0
[ $v -le 0 ]    # 小于等于0

# 实用技巧
[ $v ] && action;    # 为真执行
[ $v ] || action;    # 为假执行

# 多条件
[ $v -ne 0 -a $v -gt 2 ]    # 等价[] && []
[ $v -ne 0 -o $v -gt 2 ]    # 等价[] || []

# 文件系统测试

[ -f $v ]   # 文件
[ -x $v ]   # 可执行
[ -d $v ]   # 目录
[ -e $v ]   #
[ -c $v ]   # 文件
[ -b $v ]   # 文件
[ -w $v ]   # 文件
