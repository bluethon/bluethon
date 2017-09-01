错误处理
=======

### No module named apt_pkg

> <https://stackoverflow.com/a/36232975/4757521>

系统安装多版本py3时, 默认识别高版本, 但是我的是识别了低版本,
所以需要创建反过来的链接(36m -> 35m)

``` python
# python3-apt checks the highest python version, instead of the current python version in use.
cd /usr/lib/python3/dist-packages
sudo ln -s apt_pkg.cpython-{35m,36m}-x86_64-linux-gnu.so
```

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
