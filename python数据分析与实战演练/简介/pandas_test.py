import pandas as pd

s = pd.Series([1,2,3], index=['a','b','c']) #创建一个序列，并制定索引的方式
d = pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c']) #创建一个表，使用的是DataFrame
d2 = pd.DataFrame(s) #将序列s转换为DataFrame，即二维数组

data_head = d.head() #预览前5行数据
data_total = d.describe() #数据基本统计量
print(data_head)
print(data_total)
pd.read_excel('data.xls') #读取xls文件，创建DataFrame
pd.read_csv('data.csv',encoding='utf-8') #读取csv文件，用utf-8编码