# -*- encoding: utf-8 -*-
'''
file       :slots.py
Description: 槽: 固定类所具有的属性, 实例不会分配__dict__, 不能动态添加属性,优化内存分配(固定申请的内存)
Date       :2022/03/02 16:10:00
Author     :Xu Zhiwen
version    :python3.7.8
'''

# 游戏开发，装备宝石镶嵌的开槽
class A:
    __slots__ = ('x', 'y')


a = A()
a.x = 123
print(a.x)
# a.z = 222
# print(a.z)  : 抛错


    



 