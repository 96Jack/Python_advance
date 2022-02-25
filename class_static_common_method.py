# -*- encoding: utf-8 -*-
'''
file       :class_static_method.py
Description:
Date       :2022/02/24 22:06:25
Author     :Xu Zhiwen
version    :python3.7.8
'''

# class Test(object):
class Test():
    x = 123

    def __init__(self) -> None:
        self.y = 456

    def bar1(self):
        print("common method")
        return self

    @classmethod
    def bar2(cls):
        print("class method")
        return cls

    @staticmethod
    def bar3():
        print("static method")


    def foo1(self):
        print(self.x)
        print(self.y)
        self.bar1()
        self.bar2()
        self.bar3()

    @classmethod
    # cls = Test 此时的类
    def foo2(cls):
        print(cls.x)
        # y为类中函数__init__()的属性，不可调用
        # print(cls.y)

        # cls = Test 不可通过类调用具体的实例的方法
        # cls.bar1()
        cls.bar2()
        cls.bar3()
    
    @staticmethod
    # 静态方法不需要传入任何东西 
    # t.foo3(t) ：相当于普通方法 : t = self (实例对象)
    # t.foo3(Test): 相当于类方法： 传入一个类

    def foo3(obj):
        print(obj.x)
        print(obj.y)
        obj.bar1()
        obj.bar2()
        obj.bar3()




""" 
t = Test()
# self = t 实例本身 Test()
print(t.bar1() is t )

# 类方法传入一个类
# 类本身也是一个对象
print(t.bar2() is Test )
 """

t = Test()
# self = t 实例本身体
# 普通方法可以通过实例调用，引用类内部的任何属性和方法
# t.foo1()

# @classmethod : 无需实例化,可以调用类的方法，不可调用类中函数包含的方法
t.foo2()
# 默认传入self,不可通过类调用具体的实例的方法,但是外部可以给通过给类传入一个实例调用
# Test.bar1(t)
# 应用场景： 直接使用类的名字创建一个实例的时候使用 ：User.create()


# @staticmethod ：静态方法，无传入参数时，无论是用类还是用实例都无法调用类内部的方法和属性，完全独立的方法
# t.foo3()
t.foo3(t)




