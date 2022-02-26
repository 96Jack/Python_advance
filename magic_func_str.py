# -*- encoding: utf-8 -*-
'''
file       :magic_func.py
Description:
Date       :2022/02/26 21:23:03
Author     :Xu Zhiwen
version    :python3.7.8
'''

class P:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self):
        return '<P(%s, %s)>' % (self.x, self.y)

p = P(2.33, 4.67)
print(p)
# [Running] python -u "c:\Xuzhiwen\Py\Python_advance\magic_func_str.py"
# <P(2.33, 4.67)>