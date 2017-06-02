#!/bin/bash

################
# 必须使用bash
#
# > https://stackoverflow.com/a/34752001/4757521
################

python_script='
import sys
d = {}                                    # create a context for variables
exec(open(sys.argv[1], "r").read()) in d  # execute the Python code in that context
for k in sys.argv[2:]:
  print "%s\0" % str(d[k]).split("\0")[0] # ...and extract your strings NUL-delimited
'

read_python_vars() {
  local python_file=$1; shift
  local varname
  for varname; do
    IFS= read -r -d '' "${varname#*:}"
  done < <(python -c "$python_script" "$python_file" "${@%%:*}")
}


# user                            文件内变量名:脚本内名称
read_python_vars /path/to/file.py py_foo:foo py_bar

echo $foo
echo $py_bar
