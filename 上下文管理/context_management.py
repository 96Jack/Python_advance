# -*- encoding: utf-8 -*-
'''
file       :context_management.py
Description:
Date       :2022/03/01 21:30:23
Author     :Xu Zhiwen
version    :python3.7.8
'''

# open
# ---------------------------------------------------------------------------------------
# open 一个文件需要手动使用lose方法退出锁定状态
# f = open(r"c:\Xuzhiwen\Py\temp.py",encoding="utf-8")
# print(f.readline())
# print("before close: ======")
# print(f.closed)
# f.close()
# print("after close:  ======")
# print(f.closed)


# with
# -----------------------------------------------------------------------------------------
# with : 内部有__enter__及__exit__方法，不用手动关闭
# with open(r"c:\Xuzhiwen\Py\temp.py",encoding="utf-8") as p :
#     print(p.read())

# --------------------------------------------------------------------------------------
# from threading import Lock

# lc = Lock()
# with lc:
#     # 查看with内部锁的状态
#     print(lc.locked())
#     # True 

# print(lc.locked())
# False
# ---------------------------------------------------------------------------------------



exceptions = []


class A:
    # 进入with语句的一些初始化的操作
    def __enter__(self, *args):
        print("enter:.....")
        return self

    # 退出时一些善后的工作，若是网络连接，此时设置退出断开
    # 即使发生了异常，这里仍然能退出，防止死锁
    def __exit__(self, *args):
        print("exit:......")

        exceptions.extend(args)

with A() as a:
    print("===========")        
    print(a)
    print("===========")
    print(a.locked())
    raise ValueError("hahaha")

# print(A.locked())
# ipython 
# print(exceptions)
# a, b, c = exceptions
# [ValueError, ValueError('hahaha'), <traceback at 0x12ed6b217c8>]
# b 是 a 的实例
# isinstance(b, a)  ->  True
# <traceback at 0x12ed6b217c8> : traceback:异常信息的封装

# from traceback import print_exception : python异常打印的模块

# print_exception(a, b, c)
# >>
# Traceback (most recent call last):
#   File "<ipython-input-1-856e57cec2c5>", line 17, in <module>
#     raise ValueError("hahaha")
# ValueError: hahaha