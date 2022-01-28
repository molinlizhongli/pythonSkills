from __future__ import  print_function
import pandas as pd
import matplotlib.pyplot as plt
#初始化参数
dish_profit = 'profit.xls'
data = pd.read_excel(dish_profit, index_col=u'菜品ID')
data = data [ u'盈利'].copy()
# 复制一份数据
data.sort(ascending = False)

plt.rcParams['font.sans-serif'] = ['SimHei']
#设置字体正常显示中文
plt.rcParams['axe.unicode_minus'] = False
#用来正常显示负号

plt.figure() #设置图像大小
data.plot(kind = 'bar')
plt.ylabel(u'盈利（元）')
p = 1.0*data.cumsum()/data.sum()
p.plot(color = 'r', secondary_y = True, style = '-o', linewidth = 2)
plt.annotate(format(p[6],'.4%'),xy = (6,p[6]), xytext = (6*0.9, p[6]*0.9), arropwprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=.2'))
#添加注释，85%处标记，包括箭头
plt.ylabel(u'盈利（比例）')
plt.show()
