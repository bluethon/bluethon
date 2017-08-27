Fcitx Note
==========

install
-------

### 配置中添加sogou键盘

debug
-----

### No such key 'Gtk/IMModule'

> <http://www.cnblogs.com/raybiolee/p/5693279.html>

``` shell
# simple version
vim /usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override
# 把第四行改成
overrides={'Gtk/IMModule':<'fcitx'>}

# all version
mkdir -p extract/DEBIAN
#prepare the environ
# 准备环境
dpkg-deb -x sogoupinyin_2.0.0.0078_amd64.deb extract/
# extract the content files
# 解压出内容文件
dpkg-deb -e sogoupinyin_2.0.0.0078_amd64.deb extract/DEBIAN
# extract the control file
# 解压出控制文件
vi extract/usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override
# correct the file
# change line 4 to overrides={'Gtk/IMModule':<'fcitx'>}
# 更正文件
# 把第四行改成 overrides={'Gtk/IMModule':<'fcitx'>}
dpkg-deb -b extract/ ./sogoupinyin_2.0.0.0078_wkd.deb
# pack the files into deb installer file san save to current dir with name sogoupinyin_2.0.0.0078_wkd.deb
# 重新打包为...
# 无果没有指定文件名，就和原文件名一样，这是在/extract/DEBIAN/control中定义的
sudo gdebi sogoupinyin_2.0.0.0078_wkd.deb
# 安装 install
```
