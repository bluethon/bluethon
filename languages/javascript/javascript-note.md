JavaScript 学习笔记
==========

site
-----

> [代码优劣对比](https://jsperf.com/browse)

代码片段
-------

``` js
// 查看对象信息
console.dir(info);

// 显示某个节点的内容
console.dirxml(info);

// 判断变量值
console.assert(info===true);

// 追踪函数的调用轨迹(在body中加入下面代码)
console.trace();

// 计时
console.time("计时器1");
console.timeEnd("计时器1");

// 性能分析(浏览器Profiles中查看)
console.profile('性能分析器');
All();
console.profileEnd();

// es5添加默认值
args1 = args1 || 1
```

---

JavaScript语言精粹读书笔记
-----------------------

### P021 对象字面量
对象字面量属性中带连接符(-)是不合法的, 必须引号括住, 下划线则可选

``` js
var stooge = {
    "first-name": "Jack",
    last_name: "Hoard"
}
```

### P021 检索

``` js
// ||运算符 填充默认值
var status = flight.status || "default"
// &&运算符避免 从undefined的成员属性中取值将导致TypeError异常
flight.equipment                            // undefined
flight.equipment.model                      // throw "TypeError"
flight.equipment && flight.equipment.model  // undefined
```

### P023 反射 Reflection

``` js
// typeof 操作符确定对象属性
typeof flight.number        // 'number'

// 原型链中的任何属性都会产生值
typeof flight.toString      // 'function'

// hasOwnProperty 检查独有属性, 不检查原型链
flight.hasOwnProperty('number')         // true
flight.hasOwnProperty('constructor')    // false
```

### P025 减少全局变量污染

``` js
// 只创建一个唯一的全局变量
var MYAPP = {};

// 该变量变成应用容器
MYAPP.stooge = {};
```

### P026 函数

每个函数在创建时会附加两个隐藏属性: 函数的上下文和实现函数行为的代码

> JavaScript创建一个函数对象时, 会给该对象设置一个"调用"属性, 当JS调用一个函数时, 可以理解
为调用此函数的"调用"属性

通过函数字面量创建的函数对象包含一个连接到外部上下文的连接, 这被称为闭包

### P028 函数调用模式 The Function Invocation Pattern

若函数非对象的属性, 则被当做一个函数调用, 此模式下, this被绑定到全局对象

``` js
var add = function (a, b) {
    return a + b;
};

var myObject = {
    value: 0,
};

myObject.double = function () {
    var that = this;        // 解决方法

    var helper = function () {
        // 此处的this被绑定到全局对象, 是错误
        // this === window
        that.value = add(that.value, that.value);
    };

    helper();       // 以函数的形式调用 helper
};

// 以方法的形式调用double

myObject.double();
document.writeln(myObject.value);
```

---

廖雪峰js读书笔记
-------------

#### 数据类型

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

    Math.abs(1 / 3 - (1 - (2 / 3)) < 0.00000001; // true

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

#### 字符串
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

#### 数组
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

#### 对象
用一个`{...}`表示一个对象, 键值对以`xxx: xxx`形式申明, 用`,`隔开, 末尾对不加`,`

访问属性通过`.`操作符, 属性名包含特殊字符, 需用`''`括起来, 用`['xxx']`访问

可以随时添加和删除属性

用`in`检测属性是否存在(包括继承的)
只检测自身拥有, 使用`hasOwnProperty()`方法

``` js
var s = {
    'mid-night': 'Yes'
}
s['mid-night']; //访问;
s.age = 18; //增加
delete s.age; //删除
'age' in s; //检测
s.hasOwnProperty('age'); //only own
```

#### 条件判断
JavaScript把`null`、`undefined`、`0`、`NaN`和空字符串`''`视为`false`, 其他值一概视为`true`

#### 循环
`for (var key in Array)`

`for ... in`对`Array`循环得到的是`String`不是`Number`

``` js
var a = ['A', 'B', 'C'];
for (var i in a) {
    alert(i); // '0', '1', '2'
    alert(a[i]); // 'A', 'B', 'C'
}
```

#### Map&Set

**Map**
原版js不能使用`String`外的值做`{}`索引
新版引入`Map`可以
具有以下方法

``` js
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
```
同一索引多次赋值会覆盖

**Set**
`Set`和`Map`类似, 也是key的集合, 但不储存value, 且key不会重复
通过`add(key)`添加
通过`delete(key)`删除

#### iterable
`Array`、`Map`和`Set`都属于`iterable`类
`iterable`类型的集合可以使用`for ... of`循环遍历

``` js
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    alert(x);
}
for (var x of s) { // 遍历Set
    alert(x);
}
for (var x of m) { // 遍历Map
    alert(x[0] + '=' + x[1]);
}
```

**`for ... of`循环和`for ... in`循环区别**
`for ... in`循环由于历史遗留问题，它遍历的实际上是对象的属性名称。一个`Array`数组实际上也是一个对象，它的每个元素的索引被视为一个属性

`for ... in`循环将把`name`包括在内，但`Array`的`length`属性却不包括在内
`for ... of`循环则只循环集合本身的元素

``` js
var a = ['A', 'B', 'C'];
a.name = 'Hello'; //手动添加属性
for (var x in a) {
    alert(x); // '0', '1', '2', 'name'
}
```

更好的方式为使用`iterable`内置的`forEach`方法, 它接受一个函数, 每次迭代就自动会调该函数
**参数命名不固定, 但位置固定**
ES5.1标准引入

``` js
//Array
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
    console.log(element);
    console.log(index);
    console.log(array);
});

//Set
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    alert(element);
});

//Map
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
});

//如对个别参数不感兴趣 可省略, 但是必须在它之前的位置的不可省略
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    alert(element);
});
```

#### 函数

**两种等价定义方式**
第二种方式`function (x) { ... }`是一个匿名函数，它没有函数名。但是，这个匿名函数赋值给了变量`abs`，所以，通过变量`abs`就可以调用该函数, 但要按语法末尾加`;`

``` js
function abs(x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```

``` js
var abs = function (x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
};
```

调用函数时可以传入任意个参数
额外的不会起作用
少的也可以, 此时函数收到`undefined`

``` js
abs(10, 'blablabla'); // 返回10
abs(-9, 'haha', 'hehe', null); // 返回9
abs(); // 返回NaN
```

避免此问题, 需检查参数

``` js
function abs(x) {
    if (typeof x !== 'number') {
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```
