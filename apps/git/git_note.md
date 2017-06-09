Git学习笔记
===========

Error
-----

### Permission denied (publickey)

    # test
    ssh -T git@github.com
    ssh -vT git@github.com

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa_xxx
    
    ssh-add -l

常用
---

### 更新origin url

    git remote set-url origin [new-url]

### 更新已删除的远程分支

    git fetch --all --prune
    git branch -a

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

#### 重置修改到特定版本

    git reset --hard [HEAD]
    
`--hard` 不加入则重置到`HEAD`版本修改后未提交状态, 加入则重置到`HEAD`版本未修改时

> [所有修改方法](http://gitbook.liuhui998.com/4_9.html)

#### 安装 设置config

`--global`表示这台机器上所有仓库都使用此配置

``` shell
git config --global user.name "bluethon"
git config --global user.email "j5088794@gmail.com"
# 默认使用vim 编辑merge信息
git config --global core.editor vim
# 只push当前分支
git config --global push.default current
```

#### 误提交或者不再跟踪

``` bash
# --cached  仅删除暂存区(index) -r recursive
git rm -r --cached [folder/]
```

#### 修改最后一次commit

``` bash
git add -A
git commit --amend -m 'change the last commit'
```

#### 编辑config

    git config -e
    git config --global -e

---

Git cmd
-------

### ubuntu 默认中文转为英文 想恢复中文 用#注释掉
`echo "alias git='LANG=en_GB git'" >> ~/.bashrc`

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
`git config --global core.quotepath false`

Git Bash
--------

MinTTY 不支持交互操作, 需使用`winpty + python`类似
提示在安装时选择终端方式时有写
[参考](https://www.zhihu.com/question/36142943/answer/81467036)


GitHub部分
---------

#### 比较功能

url末尾加`/compare`

带tag版

    /compare/2a...2b


#### 创建SSH key

`ssh-keygen -t rsa -C "youremail@example.com"`

默认存在User目录下.ssh

> GitHub->Account Setting->SSH Keys->id_rsa.pub

#### 本地库关联到GitHub  origin为远程仓库名称,可以修改
`git remote add origin git@github.com:Bluethon/bluegit.git`

#### 推送 显式建立本地master与远程master分支关联
`git push -u origin master`

#### 提交[branch1]为远程的[branch2]
`git push origin branch1:branch2`



#### 更新origin url
`git remote set-url origin [new-url]`

Git Note
--------

Git本地新建repository
`git init`

退回之前(后)的文件版本

``` bash
git reset --hard HEAD^
git reset --hard HEAD~100
git reset --hard 3628164(commit ID)
git reset --hard origin/master
```

查看命令记录
`git reflog`

查看工作区和版本库最新版本区别
`git diff HEAD --[filename]`

丢弃工作区的修改, 退回最近一次add 或者 commit 状态  与创建分支区分
`git checkout -- [file]`

删除stage区域的文件
`git rm [file]`

创建分支 -b参数表示创建并切换
`git checkout -b [name]`

切换分支
`git checkout [name]`

查看当前分支
`git branch`
查看远程库的分支
`git branch -a`

合并[name]分支到当前分支  如果可能, Git优先使用"Fast forward"模式 快速但是合并后 分支信息丢失
`git merge [name]`

合并分支 --no-ff模式 可以保留分支信息
`git merge --no-ff -m "dev message" [dev_name]`

删除分支
`git branch -d [name]`
强制删除未合并分支
`git branch -D [name]`


查看远程库信息
`git remote -v`

推送本地分支
`git push origin [branch-name]`

本地创建远程分支的对应分支(本地分支和远程分支名称最好一致)
`git checkout -b origin/[branch-name] [branch-name]`

建立本地分支和远程分支的关联
`git branch -u origin/<remote-branch> <local-branch>`

从远程抓去分支信息
`git pull <远程主机名> <远程分支>:<本地分支>`
 若为当前分支 可省略:<本地分支>
`git pull origin master`
 若当前分支建立upsteam联系 可省略<远程分支>
`git pull origin`
 若只track了一个追踪分支 <远程主机名>可省略
`git pull`

本地添加远程分支
`git fetch origin/[branch-name]`

给当前分支的最新commit打标签
`git tag [name]`
查看所有标签
`git tag`
给历史commit打标签
`git tag v1.0 [commitID]`
给历史commit打标签(带备注)
`git tag -a v1.1 -m "version 1.1 released" [commitID]`
查看单个标签详细信息
`git show [tagname]`
删除标签
`git tag -d [v0.1]`

标签默认本地 推送远程
`git push origin [v1.0]`

一次推送全部标签
`git push origin --tags`
删除远程标签
`git tag -d v0.9`
`git push origin :refs/tags/v0.9`

修改远程主机名称
`git remote rename [原主机名] [新主机名]`

缓存当前工作区
`git stash`
查看
`git stash list`
恢复缓存区(不删除stash)
`git stash apply`
删除缓存区
`git stash drop`
恢复缓存区(删除stash)
`git stash pop`

给命令配置别名(配置global则针对整个git 存在用户目录下.gitconfig)
```
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
```
别名 当前仓库.git/config中



> 有些时候，你必须把某些文件放到Git工作目录中，但又不能提交它们，比如保存了数据库密码的配置文件啦，等等，每次git status都会显示“Untracked files ...”，有强迫症的童鞋心里肯定不爽。
好在Git考虑到了大家的感受，这个问题解决起来也很简单，在Git工作区的根目录下创建一个特殊的.gitignore文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。
不需要从头写.gitignore文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：https://github.com/github/gitignore

>使用Windows的童鞋注意了，如果你在资源管理器里新建一个.gitignore文件，它会非常弱智地提示你必须输入文件名，但是在文本编辑器里“保存”或者“另存为”就可以把文件保存为.gitignore了
