Git Common Use Command
======================

``` shell

git branch -u origin/<branch> <local-branch>        # 设定默认拉取分支

### git reset
#   重置HEAD指针到某次提交
git reset HEAD~1
git reset --soft [HEAD]                             # 仅HEAD指针
git reset [--mixed] [HEAD]                          # HEAD指针和INDEX
git reset --hard [HEAD]                             # 全部, HEAD指针 index work
git reset --hard origin/dev                         # 重置当前分支头到指定分支头
git log --graph --oneline --decorate                # decorate 显示branch HEAD
git branch -f <branch-name> [<start-point>]         # --force 强制重置X分支到Y提交
git stash save -u 'message'                         # 以message标记保存, 包含untracked file
git stash list                                      # 查看序号
git stash pop/apply stash@{n}                       # 弹出/应用 n序号的stash

git show <branch>:/path/to/file > foo               # [#1]获取其他分支的文件到foo

git push origin :[branch2]                          # 删除远程分支
git rm --cached <FILENAME>                          # untrack file

git describe --tags `git rev-list --tags --max-count=1` | sed 's/.*-v//'
                                                    # 获取最新tag
```

[#1](https://stackoverflow.com/a/2364223/4757521)
