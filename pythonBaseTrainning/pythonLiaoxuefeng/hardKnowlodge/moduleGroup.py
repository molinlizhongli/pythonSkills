# _*_ coding:utf-8 _*_
# Created by lzl
# TIME: 2021/2/25 13:52
'''
    python模块篇，介绍python内置模块、第三方模块等常用方法及说明
'''

'''
    # 使用模块
    内置很多有用模块，sys,os等，标准格式：
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    ' a test module '
    
    __author__ = 'Michael Liao'
    
    import sys
    
    def test():
        args = sys.argv
        if len(args)==1:
            print('Hello, world!')
        elif len(args)==2:
            print('Hello, %s!' % args[1])
        else:
            print('Too many arguments!')
    
    if __name__=='__main__':
        test()
    作用域：_前缀的是内部使用，正常函数和通用变量直接引用，特殊变量（__xxx__）不应该直接引用，private函数主要是做封装和抽象使用
    
    第三方模块：通过包管理工具pip完成 pip install Pillow，一个个安装采用这种方式
    推荐使用anaconda内置了很多第三方库
    模块路径：sys.path变量中，可以修改环境变量
    
    
    从新手到高手的100个模块（来源微信读书python高手修炼之道这本书附录B）
    （1）基础功能
    （2）数据库接口
    （3）网络通信
    （4）音像游戏
    （5）GUI
    （6）Web框架
    （7）科学计算
    （8）2D/3D
    （9）数据处理
    （10）机器学习
    （11）工具
    
'''
# 内建模块
'''
    datetime、collections、bases、 struct、hashlib、hmac、itertools、contextlib、urllib、XML、HTMLParser
    
'''
# 序列化模块 pickle
import pickle
import json
def pickleModule():

    dict_name = dict(name = 'Bob',age = 20, score = 90)
    print(pickle.dumps(dict_name)) # 任意对象序列化成bytes
    f = open('dump.txt','wb')
    pickle.dump(dict_name,f)
    f.close()
    # 反序列化
    fv = open('dump.txt','rb')
    print(pickle.load(fv))

    #序列化成json格式,使用json模块
    d_json = dict(name = 'Bob',age = 22, score =80)
    print(json.dumps(d_json))
    # 反序列化就是使用loads()或者load()方法，




# 第三方模块
'''
    pillow、requests、chardet、psutil
'''

if __name__ == '__main__':
    pickleModule()

