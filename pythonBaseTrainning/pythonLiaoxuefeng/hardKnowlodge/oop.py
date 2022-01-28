# _*_ coding = utf-8 _*_
# @Date : 2021/10/21
# @Time : 11:06
# @NAME ：molin

'''
    # 面向对象编程基础篇和高级篇、错误异常调试
    面向对象：一个对象包含了数据和操作数据的函数，每个对象可以接收其他对象发过来的消息，并处理这些消息
    计算机程序的执行就是一系列消息在各个对象之间传递的机制

    # class Student(object) # 定义类通常是大写开头
    # Student()  # 创建实例
    # __init__ # 特殊方法，初始化实例属性，绑定属性
    # 封装思想：在定义类的时候定义方法，方法内部定义逻辑

    # 访问限制：相对属性进行限制访问（外部不能访问内部）在__init__方法中，self__name，要是访问必须设置get和set方法;
    # 一个下划线_name:外部可以访问，但是虽然可以访问，是私有变量，不能随意访问
    # 继承: 要一个父类，直接在类的括号里输入父类名代表继承
    # 多态：数据类型不同，判断某个变量是否是某个数据类型（isinstance),如 isinstance(a,list)
    # 多态好处是：函数结果随着传入的父类数据类型而变化，不需要修改代码，当新增一个子类时，只需要确保方法编写正确，不用管原来的代码
    # 如何调用
    python 多态的特点是只要传入的对象具备某个方法，不需要严格的继承体系，只要像就可以当做是鸭子类型
    俗称 file-like object
    type(object)  获取对象类型 一般
    最好的方法是：isinstance(a, list)
    获得一个对象所有的属性：dir()
    有某个属性：hasattr(object,'x')


    # 实例属性和类属性
    通过self变量的，如self.name = name
    类本身需要绑定一个属性： name = 'Student' student是个类，这个name属性属于类属性
    实例属性和类属性不要相同，否则类属性会被屏蔽掉，如加一个统计的属性count


    # 高级篇：多重继承，定制类，元类
    限制实例的属性，如只允许对student实例添加name和age属性，定义类时定一个特殊变量__slots__
    class Student(object):
        __slots__ = ('name', 'age')
    实例化：s = Student()
    s.score  = 99 就会报错没有score属性
    但是这个__slots__ 支队当前类实例起作用，对继承的子类没有作用

    既能检查参数，又能用类似属性这样简单的方式访问类的变量，装饰器就是 @property装饰器就是负责把一个方法变成属性调用
    定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    birth是可读写属性，age是只读属性


    如果类层次不断增加，采用单纯的分类就显得特别冗长，正确的方法是多重继承，一个子类可以获得几个父类的所有功能
    多重继承设计往往被诟病，mixin命名的类表示作为功能加入子类，只代表一个功能，责任单一，不依赖子类的实现
    class Dog(Mammal, Runnable):
        pass
    编写一个多进程模式的TCP服务
    class MyTCPServer(TCPServer, ForkingMixIn):
        pass

    一个多线程模式的UDP服务，定义如下：
    class MyUDPServer(UDPServer, ThreadingMixIn):
        pass
    搞一个更先进的协程模型，可以编写一个CoroutineMixIn
    class MyTCPServer(TCPServer, CoroutineMixIn):
        pass

    # 定制类，类似__slots__ __len__(),列举常用的定制类
    __str__  返回一个好看的字符串
    __repr__ 返回开发者看到的字符串，是为调式服务的
    __iter__ 类实现for...in循环，该方法返回一个迭代对象
    __next__ 返回循环的下一个值，直到StopIteration错误退出循环
    __getitem__ 按照下标取出元素
    __getattr__ 尝试获得属性，若属性不存在返回属性的值
    __call__ 直接对实例进行调用，相当于把对象当成函数，
    callable(对象) 判断是否是一个可调用对象

    #枚举类
    为枚举类型定一个class类型，Enum类
    from enum import Enum

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    遍历一下
    for name,member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    若需要精准的控制枚举类型，可以从Enum派生出自定义类
    from enum import Enum, unique

    @unique
    class Weekday(Enum):
        Sun = 0
        Mon = 1
        Tue = 2
        Wed = 3
        Thu = 4
        Fri = 5
        Sat = 6

    # bug：编写问题
    # 用户输入造成：校验
    # 异常：比如断网、磁盘满了，这些异常需要做处理
    错误：约定错误代码，如404,500
    错误处理机制
    try:
        ...
    except Exception as e:
        ...
    finally:
        ...
    如：
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')
    如果错误没有被捕获，会一直往上抛，最后被python解释器捕获，打印错误信息

    记录错误，让程序继续执行，使用logging模块记录信息

    import logging

    def foo(s):
        return 10 / int(s)

    def bar(s):
        return foo(s) * 2

    def main():
        try:
            bar('0')
        except Exception as e:
            logging.exception(e)

    main()
    print('END')

    raise语句抛出一个错误的实例
    最常见的处理错误的方式是不断往上抛，让最顶层去处理

    # 调式： print(), 断言（assert），关闭assert可以用-O   python -O err.py, logging, ide（pycharm)
    def foo(s):
        n = int(s)
        assert n != 0, 'n is zero!'
        return 10 / n

    def main():
        foo('0')

    import logging
    logging.basicConfig(level=logging.INFO)

   # 单元测试：用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
   setup()和tearDown()方法，作用：如setup中连接数据库，tearDown方法中关闭数据库
   assertEqual(),断言输出是否是我们所期望的

   # 文档测试 doctest可以直接提取注释中的代码进行测试
   举个例子：
   # mydict2.py
   class Dict(dict):
    """
        simple dict but alse support access as x.y style
        >>> d1 = Dict()
        >>> d1['x'] = 100
        >>> d1.x
        100
        >>> d1.y = 200
        >>> d1['y']
        200
        >>> d2['empty']
        Traceback (most recent call last):
            KeyError:'empty'
    """
        def __init__(self, **kw):
            super(Dict, self).__init__(**kw)
        def __getattr__(self, key):
            try:
                return self[key]
            except KeyError:
                raise AttributeError(r"'Dict' object has no attribute '%s' % key)
        def __setattr__(self, key, value):
            self[key] = value
    if __name__= '__main__':
        import doctest
        doctest.testmod()


'''
