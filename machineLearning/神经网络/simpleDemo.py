# _*_ coding = utf-8 _*_
# @Date : 2022/2/21
# @Time : 13:36
# @NAME ：molin


import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import datasets,layers,optimizers,Sequential,metrics

def showClothes():
    (x,y),(x_test,y_test) = datasets.fashion_mnist.load_data()
    index = 1
    fig, axes = plt.subplots(4,3,figsize=(8,4),tight_layout=True)
    for row in range(4):
        for col in range(3):
            axes[row,col].imshow(x[index])
            axes[row,col].axis('off')
            axes[row,col].set_title(y[index])
            index += 1
    plt.show()

# 处理图片像素
def  preprocessPic(x,y):
    x = tf.cast(x,dtype=tf.float32) / 255.
    y = tf.cast(y,dtype=tf.int32)
    return x,y

# 建立模型
def setModel():
    model = Sequential([
        layers.Dense(256,activation=tf.nn.relu),
        layers.Dense(128,activation=tf.nn.relu),
        layers.Dense(64,activation=tf.nn.relu),
        layers.Dense(32,activation=tf.nn.relu),
        layers.Dense(10)
    ])
    model.built(input_shape=[None, 28*28])
    model.summary()
    optimizers = optimizers.Adam(lr=1e-3)


if __name__ == '__main__':
    db = tf.data.Dataset.from_tensor_slices((x,y))
    db = db.map(preprocessPic).shuffle(10000).batch(128)
    db_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))
    db_test = db_test.map(preprocessPic).batch(128)
    showClothes()