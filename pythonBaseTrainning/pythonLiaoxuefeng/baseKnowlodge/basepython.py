# _*_ coding:utf-8 _*_
# Created by lzl
# TIME: 2021/2/25 13:50
'''
    python基础篇，介绍python安装、数据类型等基础知识
'''

# 数据类型和变量
print(100)
print(100 + 200)
print('I\'m \"ok"!')
print('https://www.baidu.com')
print('line','line2','line3')
print(True,False)
PI = 3.14159265359
print(PI)
print(10 // 3)
print(10 / 3)

#字符串和编码

'''
    编码ASCII和Unicode和UTF-8
    ASCII一个字节（8bit），Unicode两个字节（16bit），UTF-8可变字节，根据字符进行划分字节（A就是1个字节，中就是3个字节）
    计算机内存中统一使用Unicode编码，只有保存到硬盘或者需要传输的时候才转换成UTF-8编码
'''
print("包含中文的str")
print(ord('A')) # 获取字符的整数表示
print(chr(66)) # 转换成对应的字符
print(b'ABC') #若是在网络上传输或者保存到磁盘上，需要把str变为以字节为单位的bytes
print('ABC'.encode('ascii')) #通过encode编码为ascii的bytes
# 编码只能从范围高的到低的，不能超出范围，如中文的str不能用ascii编码
print(b'ABC'.decode('ascii',errors='ignore')) #通过decode解码为ascii的str,后面的errors表示忽略无效的部分，可以不要

'''
    在操作字符串的时候，经常会遇到bytes和str的互换，为了避免乱码问题，始终使用utf-8编码
    文件开头写上两行：
    #!/usr/bin/env python3
    # _*_ coding:utf-8 _*_
'''

'''
    格式化：通常用%，%s表示用字符串替换，%d表示用整数替换，%?表示占位符，后面有几个变量就带上
    一种格式化字符串的使用是f开头，f-string，
    如： r = 2.5
    s = 3.14 ** r ** 2
    print(f'the area of a circle with radius {r} is {s:.2f}')
'''
print('%2d-%02d' %(3,1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' %7) #若%是普通字符，则用%%表示

print('hello,{0},成绩提高了{1:.1f}分'.format('小明',18.26))

print(f'PI的值是：{PI},保留三位小数是：{PI:.3f}') #f开头的会直接可以存变量名，动态加载

#使用list和tupple
'''
    list 可以修改，查找list[index]，append(),insert()
    tuple 元组不可以修改，t = ()空元组，t = (1,)一个元素的元组,不可改变的是元组的指向
'''
calssmates = ['张三','李四','王五']
print(calssmates)
print(len(calssmates))
print(calssmates[0])
print(calssmates[-1])
calssmates.append('徐六')
print(calssmates)
calssmates.insert(1,'钱七')
print(calssmates)
calssmates[-1] = '徐柳' #将最后一个人替换为徐柳
calssmates.pop() # 删除末尾元素
calssmates.pop(1) # 删除索引为1的元素
print(calssmates)

#元组（没有append和insert方法，元组不可变，代码安全，元组无论是不是一个，后面都要加逗号，防止歧义）
classmates = ('1','2','3')


# 条件判断
'''
 if:
 showFlag = true
 if showFlag :
    print("yes")
 else:
    print("no")
多个条件使用elif，判断时要注意类型
'''
showFlag = True
if showFlag:
    print("yes")
else:
    print("no")

# 循环
'''
    for ...in
    names = ['张三','李四','王五']
    for name in names:
        print(name)
        
    range()函数，生成整数序列 list()函数转成list
    print(list(range(5)))
    
    while 
    满足条件就循环，如计算100以内奇数之和
    sum = 0 
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    
    break
    提前退出循环
    continue
    跳过当前循环，进入下一次循环
'''
print(list(range(5)))
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 使用dict和set
'''
    dict的key判断是否存在,key必须是不可变对象,需要通过key计算value位置，算法是hash算法（字符串、整数）
    key in dict(in,get())
    dict.get(key)
    dict.pop(key)删除key
    
    set是一组key集合，不含value，创建set需先提供一个list作为输入
    s = set([1,2,3])
    add(key),remove(key)
'''



