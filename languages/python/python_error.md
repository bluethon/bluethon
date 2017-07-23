错误处理
=======

### No module named pkg_resources
> <https://stackoverflow.com/a/10538412/4757521>

curl https://bootstrap.pypa.io/ez_setup.py | python

### error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

    sudo apt install python3-dev

### ImportError: No module named XXX

> <https://stackoverflow.com/a/2326045/4757521>

To add current dir to python path, use

    export PYTHONPATH=`pwd`

### UnicodeDecodeError: 'ascii' codec can't decode byte

> <https://stackoverflow.com/a/35444608/4757521>

- python2默认decode使用的是ascii, codec(coder & decoder)
- 变量定义统一使用u'', unicode, PS: 这不是utf-8
