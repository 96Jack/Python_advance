# -*- encoding: utf-8 -*-
'''
file       :mutil_ps.py
# Description: 多线程，线程锁，线程安全
Date       :2022/03/08 21:51:15
Author     :Xu Zhiwen
version    :python3.7.8
'''

import threading

lk = threading.Lock()

def add():
    global N
    for i in range(500000):
        # 获取线程锁
        lk.acquire()
        N += 1
        # 释放线程锁
        lk.release()

N = 0
tasks = [threading.Thread(target=add) for i in range(10)]
for t in tasks:
    t.start()

for t in tasks:
    t.join()

print(N)
