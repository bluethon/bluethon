Autoenv Note
------------

### Install

``` sh
sudo pip install autoenv
echo "source `which activate.sh`" >> ~/.zshrc
```

### Usage

touch $project/.env

``` sh
cwd=$(dirname $(readlink -f $0))
source $cwd/venv/bin/activate
```
