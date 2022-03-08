# -*- encoding: utf-8 -*-
'''
file       :muti_ps.py
Description:
Date       :2022/03/08 22:10:39
Author     :Xu Zhiwen
version    :python3.7.8
'''


import threading

lk = threading.Lock()

def add():
    global N
    for i in range(50000):
        N += 1
N = 0
tasks = [threading.Thread(target=add) for i in range(10)]
for t in tasks:
    t.start()
for t in tasks:
    # 等待线程结束
    t.join()

print(N)
# 493983
# 结果应该为500000
# 多线程安全问题： 多个线程同时操作一个全局变量
#              ： 当前一个线程对全局变量的值未计算完成时，下一个线程就开始用为计算完成的全局变量进行计算，相当于重复操作。