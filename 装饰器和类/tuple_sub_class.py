# -*- encoding: utf-8 -*-
'''
file       :tuple_sub_class.py
Description:
Date       :2022/02/28 16:44:36
Author     :Xu Zhiwen
version    :python3.7.8
'''



class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __sub__(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return (dx, dy)
p0 = P(1, 1)
p1 = P(2, 3)

# 调用减法__sub___,两个实例对象传入，此时self = P1, p = p0
r = p1 - p0
print(r)
# (1, 2)