from sklearn.linear_model import LinearRegression #导入线性回归
from sklearn import datasets #导入数据集
from sklearn import svm #导入SVM模型

iris = datasets.load_iris() #加载鸢尾花数据集
print(iris.data.shape) #查看数据维度
'''
结果：(150,4) 表示150条数据，4个分类
'''
clf = svm.LinearSVC() #建立线性SVM分类器
clf.fit(iris.data, iris.target) #用数据训练模型
clf.predict([[5.0, 3.6, 1.3, 0.25]])  #用新的数据预测
test_data = clf.coef_ #查看训练模型的参数
print(test_data)