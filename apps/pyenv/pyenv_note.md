pyenv notes
===========

CMD
---

``` sh
pyenv install -l                        # 可安装版本
pyenv global 3.6.7                      # 设定默认版本
```

Installation
------------

### Install(OSX)

    brew install pyenv
    # .zshrc
    eval "$(pyenv init -)"

### Install(Linux)

    $ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

    # add below
    export PATH="/home/<user>/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    $ exec $SHELL           # restart shell

### Upgrade

    cd ~/.pyenv
    git pl

or

    pyenv update

### Remove

    $ rm -fr ~/.pyenv

    # and remove below
    export PATH="/home/<user>/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Usage
-----

### install python

    # before
    sudo apt install libbz2-dev libsqlite3-dev libreadline-dev

    pyenv install 3.6.1

### use virtualenv()

virtualenvwrapper 已不需要, virtualenv已可以自动激活

``` sh
# 创建3.6.1的虚拟环境venv
pyenv virtualenv 3.6.1 foo-venv
# 创建当前文件夹名称的环境
pyenv virtualenv 3.6.7 ${PWD##*/}-3.6.7
# 将当前目录 设定为某个名称的虚拟环境
pyenv local foo-venv

# 查看所有虚拟环境
pyenv virtualenvs
# 显示当前python版本
pyenv version
```

### remove

    pyenv uninstall venv

dependence
----------

> <https://github.com/pyenv/pyenv/wiki/Common-build-problems>

``` sh
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev
```
