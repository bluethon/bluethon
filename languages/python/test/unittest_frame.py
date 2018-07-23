# unittest单元测试框架
# 单元测试框架并非只能用于代码级别的测试，对于单元测试框架来讲，它主要完成三件事
# 1）提供用例组织与执行：当用例达到成百上千条时，大量的测试用例堆砌在一起，就产生了扩展性与
# 维护性等问题，此时需要考虑用例的规范和组织问题了。单元测试框架就是用来解决这个问题的
# 2）提供丰富的比较方法：不论是功能测试，还是单元测试，用例执行完成后都需要将实际结果与预期
# 结果进行比较(断言)，从而断定用例是否执行通过。单元测试框架一般会提供丰富的断言方法。例如
# 判断相等/不等、包含/不包含、True/False的断言方法等
# 3）提供丰富的日志：当测试用例执行失败时能抛出清晰的失败原因，当所有用例执行完成后能提供
# 丰富的执行结果。例如，总执行时间、失败用例数、成功用例数等

# 什么是单元测试
# 单元测试对最小的软件设计单元(模块)进行验证，它使用软件设计文档中对模块的描述作为指南，对
# 重要的程序分支进行测试以发现模块中的错误。在Python语言下有诸多单元测试框架，如doctest、
# unittest、pytest、nose等，unittest框架(原名PyUnit框架)为Python语言自带的单元测试
# 框架，Python2.1及其以后的版本已将unittest作为一个标准模块放入Python开发包中

# 不用测试框架的单元测试, calculator.py
# # 计算器类
# class Count:

# 	def __init__(self, a, b):
# 		self.a = int(a)
# 		self.b = int(b)

# 	# 计算加法
# 	def add(self):
# 		return self.a + self.b

# # 编写单元测试calculator_dont_unit.py
# from calculator import Count


# # 测试两个整数相加
# class TestCount:

#     def test_add(self):
#         try:
#             j = Count(2, 3)
#             add = j.add()
#             assert(add == 5), "Integer addition result error!"
#         except AssertionError as msg:
#             print(msg)
#         else:
#             print("Test pass!")


# # 执行测试类的测试方法
# mytest = TestCount()
# mytest.test_add()

# 不难发现这种测试方法存在许多问题。首先，测试程序的写法没有一定的规范可以遵循，十个程序员
# 完全可能写出十种不同的测试程序来，不统一的代码维护起来会十分麻烦。其次，需要编写大量的辅
# 助代码才能进行单元测试，在calculator_dont_unit.py中用于测试的代码甚至比被测试的代码
# 还要多，而且这仅仅是一个测试用例，对一个单元模块来说，只编写一条测试用例显然是不够的

# # 为了让单元测试代码更容易维护和编写，最好的方式是遵循一定的规范来编写测试用例，这也是单元
# # 测试框架诞生的初衷。接下来讲如何通过unittest单元测试框架编写单元测试用例
# # calculator_unittest.py
# from calculator import Count
# import unittest


# class TestCount(unittest.TestCase):

#     def setUp(self):
#         print("test start")

#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)

#     def tearDown(self):
#         print("test end")


# if __name__ == "__main__":
#     unittest.main()

# 分析上面的代码，首先引入unittest模块，创建TestCount类继承unittest的TestCase类，我们
# 可以将TestCase类看成是对特定类进行测试的集合

# setUp()方法用于测试用例执行前的初始化工作，这里只简单打印"test start"信息。tearDown()
# 方法与setUp()方法相呼应，用于测试用例执行之后的善后工作，这里打印"test end"信息

# 在test_add()中首先调用Count类并传入要计算的数，通过调用add()方法得到两数相加的返回值。
# 这里不再使用繁琐的异常处理，而是调用unittest框架所提供的assertEqual()方法对add()的返
# 回值进行断言，判断两者是否相等，assertEqual()方法由TestCase类继承而来

# unittest提供了全局的main()方法，使用它可以方便地将一个单元测试模块变成可以直接运行的测试
# 脚本。main()方法使用TestLoader类来搜索所有包含在该模块中以"test"命名开头的测试方法，并
# 自动执行它们


# 重要概念
# 在unittest的文档中开篇就介绍了4个重要的概念：test fixture、test case、test suite和
# test runner，只有理解了这几个概念才能理解单元测试的基本特征
# 1.Test Case
# 一个TestCase的实例就是一个测试用例。什么是测试用例呢?就是一个完整的测试流程，包括测试前
# 准备环境的搭建(setUp)、实现测试过程的代码(run)，以及测试后环境的还原(tearDown)。单元
# 测试(unit test)的本质也就在这里，一个测试用例就是一个完整的测试单元，通过运行这个测试
# 单元，可以对某一个功能进行验证
# 2.Test Suite
# 一个功能的验证往往需要多个测试用例，可以把多个测试用例集合在一起来执行，这就产生了测试套件
# TestSuite的概念。Test Suite用来组装单个测试用例。可以通过addTest加载TestCase到
# TestSuite中，从而返回一个TestSuite实例。
# 3.Test Runner
# 测试的执行也是单元测试中非常重要的一个概念，一般单元测试框架中都会提供丰富的执行策略和执行
# 结果。在unittest单元测试框架中，通过TextTestRunner类提供的run()方法来执行test suite/
# test case。test runner可以使用图形界面、文本界面，或返回一个特殊的值等方式来表示测试执行
# 的结果
# 4.Test Fixture
# 对一个测试用例环境的搭建和销毁，就是一个fixture，通过覆盖TestCase的setUp()和tearDown()
# 方法来实现。有什么用呢？比如说在这个测试用例中需要访问数据库，那么可以在setUp()中通过建立
# 数据库连接来进行初始化，在tearDown()中清除数据库产生的数据，然后关闭连接等
# 注意：tearDown的过程很重要，要为下一个test case留下一个干净的环境

# 下面结合例子来学习, unittest_caculator.py
# from calculator import Count
# import unittest


# class TestCount(unittest.TestCase):

#     def setUp(self):
#         print("测试开始")

#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)

#     def test_add2(self):
#         j = Count(41, 76)
#         self.assertEqual(j.add(), 117)

#     def tearDown(self):
#         print("测试结束")

# if __name__ == '__main__':
#     # 构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount("test_add2"))
#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


# 断言方法
# 在执行用例的过程中，最终用例是否执行通过，是通过判断测试得到的实际结果与预期结果是否相等
# 决定的。unittest框架的TestCase类提供下面这些方法用于测试结果的判断
# 方法                            检查                      版本
# assertEqual(a, b) ->           a == b
# assertNotEqual(a, b) ->        a != b
# assertTrue(x) ->               bool(x) is True
# assertFalse(x) ->              bool(x) is False
# assertIs(a, b) ->              a is b                    3.1
# assertIsNot(a, b) ->           a is not b                3.1
# assertIsNone(x) ->             x is None                 3.1
# assertIsNotNone(x) ->          x is not None             3.1
# assertIn(a, b) ->              a in b                    3.1
# assertNotIn(a, b) ->           a not in b                3.1
# assertIsInstance(a, b) ->      isinstance(a, b)          3.2
# assertNotIsInstance(a, b) ->   not isinstance(a, b)      3.2

# 用法
# assertEqual(first, second, msg=None)
# 断言第一个参数和第二个参数是否相等，如果不相等则测试失败。msg为可选参数，用于定义测试失败
# 时打印的信息, test_assertEqual.py
# import unittest


# class Test(unittest.TestCase):

#     def setUp(self):
#         number = input("Enter a number:")
#         self.number = int(number)

#     def test_case(self):
#         self.assertEqual(self.number, 10, msg="your input is not 10!")

#     def tearDown(self):
#         pass

# if __name__ == "__main__":
#     unittest.main()

# assertNotEqual(first, second, msg=None)
# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)

# 下面来实现判断一个数是否为质数的功能，所谓的质数（又叫素数）是指只能被1和它本身整除的数
# count_isprime.py
# 用于判断质数
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# 为质数功能编写测试，test_isprime.py
# from count_isprime import is_prime
# import unittest


# class Test(unittest.TestCase):

#     def setUp(self):
#         print("test start")

#     def test_case(self):
#         self.assertTrue(is_prime(8), msg="不是质数!")

#     def tearDown(self):
#         print("test end")

# if __name__ == "__main__":
#     unittest.main()


# assertIn(first, second, msg=None)
# assertNotIn(first, second, msg=None)

# 举例
# import unittest
# import requests
# import time
# import os
# import sys
# sys.path.append('../..')

# from db_fixture.mysql_db import DB


# class GetBranchListTest(unittest.TestCase):
#     ''' 获取分校列表接口 '''

#     def setUp(self):
#         self.base_url = 'http://192.168.1.161:8181/frontend/web/index.php?r=branch/list'

#     def tearDown(self):
#         print(self.base_url)
#         print(self.result)

#     def test_param_all(self):
#         ''' 传入所有参数 '''
#         # 数据库查询所有分校数量
#         table_name = 'wx_branchcampus'
#         columns = ['bc_name']
#         values = []
#         like = '%昌平%'
#         db = DB()
#         result = db.select(table_name, columns, values, like)
#         resultNum = result[1]
#         db.close()

#         # 接口查询分校信息
#         payload = ['userId=1', 'sessionKey=5a65bf7ed4787', 'keyword=昌平',
#                    'city=北京', 'area=昌平区', 'start=', 'count=60']
#         for paydata in payload:
#             self.base_url += '&'
#             self.base_url += paydata
#         r = requests.get(self.base_url)
#         self.result = r.json()
#         self.assertIn('昌平', self.result['list'][0]['name'], '查询结果错误')


# if __name__ == '__main__':
#     unittest.main()

# 断言第一个参数和第二个参数是否为同一对象
# assertIs(first, second, msg=None)
# assertIsNot(first, second, msg=None)
# 断言表达式是否为None对象
# assertIsNone(expr, msg=None)
# assertIsNotNone(expr, msg=None)
# 断言obj是否为cls的一个实例
# assertIsInstance(obj, cls, msg=None)
# assertNotIsInstance(obj, cls, msg=None)

# 在unittest中还提供了其他检查比较的方法，可以参考Python官方文档的unittest章节进行学习


# 组织单元测试用例
# 当我们增加被测功能和响应的测试用例之后，再来看看unittest单元测试框架是如何扩展和组织新增
# 的测试用例的

# 同样以calculator.py文件为例，为其扩展sub()方法，用来计算两个数相减的结果
# class Count:

#     def __init__(self, a, b):
#         self.a = int(a)
#         self.b = int(b)

#     # 计算加法
#     def add(self):
#         return self.a + self.b

#     # 计算减法
#     def sub(self):
#         return self.a - self.b

# 因为对计算器(calculator)又新增了减法功能(sub)，所以需要针对新功能编写测试用例，扩展后的
# test.py文件如下
# from calculator import Count
# import unittest


# class TestAdd(unittest.TestCase):

#     def setUp(self):
#         print("test add start")

#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)

#     def test_add2(self):
#         j = Count(41, 76)
#         self.assertEqual(j.add(), 117)

#     def tearDown(self):
#         print("test add end")


# class TestSub(unittest.TestCase):

#     def setUp(self):
#         print("test sub start")

#     def test_sub(self):
#         j = Count(2, 3)
#         self.assertEqual(j.sub(), -1)

#     def test_sub2(self):
#         j = Count(71, 46)
#         self.assertEqual(j.sub(), 25)

#     def tearDown(self):
#         print("test sub end")


# if __name__ == "__main__":
#     # 构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(TestAdd("test_add"))
#     suite.addTest(TestAdd("test_add2"))
#     suite.addTest(TestSub("test_sub"))
#     suite.addTest(TestSub("test_sub2"))

#     # 运行测试集合
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# 通过测试结果可以看到，setUp()和tearDown()方法分别作用于每个测试用例的开始与结束。如果
# 每个类中的setUp()和tearDown()所做的事情是一样的，那是不是可以封装一个自己的测试类呢？
# from calculator import Count
# import unittest


# class MyTest(unittest.TestCase):

#     def setUp(self):
#         print("test case start")

#     def tearDown(self):
#         print("test case end")


# class TestAdd(MyTest):

#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)

#     def test_add2(self):
#         j = Count(41, 76)
#         self.assertEqual(j.add(), 117)


# class TestSub(MyTest):

#     def test_sub(self):
#         j = Count(2, 3)
#         self.assertEqual(j.sub(), -1)

#     def test_sub2(self):
#         j = Count(71, 46)
#         self.assertEqual(j.sub(), 25)

# if __name__ == "__main__":
#     unittest.main()

# 创建MyTest()类的好处显而易见，对于测试类和测试方法来说，应该将注意力放在具体用例的编写上
# 无须关心setUp()和tearDown()所做的事情。不过，前提条件是setUp()和tearDown()所做的事情
# 是每个用例都需要的


# discover更多测试用例
# 随着软件功能的不断增加，对应的测试用例也会呈现指数级增长。一个实现几十个功能的项目，对应的
# 单元测试用例可能达到上百个。如果把所有的测试用例都写在一个test.py文件中，那么这个文件会
# 越来越臃肿，后期维护起来也比较麻烦。需要将这些用例按照所测试的功能进行拆分，分散到不同的测
# 试文件中

# 对上面的例子中的测试用例进行拆分，拆分后的目录结构如下：
# testpro/
# |---- calculator.py
# |---- testadd.py
# |---- testsub.py
# |---- runtest.py

# 文件拆分后实现代码如下, testadd.py
# from calculator import Count
# import unittest


# class TestAdd(unittest.TestCase):

#     def setUp(self):
#         print("test case start")

#     def tearDown(self):
#         print("test case end")

#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)

#     def test_add2(self):
#         j = Count(41, 76)
#         self.assertEqual(j.add(), 117)


# if __name__ == "__main__":
#     unittest.main()

# testsub.py
# from calculator import Count
# import unittest


# class TestSub(unittest.TestCase):

#     def setUp(self):
#         print("test case start")

#     def tearDown(self):
#         print("test case end")

#     def test_sub(self):
#         j = Count(2, 3)
#         self.assertEqual(j.sub(), -1)

#     def test_sub2(self):
#         j = Count(71, 46)
#         self.assertEqual(j.sub(), 25)


# if __name__ == "__main__":
#     unittest.main()

# 创建用于执行所有用例的runtest.py文件
# import unittest
# # 加载测试文件
# import testadd
# import testsub

# # 构造测试集
# suite = unittest.TestSuite()

# suite.addTest(testadd.TestAdd("test_add"))
# suite.addTest(testadd.TestAdd("test_add2"))

# suite.addTest(testsub.TestSub("test_sub"))
# suite.addTest(testsub.TestSub("test_sub2"))

# if __name__ == "__main__":
#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# 这样的拆分带来了好处，可以根据不同的功能创建不同的测试文件，甚至是不同的测试目录，测试文件
# 中还可以分为不同的测试类，在类下编写测试用例，整体结构更加清晰

# 这样的设计看上去很完美，但依然没有解决添加用例的问题，当用例达到成百上千条时，
# 在runtest.py文件中通过addTest()添加/删除测试用例就变得非常麻烦，那么有没有方法让
# unittest单元测试框架自动识别测试用例呢？答案是肯定的，TestLoader类中提供的discover()
# 方法可以解决这个问题

# TestLoader
# 该类负责根据各种标准加载测试用例，并将它们返回给测试套件。正常情况下，不需要创建这个类的
# 实例。unittest提供了可以共享的defaultTestLoader类，可以使用其子类和方法创建实例，
# discover()方法就是其中之一

# discover(start_dir, pattern="test*.py", top_level_dir=None)
# 找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才能被加载。
# 如果启动的不是顶层目录，那么顶层目录必需单独指定
# 1）start_dir: 要测试的模块名或测试用例目录
# 2) pattern="test*.py": 表示用例文件名的匹配原则。此处匹配文件名以"test"开头的".py"类
# 型的文件，星号"*"表示任意多个字符
# 3) top_level_dir=None: 测试模块的顶层目录，如果没有顶层目录，默认为None。

# 现在通过discover()方法重新实现runtest.py文件的功能, runtestNew.py
# import unittest


# # 定义测试用例的目录为当前目录
# test_dir = "./"
# discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(discover)


# 关于unittest还需要知道的
# 1) 用例的执行顺序
# 用例的执行顺序涉及多个层级：在多个测试目录的情况下，先执行哪个目录？在多个测试文件的情况下
# 先执行哪个文件？在多个测试类的情况下，先执行哪个测试类？在多个测试方法（用例）的情况下，先
# 执行哪个测试方法？

# 运行一个例子
# import unittest


# class TestBdd(unittest.TestCase):

#     def setUp(self):
#         print("test TestBdd")

#     def test_ccc(self):
#         print("test ccc")

#     def test_aaa(self):
#         print("test aaa")

#     def tearDown(self):
#         pass


# class TestAdd(unittest.TestCase):

#     def setUp(self):
#         print("test TestAdd:")

#     def test_bbb(self):
#         print("test bbb")

#     def tearDown(self):
#         pass


# if __name__ == "__main__":
#     # 按照ASCII码顺序加载，0~9,A-Z,a-z
#     # unittest.main()

#     # 按照addTest加载顺序执行
#     suite = unittest.TestSuite()
#     suite.addTest(TestBdd("test_ccc"))
#     suite.addTest(TestAdd("test_bbb"))
#     suite.addTest(TestBdd("test_aaa"))

#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# unittest框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0～9，A～Z，a～z。
# 所以，TestAdd类会优先于TestBdd类被执行，test_aaa()方法会优先于test_ccc()被执行，因
# 而它并没有按照用例从上到下的顺序执行

# 对于测试目录和测试文件来说，unittest框架同样是按照这个规则来加载测试用例的

# 那么可不可以让test_ccc()先执行？答案是肯定的，只是不能使用默认的main()方法了，而是需要
# 通过TestSuite类的addTest()方法按照一定的顺序来加载

# discover()的加载测试用例的规则与main()方法相同。所以，我们只能通过测试用例的命名来提高
# 被执行的优先级。例如，将希望先被执行的测试用例命名为"test_a"，将希望最后执行的测试用例命
# 名为"test_z"


# 执行多级目录的用例
# 我们要控制Web用例的数量，但是当测试用例达到一定量级时，就要考虑划分目录，比如规划如下测试
# 目录：
# test_project/test_case/
#             |----test_bbb/
#             |    |
#             |    |----test_ccc/
#             |    |    |----test_c.py
#             |    |
#             |    |----test_b.py
#             |
#             |----test_ddd/
#             |    |----test_d.py
#             |
#             |----test_a.py
# 对于上面的目录结构，如果将discover()方法中的start_dir参数定义为"./test_case/"目录，
# 那么只能加载test_a.py文件中的测试用例。怎样让unittest框架查找到test_case/的子目录中
# 的测试文件呢？方法很简单，在每个子目录下放一个__init__.py文件。


# 跳过测试和预期失败
# 在运行测试时，有时需要直接跳过某些测试用例，或者当用例符合某个条件时跳过测试，又或者直接
# 将测试用例设置为失败。unittest提供了实现这些需求的装饰器
# 1) unittest.skip(reason) -> 无条件的跳过装饰的测试，说明跳过测试的原因
# 2) unittest.skipIf(condition, reason) -> 如果条件为真则跳过装饰的测试
# 3）unittest.skipUnless(condition, reason) -> 跳过装饰的测试，除非条件为真
# 4) unittest.expectedFailure() -> 测试标记为失败，不管执行结果是否失败，统一标为失败

# 例子, test_skip.py
# import unittest


# class MyTest(unittest.TestCase):

#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

#     @unittest.skip("直接跳过测试")
#     def test_skip(self):
#         print("test bbb")

#     @unittest.skipIf(3 > 2, "当条件为True时跳过测试")
#     def test_skip_if(self):
#         print("test bbb")

#     @unittest.skipUnless(3 > 2, "当条件为True时执行测试")
#     def test_skip_unless(self):
#         print("test ccc")

#     @unittest.expectedFailure
#     def test_expected_failure(self):
#         self.assertEqual(2, 3)


# if __name__ == "__main__":
#     unittest.main()

# 共创建了4条测试用例。第一条测试用例通过@unittest.skip()装饰，直接跳过不执行。第二条用例
# 通过@unittest.skipIf()装饰，当条件为真时不执行, 3>2条件为真(True), 跳过不执行。第三条
# 用例通过@unittest.skipUnless()装饰，当条件为真时执行，判断3>2条件为真(True), 第三条
# 用例执行。第四条用例通过@unittest.expectedFailure装饰，不管执行结果是否失败，统一标记
# 为失败，但不会抛出错误信息

# 当然，这些方法同样可以作用于测试类，只需将它们定义在测试类上面即可
# import unittest

# @unittest.skip("直接跳过测试该测试类")
# class MyTest(unittest.TestCase):
# ......


# fixtures
# fixtures的概念前面已经有过简单的介绍，可以形象地把它看作是夹心饼干外层的两片饼干，这两片
# 饼干就是setUp/tearDown，中间的心就是测试用例。除此之外，unittest还提供了更大范围的
# fixtures, 例如对于测试类和模块的fixtures。test_fixtures.py
# import unittest


# def setUpModule():
#     print("test module start >>>>>>>>>>>>>>>>>")


# def tearDownModule():
#     print("test module end >>>>>>>>>>>>>>>>>>>")


# class Test(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print("test class start =============>")

#     @classmethod
#     def tearDownClass(cls):
#         print("test class end =============>")

#     def setUp(self):
#         print("test case start ----------->")

#     def tearDown(self):
#         print("test case end ------------>")

#     def test_case(self):
#         print("test case1")

#     def test_case2(self):
#         print("test case2")


# if __name__ == "__main__":
#     unittest.main()

# setUpModule/tearDownModule -> 在整个模块的开始与结束时被执行
# setUpClass/tearDownClass -> 在测试类的开始与结束时被执行
# setUp/tearDown -> 在测试用例的开始与结束时被执行
# 需要注意的是，setUpClass/tesrDownClass的写法稍微有些不同。首先，需要通过@classmethod
# 进行装饰，其次方法的参数为cls。其实，cls与self并没有什么特别之处，都只表示类方法的第一个
# 参数，只是大家约定俗成，习惯于这样来命名，当然也可以用abc来代替


# doctest可不可以用正则?
# 快速指导工作
# 工作中已经出现的代码
# 文档太费劲，用markdown语法写比较好
# 为什么这种东西会出现


# 把代码找到一些，测试时候比较头疼的代码，太难的是什么问题，是设计还是？找到问题根源
