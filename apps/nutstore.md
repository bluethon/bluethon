# 坚果云

## Linux安装

> <https://www.jianguoyun.com/s/downloads/linux>

Linux官网的版本不能使用, 使用如下命令安装

``` shell
wget https://www.jianguoyun.com/static/exe/installer/nutstore_linux_src_installer.tar.gz
tar zxf nutstore_linux_src_installer.tar.gz
cd nutstore_linux_src_installer && ./configure && make
sudo make install
# 重启Nautilus
nautilus -q
./runtime_bootstrap
```

中途出现包缺失的情况, 按需要安装
