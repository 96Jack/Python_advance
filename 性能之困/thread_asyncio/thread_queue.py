# -*- encoding: utf-8 -*-
'''
file       :thread_queue.py
Description: 10个线程写入文件会要一个一个写,当前写的文件会被锁住;用队列,直接写入队列,然后从队里中取出数据,写入文件。
Date       :2022/03/04 20:05:30
Author     :Xu Zhiwen
version    :python3.7.8
'''


from queue import Queue
import random
import threading

# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# q.put(6)
# print("get : +++++++++++")
# # 先进入先出，取不到会一直等待
# print(q.get())
# print(q.get())
# # 设置等待时间3秒，取不到会抛出empty异常，来控制流程
# q.get(timeout=3)
# # 取不到值时，立即返回empty错，不等待
# q.get(block=False)


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.q = Queue()
        self.result = None

    def run(self):
        self.result = 0
        print("give me a number\n")
        # 取不到值会等待
        n = self.q.get(timeout=10)
        print("n = %s" % n)
        for i in range(n):
            self.result += random.randint(1, 100)

t = MyThread()
t.start()
t.q.put(1000)
print("result={}".format(t.result))





