# -*- encoding: utf-8 -*-
'''
file       :singleton_mode.py
Description: 单例模式产生的对象都是同一个东西,一个改变另一个也会跟着改变
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
"True"