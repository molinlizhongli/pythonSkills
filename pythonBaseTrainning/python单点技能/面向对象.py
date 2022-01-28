# _*_ coding = utf-8 _*_
# @Date : 2022/1/6
# @Time : 12:47
# @NAME ：molin

'''
    一、
    面向对象：类对象、实例对象、类变量、实例变量、类方法、实例方法、静态方法

    二、
    super与mro机制
'''

# 类对象和实例对象
class Person: # 声明一个类对象

    move = True    # 这是类变量

    def __init__(self, name, age): # 实例函数
        self.name = name  # 这是实例变量

        self.age = age  # 这是实例变量
    pass

p1 = Person() #声明一个实例对象

# 类变量和实例变量区别
    # 1、概念上 ：实例变量必须在实例函数中，类变量在类内部
    # 2、声明上 ：实例变量只能在内部声明，且用self关键字修饰
    # 3、访问上 ：类变量使用类名.变量名或者实例名.变量名，实例变量只能使用实例名.变量名
    # 4、存储上 ：类变量只会在class关键字声明类时创建，只会保存在类的命名空间里，实例变量访问的是各自的实例命名空间中
# 类变量声明通常在类内部，但函数体外，不需要用任何关键字修饰。
# 实例变量一般声明在实例方法内部（其他方法内部也不行），且用self关键字修饰。

p1.gender='男' # 声明实例对象结束之后再绑定一个实例变量

Person.eat = True  # 声明类对象结束之后再绑定一个类变量

# 静态方法、类方法、实例方法
# 1、静态方法： @staticmethod装饰器来修饰，无需实例化类，直接类名.方法名()调用，也可以实例化调用，
#   静态方法内部，只能通过类名.类变量名访问类变量
'''
    @staticmethod

    def static_fun(): # 声明一个静态方法

        print(Person.move)
'''

# 2、类方法：类方法需要使用@classmethod装饰器来修饰，且传入的第一个参数为cls，指代的是类本身，
# 类方法可以在方法内部通过cls关键字访问类变量。在类方法内部，既能通过“类名.类变量名”的方式访问类变量，
# 也能通过“cls.类变量名”的方式访问类变量
'''
    @classmethod

    def class_fun(cls): # 声明一个类方法

        print(cls.move)

        print(Person.move)# cls 指的就是Person类，等效
'''

# 3、实例方法：实例方法不需要装饰器修饰，不过在声明时传入的第一个参数必须为self，self指代的就是实例本身
'''
    def instance_fun(self): # 声明一个实例方法

        print(Person.move) # 访问类变量

        print(self.name , self.age)
        
p1.instance_fun()

Person.instance_fun(p1) #通过类访问实例方法时，必须显式地将实例当做参数传入
'''

# 二、super和mro（Method Resolution Order,方法解析顺序）
# super主要解决多继承问题中出现的重复实例化问题，
'''
    super传参方式：3种
    super()
    super(type , obj)
    super(type_1 , type_2)
    上面其实调用的是父类下一个类的方法
    super() 只会按照继承的解析顺序排列，原理就是mro
    class A(object):
        pass

    class B(object):
        pass
    
    class C(object):
        pass
    
    class D(A,B):
        pass
    
    class E(B, C):
        pass
    
    class F(D, E):
        pass
    
    print(F.__mro__)
    
    输出结果为：按照F>D>A>E>B>C  左侧优先顺序解析

　　(<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
'''
