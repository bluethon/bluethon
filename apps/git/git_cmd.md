Git Common Use Command
======================

``` shell
### git checkout
git checkout <branch> -- <file>                     # 从其他分支提取文件

### git branch
git push --delete <remote> <branch>                 # 删除远程分支(remote branch)
git branch -d <branch>                              # 删除分支
git branch -D <branch>                              # 强制删除未合并分支
git branch -u origin/<branch> <local-branch>        # 设定默认拉取分支
git branch -f <branch-name> [<start-point>]         # --force 强制重置X分支到Y提交

### git clean
git clean -n                                        # 预览要清除的文件
git clean -f                                        # 清理合并产生的额外文件

### git diff
git diff --ours                                     # 对比改动和当前分支差异
         --base                                     # 和共同祖先对比
         -b                                         # 忽略空格造成的差异
git diff dev v1.2 -- foo/bar.txt                    # 对比两个commit的特定文件

git reset                                           # 重置HEAD指针到某次提交
          HEAD^                                     # 上个版本
          HEAD~5                                    # 5个版本前
          322455                                    # 到特定commit
          'HEAD@{1}'                                # 撤销刚才操作的reset(具体看reflog)
          --soft [HEAD]                             # 仅HEAD指针
          [--mixed] [HEAD]                          # HEAD指针和INDEX
          --hard [HEAD]                             # 全部, HEAD指针 index work
          --hard origin/dev                         # 重置当前分支头到指定分支头

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

[#1](https://stackoverflow.com/a/2364223/4757521)
