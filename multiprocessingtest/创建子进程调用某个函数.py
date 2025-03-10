from multiprocessing import Process
import os
import time


def func1(name):
    print("子进程1开始",os.getpid())
    print("子进程1开始",os.getppid())
    print("子进程1开始",name)
    time.sleep(5)

if __name__ == '__main__':
    start = time.time()
    for i in range(10):
      p = Process(target=func1,args=("子进程1",))
      p.start()
    print('父进程的代码块执行完成✅')