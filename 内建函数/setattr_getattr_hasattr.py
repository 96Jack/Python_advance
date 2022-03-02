# -*- encoding: utf-8 -*-
'''
file       :setattr_getattr_hasattr.py
Description:  attribute: 属性  内建函数: setattr, getattr, hasattr
Date       :2022/03/02 10:50:17
Author     :Xu Zhiwen
version    :python3.7.8
'''




class A:
    pass

a = A()

setattr(a, "a", 111)
# print(getattr(a, "z"))
# print(getattr(a, 'b', 222))
# print(vars(a))
# print(hasattr(a, "b"))

# __dict__保存对象属性的地方
# print(a.__dict__)


# --------------------------------------------------------------
class B:
    z = 333
    def __init__(self, x=111, y=222):
        self.x = x
        self.y = y

    def foo(self):
        return self.x ** self.y

# 调用父类开辟一个内存空间
a = object.__new__(B)
print(a.__dict__)
# >
# {}

# 初始化实例属性
a.__init__()
print(a.__dict__)
# {'x': 111, 'y': 222}

# 类属性及方法的保存位置
print(B.__dict__)

















