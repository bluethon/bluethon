#GitHub部分
#--------------------

#创建SSH key
ssh-keygen -t rsa -C "youremail@example.com"
#默认存在User目录下.ssh\
#GitHub->Account Setting->SSH Keys->id_rsa.pub

#本地库关联到GitHub  origin为远程仓库名称,可以修改
git remote add origin git@github.com:Bluethon/bluegit.git

#推送 显式建立本地master与远程master分支关联
git push -u origin master
#提交[branch1]为远程的[branch2]
git push origin branch1:branch2
#删除远程分支
git push origin :[branch2]

#更新origin url
git remote set-url origin [new-url]
#----------------------

#Git本地新建repository
git init

#退回之前(后)的文件版本
git reset --hard HEAD^
git reset --hard HEAD~100
git reset --hard 3628164(commit ID)

#查看命令记录
git reflog

#查看工作区和版本库最新版本区别
git diff HEAD --[filename]

#丢弃工作区的修改, 退回最近一次add 或者 commit 状态  与创建分支区分
git checkout -- [file]

#删除stage区域的文件
git rm [file]

#创建分支 -b参数表示创建并切换
git checkout -b [name]

#切换分支
git checkout [name]

#查看当前分支
git branch

#合并[name]分支到当前分支  如果可能, Git优先使用"Fast forward"模式 快速但是合并后 分支信息丢失
git merge [name]

#合并分支 --no-ff模式 可以保留分支信息
git merge --no-ff -m "dev message" [dev_name]

#删除分支
git branch -d [name]

#查看分支合并情况 --图 --单行 --简化commit
git log --graph --pretty=oneline --abbrev-commit

#查看远程库信息
git remote -v

#推送本地分支
git push origin [branch-name]

#本地创建远程分支的对应分支(本地分支和远程分支名称最好一致)
git checkout -b origin/[branch-name] [branch-name]

#建立本地分支和远程分支的关联
git branch --set-upstream origin/[branch-name] [branch-name]

#从远程抓去分支信息
git pull

#本地添加远程分支
git fetch origin/[branch-name]

#查看远程库的分支
git branch -a

#删除标签
git tag -d [v0.1]

#标签默认本地 推送远程
git push origin [v1.0]

#一次推送全部标签
git push origin --tags

#修改远程主机名称
git remote rename [原主机名] [新主机名]
