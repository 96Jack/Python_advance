# -*- encoding: utf-8 -*-
'''
file       :class_retry_deco.py
Description:
Date       :2022/02/24 17:00:01
Author     :Xu Zhiwen
version    :python3.7.8
'''


import time 
import random

class Retry:
    # exception 接收的是元组
    def __init__(self, max_retries=3, wait=0, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.wait = wait
        self.exceptions = exceptions

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                except self.exceptions:
                    time.sleep(self.wait)
                    print("retry :",i)
                    continue 
                else:
                    return result
        return wrapper
    

@Retry(3, 1, (ValueError,))
def foo(m, n):
    res = random.randint(m, n)
    if res < 0:
        raise ValueError()
    else:
        return res


print(foo(-5, 0))

