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
var s =
s.length;
可以使用下标操作 s[5];
**字符串是不可变的**, 索引赋值不报错 但也修改不了值

以下方法不会改变原字符串, 而是返回新的
`toUpperCase()` 大写
`toLowerCase()` 小写
`indexOf()` 搜索指定字符串出现的位置 **值找索引**
未找到返回-1
`substring()` 返回指定索引区间的字符串
``` js
s.substring(2, 5); //2开始到5 不包括5
s.substring(7); //索引7到结尾
```

### 数组
js的`Array`可以包含任意数据类型 在同一个数组里

给`Array`的`length`直接赋值会导致数组大小变化, 大小变为新值

可通过对某个索引值赋值修改数组

越界赋值会引起`Array`变大 但是**不会报错**

**indexOf**

**slice**
同String的`substring`类似
不给`slice()`传参 它会从头截到尾, 此原理可用来复制`Array`
直接赋值会引用同一个`Array`
``` js
var arr;
var aCopy = arr.slice();
```
**push&pop**
`push()` 向末尾添加若干元素
`pop` 删除最后一个 空数组pop不报错 返回undefined

**unshift&shift**
`unshift()` 向`Array`头部加若干元素
`shift()` 删除第一个元素

**sort**
修改当前`Array`元素位置, 直接调用, 默认顺序重排

**reverse**
逆序排列当前`Array`

**splice**
从指定索引开始删除若干元素, 在从**该**位置添加若干元素
``` js
var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
```

**concat**
将当前`Array`和其他拼接 返回一个**新**的`Array`
此方法可接受任意多个元素和`Array`, 可混合写在一起

**join**
将当前`Array`每个元素用指定字符链接
``` js
arr.join('-');
```

**多维数组**
``` js
arr[2][3]; //此方法引用
```
