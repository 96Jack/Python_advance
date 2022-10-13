# -*- encoding: utf-8 -*-
'''
file       :fibonacci.py
Description:  递归实现斐波那契数列
Date       :2022/10/13 10:07:57
Author     :Xu Zhiwen
version    :python3.7.8
'''



n = int(input("请输入数据: "))
def fb(n):
    if n <=2:
        return 1
    else:
        return(fb(n-2) + fb(n-1))
print(fb(n), end="")



