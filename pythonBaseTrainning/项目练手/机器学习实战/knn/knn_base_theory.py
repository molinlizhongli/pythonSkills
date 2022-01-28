# _*_ coding = utf-8 _*_
# @Date : 2021/12/13
# @Time : 13:22
# @NAME ：molin

import math
import csv
import operator
import random
import numpy as np
from sklearn.datasets import make_blobs


# 加载鸢尾花卉数据集 filename(数据集文件存放路径)
def loadIrisDataset(filename):
    with open(filename, 'rt') as csvfile:
        lines = csvfile.readlines(csvfile)
        dataset = list(lines)

        for x in range(len(dataset)):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
        return dataset

def main():
    # 使用自定义创建的数据集进行分类
    # x,y = createDataSet(features=2)
    # dataSet= np.c_[x,y]


    # 使用鸢尾花卉数据集进行分类
    dateSet = loadIrisDataset(r'../dataset/iris.txt')
    print(dateSet)

if __name__ == '__main__':
    main()