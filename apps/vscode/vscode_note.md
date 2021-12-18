# VSCode Note

## CMD

``` shell
# 导出插件列表
# https://stackoverflow.com/a/49398449/4757521
code --list-extensions | xargs -L 1 echo code --install-extension
```

## Apps

- python-extension-pack Python开发包

## Notes

### vscodevim 自动切换输入法

> https://github.com/daipeihust/im-select  
> [如何解决VSCode Vim中文输入法切换问题？ - somenzz的回答 - 知乎](https://www.zhihu.com/question/303850876/answer/822818615)

- 下载[im-selecotr](https://github.com/daipeihust/im-select)
- 配置vscodevim
  - 注意路径用双反斜线
  - 语言默认1033(英文)

### Git Bash 历史记录不生效

> <https://code.visualstudio.com/docs/editor/integrated-terminal#_git-bash-isnt-saving-history-when-i-close-the-terminal>

在windows下的`~/.bashrc`中增加

    export PROMPT_COMMAND='history -a'
