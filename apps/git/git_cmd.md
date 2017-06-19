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
git log --graph --oneline --decorate                # decorate 显示branch HEAD
git branch -f <branch-name> [<start-point>]         # --force 强制重置X分支到Y提交
git stash save -u 'message'                         # 以message标记保存, 包含untracked file
git stash list                                      # 查看序号
git stash pop/apply stash@{n}                       # 弹出/应用 n序号的stash
```
