from scipy.optimize import fsolve  #导入求方程组函数
from scipy import  integrate #导入积分函数
#求解非线性方程组2x1-x2^2 = 1,x1^2-x2 = 2
def f(x): #定义求解的方程组
    x1 = x[0]
    x2 = x[1]
    return [2*x1-x2**2-1,x1**2-x2-2]

result = fsolve(f,[1,1]) #输入初值
print(result)

#求解数值积分
def g(x):
    return (1-x**2)**0.5

pi_2,err = integrate.quad(g,-1,1) #积分结果和误差
print(pi_2*2)
