import numpy as np
import operator
from os import listdir
"""
函数说明:kNN算法,分类器
Parameters:
	inX - 用于分类的数据(测试集)
	dataSet - 用于训练的数据(训练集)
	labes - 分类标签
	k - kNN算法参数,选择距离最小的k个点
Returns:
	sortedClassCount[0][0] - 分类结果
Modify:
	2017-03-25
"""

def classifyO(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向),行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = diffMat**2
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方,计算出距离
    distances = sqDistances**0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}

    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]

"""
函数说明:将32x32的二进制图像转换为1x1024向量。
Parameters:
	filename - 文件名
Returns:
	returnVect - 返回的二进制图像的1x1024向量
Modify:
	2017-03-25
"""
def img2vector(filename):
    # 创建1x1024零向量
    returnVect = np.zeros((1, 1024))
    # 打开文件
    fr = open(filename)
    # 按行读取
    for i in range(32):
        # 读一行数据
        lineStr = fr.readline()
        # 每一行的前32个元素依次添加到returnVect中
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    # print(returnVect)

    return returnVect

"""
函数说明:手写数字分类测试
Parameters:
	无
Returns:
	无
Modify:
	2017-03-25
"""
def handwritingClassTest():

    hwLabels = []

    trainingFileList = listdir('trainingDigits')

    m = len(trainingFileList)

    trainingMat = np.zeros((m, 1024))

    for i in range(m):

        fileNameStr = trainingFileList[i]

        classNumber = int(fileNameStr.split("_"
                                            ))

if __name__ == '__main__':
    filename = r"../dataset/knn_shouxiebi0_01.txt"
    img2vector(filename)

