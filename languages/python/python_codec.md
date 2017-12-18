Python Codec
============

> <http://www.wklken.me/posts/2013/08/31/python-extra-coding-intro.html>

    str  -> decode('the_coding_of_str') -> unicode
    unicode -> encode('the_coding_you_want') -> str

### Python2 获得和设置系统默认编码

``` python
import sys

sys.getdefaultencoding()        # 'ascii'

reload(sys)                     # <module 'sys' (built-in)>

sys.setdefaultencoding('utf-8')
sys.getdefaultencoding()        # 'utf-8'
```

### \u字符串转成unicode字符串

``` python
u'中'                                # u'\u4e2d'
s = '\u4e2d'
print s.decode('unicode_escape')    # 中
```
