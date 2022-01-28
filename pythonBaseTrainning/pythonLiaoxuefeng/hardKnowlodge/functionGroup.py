# _*_ coding:utf-8 _*_
# Created by lzl
# TIME: 2021/2/25 13:52
'''
    python函数篇，介绍python初级函数、高级函数、函数式编程等进阶知识
'''

# 函数篇
'''
    内置函数：abs
    help(函数名)，需要注意传入的参数个数、类型
    定义函数：def 函数名（参数）：
        return 值
    导入函数：from 文件名 import 函数名
    import math
    数据类型检查：isinstance()
    如：if not isinstance(x,(int,float)):
            raise TypeError('bad operated type')
    位置参数，如x的平方，但不影响默认值,默认值必须是不可变对象
    def power(x,n=2):
        s = 1 
        while n > 0:
            n = n - 1
            s = s * x
        return s
    def calc(*numbers):  可变参数，可以传入任意个参数，包括0个参数，参数其实自动组装成一个tuple
    def calc(**numbers): 参数自动组装成一个dict
    def calc(**kw)： 其中kw是需要在函数内部检查，命名关键字参数是需要一个特殊分隔符*
    如： def person(name,age,**kw):
            if 'city' in kw:
                pass
            if 'job' in kw:
                pass
            print('name:',name,'age:',age,'other:',kw)
    参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    >>> f1(1, 2, 3, 'a', 'b', x=99)
        a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

    递归函数：
    调用函数本身，如阶乘,需要注意栈溢出，调用次数需要收到限制，尾递归优化，return语句不能包含表达式自身，只会占用一个栈帧

    fact(n) = n * fact(n-1)
    原：def fact(n):
        if n==1:
            return 1
        return n * fact(n - 1)
    尾递归优化：每次只返回递归函数本身，不含表达式
        def fact(n):
            return fact_iter(n, 1)

        def fact_iter(num, product):
            if num == 1:
                return product
            return fact_iter(num - 1, num * product)
'''


# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print(power(5, 2))
# print(power(5))
# print(power(5, 3))

'''
    # 高级特性
    切片：取片段都可以采用切片，负责取指定索引范围的操作
    L[0:3] 取0，1,2索引数据
    L[:3] 同上
    L[::] 取所有
    L[-2:] 去后两个，后面开始索引获取，第一个数索引是-1
    range() 自带创建序列数方法
    L[1:10:2] 1-10的按照步长2获取
    切片适合数据类型：list,tuple,字符串等
    
    迭代：通过for循环遍历对象的过程就称为迭代
    for key in d:  迭代一个变量
    for i, value in enumerate(['A', 'B', 'C'])  迭代两个变量，其中enumerate函数把一个list变成索引-元素对
    isinstance('abc',Iterable)  判断对象是否是可迭代对象
    isinstance('abc',Iterator)  判断对象是否是迭代器
    
    列表生成式：使用表达式+for的形式表示
    [x * x for x in range(1:10)]
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    [k + '=' + v for k,v in d.items()]  包含两个或者多个变量的列表生成式
    [x for x in range(1,11) if x % 2 = 0 ]  穿插条件 if
    [ x if x % 2 = 0 else -x for x in range(1,11)] 穿插条件 if... else
    
    生成器：只需要将列表生成器[]编程（）就可以，机制是一遍循环一遍计算，惰性计算，返回的是一个算法，或者说是数据流
    通过next()获得generator返回值，超过范围报StopIteration异常
    含有yield的都可以看做是生成器
    
    迭代器：直接作用关于for循环的对象是可迭代对象 Iterable
    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
    生成器都是Iterator，但是list,str,dict不是Iterator，可以通过调用iter()方法成为Iterator
    Iterator甚至可以表示一个无限大的数据流 
    
    
    # 函数式编程
    高阶函数：函数本身可以作为变量，指向另一个函数的
    map/reduce、filter、sorted
    map/reduce:格式相差无几，只是一个是单体计算，一个是累积计算
    map: f(x) = x * x;   表示为： r = map(f,[1,2,3,4,5]) 最后形成是一个Iterator，需要list()返回整个序列
    list(r) 最后结果为一个list
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4),就是累积计算
    
    filter :用于过滤序列，思路是先给定序列，然后定义筛选函数，最后定一个生成器，不断返回过滤结果
    以获取1000 以内的素数为例：
        def _odd_iter():
            n = 1
            while True:
                n = n + 2 
                yield n
        
        def _not_divisible(n):
            return lambda x: x % n > 0 
            
        def primes():
            yield 2
            it = _odd_iter() # 初始序列
            while True :
                n = next(it) # 返回序列的第一个数
                yield n 
                it = filter(_not_divisible(n),it)
                
        for n in primes():
            if n < 1000:
                print(n)
            else:
                break
                
    sorted:函数抽象的方式
    sorted([36, 5, -12, 9, -21])
    sorted([36, 5, -12, 9, -21], key=abs)
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    
    返回函数：可变参数求和为例（不需要立刻求和，只需要返回求和函数）
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax
        return sum
    f = lazy_sum(1, 3, 5, 7, 9)  返回的是函数，这种方式成为“闭包”
    f() 才返回的是求和结果
    
    匿名函数：正则表达式就是匿名函数的经典表示法，不直接显示定义函数 lambda
    list(map(lambda x: x * x ,[1,2,3,4,5]))
    
    装饰器：函数对象自带类似__name__属性，想在代码运行期间动态增加功能，不改变函数定义的方式
    其本质上是返回函数的高阶函数
        def log(func):
            def wrapper(*args, **kw):
                print('call %s():' % func.__name__)
                return func(*args, **kw)
            return wrapper
        @log
        def now():
            print('2015-3-25')
        now()后就会在前面先打印log
        
    偏函数：可以做到如同设定参数默认值，降低函数调用的难度作用
        # 二进制转换，functools.partial的功能就是这个，对于参数个数太多，就可以依据这个创建新函数，固定部分参数
        def int2(x ,base=2):
            return int(x,base)
'''

# 求1000以内素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break