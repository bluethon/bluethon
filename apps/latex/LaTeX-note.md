# LaTex Notes

## 工具网站

- [OCR识别/全平台支持](https://mathpix.com/)
- [手写识别/符号大全](https://mathpix.com/)
- [手写识别/公式转换](https://webdemo.myscript.com/views/math/index.html#)

## 教程网站

- [texlive安装及vscode配置](https://zhuanlan.zhihu.com/p/38178015)
- [一份其实很短的 LaTeX 入门文档](https://liam.page/2014/09/08/latex-introduction/)
- [tex2png](https://gist.github.com/retorillo/4ed72e705bdb6e3e2c6c29cada29f012)

## snippets

``` TeX
# 产生带圈数字⑧
\raisebox{.5pt}{\textcircled{\raisebox{-.9pt} {8}}}
```

## Notes

### 设置Katex宏(Macros)

user setttings

``` json
    "markdown.extension.katex.macros": {
        "\\ci": "\\raisebox{.5pt}{\\textcircled{\\raisebox{-.9pt} {#1}}}",
    }
```

reload window

`\ci{<param>}`使用

> - <https://github.com/yzhang-gh/vscode-markdown/issues/426#issuecomment-502582712>
> - <https://katex.org/docs/supported.html#macros>
