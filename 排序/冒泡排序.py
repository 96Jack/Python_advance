# -*- encoding: utf-8 -*-
'''
file       :冒泡排序.py
Description: 比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个
Date       :2022/05/09 15:24:13
Author     :Xu Zhiwen
version    :python3.7.8
'''
import random


l = [random.randint(0, 100) for _ in range(6)]

for i in range(len(l) -1):
    flag = 0
    for j in range(len(l) - 1 - i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            flag = 1
    if flag == 0:
        break

print(l)
