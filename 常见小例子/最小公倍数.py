# -*- encoding: utf-8 -*-
'''
file       :最小公倍数.py
Description:  两个自然数的乘积等于这两个自然数的最大公约数和最小公倍数的乘积
Date       :2022/09/27 17:51:06
Author     :Xu Zhiwen
version    :python3.7.8
'''
def bei(num1,num2):
    b = []
    for i in range(1,(num1 * num2)+1):
        if i % num1 == 0 and i % num2 == 0:
            b.append(i)
            break
    return b[0]
num1=int(input("请输入第一个数字: "))
num2=int(input("请输入第二个数字: "))
print(bei(num1, num2))
