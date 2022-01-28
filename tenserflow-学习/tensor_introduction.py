import tensorflow as tf
import numpy as np

# 基础知识
# 创建基本张量
# 标量（或称0秩张量，只包含单个值，没有轴）
rank_0_tensor = tf.constant(4)
print(rank_0_tensor)

# 向量（或称1秩张量，像一个值得列表），向量只有一个轴
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)

# 矩阵”（或称“2 秩”张量）有 2 个轴
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
print(rank_2_tensor)
print('+++++++++++++++++++++++++++++++++++++++++++')
# 下面是一个包含 3 个轴的张量
rank_3_tensor = tf.constant([
  [[0, 1, 2, 3, 4],
   [5, 6, 7, 8, 9]],
  [[10, 11, 12, 13, 14],
   [15, 16, 17, 18, 19]],
  [[20, 21, 22, 23, 24],
   [25, 26, 27, 28, 29]],])

print(rank_3_tensor)

# 通过使用 np.array 或 tensor.numpy 方法，您可以将张量转换为 NumPy 数组
np.array(rank_2_tensor)
rank_2_tensor.numpy()

# tf.Tensor 基类要求张量是“矩形”
# 张量执行基本数学运算
a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]]) # Could have also said `tf.ones([2,2])`

print(tf.add(a, b), "\n")  #矩阵相加
print(tf.multiply(a, b), "\n") #数字相乘
print(tf.matmul(a, b), "\n")  #矩阵相乘
# 还可以写成这样
'''
print(a + b, "\n") # element-wise addition
print(a * b, "\n") # element-wise multiplication
print(a @ b, "\n") # matrix multiplication
'''
# 各种运算 (op) 都可以使用张量
c = tf.constant([[4.0, 5.0], [10.0, 1.0]])
print('---------------------------------------------')
# Find the largest value
print(tf.reduce_max(c))
# Find the index of the largest value
print(tf.argmax(c))
# Compute the softmax
print(tf.nn.softmax(c))

# 張量有形狀
'''
形状：张量的每个维度的长度（元素数量）。
秩：张量的维度数量。标量的秩为 0，向量的秩为 1，矩阵的秩为 2。
轴或维度：张量的一个特殊维度。
大小：张量的总项数，即乘积形状向量
'''
# 4秩张量
rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Type of every element:", rank_4_tensor.dtype)
print("Number of dimensions:", rank_4_tensor.ndim)
print("Shape of tensor:", rank_4_tensor.shape)
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())

#轴一般按照从全局到局部的顺序进行排序：首先是批次轴，随后是空间维度，最后是每个位置的特征。这样，在内存中，特征向量就会位于连续的区域。
