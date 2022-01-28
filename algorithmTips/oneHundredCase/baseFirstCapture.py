# _*_ coding = utf-8 _*_
# @Date : 2021/4/26
# @Time : 12:36
# @NAME ：molin
'''
    python 100算法例入门篇
'''

# 1.1 抓交通肇事犯，算出出车号，前两位相同后两位相同，相互间又不相同的4位整数
# 思路:穷举法，设计双层循环
def carNumberCase():
    # 设置标识变量tag，一旦找到值就退出循环，减少循环的次数
    # i 代表前两位的数字，j代表后两位的数字，k代表车牌
    tag = 0
    for i in range(10):
        if tag:
            break;
        for j in range(10):
            if tag:
                break
            if i != j:
                k = 1000 * i + 100 * i + 10 * j + j

                # 判断车牌k是否是某个整数的平方
                for temp in range(31,100):
                    if temp * temp == k:
                        print("车牌的号码是：{}".format(k))
                        tag = 1
                        break

# 1.2 兔子产子（fibonacci数列）：从第三个数起，等于前两个数字之和
# 思路：构造迭代函数，调用自身
def rabbitNumberCase():
    fib1 = 1
    fib2 = 1
    i = 1
    while i <= 15: #每次求两个，相邻两个月的兔子对数
        print("%8d    %8d" %(fib1,fib2),end="       ")
        if i % 2 == 0:
            print()
        fib1 = fib1 + fib2 #最新一个月的兔子对数
        fib2 = fib1 + fib2 #第四个月的兔子对数
        i += 1

# 1.3 牛顿迭代法求方程根
# 思路：先找到一个x0,然后不断迭代x-x0的绝对值，控制在给定范围内
# 方程为 ax3 + bx2 +cx + d = 0,系数a,b,c，d由主函数输入
def niudunIterFunctionCase(a,b,c,d):
    x = 1.5
    x0 = x
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 * x0 + 2 * b * x0 + c  #对f求导
    h = f / fd
    x = x0 - h #求接近方程根的x值
    while abs(x - x0) >= 1e-5:
        x0 = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c  # 对f求导
        h = f / fd
        x = x0 - h
    print("所求方程的根为：{:.4f}".format(x))

# 1.4 百钱买百鸡
# 思路：不定方程组问题，设置变量，组成方程式
def hundredMoneyBuyHundredChickenCase():
    # cock公鸡，hen母鸡，chicken小鸡,公鸡5钱，母鸡3钱，3只小鸡1钱,只要100只
    cock = 0
    while cock  <= 20:
        hen = 0
        while hen <= 33:
            # 小鸡的数量确定
            chicken = 100 - cock -hen
            if(5 * cock + 3 * hen + chicken / 3.0 == 100) and (cock + hen + chicken == 100):
                print("cock = %2d,hen = %2d, chicken = %2d\n" %(cock,hen,chicken))
            hen += 1
        cock += 1

# 1.5 借书方案，5本书借给3个人，每个人只能借一本，多少种方案
# 思路：排列组合问题A(5)(3)，在第三个人选书时，前判断前两个人借的是否是同一本书，若是则无效，提高效率
def borrowBookNumberCase():
    # A,B,C代表3人，a,b,c代表书编号，i代表有效借阅次数
    i = 0
    a = 1
    while a <= 5:
        b = 1
        while b <= 5:
            c = 1
            while c <= 5 and a != b:  #判断前两个是否借阅同一本
                if a != c and b != c:  #控制有效借阅组合
                    print("A:%2d B:%2d c:%2d   " %(a,b,c),end='')
                    i += 1
                    if i % 4 == 0:
                        print() #换行
                c += 1
            b += 1
        a += 1
    print("共有%d种有效借阅方法" % i)

# 1.6 打鱼还是晒网，判断1990年1.1起一年内以后某天是打鱼还是晒网
# 思路：数值计算算法，判断1990年闰年和每个月的天数，天数除以5求余数，余数1,2,3是打鱼
def daYuOrShaiWangNumberCase():
    # 每月天数数组
    perMonth = [0,31,28,31,30,31,30,31,31,30,31,30]
    totalDay = 0
    year = 1990
    currentDay = {'year':1992,'month':1,'day':9}
    while year < currentDay['year']: #求出指定日期之前的每一年的天数之和
        if runYear(year) == 1:
            totalDay = totalDay +366
        else:
            totalDay = totalDay +365
        year += 1
    if runYear(currentDay['year']) == 1:
        perMonth[2] += 1
    i = 0
    while i < currentDay['month']:
        totalDay += perMonth[i]
        i += 1
    totalDay += currentDay['day']
    print("当前天数是：%2d" %totalDay)
    result = totalDay % 5
    if result > 0 and result < 4:
        print("今天打鱼！")
    else:
        print("今天晒网")


# 1.6.1 判断是否为闰年，是返回1，否返回0
def runYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0

# 1.7 最佳存款方案 复利的计算方法，一年整存领取月息0.63%，打算今后5年每年年底取1000，到第五年刚好取完，存多少合适
# 思路：从第五年开始算，往前推,循环计算四次
def bestDepositMoneyCase():
    i = 0
    money = 0.0
    while i < 5:
        money = (money + 1000)/(1 + 0.0063 * 12)
        i += 1
    print("应该存入{:.2f}元".format(money))

# 1.8 冒泡排序 排序算法中重要的一种
# 思路：将无序表变成有序表，最坏的的比较次数是n(n-1)/2,两层循环控制，第一层控制交换的轮数，第二层控制每轮交换的次数
def bubbuleSortCase():
    a_list = [2,8,3,4,1,9,5]
    n = len(a_list)
    i = 1
    while i <= n-1: #控制交换的轮数
        j = 0
        while j < n-1: #控制比较的次数
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
            j += 1
        i += 1
    # for ai in a_list:
        # print("冒泡排序后的顺序为：{}".format(ai))
        # print("结果是：",ai,end='')
    print("冒泡排序的列表为：",a_list)
# 1.8.1 选择排序
# 思路：每一轮都是拿轮数第一个跟后面的比较，最小的放前面，复杂度：n(n-1)/2
def selectionSortCase():
    a_list = [2,8,3,4,1,9,5]
    n = len(a_list)
    for i in range(0,n-1):
        for j in range(i+1,n):
            # 交换
            if a_list[j] < a_list[i]:
                temp = a_list[i]
                a_list[i] = a_list[j]
                a_list[j] = temp

    print("选择排序后的数组是：",a_list)

# 1.9 折半查找 又叫二分查找（分治算法一种）只适用有序序列，需要先排序
# 思路，定义中间变量 存储low + high的平均值，然后比较平均值和整数大小
def zhebanSearchCase():
    li = [2,8,3,4,1,9,5]
    low = 0
    high = len(li) - 1 #数组下界
    k = -1 #记录下标
    for i in sorted(li):
        print(i, end=',') #打印原数组的序列
    print()
    m = int(input('请输入整数：')) #需要查找的整数
    while low <= high:
        mid = (low + high) // 2
        if m < li[mid]:
            high = mid - 1
        else:
            if m > li[mid]:
                low = mid + 1
            else:
                k = mid
                break  #一旦找到对应的整数就跳出循环
    if k >= 0:
        print("整数%d,index = %d" % (m, k))
    else:
        print("数组中没有该整数")

# 1.10 任意进制转换
# 思路：二进制、八进制、十六进制转十进制按权展开相加，十进制转其他，除以基数取余，二、八、十六相互转换是通过
# 先转成十进制，在转相应进制



if __name__ == '__main__':
    # carNumberCase()  #1.1 车牌查询
    # rabbitNumberCase() #1.2 兔子产子，fibonacci数列
    # 1.3 牛顿法求方程组的根
    # print("\n请输入方程的系数,以逗号隔开")
    # a,b,c,d = map(float,input().split(','))
    # niudunIterFunctionCase(a,b,c,d)
    # hundredMoneyBuyHundredChickenCase() #1.4 百钱买百鸡
    # borrowBookNumberCase()  #1.5 借书方案
    # daYuOrShaiWangNumberCase() #1.6 打鱼还是晒网
    # bestDepositMoneyCase() #1.7 最佳存款方案
    # bubbuleSortCase()  #1.8 冒泡排序
    # selectionSortCase() #1.8.1 选择排序
    zhebanSearchCase() #1.9 折半查找