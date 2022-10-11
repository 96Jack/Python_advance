# -*- encoding: utf-8 -*-
'''
file       :打印菱形.py
Description: 必须是奇数层, 因为菱形是关于中间一行对称的
Date       :2022/09/26 23:32:34
Author     :Xu Zhiwen
version    :python3.7.8
'''



layer = int(input("请输入层数："))

"""
判断奇偶数: 
1. 对2取余
if n%2 == 0:
    print(n为偶数)

2. 对1按位&（乘）运算
if n & 1 == 0:
    print(n为偶数)

解析: 
1 的二进制代码是0000 0001
偶数的二进制代码的末尾最后一位为0,所以按位与运算时, 结果为0的为偶数
"""
while layer & 1 == 0:
    layer = int(input("层数必须是奇数层！"))

for i in range(1, layer//2 + 2):
    # 打印两个空格一个*
    # 打印一个空格三个*
    # print(" "* (layer - i - 2), end="")

    # 多留两个空格：打印一层和三层的时候有空格
    print(" "* (layer - i), end="")
    print("*"* (2*i - 1))

for i in range(layer//2, 0, -1):
    # -1 表示倒叙
    print(" "* (layer - i), end="")
    print("*"* (2*i - 1))


