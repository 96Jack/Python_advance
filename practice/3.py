# -*- encoding: utf-8 -*-
'''
file       :3.py
Description: insert_sort
Date       :2022/05/10 23:25:56
Author     :Xu Zhiwen
version    :python3.7.8
'''
lst = [6, 5, 4, 3, 2, 1]
for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]

print(lst)
        


