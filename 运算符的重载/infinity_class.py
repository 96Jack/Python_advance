# -*- encoding: utf-8 -*-
'''
file       :infinity_class.py
Description:  运算符重载实现无穷大
Date       :2022/02/28 19:48:37
Author     :Xu Zhiwen
version    :python3.7.8
'''



class Inf:
    def __lt__(self, other):
        return False
    
    def __le__(self, other):
        return False

    def __ge__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return False
 # not equal : !=
    def __ne__(self, other):
        return True

o = Inf()
print(o >= 12344 ** 378)
