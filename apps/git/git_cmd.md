Git Common Use Command
======================

CMD
---

``` shell
### change directory
git -C /path/to/dir                                 # 指定git文件夹

### git checkout
git checkout <branch> -- <file>                     # 从其他分支提取文件

### git tag
git tag
    -l                                              # list
    --sort=-v:refname                               # 名称逆序(-)排列, .10 > .1
                                                    # https://stackoverflow.com/a/22634649/4757521
git tag -l --sort=-v:refname                        # tag sort by order v.x.y.z

### git branch
git push -d <remote> <branch>                       # 删除远程分支(remote branch)
git branch -d <branch>                              # 删除分支
git branch -D <branch>                              # 强制删除未合并分支
git branch -u origin/<branch> <local-branch>        # 设定默认拉取分支
git branch -f <branch-name> [<start-point>]         # --force 强制重置X分支到Y提交

### git clean
git clean -n                                        # 预览要清除的文件
git clean -f                                        # 清理合并产生的额外文件

### git diff
git diff
    --ours                                          # 对比改动和当前分支差异
    --base                                          # 和共同祖先对比
    -b                                              # 忽略空格造成的差异
    --cached/--staged                               # stage
    --name-only                                     # 仅文件名
git diff dev v1.2 -- foo/bar.txt                    # 对比两个commit的特定文件
git diff --name-only --cached                       # 已add的文件名

git reset                                           # 重置HEAD指针到某次提交
    HEAD^                                           # 上个版本
    HEAD~5                                          # 5个版本前
    322455                                          # 到特定commit
    'HEAD@{1}'                                      # 撤销刚才操作的reset(具体看reflog)
    --soft [HEAD]                                   # 仅HEAD指针
    [--mixed] [HEAD]                                # HEAD指针和INDEX
    --hard [HEAD]                                   # 全部, HEAD指针 index work
    --hard origin/dev                               # 重置当前分支头到指定分支头

git log --graph --oneline --decorate                # decorate 显示branch HEAD
        --tags                                      # 显示Tag
        --all                                       # 显示所以分支
        --left-right                                # 以左右改动格式显示
        --merge                                     # 只显示冲突的提交
        -p                                          # 显示代码详情
git log --oneline --left-right --merge -p           # 显示冲突内容

git stash save -u 'message'                         # 以message标记保存, 包含untracked file
git stash list                                      # 查看序号
git stash pop/apply stash@{n}                       # 弹出/应用 n序号的stash

git ls-files -u                                     # show unmerged files(显示未合并文件)

git show <branch>:/path/to/file > foo               # [#1]获取其他分支的文件到foo
git show :1:/path/to/file > foo                     # Stage1 共同祖先
git show :2:/path/to/file > foo                     # Stage2 yours
git show :3:/path/to/file > foo                     # Stage3 theirs

git push origin :[branch2]                          # 删除远程分支
git rm --cached <FILENAME>                          # untrack file

git describe --tags `git rev-list --tags --max-count=1` | sed 's/.*-v//'
                                                    # 获取最新tag

git blame <file>                                    # 文件每行改动
          -L 5,10                                   # Look, 看5,10行内容
```

TODO
----

``` shell
git remote set-url origin [new-url]         # 更新origin url

git fetch --all --prune                     # 更新已删除的远程分支
git branch -a

git init                            # Git本地新建repository

git reflog                          # 查看命令记录
git diff HEAD --[filename]          # 查看工作区和版本库最新版本区别
git checkout -- [file]              # 丢弃工作区的修改, 退回最近一次add 或者 commit 状态  与创建分支区分
git rm [file]                       # 删除stage区域的文件
git checkout -b [name]              # 创建分支 -b参数表示创建并切换
git checkout [name]                 # 切换分支
git branch                          # 查看当前分支
git branch -a                       # 查看远程库的分支
git merge [name]                    # 合并[name]分支到当前分支  如果可能, Git优先使用"Fast forward"模式 快速但是合并后 分支信息丢失
git merge --no-ff -m "dev message" [dev_name]
                                    # 合并分支 --no-ff模式 可以保留分支信息

git remote -v                       # 查看远程库信息

git push origin [branch-name]       # 推送本地分支
git checkout -b origin/[branch-name] [branch-name]
                                    # 本地创建远程分支的对应分支(本地分支和远程分支名称最好一致)

git branch -u origin/<remote-branch> <local-branch>
                                    # 建立本地分支和远程分支的关联

git pull <远程主机名> <远程分支>:<本地分支>
                                    # 从远程抓去分支信息
git pull origin master              # 若为当前分支 可省略:<本地分支>
git pull origin                     # 若当前分支建立upsteam联系 可省略<远程分支>
git pull                            # 若只track了一个追踪分支 <远程主机名>可省略
git fetch origin/[branch-name]      # 本地添加远程分支

git tag [name]                      # 给当前分支的最新commit打标签
git tag                             # 查看所有标签
git tag v1.0 [commitID]             # 给历史commit打标签
git tag -a v1.1 -m "version 1.1 released" [commitID]
                                    # 给历史commit打标签(带备注)
git show [tagname]                  # 查看单个标签详细信息
git tag -d [v0.1]                   # 删除标签
git push origin [v1.0]              # 标签默认本地 推送远程
git push origin --tags              # 一次推送全部标签

git tag -d v0.9                     # 删除远程标签
git push origin :refs/tags/v0.9

git remote rename [origin] [new]    # 修改远程主机名称

git stash                           # 缓存当前工作区
git stash list                      # 查看
git stash apply                     # 恢复缓存区(不删除stash)
git stash drop                      # 删除缓存区
git stash pop                       # 恢复缓存区(删除stash)
```

[#1](https://stackoverflow.com/a/2364223/4757521)
