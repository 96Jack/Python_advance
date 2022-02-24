# -*- encoding: utf-8 -*-
'''
file       :deco_3.py
Description: 类实现装饰器
Date       :2022/02/24 15:34:03
Author     :Xu Zhiwen
version    :python3.7.8
'''
from msilib.schema import CheckBox
import random 

class Deco:
    # 接收类参数(传入的函数func)
    def __init__(self, func):
        # 接收func
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("exec.__call__")
        result = self.func(*args, **kwargs)
        if result >= 0:
            return result
        else:
            return 0
""" 
class Check:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __call__(self, *args, **kwargs):
        return self.x ** self.y

 """

""" 
a = Check(1, 2)
a 是一个实例对象: 类中有__call__方法后,可以让实例变得可调用
print(a)
print(a(1,2))
print(callable(a))

>>
[Running] python -u "c:\Xuzhiwen\Py\Python_advance\deco_3.py"
<__main__.Check object at 0x000001D7A37F5A48>
1
True """
        

# instance = Deco(foo)
@Deco
def foo(m, n):
    return random.randint(m, n)

# print(foo(-10, 10))


