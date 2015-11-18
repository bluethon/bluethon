JavaScript 学习笔记
==========

### 数据类型

**Number**
JavaScript不区分整数和浮点, 统一用`Number`表示
``` js
NaN; // NaN表示Not a Number, 当无法计算结果是用此表示
2/0;

Infinity; // 无限大, 数值超过JavaScript的Number最大值是 都表示为Infinity
0/0;
```

**字符串**
单引号 双引号均可
ASCII字符可以用`\x##`形式的十六进制表嫂
Unicode字符 `\u####`
换行`\n`

ES6新增多行字符串表示方法
``` js
`A
B
C`;
```

**比较运算符**
`==` 自动转换数据类型 不推荐
`===` 不自动转换类型 推荐
``` js
false == 0; // true
false === 0; // false
```

`NaN`不与任何值相等 包括自己
判断方法
``` js
isNaN(NaN); //  true
```

浮点数比较 计算差值的绝对值小于某阈值
``` js
Math.abs(1 / 3 - (1 - (2 / 3)) < 0.00000001; // true
```

**null & undefined**
用null 基本没区别
undefined仅仅在判断函数参数是否传递的情况下有用

**数组**
js的数组可以包括任意数据类型
使用`[]`直接创建, 另可通过`new Array()`, 不推荐
``` js
[1, 2, 'hello', null];
```

**对象**


**变量**
用`var`声明
变量为任意类型 可被不同类型的值赋值
只能用`var`声明一次
变量本身类型不固定的语言即为动态语言

**strict模式**
不用`var`声明的变量自动为全局变量
此模式下强制使用`var`声明,否则将导致运行错误
使用方法,代码第一写入
'use strict';
上为字符串, 不支持strict的浏览器讲视为一个字符串语句执行

### 字符串

