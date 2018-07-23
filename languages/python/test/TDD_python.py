# 在Python中的代码测试包含两种类型：unittest和doctest

# 测试驱动开发(Test Driven Development, TDD)是敏捷开发中的一个重要组成部分，其基本思想
# 是测试先行。也就是说在开发具体的功能代码之前，需要首先编写此功能的测试代码。只有通过了测试
# 的代码，才能够加入代码仓库中。

# 测试驱动开发模式
# 随着软件规模的增大，软件开发人员的增多，在软件开发过程中出现了指导软件开发的开发模式。这规
# 定了在软件开发的过程中各种文档和功能的规范标准。在软件开发的生命周期中，包含需求、设计、
# 编码、测试和维护等阶段。通过采用不同的开发方法，可以使不同类型的开发人员参与其中，从而实现
# 最终的软件开发目标。不同的阶段所承载的任务和完成的时间是不一样的。

# # 传统的软件开发模型包括瀑布模型、演进模型、螺旋模型、喷泉模型和智能模型等。现在还在广泛使用
# # 的是瀑布模型，它将软件开发的生命周期分成了6个阶段：软件计划、需求分析和定义、系统设计、编码
# # 实现、软件测试和软件维护。每个阶段各有自己的工作内容，并且需要有相应的文档支持。其关系是一
# # 种自上向下加上部分反馈的运作模式。如下图所示
# from PIL import Image


# img = Image.open(r"waterfall_model.jpeg")
# img.show()

# 虽然瀑布模型为软件开发提供了按照阶段划分的检查点，但是这种开发模型已经越来越不适应现代化软件
# 开发的要求。这种开发模式最大的问题在于只能够在软件生命周期的后期才能够看到最终结果，无法适应
# 多变的用户需求。由于缺少应变能力，使得项目的开发具有比较大的风险。

# 传统的软件开发模型中，测试阶段是放在软件生命周期的后期来完成的。这种处理方式使得软件编码中
# 的问题只有在后期才能够被发现，从而带来严重的问题。这种开发模式下，测试阶段所占的时间比例要
# 占整个开发所用时间的一半左右。为了避免传统开发模式下的这些问题，敏捷方法学在快速开发的目标
# 上强调基于测试的开发过程。

# 测试驱动开发的核心思想是强调测试在整个开发过程中的作用。在开始编写功能代码之前，需要首先编写
# 符合需求的测试代码。对于一个特定的功能，需要完成此功能的测试代码，包括测试用例。在整个开发
# 过程中，需要对每个阶段都进行测试驱动。也就是说，在实现某种功能之前，需要思考这个功能的测试
# 和验证过程，在编写了相关的测试代码之后，才开始进一步的编码工作。通过这样的方式，将各个功能
# 完善，从而形成最终的目标软件。

# # 比较流行的测试驱动开发模型包括V测试模型和X测试模型。如下图所示
# from PIL import Image


# img = Image.open(r"V_model.jpeg")
# img.show()
# 在途中可以看到，在软件开发周期中的每个阶段，都需要考虑相应的测试工作。这些阶段包括需求分析
# 阶段、概要设计阶段、详细设计阶段和编码实现阶段。相应的测试过程则称为单元测试、集成测试、系
# 统测试和验收测试。在软件的实际开发过程中，这些测试阶段可以根据需要来进行调整。测试代码也最
# 好包含相关的测试文档，但是和强调文档的传统开发模型不同，这里的文档也都是围绕着测试这个需求
# 的。这种开发模型使得项目及其质量保证同时展开。


# TDD的优势
# 因为TDD采用的是以测试作为核心的开发模式，所以具有传统开发模型所不具备的优点。一个最大的好处
# 就是可以在短时间内构建出一个软件的原型出来。这使得在真正开始软件开发的时候能够对软件的实现
# 规划有个好的了解，从而规避风险。在实际的开发中，这种以测试为核心的开发方法也可以使得在改正
# 程序错误方面有着独特的优势。设想在写了一段代码后，开始进行单元测试，这个时候发现的问题就是
# 在新写的这部分代码中。但是在传统的开发模型中，在整体编码完毕后再进行测试，这时候出现的问题
# 就很难定位了。

# 在软件开发结束的时候，最终产品是伴随着详细的测试套件一起发布的。这从另一个侧面加强了最终产品
# 的可靠性，同时为软件产品的升级和维护提供了便利。在测试驱动开发中，项目主管可以很清楚地看到
# 已经完成了哪些软件需求，从而有助于把握项目进度。而传统的方式则只能够定义一些检查点，而不能
# 更细的划分功能需求点。

# 在传统的基于文档的开发模式中，开发人员和文档编写人员是分开的。这样一方面加重了沟通成本，另
# 一方面则使得开发人员对修订文档并不关心。而在测试驱动开发中，测试过程中所使用的测试用例代码
# 就是代码的注释文档。也就是说，在编写代码的时候实际上也是在编写代码文档。在Python标准库中，
# 提供了一种doctest模块，可以直接在代码的注释中书写测试用例。

# 测试驱动开发模式作为敏捷开发中的核心组成部分，所以也具有敏捷方法学的共同目标，也就是适应快速
# 多变的用户需求。在传统的开发模型中，当前的需求设计阶段确定下来后，后面如果需要再度更改需求
# 是一件不太可能的事情。因为这意味着项目需要从瀑布的顶端开始运作。而对于测试驱动开发来说，总
# 是通过编写测试用例，优先考虑实现代码的使用需求，包括功能、过程和接口等。这种方式使得最终代码
# 符合后期开发的需求，能够提供代码的内聚性和复用性。


# TDD的使用步骤
# TDD这种开发模式在实现软件开发目标的同时，实现了整洁可用的代码。在明确了当前软件开发的需求后，
# TDD中新添加一个功能的基本过程如下：
# 1）明确当前代码需要完成的功能，必要的时候书写相关的接口等。
# 2）快速新增一个测试。
# 3）运行所有的测试，看是否可以通过。若通过则跳到步骤6）
# 4）对功能代码进行细微的改动
# 5）重新运行所有的测试用例，保证全部通过。
# 6）对代码进行重构，消除重复设计，优化代码结构。
# 上面的过程是对于一个功能点的添加过程。将需求分解成多个不同的功能点，循环将其加入软件中，即
# 完成了一个软件实现的目标。在实际的操作中，还有一些注意事项。

# 在书写功能代码之前需要编写测试代码。书写功能代码的目的就是能够通过测试代码的测试。这里可以
# 看到，测试实例越丰富，表示功能代码书写得越完备。当有部分测试用例没有通过的时候，就要对功能
# 代码进行修改，这样重复编码和测试的过程，直到通过测试。

# 那些没有通过测试的代码是不能够放入产品代码之中的。产品中的每行代码应该都是通过了充分测试的。
# 只有这样才能够保证后续加入的代码不会受前面加入的错误代码的影响。最后，在实际测试的时候，只
# 需要对实现功能代码的部分进行测试就可以了。这样可以保证测试用例的简单。

# 在多个测试阶段中，最核心的是单元测试。在Python的标准库中，包含两类代码测试模块，
# 分别为unittest和docttest。两者都可以实现单元测试的功能。
# unittest可以用来书写PyUnit的测试代码。和其他语言的单元测试工具一样，支持对软件代码的自动
# 化测试。doctest是一个特殊的测试模块，此模块将测试用例内置在了函数的文档字符串中，从而达到
# 了文档和测试代码的统一。接下来将具体的介绍如何使用Python标准库所提供的模块进行测试驱动开发


# unittest测试框架
# 在Python标准库中，用来实现单元测试的模块是unittest。在其他编程语言中，都有着自己的一套
# 测试驱动开发工具。大多数都是属于xUnit家族的。如Java语言的JUnit工具，C++语言中的CppUnit
# 工具，还包括NUnit、RubyUnit和vbUnit工具等。Python也有这样的测试驱动开发工具，即PyUnit
# 在Python版本2.1后此模块被标准库引入，别名为unittest。unittest模块提供了一种规范的方法
# 来构造单元测试用例。如果不使用这个模块提供的方法而采用手工构造，则将需要编写大量的辅助测试
# 代码。

# 和其他自动化测试框架一样，unittest框架有着和其他自动化测试框架类似的接口。特别要提到的是，
# PyUnit可以看作是JUnit工具的Python语言版本。所以如果对于JUnit的API熟悉，则可以看到
# PyUnit和其是非常相似的

# unittest模块支持测试的自动化处理。更多的功能包括可以共享代码测试的初始化和结束代码、将测试
# 用例封装成一个测试套件以及测试的多元化显示等。在unittest模块中提供了相关类和方法，使得开发
# 者可以很容易地处理这些测试工作

# unittest模块支持单元测试的各种重要概念。其中最重要的概念是测试用例。这是单元测试的最小组成
# 部分。在其中只是查看特定的功能实现，检查在特定输入下的响应情况。unittest模块提供了TestCase
# 基类，用来创建新的测试用例。

# 在一组测试用例中，包含共同需要处理的代码，被称为测试固件。这些代码可能是测试之前需要进行的
# 初始化工作，也可能是测试结束后所做的代码清理工作。例如在测试之前，可能需要建立某些文件夹或
# 者开启某些服务。在构建测试用例的时候，可以使用setUp和tearDown来执行初始化和结束工作。在
# 测试执行的时候，setUp将首先被执行，而且只会执行一次。当此方法通过后，不管后面的测试是否通
# 过，都会执行tearDown函数。

# 随着测试用例的增多，对测试用例一个一个管理显然是非常低效的。unittest模块中提供了测试套件来
# 解决这个问题。测试套件将一组测试用例集合起来作为一个测试对象。需要注意的是，测试套件是可以
# 嵌套的，也就是说，可以在测试套件中包含测试套件。这是在TestSuite类中提供的功能。在其中的测
# 试用例或者测试套件都将会依次运行。

# 在unittest模块中还包含一个测试运行器，用来运行这些测试并为用户提供输出。这些运行器可能是
# 一个图形化的接口或者是文本的接口，甚至只是一个简单的值来指示测试运行的结果。unittest测试
# 框架中使用TestRunner类来为测试的运行提供环境。这些类对象中提供了一个run方法，其中接收
# TestCase或者TestSuite参数，并返回运行结果。最常用的是TextTestRunner运行器，默认情况下
# 将向终端输出测试运行结果。

# 对于一个基于测试的软件来说，测试是软件产品中的一部分。实际上，在Python的标准安装中，实际上
# 就有对于标准模块的测试代码。这可以从其安装目录Lib/test中看到。


# # 构建测试用例
# # 软件测试的基本组成单元是测试用例，也可以说，单元测试是通过一些测试用例构建而成的。在测试用
# # 例中，包含对于特定功能的测试。在unittest模块中，可以通过继承TestCase类来构建单元测试用例
# # 通过覆盖TestCase类中的runTest函数可以实现功能的具体测试。在下面的示例代码中，演示了如何
# # 构建单元测试用例, tdd_1.py
# import unittest
# import string


# class StringReplaceTestCase1(unittest.TestCase):
#     ''' 测试空字符替换 '''

#     def runTest(self):
#         source = "HELLO"
#         expect = "HELLO"
#         result = string.replace(source, "", "")
#         self.assertEqual(expect, result)    # 单元测试的最后步骤都是使用断言


# class StringRelaceTestCase2(unittest.TestCase):
#     ''' 测试空字符替换成常规字符 '''

#     def runTest(self):
#         source = "HELLO"
#         expect = "*H*E*L*L*O*"
#         result = string.replace(source, "", "*")
#         self.assertEqual(expect, result)    # 使用断言判断测试是否通过


# class StringReplaceTestCase3(unittest.TestCase):
#     ''' 测试常规字符替换为空字符 '''

#     def runTest(self):
#         source = "HELLO"
#         expect = "HEO"
#         result = string.replace(source, "LL", "")
#         self.assertEqual(expect, result)


# class StringReplaceTestCase4(unittest.TestCase):
#     ''' 测试常规字符替换 '''

#     def runTest(self):
#         source = "HELLO"
#         expect = "HEMMO"
#         result = string.replace(source, "LL", "MM")
#         self.assertEqual(expect, result)


# 在Python中，内置assert语句可以用来实现测试用例运行时候的断言。当测试用例运行时，如果断言
# 为假，则会触发AssertionError异常，同时，自动化测试框架会认为此测试用例测试失败。由于
# Python语言中的assert语句可能会在某些情况下被优化，所以在TestCase类中提供了assert_方法，
# 使得其在测试用例中不会因为优化而被去掉。实际上，assert_方法是assertTrue和failUnless的
# 别名。在unittest模块中，提供了丰富的方法来对测试结果进行判断。

# unittest模块中的测试方法
# assertEqual -> 当两者相等时测试通过
# assertEquals -> 当两者相等时测试通过
# failUnlessEqual -> 当两者相等时测试通过


# assertNotEqual -> 当两者不相等时测试通过
# assertNotEquals -> 当两者不相等时测试通过
# failIfEqual -> 当两者不相等时测试通过

# assertAlmostEqual -> 当两者几乎相等时测试通过
# assertAlmostEquals -> 当两者几乎相等时测试通过
# failUnlessAlmostEqual -> 当两者几乎相等时测试通过

# assetNotAlmostEqual -> 当两者几乎不相等的时候测试通过
# assertNotAlmostEquals -> 当两者几乎不相等的时候测试通过
# failIfAlmostEqual -> 当两者几乎不相等的时候测试通过

# assertRaises -> 当触发指定异常的时候测试通过
# failUnlessRaises -> 当触发指定异常的时候测试通过

# assert_ -> 当表达式为真的时候测试通过
# assertTrue -> 当表达式为真的时候测试通过
# failUnless -> 当表达式为真的时候测试通过

# assertFalse -> 当表达式为假的时候测试通过
# failIf -> 当表达式为假的时候测试通过

# 这些提供的方法中，除了测试是否触发异常的方法外，其他方法都包含一个可选的信息参数。此参数可
# 以在测试不通过的时候显示出来。

# # 可以通过直接使用这些类的构造函数来生成一个测试用例的示例
# testcase1 = StringReplaceTestCase1()


# 构建测试固件
# 随着单元测试实例的增多，在各个测试代码中会有很多相似的操作。如在上面的测试用例中，每个测试
# 用例都需要在测试代码的前面加入对源字符串的定义。当然这里只是为了简单起见，在实际中可能会有
# 很多复杂而琐碎的工作，如建立数据库的连接或启动某些服务等。为了减少这种重复，testCase类提供
# 了setUp方法，使得单元测试实例在执行的时候都执行

# # 下面的示例代码是对tdd_1.py加入测试固件后的修改版本, tdd_2.py
# import unittest
# import string


# class SimpleStringReplaceTestCase(unittest.TestCase):
#     ''' 准备测试的源字符串 '''

#     def setUp(self):
#         self.source = "HELLO"


# class StringReplaceTestCase1(SimpleStringReplaceTestCase):
#     ''' 测试空字符替换 '''

#     def runTest(self):
#         expect = "HELLO"
#         result = string.replace(source, "", "")
#         self.assertEqual(expect, result)    # 单元测试的最后步骤都是使用断言


# class StringRelaceTestCase2(SimpleStringReplaceTestCase):
#     ''' 测试空字符替换成常规字符 '''

#     def runTest(self):
#         expect = "*H*E*L*L*O*"
#         result = string.replace(source, "", "*")
#         self.assertEqual(expect, result)    # 使用断言判断测试是否通过


# class StringReplaceTestCase3(SimpleStringReplaceTestCase):
#     ''' 测试常规字符替换为空字符 '''

#     def runTest(self):
#         expect = "HEO"
#         result = string.replace(source, "LL", "")
#         self.assertEqual(expect, result)


# class StringReplaceTestCase4(SimpleStringReplaceTestCase):
#     ''' 测试常规字符替换 '''

#     def runTest(self):
#         expect = "HEMMO"
#         result = string.replace(source, "LL", "MM")
#         self.assertEqual(expect, result)

# 当在setUp中定义的函数在测试运行过程中出错，则测试框架将会认为此单元测试用例出错，而并不会
# 执行runTest方法中定义的测试代码。

# 同样的，如果需要在结束时候执行某些代码。TestCase提供了tearDown方法用来执行在运行runTest
# 之后的清理工作。setUp和tearDown时对应的。也就是说，如果setUp方法执行成功，则不管runTest
# 方法是否执行成功，tearDown方法都将会执行。


# # 组织多个测试用例, tdd_3.py
# # 当有多个测试用例的时候，上面小节中使用了测试固件。但是，所有的测试用例还是单独作为一个类存
# # 在的。这种处理方式实际上是非常耗时的，所以并不推荐这样使用。unittest模块提供了另一种更方便
# # 的方式来组织多个测试用例。
# import unittest
# import string


# class StringReplaceTestCase(unittest.TestCase):

#     def setUp(self):
#         self.source = "HELLO"

#     def testBlank(self):
#         ''' 测试空字符替换 '''
#         expect = "HELLO"
#         result = string.replace(source, "", "")
#         self.assertEqual(expect, result)    # 单元测试的最后步骤都是使用断言

#     def testBlankOrd(self):
#         ''' 测试空字符替换成常规字符 '''
#         expect = "*H*E*L*L*O*"
#         result = string.replace(source, "", "*")
#         self.assertEqual(expect, result)    # 使用断言判断测试是否通过

#     def testOrdBlank(self):
#         ''' 测试常规字符替换为空字符 '''
#         expect = "HEO"
#         result = string.replace(source, "LL", "")
#         self.assertEqual(expect, result)

#     def testOrd(self):
#         ''' 测试常规字符替换 '''
#         expect = "HEMMO"
#         result = string.replace(source, "LL", "MM")
#         self.assertEqual(expect, result)

#     def suite():
#         StringReplaceTestSuite = unittest.TestSuite()
#         StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlank"))
#         StringReplaceTestSuite.addTest(StringReplaceTestCase("testOrd"))

#         return StringReplaceTestSuite


# # 生成测试用例实例
# testBlank = StringReplaceTestCase("testBlank")
# testOrd = StringReplaceTestCase("testOrd")

# # 构建测试套件
# # 当具有多个测试用例的时候，可以根据所测试的用途和特性来将其组合。unittest模块中提供了
# # TestSuite类来生成测试套件。直接使用此类的构造函数可以生成一个测试套件的实例。在此类中提供
# # 了一个方法addTest来将单元测试用例加入测试套件中
# StringReplaceTestSuite = unittest.TestSuite()
# StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlank"))
# StringReplaceTestSuite.addTest(StringReplaceTestCase("testOrd"))


# # 在实际操作中，会在测试模块中返回已经构建好的测试套件
# def suite():
#     StringReplaceTestSuite = unittest.TestSuite()
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlank"))
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testOrd"))

#     return StringReplaceTestSuite


# # 同样，可以在TestSuite类的构造函数中生成测试套件实例
# from tdd_3 import StringReplaceTestCase
# import unittest


# def suite():
#     tests = ["testBlank", "testOrd"]
#     StringReplaceTestSuite = unittest.TestSuite(
#         map(StringReplaceTestCase, tests))  # map首参为函数，第二个参为函数的参数
#     # print(list(map(StringReplaceTestCase, tests)))

#     return StringReplaceTestSuite


# print(suite())

# # 这里使用了一种在TestSuite构造函数中生成测试套件实例的方法。由于一般需要加入多个单元测试
# # 用例，而在上面的两种方法中，都要将每个测试用例加入其中。这种处理方式使得在含有大量单元测试
# # 用例的时候会很烦琐。由于经常需要加入所有的测试用例，所以在unittest模块中提供了一个使用
# # 方法makeSuite，来创建一个由测试用例类内所有的测试用例所组成的测试套件实例
# from tdd_3 import StringReplaceTestCase
# import unittest


# def suite():

#     StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,
#                                                 'test')

#     return StringReplaceTestSuite


# suite = suite()
# print(suite)

# # 这里的代码主要是使用了makeSuite方法，来为StringReplaceTestCase类中的所有单元测试用例
# # 生成测试套件。而且测试套件是可以嵌套的。也就是说，可以将测试套件加入另一个测试套件中，从而
# # 可以将多个测试套件组合在一起。这种处理方式和多个测试用例加入测试套件中是一样的。如在下面的
# # 代码中，加入了另外一个测试用例类StringStripTestCase，tdd_4.py
# import unittest


# class StringStripTestCase(unittest.TestCase):

#     def testBlank(self):
#         source = "HELLO    "
#         expect = "HELLO"
#         result = source.strip()
#         self.assertEqual(expect, result)

#     def testStr(self):
#         source = "xxHELLOxx"
#         expect = "HELLO"
#         result = source.strip("xx")
#         self.assertEqual(expect, result)


# class StringReplaceTestCase(unittest.TestCase):

#     def setUp(self):
#         self.source = "HELLO"

#     def testBlank(self):
#         ''' 测试空字符替换 '''
#         expect = "HELLO"
#         result = self.source.replace(source, "", "")
#         self.assertEqual(expect, result)    # 单元测试的最后步骤都是使用断言

#     def testBlankOrd(self):
#         ''' 测试空字符替换成常规字符 '''
#         expect = "*H*E*L*L*O*"
#         result = self.source.replace(source, "", "*")
#         self.assertEqual(expect, result)    # 使用断言判断测试是否通过

#     def testOrdBlank(self):
#         ''' 测试常规字符替换为空字符 '''
#         expect = "HEO"
#         result = self.source.replace(source, "LL", "")
#         self.assertEqual(expect, result)

#     def testOrd(self):
#         ''' 测试常规字符替换 '''
#         expect = "HEMMO"
#         result = self.source.replace(source, "LL", "MM")
#         self.assertEqual(expect, result)

# 加入测试套件中的测试实例，其运行的顺序是通过Python内置函数cmp对测试方法名排序而得到的


# # 重构代码
# # 重构可以使软件产品维持一种相对简单和可读的特性。这种特性在后续的维护中是很重要的。在上面的
# # 测试类中，测试用例是很多的，在这种情况下，如果对于每个测试用例都用具体代码实现，会使得代码
# # 非常冗长。为此，可以将具体代码进行重构，使得测试用例看起来更好
# import unittest


# class StringStripTestCase(unittest.TestCase):

#     def setup(self):
#         self.expect = "HELLO"

#     def checkequal(self, result, object, methodname, *args):
#         realresult = getattr(object, methodname)(*args)
#         self.assertEqual(result, realresult)

#     def testBlank(self):
#         self.checkequal(self.expect, "HELLO    ", "strip")

#     def testStr(self):
#         self.checkequal(self.expect, "xxHELLOxx", "strip", "xx")


# class StringReplaceTestCase(unittest.TestCase):

#     def setUp(self):
#         self.source = "HELLO"

#     def checkequal(self, result, object, methodname, *args):
#         realresult = getattr(object, methodname)(*args)
#         self.assertEqual(result, realresult)

#     def testBlank(self):
#         ''' 测试空字符替换 '''
#         self.checkequal("HELLO", self.source, "replace", "", "")

#     def testBlankOrd(self):
#         ''' 测试空字符替换成常规字符 '''
#         self.checkequal("*H*E*L*L*O*", self.source, "replace", "", "*")

#     def testOrdBlank(self):
#         ''' 测试常规字符替换为空字符 '''
#         self.checkequal("HE*O", self.source, "replace", "LL", "*")

#     def testOrd(self):
#         ''' 测试常规字符替换 '''
#         self.checkequal("HEMMO", self.source, "replace", "LL", "MM")


# def suite():
#     StringStripTestSuite = unittest.makeSuite(StringStripTestCase, "test")
#     StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase, "test")

#     alltests = unittest.TestSuite((StringStripTestSuite,
#                                    StringReplaceTestSuite))
# 重构代码是伴随着测试进行的。在对代码进行修改的时候，最好也是同时对代码进行重构，从而保持代
# 码的整洁


# 执行测试
# 在测试用例和测试套件都完成之后，可以通过测试来检查软件产品代码编写是否正确。有多种测试方法
# 可以用来测试代码

# # 1）交互式执行测试
# # 在unittest测试框架中提供了TestRunner类为测试的运行提供环境。实际使用中，最常见的
# # TestRunner类是TextTestRunner类。此类的实现使用一种文字化的运行方式来报告最后的测试结果
# # 默认情况下，此类会把输出发送到sys.stderr上, tdd_5.py
# import unittest


# import unittest


# class StringStripTestCase(unittest.TestCase):

#     def setUp(self):
#         self.expect = "HELLO"

#     def checkequal(self, result, object, methodname, *args):
#         realresult = getattr(object, methodname)(*args)
#         self.assertEqual(result, realresult)

#     def testBlank(self):
#         self.checkequal(self.expect, "HELLO    ", "strip")

#     def testStr(self):
#         self.checkequal(self.expect, "xxHELLOxx", "strip", "xx")


# class StringReplaceTestCase(unittest.TestCase):

#     def setUp(self):
#         self.source = "HELLO"

#     def checkequal(self, result, object, methodname, *args):
#         realresult = getattr(object, methodname)(*args)
#         self.assertEqual(result, realresult)

#     def testBlank(self):
#         ''' 测试空字符替换 '''
#         self.checkequal("HELLO", self.source, "replace", "", "")

#     def testBlankOrd(self):
#         ''' 测试空字符替换成常规字符 '''
#         self.checkequal("*H*E*L*L*O*", self.source, "replace", "", "*")

#     def testOrdBlank(self):
#         ''' 测试常规字符替换为空字符 '''
#         self.checkequal("HEO", self.source, "replace", "LL", "")

#     def testOrd(self):
#         ''' 测试常规字符替换 '''
#         self.checkequal("HEMMO", self.source, "replace", "LL", "MM")


# def suite():
#     StringStripTestSuite = unittest.makeSuite(StringStripTestCase, "test")
#     StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase, "test")

#     alltests = unittest.TestSuite((StringStripTestSuite,
#                                    StringReplaceTestSuite))

#     return alltests


# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

# 和tdd_4.py不同的是最后加入了执行测试的代码。使用TextTestRunner类构建了一个运行器对象。
# 此对象提供了一个run方法，开始执行测试。run方法所接收的参数为前面生成的测试套件。这样，测试
# 框架将会自动运行测试套件中的测试用例

# # 实际上，使用TextTestRunner类可以很容易地在交互式终端环境下进行测试。
# import unittest
# import tdd_5

# runner = unittest.TextTestRunner()
# result = runner.run(tdd_5.StringReplaceTestCase("testBlank"))
# # print(result.errors)
# # print(result.failures)
# print()
# for f in result.failures[0]:
#     print(f)
# print(result.__dict__)          # 获取对象属性


# # 2）命令行运行测试
# # 在unittest模块中包含一个全局方法main，可以方便地测试已经构建好的测试模块。下面是对tdd_5.py
# # 使用main方法后的修改代码
# 省略部分代码

# def suite():
#     StringStripTestSuite = unittest.makeSuite(StringStripTestCase, "test")
#     StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase, "test")

#     alltests = unittest.TestSuite((StringStripTestSuite,
#                                    StringReplaceTestSuite))

#     return alltests


# if __name__ == "__main__":
#     # runner = unittest.TextTestRunner()
#     # runner.run(suite())

#     unittest.main()

# 这段代码的主要特点是使用了unittest.main方法。实际上，main方法将使用unittest.TestLoader
# 类来自动查找和加载测试类中的测试用例。在执行的时候，测试模块中的所有单元测试用例都将会被执行
# 这里显示了具体的测试用例运行的过程。可以看到，这里的顺序是根据类名和方法名的字母顺序来排定
# 的。
# In [3]: run tdd_5.py -v
# testBlank (__main__.StringReplaceTestCase)
# 测试空字符替换 ... ok
# testBlankOrd (__main__.StringReplaceTestCase)
# 测试空字符替换成常规字符 ... ok
# testOrd (__main__.StringReplaceTestCase)
# 测试常规字符替换 ... ok
# testOrdBlank (__main__.StringReplaceTestCase)
# 测试常规字符替换为空字符 ... ok
# testBlank (__main__.StringStripTestCase) ... ok
# testStr (__main__.StringStripTestCase) ... ok

# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# OK


# 可以通过加上"-v"参数来显示详细的信息。更多的参数可以使用"-h"来查看
# In [4]: run tdd_5 -h
# usage: tdd_5.py [-h] [-v] [-q] [--locals] [-f] [-c] [-b] [tests [tests ...]]

# positional arguments:
#   tests           a list of any number of test modules, classes and test
#                   methods.

# optional arguments:
#   -h, --help      show this help message and exit
#   -v, --verbose   Verbose output
#   -q, --quiet     Quiet output
#   --locals        Show local variables in tracebacks
#   -f, --failfast  Stop on first fail or error
#   -c, --catch     Catch Ctrl-C and display results so far
#   -b, --buffer    Buffer stdout and stderr during tests

# Examples:
#   tdd_5.py                           - run default set of tests
#   tdd_5.py MyTestSuite               - run suite 'MyTestSuite'
#   tdd_5.py MyTestCase.testSomething  - run MyTestCase.testSomething
#   tdd_5.py MyTestCase                - run all 'test*' test methods
#                                        in MyTestCase


# 修改StringReplaceTestCase测试类中的testOrdBlank实现代码，如将"HE*O"改为"HEO"。这时候
# 在此运行测试的时候将出错
# In [8]: run tdd_5.py -v
# testBlank (__main__.StringReplaceTestCase)
# 测试空字符替换 ... ok
# testBlankOrd (__main__.StringReplaceTestCase)
# 测试空字符替换成常规字符 ... ok
# testOrd (__main__.StringReplaceTestCase)
# 测试常规字符替换 ... ok
# testOrdBlank (__main__.StringReplaceTestCase)
# 测试常规字符替换为空字符 ... FAIL
# testBlank (__main__.StringStripTestCase) ... ok
# testStr (__main__.StringStripTestCase) ... ok

# ======================================================================
# FAIL: testOrdBlank (__main__.StringReplaceTestCase)
# 测试常规字符替换为空字符
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/zjy/study/python/tdd_5.py", line 42, in testOrdBlank
#     self.checkequal("HE*O", self.source, "replace", "LL", "")
#   File "/Users/zjy/study/python/tdd_5.py", line 30, in checkequal
#     self.assertEqual(result, realresult)
# AssertionError: 'HE*O' != 'HEO'
# - HE*O
# ?   -
# + HEO


# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# FAILED (failures=1)
# An exception has occurred, use %tb to see the full traceback.

# SystemExit: True

# 这里可以看到，6个单元测试用例成功了5个，失败了一个。同时给出了失败的具体信息：
# AssertionError: 'HE*O' != 'HEO'。当然，这里并不是功能代码实现的问题，而是预期的测试结果
# 不正确。实际操作中，需要对代码进行修改


# 实际上，也可以将unittest模块作为脚本运行。可以将需要执行的测试套件中的测试用例名来作为参数
# 传递, 查看模块路径sys.modules["os"], 需要import sys
# run unittest.py tdd_5.StringReplaceTestCase.testBlank


# # 3）图形界面下的测试
# # /usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/
# # 3.6/share/doc/python3.6/examples/Tools/unittestgui/unittestgui.py
# # 在PyUnit中还包含一个图形化的测试界面，可以用来实现测试的图形化显示。这是使用Tkinter来编写
# # 的，可以使用下面的命令来执行
# # run unittestgui.py tdd_5.suite
# from PIL import Image


# img = Image.open(r"unittestgui1.png")
# img1 = Image.open(r"unittestgui2.png")
# img.show()
# img1.show()

# 图中所示为测试模块中含有测试用例失败情况的显示。当测试执行完毕后，图中显示了总共完成的测试
# 用例和失败的测试用例。这里的进度条中使用红色明确地指示了测试模块含有未通过的测试。这些信息
# 在下面的对话框中显示了出来。单机下面的失败测试用例，可以看到更详细的错误信息。

# 在修正了源代码中的错误后，重新执行此测试，可以看到图中的正确结果。这也是测试驱动开发需要
# 达到的结果。只有在这种测试用例都通过的前提下，才能够继续添加新的功能和代码。


# 使用doctest进行测试
# python还支持另外一种测试框架，就是doctest模块。使用此模块可以将代码中的docstring作为测试
# 用例运行，从而判断函数执行的正确性，形成运行结果。

# doctest模块介绍
# doctest模块作为一种新的单元测试框架，可以有效地利用代码注释中的文档内容。这种处理方式使得
# 文档即可以作为测试代码来执行

# 在支持doctest模块的代码中，docstring由普通注释部分和代码执行部分构成。其中，普通注释部分
# 和原来的注释形式是相同的。而对于可执行部分则有着一定的格式。其中可执行部分使用">>>"和"..."
# 来和普通注释部分区分。可以看到，这里的提示符均为Python标准shell中的提示符。对于可执行部分
# 开发人员可以预先编写测试用例。这些测试用例的书写和unittest模块中是类似的，只不过这里采用了
# 在python终端下运行的方法。在可执行部分中包含输入和输出两个部分。在实际运行过程中，doctest
# 模块将搜索代码中的docstring的可执行部分，并实际执行这段代码，然后比较运行的结果和期望值，
# 作为一次测试结果。

# doctest作为另一种测试框架，可以实现文档和代码的同步。另外，可以将文档字符串变成可执行文档
# 从而完成对于代码的测试。相对于unittest模块来说，doctest测试框架具有自身的一些特点。首先
# 是其使用方法简单，只需要复制和粘贴Python终端下的交互式输入和输出即可。这种处理方式使得开发
# 人员在项目初期可以更快的入手。另外，可以使用命令行参数来灵活地控制测试代码的运行，并通过增
# 强选项来增强文本输出显示。同时，还可以灵活地选择需要测试的docstring

# 正由于doctest模块的这种简单性，使得其有一些固有的弱点，不适合于有些领域。doctest采用的是
# 通过终端获取用户的输出结果来进行比较的，这样就要求测试的机器所输出的结果都是一致的。另外，
# 在doctest模块中并没有提供测试固件，这在有多个单元测试用例的时候会比较繁琐。

# 虽然doctest并不是一种很严格的测试驱动开发框架，但是作为一种新的测试框架，也给开发者提供了
# 另外一种选择。doctest模块的设计初衷是开发人员不需要再书写相关的测试代码，而仅仅是将这种
# 测试内置于文档字符串中。这种方式可以完善文档的书写和审核。如果是刚开始编写测试，文档测试将
# 会更加容易上手。而如果需要编写大量的单元测试用例，则可以考虑使用unittest测试框架。因为
# unittest模块提供了完善的类和方法，使得管理多个测试用例更加方便。同时，unittest框架还可以
# 对测试用例进行自定义，从而有助于提高软件测试的可靠性。


# 构建可执行文档
# # 查看整形范围
# import sys

# print(sys.maxsize)
# print(2 ** 63)
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# doctest测试框架的核心是构建可执行文档部分。因为在doctest模块中并没有包含测试类或者方法，
# 而都是包含在可执行文档中的。下面以Python文档中介绍的例子为基础来介绍doctest模块的使用。
# 下面就是一个简单的可执行文档。
# >>> factorial(5)
# 120
# """
# 这个代码片段中的factorial为函数名，其功能为得到一个数的阶乘值。在这里，使用了5作为参数，
# 而120是期望得到的结果。可以注意到，这里使用了Python的提示符">>>"，看起来这就像是在Python
# 标准Shell中输入的一样。下面代码中包含完整的阶乘实现和其docstring, doctest_1.py
# """
# This is the "example" module.

# The example module supplies one function, factorial().  For example,

# >>> factorial(5)
# 120
# """

# import math


# def factorial(n):
#     """
#     Return the factorial of n, an exact integer >=0.
#     If the result is small enough to fit in an int, return an int.
#     Else return a long.

#     这里包含了多个测试用例，用来测试factorial方法的返回值
#     >>> [factorial(n) for n in range(6)]
#     [1, 1, 2, 6, 24, 120]
#     >>> factorial(30)
#     265252859812191058636308480000000
#     >>> factorial(-1)
#     Traceback (most recent call last):
#     ...
#     ValueError: n must be >= 0

#     Factorials of floats are OK, but the float must be an exact integer:
#     检测浮点数是否为整数
#     >>> factorial(30.1)
#     Traceback (most recent call last):
#         ...
#     ValueError: n must be exact integer
#     >>> factorial(30.0)
#     265252859812191058636308480000000

#     It must also not be ridiculously large:
#     溢出检查
#     >>> factorial(1e100)
#     Traceback (most recent call last):
#         ...
#     OverflowError: n too large
#     """

#     if not n >= 0:
#         raise ValueError("n must be >= 0")
#     if math.floor(n) != n:
#         raise ValueError("n must be exact integer")
#     if n + 1 == n:  # catch a value like 1e300
#         raise OverflowError("n too large")
#     result = 1
#     factor = 2
#     while factor <= n:
#         result *= factor
#         factor += 1
#     return result


# def _test():
#     import doctest
#     doctest.testmod()


# if __name__ == "__main__":
#     _test()

# 在doctest模块的实际使用中可以直接从Python标准终端上进行复制。但是在docstring中并非所有
# 的内容都是测试用例，docstring中还包含其他文本，那怎么去区分这些内容呢？在docstring中测
# 试用例以提示符>>>开始，以空行或者下一个>>>结束，介于中间的文本会被忽略。

# 有些情况下，可能无法预测准确的输出，但是依然可以进行测试。例如，获取某个对象的ID，每次运行
# 测试的时候，得到的ID都是不一样的。
# def identity(obj):
#       """
#       >>> identity(1)
#       23400792
#       """
#       return id(obj)

# 每次运行的时候，获取的ID值都是不一样的，所以执行上面的测试代码是不能通过的。
# 测试的值可能会以不可预测的方式改变时，如果具体值对于测试结果并不重要，可以使用ELLIPSIS选
# 项来告诉doctest忽略验证值的某些部分。
# 例如：
# class MyClass(object):
#     pass

# def unpredictable(obj):
#     """Returns a new list containing obj.

#     >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
#     [<demo.MyClass object at 0x...>]
#     """
#     return [obj]

# unpredictable之后的注释#doctest: ELLIPSIS告诉doctest打开这个测试的ELLIPSIS选项，
# ...将替换对象id的内存地址，这样就会忽略期望值中的一部分，实际输出将匹配，并通过测试。


# # 执行doctest测试
# # 方法一：可以在终端中直接输入，如：~$ python3 -m doctest -v doctest_1.py
# # 方法二：可以在需要测试的代码后面加上下面的代码段。 通过这样的处理，此模块就具有了
# # doctest测试的功能
# def _test():
#     import doctest
#     doctest.testmod()


# if __name__ == "__main__":
#     _test()
# 这里实际上是定义了一个_test函数。此函数首先导入doctest模块，然后调用了其中的testmod方法
# testmod方法会搜索整个模块中的__doc__来寻找文档字符串中的可执行部分，并进行doctest测试
# 直接运行此文件，即可执行doctest测试，具体操作如下
# In [7]: run /Users/zjy/study/python/doctest_1.py

# 从运行结果来看，并没有任何的输出。这是因为现在所有的测试用例都通过了测试。当对文档字符串中
# 可执行部分做一些修改，doctest测试失败，则再次运行的时候，显示如下。
# **********************************************************************
# File "/Users/zjy/study/python/doctest_1.py", line 20, in __main__.factorial
# Failed example:
#     [factorial(n) for n in range(6)]
# Expected:
#     [1, 1, 3, 6, 24, 120]
# Got:
#     [1, 1, 2, 6, 24, 120]
# **********************************************************************
# 1 items had failures:
#    1 of   6 in __main__.factorial
# ***Test Failed*** 1 failures.

# # 从上面的输出可以看出给出了很详细的出错信息。其中包括出错的单元实例以及最终输出结果的对比。
# # 当测试用例全部通过测试的情况下，可以加上"-v"参数来显示具体的测试过程。
# # 或设置verbose参数，如doctest.testmod(verbose=True)      # 显示成功的测试
# In [9]: run /Users/zjy/study/python/doctest_1.py -v
# Trying:
#     factorial(5)
# Expecting:
#     120
# ok
# Trying:
#     [factorial(n) for n in range(6)]
# Expecting:
#     [1, 1, 2, 6, 24, 120]
# ok
# Trying:
#     factorial(30)
# Expecting:
#     265252859812191058636308480000000
# ok
# Trying:
#     factorial(-1)
# Expecting:
#     Traceback (most recent call last):
#     ...
#     ValueError: n must be >= 0
# ok
# Trying:
#     factorial(30.1)
# Expecting:
#     Traceback (most recent call last):
#         ...
#     ValueError: n must be exact integer
# ok
# Trying:
#     factorial(30.0)
# Expecting:
#     265252859812191058636308480000000
# ok
# Trying:
#     factorial(1e100)
# Expecting:
#     Traceback (most recent call last):
#         ...
#     OverflowError: n too large
# ok
# 1 items had no tests:
#     __main__._test
# 2 items passed all tests:
#    1 tests in __main__
#    6 tests in __main__.factorial
# 7 tests in 3 items.
# 7 passed and 0 failed.
# Test passed.

# 输出给出了doctest模块的详细测试过程。doctest模块将执行文档字符串中的可执行部分，并和期望
# 值进行比较，从而形成测试结果。最后给出了此次doctest测试的综合结果信息。

# 另外，在doctest模块中还包含一个testfile方法，用来读取指定文件中包含可执行文档的
# docstring
# 如果将文档字符串保存在factorial_docstring.txt文件中，则使用下面的代码同样可以实现
# doctest测试。这种处理方法的好处是可以将docstring集中处理。
# 首先创建factorial_docstring.txt文件，文件内容如下:
# >>> from doctest_1 import factorial
# >>> [factorial(n) for n in range(6)]
# [1, 1, 2, 6, 24, 120]
# >>> factorial(30)
# 265252859812191058636308480000000
# >>> factorial(-1)
# Traceback (most recent call last):
# ...
# ValueError: n must be >= 0
# >>> factorial(30.1)
# Traceback (most recent call last):
#     ...
# ValueError: n must be exact integer
# >>> factorial(30.0)
# 265252859812191058636308480000000
# >>> factorial(1e100)
# Traceback (most recent call last):
#     ...
# OverflowError: n too large

# # 然后在doctest_1.py文件最下方加入如下内容即可运行
# def _test():
#     import doctest
#     doctest.testfile("factorial_docstring.txt", verbose=True)


# if __name__ == "__main__":
#     _test()


# 上面介绍了doctest测试的应用。从示例代码中可以看到，这种测试方法还是相对比较简单的。在实际
# 操作中，doctest模块将会根据具体情况和unittest模块结合起来使用，从而发挥测试驱动开发模式
# 的最大优势
