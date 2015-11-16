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

