# -*- encoding: utf-8 -*-
'''
file       :带参数(三层函数)装饰器.py
Description:
        相当于先执行最外层time_1()函数, 后面两层相当于无参装饰器【， 

Date       :2022/09/02 20:25:35
Author     :Xu Zhiwen
version    :python3.7.8
'''
import time 

def time_1(count):
    def wrapper_1(fun):
        def wrapper_2(*args, **kwargs):
            t1 = time.time()
            result = fun(*args)
            t2 = time.time()        
            print("Cycle:{} \n total_time:{:.6}".format(count, (t2-t1)))
            print("*"*30)
            return result
        return wrapper_2
    return wrapper_1

@time_1(100)
def foo(x, y):
    return x*y

print(foo(2, 3))        