[TOC]
# 重装步骤
=======
## QQ
- 下载
[下载地址](http://www.ubuntukylin.com/applications/showimg.php?lang=cn&id=23)
- 安装
1 在wine-qqintl目录下打开终端输入：
`sudo dpkg -i fonts-wqy-microhei_0.2.0-beta-2_all.deb ttf-wqy-microhei_0.2.0-beta-2_all.deb wine-qqintl_0.1.3-2_i386.deb`
2 如果报依赖错误，输入：
`sudo apt-get install -f`
3 自动解决依赖后再执行步骤1
## Chrome
- 下载
[下载地址](http://down.tech.sina.com.cn/page/43719.html)
## Vim
`wget -qO- https://raw.github.com/ma6174/vim/master/setup.sh | sh`
>a. 多窗口操作
:sp + 文件名水平分割窗口
:vs + 文件名垂直分割窗口
Ctrl+w快速切换窗口
b. Taglist和NerdTree
F3：快速打开或关闭树形目录
F9：查看当前代码结构及自动补全
c. 其他
F5：一键运行程序
F6：代码格式化
F8：调试C和C++
F2：去除代码中的空行(个人觉得不实用)

## 其他
[见此](http://www.cnblogs.com/xionghj/p/4211417.html)
