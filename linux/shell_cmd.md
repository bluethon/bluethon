Shell Commands
==============

Usage
-----

``` shell

### current directory
CWD=$(dirname $(readlink -f $0))

### 试试查看文件末尾
less +F ...

### 查看service 信息
service --status-all

### tar exclude 打包 排除 
tar -cvf name dir1 --exclude dir2

### 查看文件夹大小
du -sh .
du -sh *    #list all files

### copy keep own perrmission 复制 移动 保留权限
# -p     same as --preserve=mode,ownership,timestamps
cp -rp foo bar

### change shell
sudo chsh username -s /bin/zsh

### 7z 解压
sudo apt install p7zip
# x 解压 -o 设置解压目录(注意中间没有空格)
7z x foo.7z -onew_folder

### scp 复制
# 复制文件file到vps主机的用户目录
scp file vps:
# remote to remote
# host1的默认用户目录 to host2的./foo/bar
scp -3 host1: host2:foo/bar

### 进程名称 查看进程信息
ps -ef | grep '[f]oobar'
# -a 所有
pgrep -a foobar
pgrep -fl foobar

### 通过端口 查看端口占用(注意权限, 否则可能会看不到)
sudo lsof -i:8118
sudo netstat -ano | grep 8118

### 获取发行版名称 ubuntu release version
# 添加源时使用
lsb_release -cs
echo $(lsb_release -cs) > foo.txt


### I/O写入文件 支持sudo tee
# -a  add 追加
echo 'foo' | tee bar.txt
echo 'foo' | tee -a bar.txt
```
