# -*- encoding: utf-8 -*-
'''
file       :setattr_getattribute_getattr_application.py
Description:  属性监听, 用户购买商品的时候,先检查用户的余额是否够,不够则抛错(所有设计买卖的商品都涉及)
Date       :2022/03/02 15:30:46
Author     :Xu Zhiwen
version    :python3.7.8
'''



class User:
    """TestClass"""
    def __init__(self) -> None:
        self.money = 10000
    
    # 所有类及实例属性的赋值操作调用;  属性监听；余额不足时抛错；当其他地方调用money的时候，余额不足的情况下回自动抛错
    
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
u.money -=10001
