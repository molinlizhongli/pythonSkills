# _*_ coding = utf-8 _*_
# @Date : 2021/4/16
# @Time : 15:01
# @NAME ：molin

import os
'''
    csvfile.py是用来实现csv格式文件读、取、写、删、查
'''

def csvRead():
    system_type = os.name
    system_detail = os.environ
    print(system_type)
    print(system_detail)

if __name__ == '__main__':
    csvRead()