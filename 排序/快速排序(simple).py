# -*- encoding: utf-8 -*-
'''
file       :快速排序.py
Description:  从数列中挑出一个元素，称为"基准",重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
Date       :2022/05/09 15:26:20
Author     :Xu Zhiwen
version    :python3.7.8
'''
import random

def quick_sort(l):
    if len(l) < 2:
        return l
    
    mid = l.pop(len(l)//2)
    left = []
    right = []
    for n in l:
        if n < mid:
            left.append(n)
        else:
            right.append(n)
    return quick_sort(left) + [mid] + quick_sort(right)


l = [random.randint(0, 100) for _ in range(6)]
print(quick_sort(l))
