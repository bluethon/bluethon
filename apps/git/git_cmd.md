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
```
