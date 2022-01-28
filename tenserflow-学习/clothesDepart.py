import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

#导入fashion mnist数据集
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#图像数据集不包括类名称，需要存储下，方便绘制图像使用
#图像是28*28的Numpy数组，像素值在0-255，标签是整数数组，值在0-9
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#浏览数据,显示数据维度
print(train_images.shape)
print(len(train_labels))
print(train_labels)
print(test_labels)
print(test_images.shape)


#预处理数据,像素值范围在0-255，需要将其缩小至0-1，然后在反馈给神经网络模型
train_images = train_images / 255.0
test_images = test_images / 255.0
#为了验证数据的格式是否正确，我们验证前36张图像
plt.figure(figsize=(10,10))
for i in range(36):
    plt.subplot(6,6,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
plt.show()

#构建模型
#需要先配置模型的层，然后在编译模型
model = keras.Sequential([
keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

#编译模型
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
# 优化器（确定如何更新），损失函数（测量模型训练准确率），指标（准确率）


# 训练模型
model.fit(train_images, train_labels, epochs=10)
#10次拟合之后，准确率达到91%

#保存模型格式为pb
tf.keras.models.save_model(model,"model_save_path") # 默认生成 .pb 格式模型，也可以通过save_format 设置 .h5 格式
print('模型已保存')

#评估模型的准确率
test_loss, test_acc = model.evaluate(test_images, test_labels,verbose=2)
print('\nTest accuracy:',test_acc)

#训练准确率和测试准确率之间的差距代表过拟合了，这个课题后面再研究

#开始进行预测
#附加一个softmax层，将上面的线性输出转换成可以理解的概率
probability_model = tf.keras.Sequential([
    model,tf.keras.layers.Softmax()
])

predictions = probability_model.predict(test_images)
#上面是测试集的预测，我们来看第一个预测结果
print(np.argmax(predictions[0]))
#其中返回的结果是一个10个数的数组，代表模型对10中不同服装的置信度,匹配对应的服装
#验证测试集的结果,可以发现模型预测的结果跟实际测试集结果一样
print(test_labels[0])

#绘制图表，看看模型对于10个类的预测情况
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# i = 0
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions[i], test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions[i],  test_labels)
# plt.show()

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()


