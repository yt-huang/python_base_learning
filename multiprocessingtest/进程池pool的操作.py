import os,time
import random
from multiprocessing import Pool


def run(name):
    start_time = time.time()
    print("子进程%s开始运行" % name)
    time.sleep(random.randint(4, 8))
    print("子进程%s运行结束" % name)
    end_time = time.time()
    print("子进程%s id:%s运行耗时：%0.2f" % (name, os.getpid(),end_time - start_time))
if __name__ == '__main__':
    p = Pool(5) #cpu的核心数
    for i in range(10):
        # 请求得到一个进程，然后异步调用run函数 （非阻塞似）
        p.apply_async(run,args=(i,))
        
    p.close()
    p.join()
    print('主进程执行完毕')
