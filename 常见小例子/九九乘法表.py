# -*- encoding: utf-8 -*-
'''
file       :九九乘法表.py
Description:
Date       :2022/09/26 21:36:24
Author     :Xu Zhiwen
version    :python3.7.8
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={j*i}', end=" ")
    print()
