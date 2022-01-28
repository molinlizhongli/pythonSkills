import os
import tensorflow as tf
import cProfile
import numpy as np
import matplotlib.pyplot as plt

print(tf.executing_eagerly())
#默认是开启eager execution的
x = [[2.]]
m = tf.matmul(x, x)
print('hello, {}'.format(m))

#tf.Tensor 对象会引用具体值，而非指向计算图中节点的符号句柄
a = tf.constant([[1, 2],[3, 4]])
print(a)
#上面返回结果
'''
tf.Tensor(
[[1 2]
 [3 4]], shape=(2, 2), dtype=int32)
'''
b = tf.add(a,1)
print(b)
'''
返回结果
tf.Tensor(
[[2 3]
 [4 5]], shape=(2, 2), dtype=int32)
'''
print(a * b)
'''
返回结果
tf.Tensor(
[[ 2  6]
 [12 20]], shape=(2, 2), dtype=int32)
'''

c = np.multiply(a, b)
print(c)
'''
返回结果
[[ 2  6]
 [12 20]]
'''

print(a.numpy())
'''
返回结果，返回的是tensor部分
[[1 2]
 [3 4]]
'''

# 编写一个函数判断fizzbuzz
def fizzbuzz(max_num):
  counter = tf.constant(0)
  max_num = tf.convert_to_tensor(max_num)
  for num in range(1, max_num.numpy()+1):
    num = tf.constant(num)
    if int(num % 3) == 0 and int(num % 5) == 0:
      print('FizzBuzz')
    elif int(num % 3) == 0:
      print('Fizz')
    elif int(num % 5) == 0:
      print('Buzz')
    else:
      print(num.numpy())
    counter += 1
fizzbuzz(15)

#计算梯度，使用tf.GradientTape
w = tf.Variable([[1.0]])
with tf.GradientTape() as tape:
    loss = w * w
grad = tape.gradient(loss, w)
print(grad)
'''
返回数据
tf.Tensor([[2.]], shape=(1, 1), dtype=float32)
'''

#训练模型，实现对mnist手写数字进行分类
# Fetch and format the mnist data
(mnist_images, mnist_labels), _ = tf.keras.datasets.mnist.load_data()

dataset = tf.data.Dataset.from_tensor_slices(
  (tf.cast(mnist_images[...,tf.newaxis]/255, tf.float32),
   tf.cast(mnist_labels,tf.int64)))
dataset = dataset.shuffle(1000).batch(32)

# Build the model
mnist_model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(16,[3,3], activation='relu',
                         input_shape=(None, None, 1)),
  tf.keras.layers.Conv2D(16,[3,3], activation='relu'),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10)
])

# 即使没有训练，也可以在 Eager Execution 中调用模型并检查输出：
for images,labels in dataset.take(1):
  print("Logits: ", mnist_model(images[0:1]).numpy())

# 训练循环
optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_history = []

# 执行训练步骤
def train_step(images, labels):
  with tf.GradientTape() as tape:
    logits = mnist_model(images, training=True)

    # Add asserts to check the shape of the output.
    tf.debugging.assert_equal(logits.shape, (32, 10))

    loss_value = loss_object(labels, logits)

  loss_history.append(loss_value.numpy().mean())
  grads = tape.gradient(loss_value, mnist_model.trainable_variables)
  optimizer.apply_gradients(zip(grads, mnist_model.trainable_variables))

#开始训练
def train(epochs):
  for epoch in range(epochs):
    for (batch, (images, labels)) in enumerate(dataset):
      train_step(images, labels)
    print ('Epoch {} finished'.format(epoch))

# train(epochs = 3)

plt.plot(loss_history)
plt.xlabel('Batch')
plt.ylabel('loss[entropy]')
# plt.show()
# 变量和优化器 tf.Variable 对象会存储在训练期间访问的可变、类似于 tf.Tensor 的值，以更简单地实现自动微分

class Linear(tf.keras.Model):
  def __init__(self):
    super(Linear, self).__init__()
    self.W = tf.Variable(5., name='weight')
    self.B = tf.Variable(10., name='bias')
  def call(self, inputs):
    return inputs * self.W + self.B

# A toy dataset of points around 3 * x + 2
NUM_EXAMPLES = 2000
training_inputs = tf.random.normal([NUM_EXAMPLES])
noise = tf.random.normal([NUM_EXAMPLES])
training_outputs = training_inputs * 3 + 2 + noise

# The loss function to be optimized
def loss(model, inputs, targets):
  error = model(inputs) - targets
  return tf.reduce_mean(tf.square(error))

def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
      loss_value = loss(model, inputs, targets)
  return tape.gradient(loss_value, [model.W, model.B])

'''
下一步：
创建模型。
损失函数对模型参数的导数。
基于导数的变量更新策略。
'''
model = Linear()
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

print("Initial loss: {:.3f}".format(loss(model, training_inputs, training_outputs)))

steps = 300
for i in range(steps):
  grads = grad(model, training_inputs, training_outputs)
  optimizer.apply_gradients(zip(grads, [model.W, model.B]))
  if i % 20 == 0:
    print("Loss at step {:03d}: {:.3f}".format(i, loss(model, training_inputs, training_outputs)))

print("Final loss: {:.3f}".format(loss(model, training_inputs, training_outputs)))
print("W = {}, B = {}".format(model.W.numpy(), model.B.numpy()))

#基于对象的保存，tf.keras.Model 包括一个方便的 save_weights 方法，您可以通过该方法轻松创建检查点
model.save_weights('weights')
status = model.load_weights('weights')
x = tf.Variable(10.)
checkpoint = tf.train.Checkpoint(x=x)
x.assign(11.)  # Change the variable after saving.
x.assign(2.)   # Assign a new value to the variables and save.
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/')

# Restore values from the checkpoint
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))

print(x)  # => 2.0
model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(16,[3,3], activation='relu'),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10)
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
checkpoint_dir = 'path/to/model_dir'
if not os.path.exists(checkpoint_dir):
  os.makedirs(checkpoint_dir)
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
root = tf.train.Checkpoint(optimizer=optimizer,
                           model=model)

root.save(checkpoint_prefix)
root.restore(tf.train.latest_checkpoint(checkpoint_dir))

'''
tf.keras.metrics 会被存储为对象。可以通过将新数据传递给可调用对象来更新指标，并使用 tf.keras.metrics.result 方法检索结果
'''
m = tf.keras.metrics.Mean("loss")
m(0)
m(5)
m.result()  # => 2.5
m([8, 9])
m.result()  # => 5.5