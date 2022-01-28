# _*_ coding = utf-8 _*_
# @Date : 2021/11/29
# @Time : 22:00
# @NAME ：molin


'''
    操作系统进程和线程在python中实现
    进程：一个任务就是一个进程，
    线程：一个任务里同时运行多个子任务，如word里打字，拼写检查，打印等子任务

    多进程如何实现：
    启动多个进程，每个进程只有一个线程
    启动一个进程，在一个进程内启动多个线程，每个线程执行一个任务
    启动多个进程，一个进程启动多个线程（很少用这种）
    多进程模式：
    多线程模式：
    多进程+多线程模式

    multiprocessing模块实现跨平台版本的多进程模块展示
    启动一个子进程并等待其结束：
    from multiprocessing import Process
    import os

    #子进程执行的代码
    def run_proc(name):
        print('')
    if __name__ == '__main__':
        print('')
        p  = Process(target=run_proc, args=('test',)
        p.start()
        p.join()
        print('')

    # 多个进程启动，采用进程池的方式批量创建子进程
    from multiprocessing import Pool
    import os, time, random
    def long_time_task(name):
        print()
        start = time.time()
        time.sleep(random.random()*3)
        end = time.time()
        print()

    if __name__ == '__main__':
        print()
        p = Pool(4)
        for i in range(5):
            p.apply_async(long_time_task, args=(i,)
        print()
        p.close()
        p.join()  会等所有子进程执行完毕，调用之前必须调用close，不能之后不能添加新的process
        print()
'''
