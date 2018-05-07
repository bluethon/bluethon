#!/bin/bash

make_file_link () {
    file=$1
    link=$2

    # 如果是文件
    # if [ -f $link ]; then
    # 如果存在
    if [ -e $link ]; then
        mv $link $link.bak
        # rm $link
    fi
    ln -sf $file $link
}

CWD=$(/bin/pwd)
des=/etc/shadowsocks-libev/config.json
echo $CWD
make_file_link $CWD/ss_config.json $des
