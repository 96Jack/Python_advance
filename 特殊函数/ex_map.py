from email import header


# -*- encoding: utf-8 -*-
'''
file       :ex_map.py
Description: 
map(func, *iterables)
生成一个迭代器

Date       :2022/08/20 15:25:33
Author     :Xu Zhiwen
version    :python3.7.8
'''



print(type(map))
print(dir(map(lambda x:x**2, [1, 2, 3, 4])))
a = map(lambda x:x**2, [1, 2, 3, 4])
b = [i for i in a.__next__]
print(b)

