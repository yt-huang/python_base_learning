import time
from multiprocessing import Process, Queue, Pipe
import os
# 创建一个进程，用于向队列中写入数据
class WriterProcess(Process):
    def __init__(self,xname,pipe):
        super().__init__()
        self.xname = xname
        self.pipe = pipe
    def run(self):
        # 把多条数据写入的队列中
        print("子进程id:%s ,子进程名字：%s",os.getpid(),self.name)
        for i in range(10):
            self.pipe.send(i)
            print("写入数据：",i)
            time.sleep(1)
        print("子进程结束:%s,子进程名字:%s",os.getpid(),self.name)

class ReaderProcess(Process):
    def __init__(self,xname,pipe):
        super().__init__()
        self.xname = xname
        self.pipe = pipe
    def run(self):
        print("子进程id:%s ,子进程名字：%s",os.getpid(),self.name)
        while True:
            print("读取数据：",self.pipe.recv())
            time.sleep(1)
        print("子进程结束:%s,子进程名字:%s",os.getpid(),self.name)
if __name__ == '__main__':
    q1,q2= Pipe()
    writer = WriterProcess(xname='writer',pipe=q1)
    reader = ReaderProcess(xname='reader',pipe=q2)
    writer.start()
    reader.start()
    writer.join()
    writer.terminate()

