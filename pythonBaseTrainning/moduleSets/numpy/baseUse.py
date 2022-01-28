# _*_ coding = utf-8 _*_
# @Date : 2021/11/8
# @Time : 13:21
# @NAME ：molin

'''
    # numpy 基础使用，包括各种数据类型和函数

'''

# 一、安装
# windows：pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
# linux : sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
# 验证：
# from numpy import *
import numpy as np
# print(eye(4))

# 类型 ：N维数组对象ndarray，存储同类型元素的多维数组
# a = np.array([1, 2, 3])
# a = np.array([[1, 2], [3, 4]]) #多维
# a = np.array([1, 2, 3, 4, 5], nadmin = 2)#最小维度
# print(a)

# 二、创建数组
# 法1 numpy.empty(shape,dtype = float, order = 'C')
import numpy as np
# x = np.empty([3,2], dtype= int)
# print(x)

# 法2 numpy.zeros(shape, dtype = float, order = 'C')
# z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
# print(z)

# 法3 创建指定形状的数组 numpy.ones(shape, dtype = float, order = 'C')
# x = np.ones([2,2], dtype = int)
# print(x)
# 法4 从已有的数组创建数组 numpy.asarray(a, dtype = None, order = None)
# x =  [1,2,3] 或 x =  (1,2,3) 或x =  [(1,2,3),(4,5)]
# a = np.asarray(x)
# print (a)
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象
'''
# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
 
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)
'''
#法4 从数值范围创建数组
# numpy.arange(start, stop, step, dtype)
# numpy.linspace
# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
# numpy.logspace
# numpy.logspace 函数用于创建一个于等比数列

# 三、操作
# 切片和索引,类似list的操作
# a = np.arange(10)
# s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
# 或者 b = a[2:7:2]
# print (a[s])
# 高级索引，数组可以由整数数组索引、布尔索引和花式索引
# x = np.array([[1,  2],  [3,  4],  [5,  6]])
# y = x[[0,1,2],  [0,1,0]]
# print (y)
# 组合：切片或者索引数组组合
# a = np.array([[1,2,3], [4,5,6],[7,8,9]])
# b = a[1:3, 1:3]
# c = a[1:3,[1,2]]
# d = a[...,1:]
# print(b)
# print(c)
# print(d)
# print (a[a >  5]) 通过一个布尔数组来索引目标数组,获取大于 5 的元素
# 花式索引指的是利用整数数组进行索引