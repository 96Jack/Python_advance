# -*- encoding: utf-8 -*-
'''
file       :class_thread.py
Description:
Date       :2022/03/04 19:57:02
Author     :Xu Zhiwen
version    :python3.7.8
'''
import threading
import random 

class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None
    
    def run(self):
        self.result = 0
        for i in range(self.n):
            self.result += random.randint(1, 100)

t = MyThread(100)
t.start()
# 通过类的属性，保存线程的返回值：原本的线程会丢弃return的结果
print(t.result)

