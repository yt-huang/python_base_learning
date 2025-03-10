import time
from multiprocessing import Process,Queue
import os
# 创建一个进程，用于向队列中写入数据
class WriterProcess(Process):
    def __init__(self,xname,queue):
        super().__init__()
        self.xname = xname
        self.queue = queue
    def run(self):
        # 把多条数据写入的队列中
        print("子进程id:%s ,子进程名字：%s",os.getpid(),self.name)
        for i in range(10):
            self.queue.put(i)
            print("写入数据：",i)
            time.sleep(1)
        print("子进程结束:%s,子进程名字:%s",os.getpid(),self.name)

class ReaderProcess(Process):
    def __init__(self,xname,queue):
        super().__init__()
        self.xname = xname
        self.queue = queue
    def run(self):
        print("子进程id:%s ,子进程名字：%s",os.getpid(),self.name)
        while True:
            print("读取数据：",self.queue.get(True))
            time.sleep(1)
        print("子进程结束:%s,子进程名字:%s",os.getpid(),self.name)
if __name__ == '__main__':
    q = Queue()
    writer = WriterProcess(xname='writer',queue=q)
    reader = ReaderProcess(xname='reader',queue=q)
    writer.start()
    reader.start()
    writer.join()
    writer.terminate()

