Git学习笔记
===========

Error
-----

### clean commit(history, big file)

``` shell

# 查看大文件
# https://stackoverflow.com/a/42544963/4757521
git rev-list --objects --all \
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| sed -n 's/^blob //p' \
| sort --numeric-sort --key=2 \
| cut -c 1-12,41- \
| $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest

### method 1
# 匹配包含foo的
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch $(find ./ -type d -name "*foo*)' \
--prune-empty --tag-name-filter cat -- --all
# path
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch /path/to/foo' \
--prune-empty --tag-name-filter cat -- --all
### method 2(默认不删除HEAD, 需要加 ----no-blob-protection)
java -jar ~/programs/bfg-1.13.0.jar --delete-files foo.py <repo>
# 删除文件夹, 但不能指定路径(!!!重名会存在问题)
java -jar ~/programs/bfg-1.13.0.jar --delete-folders foo <repo>

# repack, (删除历史后刷新, 使查看大文件命令应用新的内容)
git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin

# 强推(然后其他人clone)
git push origin --force --tags
git push origin --force --all

# gc
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

### Permission denied (publickey)

Host必须是`github.com`, 否则匹配不到config, 可注意`-vT`顶部是否匹配

    # test
    ssh -vT git@github.com

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa_xxx

    ssh-add -l
    ssh-add -l -E md5

### commit case-sensitive only filename changes

> <https://stackoverflow.com/a/20907647/4757521>

    git mv OldFileNameCase newfilenamecase

Note
----

### gitignore template

<https://github.com/github/gitignore>

### 给命令配置别名(配置global则针对整个git 存在用户目录下.gitconfig)

``` bash
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
# pull 默认使用变基
git config --global pull.rebase true
```

### fork后增加原始库remote, 并同步代码

    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
    git fetch upstream
    git checkout <branch>
    git merge upstream/master

### 修改分支名称(没有old 默认当前分支), 包括远程分支

> <http://stackoverflow.com/a/6591218/4757521>

    git branch -m [old] new
    git push -f --mirror

### checkout最新commit

    git checkout <branch>

### 重置修改到特定版本

    git reset --hard [HEAD]

`--hard` 不加入则重置到`HEAD`版本修改后未提交状态, 加入则重置到`HEAD`版本未修改时

> [所有修改方法](http://gitbook.liuhui998.com/4_9.html)

### 安装 设置config

`--global`表示这台机器上所有仓库都使用此配置

``` shell
git config --global user.name "bluethon"
git config --global user.email "j5088794@gmail.com"
# 默认使用vim 编辑merge信息
git config --global core.editor vim
# 只push当前分支
git config --global push.default current
```

### 误提交或者不再跟踪

``` bash
# --cached  仅删除暂存区(index) -r recursive
git rm -r --cached [folder/]
```

### 修改最后一次commit

``` bash
git add -A
git commit --amend -m 'change the last commit'
```

### 编辑config

    git config -e
    git config --global -e

### 查看远程库的分支

`git branch -a`

### 创建分支

`git checkout -b [name]`

### 合并分支 --no-ff模式 可以保留分支信息

`git merge --no-ff -m "dev message" [dev_name]`

### 删除分支

    git branch -d [name]

### 删除远程分支

    git push origin :[branch2]
    git push origin --delete [branch2]

### 将stash的内容新建为tesstchange分支

`git stash branch testchanges`

### [git显示中文为274\288\432](https://gist.github.com/vkyii/1079783)

    git config --global core.quotepath false

Git Bash
--------

MinTTY 不支持交互操作, 需使用`winpty + python`类似, 提示在安装时选择终端方式时有写
> [参考](https://www.zhihu.com/question/36142943/answer/81467036)

GitHub部分
---------

### 比较功能

url末尾加`/compare`

带tag版

    /compare/2a...2b

### 创建SSH key

    ssh-keygen -t rsa -C "youremail@example.com"

默认存在User目录下.ssh

> GitHub->Account Setting->SSH Keys->id_rsa.pub

### 本地库关联到GitHub  origin为远程仓库名称,可以修改

`git remote add origin git@github.com:Bluethon/bluegit.git`

### 推送 显式建立本地master与远程master分支关联

`git push -u origin master`

### 提交[branch1]为远程的[branch2]

`git push origin branch1:branch2`

Git Note
--------

别名 当前仓库.git/config中

> 有些时候，你必须把某些文件放到Git工作目录中，但又不能提交它们，比如保存了数据库密码的配置文件啦，等等，每次git status都会显示“Untracked files ...”，有强迫症的童鞋心里肯定不爽。
好在Git考虑到了大家的感受，这个问题解决起来也很简单，在Git工作区的根目录下创建一个特殊的.gitignore文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。
不需要从头写.gitignore文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：<https://github.com/github/gitignore>

> 使用Windows的童鞋注意了，如果你在资源管理器里新建一个.gitignore文件，它会非常弱智地提示你必须输入文件名，但是在文本编辑器里“保存”或者“另存为”就可以把文件保存为.gitignore了
