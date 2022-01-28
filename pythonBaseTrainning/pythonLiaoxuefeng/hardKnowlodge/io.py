# _*_ coding = utf-8 _*_
# @Date : 2021/11/29
# @Time : 20:35
# @NAME ：molin

'''
    在任何开发语言中，io编程都比较重要，python也不例外，本章主要介绍io相关，涉及到数据交换的地方，通常
    都需要IO接口
    往外发数据（请求） 叫output
    从外接收数据（接收） 叫input
    Steam（流） 是io编程重要的概念，可以想象成一个水管，input就是数据从外面流入内存，output就是从内存中
    流到外面

    cpu和内存的速度远高于外设的速度
    这种接收和发送数据不匹配的解决方法：
    cpu等着，程序暂停执行后续代码，等数据存入磁盘后在接着执行， 这种模式叫同步IO（进程线程）
    cpu不等待，磁盘慢慢写，后续代码继续执行，这种模式叫异步IO（协程等）
    区别就是是否等待IO执行的结果，异步IO性能高于同步IO，但是模型复杂，得知道通知IO完成的方法，回调还是轮询


    # 文件读写： 文件读写都是由操作系统提供
    读文件：
     open()函数  >> f = open('/user/michael/test.txt', 'r')
     read()函数  >> f.read()
     close()函数 >> f.close()
     文件读写可能产生IOError，一般需要捕获异常
     try:
        f = open('/user/michael/test.txt', 'r')
        print(f.read())
    except IOError as e:
        print(e)
    finally:
        if f:
            f.close()
    后面提供了更好的方法，上面方法太繁琐
    with open('/user/michael/test.txt', 'r') as f:
        print(f.read())
    存在一个问题，read()可以设置每次读取的最大值，反复调用，防止读取文件太大，内存爆了
    readline: 读取一行内容
    readlines: 读取所有行返回
    for line in f.readlines():
        print(line.strip()) #把末尾的换行符删掉

    读取二进制文件，文件的打开方法是：rb， 编码用encoding='gbk'

    写文件：
    和读文件类似，只是标识符为w，wb这种
    f = open('/user/michael/test.txt', 'w')
    f.write('hello world')
    f.close()

    标识符w: 写入文件，会覆盖之前的，
        wa：写入文件，是以追加的方式写入
        wb：写入二进制文件

    上面的读写文件一般指文件，在内存中读写是使用StringIO和BytesIO
    把str写入StringIO
    from io import StringIO
    f = StringIO() # 需要创建一个StringIO对象
    然后在写入
    f.write('hellowrold')
    print(f.getvalue()) # 打印写入后的str

    读取StringIO
    f = StringIO('helloworld')
    while Ture:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

    BytesIO 操作一样的

    操作文件、目录等，可以使用命令dir, cp等
    之前提到的os模块就是很好的资源
    基本功能：
    >>> import os
    >>> os.name
    'posix'
    如果是nt就是代表windows，posix代表linux，unix或mac os
    >>> os.uname() 全部的系统信息
    >>> os.environ  环境变量
    >>> os.environ.get('PATH')  获取PATH环境变量

    os.path模块常用的系统文件和目录操作的源，部分在os模块
    >>> os.path.abspath('') #当前目录绝对路径
    >>> os.path.join('/user/muchal', 'test') #在test目录下创建目录user/muchal，然后显示出来
    >>> os.mkdir('/user/muchal') #创建目录
    >>> os.rmdir('/user/muchal') #删除目录
    目录合并，使用os.path.join()函数，不要使用拼接字符串
    拆分路径，使用os.path.split()
    os.path.splittext() 直接叨叨文件扩展名txt
    >>> os.rename('', '') 重命名
    >>> os.remove('') 删除文件
    shutil文件提供了复制的功能

    过滤文件
    当前所有目录 >>> [x for x in os.listdir('.') if os.path.isdir(x))  展示所有含有.的目录
    列出所有.py文件 >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] =='py']

    # 序列化
     d= dict(name='bob', age=20, score=33)
     可以随时修改变量，如把name改为bill，bill被存储到磁盘上，重新运行程序，变量又还是bob
     其中变量从内存中编程可存储或传输的过程为序列化（pickling)
     序列化之后写入磁盘，
     反之叫反序列化（unpickling),python提供了pickle模块实现序列化
     写入文件：
     >>> import pickle
     >>> d = dict(name='bob', age=20, score=33)
     >>> pickle.dumps(d)  把对象序列化成bytes，然后就可以对bytes写入文件
     >>> f = open('dumpt.txt','wb')
     >>> pickle.dump(d, f)
     读取文件：
     >>> f = open('dump.txt', 'rb')
     >>> d = pickle.load(f)
     >>> f.close()

     不同编程语言之间传递对象，标准格式：json或者xml
     json文件：
     >>> import json
     >>> d = dict(name='bob', age=20, score=33)
     >>> json.dumps(d)  转成了json字符串
     >>> json.dump() 把json写入一个file-like object
     >>> json.loads() json字符串反序列化

     类也可以序列化为json，但是需要写一个转换函数
     >>> print(json.dumps(s, default=student2dict))
     其中student2dict
     def student2dict(std):
        return{
            'name'
        }


    # 异步IO




'''