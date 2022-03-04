# -*- encoding: utf-8 -*-
'''
file       :python_timeit.py
Description:
Date       :2022/03/04 13:31:46
Author     :Xu Zhiwen
version    :python3.7.8
'''


import profile, random

def foo(n):
    x = 0
    for i in range(n):
        x += random.randint(1, 100)
    return x 

# 参数必须是字符串；打印内部所有过程的消耗时间
profile.run('foo(1000)')

