emmet停止tab某些情况下起作用
----------------------------

emmet的`settings- User`中添加设置, 不必须都添加

``` json
{
    // 设定不起作用的范围
    "disable_tab_abbreviations_for_scopes": "text.html.markdown",
    // 起作用的tag, 下列排除了var 防止和djaneiro冲突
    "known_html_tags": "html head title base link meta style script noscript body section nav article aside h1 h2 h3 h4 h5 h6 hgroup header footer address p hr pre blockquote ol ul li dl dt dd figure figcaption div a em strong small s cite q dfn abbr data time code samp kbd sub sup i b u mark ruby rt rp bdi bdo span br wbr ins del img iframe embed object param video audio source track canvas map area svg math table caption colgroup col tbody thead tfoot tr td th form fieldset legend label input button select datalist optgroup option textarea keygen output progress meter details summary command menu main template"
}
```
