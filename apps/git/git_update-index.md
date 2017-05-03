今天遇到一个问题, 我在历史的commit中删除了`venv/`中虚拟环境之前误添加到库的文件
现在希望恢复那个文件夹(但不恢复所有)到本地, 且不再跟踪这些文件, 避免再次被提交
也不想在`git status`中看到(已添加.gitignore)

1. 先找到要恢复的commit

    `git log --oneline`
- 查看某个commit的修改信息

    `git show [commit_id]`
- 取回指定文件(夹)

    `git checkout [commit_id] -- [path_to_file]`
- 取回的文件已在stage区, 移除之, [参考](http://hittyt.iteye.com/blog/1961386)

    `git reset .`
- 不再跟踪文件, [参考](http://stackoverflow.com/questions/6104072/git-update-index-assume-unchanged-and-git-reset)

    - 假定没有更改, status中不显示

        `git update-index --assume-unchaged [file_or_folder]`
    - 所有操作忽略该路径

        `git update-index --skip-worktree [file_or_folder]`
