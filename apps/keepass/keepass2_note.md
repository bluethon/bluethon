KeePass2
========

### 内容乱码(方块)

> http://www.myjoyoo.com/node/keepass-in-ubuntu

显示内容的乱码，修改字体就行了：Tools --> Options --> Interface --> Select List Fonts，我选择的是：Noto Sans Mono CJK SC

### ubuntu 安装[0]

``` sh
sudo add-apt-repository ppa:jtaylor/keepass
sudo apt-get update
sudo apt install keepass2
```

### http插件(连接chrome)[1]

download the file

``` sh
sudo apt-get install libmono-system-xml-linq4.0-cil libmono-system-data-datasetextensions4.0-cil libmono-system-runtime-serialization4.0-cil mono-mcs
mv KeePassHttp.plgx /usr/lib/keepass2
```

### 汉化

> <http://keepass.info/translations.html>

copy to `~/.local/share/KeePass`

[0]: https://launchpad.net/~jtaylor/+archive/ubuntu/keepass
[1]: https://github.com/pfn/keepasshttp/
