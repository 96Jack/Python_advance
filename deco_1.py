
# -*- encoding: utf-8 -*-
'''
file       :test.py
Description: func decorator
Date       :2022/02/23 22:36:40
Author     :Xu Zhiwen
version    :python3.7.8
'''


def deco1(func):
    print("enter deco1 (%s)" % func.__name__)
    def wrap_1(*args, **kwargs):
        print("enter wrapers_1 (%s, %s)" % args)
        result = func(*args, **kwargs)
        print("exit wrapper_1 result * 2:{}".format(result * 2))
        return result * 2
    return wrap_1

def deco2(func):
    print("enter deco2 (%s)" % func.__name__)
    def wrap_2(*args, **kwargs):
        print("enter wrapers_2 (%s, %s)" % args)
        result = func(*args, **kwargs)
        print("exit wrapper_2 result + 1:{} ".format(result + 1))
        return result + 1 
    return wrap_2

def deco3(func):
    print("enter deco3 (%s)" % func.__name__)
    def wrap_3(*args, **kwargs):
        print("enter wrapers_3 (%s, %s)" % args)
        result = func(*args, **kwargs)
        print("exit wrapper_3 result + 3:{}".format(result + 3))
        return result + 3
    return wrap_3


@deco1
@deco2
@deco3
# foo函数功能依次由下往上添加:  wrapper函数正着进去，倒着出来。 
def foo(x, y):
     return x**y
print(foo(2, 3))

# print(foo.__name__)

""" [Running] python -u "c:\Xuzhiwen\Py\test.py"
enter deco3 (foo)
enter deco2 (wrap_3)
enter deco1 (wrap_2)
enter wrapers_1 (2, 3)
enter wrapers_2 (2, 3)
enter wrapers_3 (2, 3)
exit wrapper_3 result + 3:11
exit wrapper_2 result + 1:12 
exit wrapper_1 result * 2:24
24 """

