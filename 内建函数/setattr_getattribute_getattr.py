# -*- encoding: utf-8 -*-
'''
file       :setattr_getattribute_getattr.py
Description: 常用来做属性监听
Date       :2022/03/02 14:52:34
Author     :Xu Zhiwen
version    :python3.7.8
'''


class User:
    """TestClass"""
    z = {7, 8, 9}
    def __init__(self) -> None:
        self.money = 10000
        self.y = 'abc'
    
    # 所有类及实例属性的赋值操作调用
    def __setattr__(self, name, value) -> None:
        if name == 'money' and value < 0:
            raise ValueError('money < 0')
        print('set %s to %s' % (name, value))
        object.__setattr__(self, name, value)
    # 获取类及实例存在的属性操作
    def __getattribute__(self, name):
        print('get %s'% name)
        return object.__getattribute__(self, name)
    # 获取实例不存在的属性的操作
    def __getattr__(self, name):
        print('not has %s'%name)
        # return -1
        return object.__setattr__(self, name, 999)

    def foo(self, x, y, ):
        return x ** y


u = User()
# 触发__setattr__
# set money to 10000
# set y to abc

# u.money += 999
# 实例或类原本存在的属性，先触发__getattribute__,再触发__setattr__
# get money
# set money to 10999

print(u.x)
print(u.x)
# not has x
# None
# get x
# 999

# 当取原来实例中不存在的属性的时候调用__getattr__
# print(User.q)  : 取类中不存在的不行，会报错

User.z = 222
print(User.__dict__)
print(User.z)