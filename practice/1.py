# -*- encoding: utf-8 -*-
'''
file       :1.py
Description: maopao 
Date       :2022/05/10 22:48:26
Author     :Xu Zhiwen
version    :python3.7.8
'''

lst = [6, 5, 4, 3, 2, 1]
 
for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
