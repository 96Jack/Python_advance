
# -*- encoding: utf-8 -*-
'''
file       :volume_comparison.py
Description: 运算符重载
Date       :2022/02/28 17:13:58
Author     :Xu Zhiwen
version    :python3.7.8
'''


class Box:
    def __init__(self, w, h, l):
        self.w = w
        self.h = h
        self.l = l
    
    # 将方法变成属性
    @property
    def V(self):
        return self.w * self.h * self.l

    def __gt__(self, other):
        return self.V > other.V
    
    def __ge__(self, other):
        return self.V >= other.V

    def __lt__(self, other):
        return self.V < other.V

b1 = Box(1, 1, 1)
b2 = Box(1, 2, 3)

print(b2 > b1)


