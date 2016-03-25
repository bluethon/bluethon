sublime开启scope_name显示
=========================

#### 描述

之前在使用sublime的时候一直有一个非常严重的问题, 就是当自定义`scope`字段时, 里面的值不知道该怎么写, 多次网上查找资料, 一直没有一个比较全的list, 后来SO上给的答案也是没有, [sublime的非官方手册][0]里也是让参考textmate的manual, 进去看了一圈, 奈何英语渣渣, 还是不得所以, 最后偶然搜索, 在[SO的采纳答案的评论][1]中找到一个我认为最佳的解决方案!

#### 正文
sublime有一个`hotkey`叫`show_scope_name`, 光标定位到你需要起作用的位置, 由于我的默认快捷键被覆盖掉了, 所以自定义了一个, 可以在`kep bindings`中自行搜索

按快捷键, 状态栏会提示此处对应的scope, 泪流满面啊

[0]: http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html
[1]: http://stackoverflow.com/questions/10834765/where-to-find-a-list-of-scopes-for-sublime2-or-textmate
