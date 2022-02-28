# -*- encoding: utf-8 -*-
'''
file       :func_container.py
Description: 容器类对象: 可以往自身添加其他元素
Date       :2022/02/28 21:04:16
Author     :Xu Zhiwen
version    :python3.7.8
'''


# 容器类对象: 可以往自身添加其他元素


# 1. len(), for 遍历：                 str  bytes  list  tuple  dict  set
# 2. __getitem__() 根据索引取值    :    str  byte   list  tuple  dict  (set不可用：无序)
# 3. __setitem__() 根据索引设置值  :    list  dict : 有则改值，无则添加值 (str, tuple不可用，不可变对象)

# 4. __contains__()判断是否包含值 ->in: str  bytes  list  tuple  dict(只判断key)  set  ： 返回bool值

