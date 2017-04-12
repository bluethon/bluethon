#!/bin/bash

#------------------
# 放到根目录的scripts文件夹下执行
#----------------------

CWD=$(dirname $(readlink -f $0))

source $CWD/../venv/bin/activate

pip freeze | grep -i 'web.py\|jinja2\|mysql-python\|requests' > $CWD/../requirements.txt

deactivate
