
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
    
    # 将方法变成实例属性
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

# 应用场景：等级排序

b3 = Box(1, 3, 4)
b4 = Box(1, 2, 5)

# sorted(iterabled) : 可以排序任何的可迭代的对象,不会改变原对象内元素的顺序
# list.sort() ： 只为list定义，修改原始的list内的顺序。 
for b in sorted([b1, b2, b3, b4]):
    # vars(): 将对象转化成字典对象
    print(vars(b))


