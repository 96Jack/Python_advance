# -*- encoding: utf-8 -*-
'''
file       :class_static_method.py
Description:  类有类的属性.实例有实例的属性
Date       :2022/02/24 22:06:25
Author     :Xu Zhiwen
version    :python3.7.8
'''

# class Test(object):
class Test():
    x = 123

    def __init__(self) -> None:
        self.y = 456
    # 实例方法
    def bar1(self):
        print("common method")
        return self
    # 类方法
    @classmethod
    def bar2(cls):
        print("class method")
        return cls
    # 静态方法
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
        print(cls.x)                         #:  1. 可以调用类属性
        # y为类中函数__init__()的属性(实例属性)，   2. 不可以调用实例属性
        # print(cls.y)

        # cls = Test 不可通过类调用具体的实例的方法  3. 不可调用类的方法（实例方法）
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

类的方法 = 实例方法
 """

t = Test()
# self = t 实例本身体
# 普通方法可以通过实例调用，引用类内部的任何属性和方法
# t.bar2()
# t.bar3()

# t.foo1()
# t.foo2()

# @classmethod : 无需实例化
# Test.bar2()  #: 1.使用类名调用类方法
# t.bar2()     #: 2.也可以使用实例调用类方法
# Test.bar1()  #: 3.不可单独使用类名调用实例方法，
# Test.bar1(t) #: 4.类名调用实例方法，外部给类传入一个实例对象
# 应用场景： 直接使用类的名字创建一个实例的时候使用 ：User.create()
# Test.bar2()
Test.foo2()    #: 5.可以调用的类的属性， 不可调用实例属性





# @staticmethod ：静态方法，无传入参数时，无论是用类还是用实例都无法调用类内部的方法和属性，完全独立的方法
# Test.bar3()
# t.bar3()
# Test.bar1()
# Test.bar1(t)

# Test.foo3(t)
# t.foo3(t)










