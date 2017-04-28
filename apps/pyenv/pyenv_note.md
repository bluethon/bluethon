pyenv notes
===========

Installation
------------

### Install

    $ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
    $ exec $SHELL           # restart shell

### Upgrade

    $ pyenv update

### Remove

    $ rm -fr ~/.pyenv

and remove below

    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Usage
-----

### install python

    pyenv install 3.6.1

### use virtualenv()

virtualenvwrapper版本不需要, 已可以自动激活

    pyenv virtualenv 3.6.1 venv

显示当前python版本

    pyenv version

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
