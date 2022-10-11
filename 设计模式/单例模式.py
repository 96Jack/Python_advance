# -*- encoding: utf-8 -*-
'''
file       :单例模式.py
Description:  一个类只能创建一个实例
Date       :2022/10/10 19:47:24
Author     :Xu Zhiwen
version    :python3.7.8
'''


from re import S


class Singleton():
    __instance = None
    __is_first = False

    def __new__(cls,age, name):
        if  not cls.__instance:
            # 当第一次创建对象时，__instance 是None 会创建一个新的对象，
            # 此时__instance就为新的对象，第二次创建对象时，__instance 已经有值，则会直接返回这个对象
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name) -> None:
        if not self.__is_first:
            self.age = age
            self.name = name
            Singleton.__is_first = True
            
a = Singleton(18, 'zs')
b = Singleton(20, 'ls')
print(id(a))
print(id(b))
print(a.age)
print(b.age)
