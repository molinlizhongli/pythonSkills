import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000) #作图的变量自变量
y = np.sin(x) + 1 #因变量y
z = np.cos(x ** 2) + 1 #因变量z

plt.figure(figsize=(8, 4)) #设置图像大小
plt.plot(x , y, label = '$\sin x + 1$', color = 'red', linewidth = 2) #作图，设置标签、线条颜色、线条大小
plt.plot(x, z, 'b--', label = '$\cos x^2+1$') #作图，设置标签、线条类型
plt.xlabel('Time(s)') #设置x轴
plt.ylabel('Volt') #设置y轴
plt.title('A simple example') #设置标题
plt.ylim(0,2.2) #设置y轴显示范围
plt.legend() #显示图例
plt.show() #显示作图结果