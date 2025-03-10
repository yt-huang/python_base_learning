from multiprocessing import Process
import os
import time

a = 100
class MyProcess(Process):
    def __init__(self,name):
        super().__init__() #加载父类的资源
        self.name = name

    def run(self):
        print('%s子进程开始执行'%self.name)
        time.sleep(2)
        a=200
        print('%s子进程执行完毕'%self.name)
        print(a)

if __name__ == '__main__':
    start_time = time.time()
    process_list = []
    for i in range(10):
        p = MyProcess(name='子进程%s'%i)
        p.start()
        # p.join() #为什么不写在这里  等待时间太长了
        process_list.append(p)

    for p in process_list:
        p.join() # 当前的父进程 等待所有子进程结束
    print('主进程执行完毕')
    end_time = time.time()
    print('总耗时：%s'%(end_time-start_time))
    print(a)
