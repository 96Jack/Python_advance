# -*- encoding: utf-8 -*-
'''
file       :singleton_mode.py
Description:
Date       :2022/02/26 21:29:37
Author     :Xu Zhiwen
version    :python3.7.8
'''


class P:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

a = P()
b = P()
c = P()
print(a is b is c is P._instance)