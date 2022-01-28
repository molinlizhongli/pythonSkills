from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.datasets import mnist

#载入数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = Sequential() #模型初始化
model.add(Dense(20, 64)) #添加输入层（20节点），第一隐藏层（64节点）的连接
model.add(Activation.get('tanh'))
#激活函数选择tanh
model.add(Dropout(0.5)) #防止过拟合
model.add(Dense(64, 64)) #添加第一隐藏层（64节点），第二隐藏层（64节点）的连接
model.add(Activation.get('tanh')) #激活函数选择tanh
model.add(Dropout(0.5)) #防止过拟合
model.add(Dense(64, 1)) #添加第二隐藏层（64节点），输出层（1节点）的连接
model.add(Activation.get('sigmoid')) #激活函数选择sigmoid

'''
这里出现了一个异常，编译器无法编译激活函数
 raise TypeError(
TypeError: Could not interpret activation function identifier: 64
解决方式：


'''

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True) #定义求解算法
model.compile(loss='mean_squared_error',optimizer=sgd) #编译生成模型，损失函数和优化器

model.fit(x_train, y_train, nb_epoch=20, batch_size=16) #训练模型
score = model.evaluate(x_test, y_test,batch_size=16) #测试模型
print(score)