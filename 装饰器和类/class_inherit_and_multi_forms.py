# -*- encoding: utf-8 -*-
'''
file       :class_inherit.py
Description:
继承: 子类拥有父类的全部功能
多态: 子类表现出不同于父类的形态:(重载父类的方法) 
Date       :2022/02/25 09:43:16
Author     :Xu Zhiwen
version    :python3.7.8
'''


class Student:
    def __init__(self, *, age, name, number):
        self.age = age
        self.name = name
        self.number = number
    def test(self):
        print("this is Student test")


class BoyStudent(Student):
    # 重载父类的方法
    def test(self):
        # 重载同时继承父类方法
        super().test()
        print("this is BoyStudent test")


class GirlStudent(Student):
    def __init__(self, *, age, name, number, grade_800):
        super().__init__(age=age, name=name, number=number)
        self.grade_800 = grade_800

    def show(self):
        print("girlage : {}".format(self.age))
        print("girlname : {}".format(self.name))
        print("girlnumber : {}".format(self.number))
        print("girlgrade_800 : {}".format(self.grade_800))

    def test(self):
        super().test()
        print("this is GirlStudent test")

# 多重继承：按照cls.mro()内的继承关系继承：菱形继承:非Mixin模式继承关系混乱
class Professor(BoyStudent, GirlStudent):
    def __init__(self, *, age, name, number, grade_800, salary):
        super().__init__(age=age, name=name, grade_800=grade_800, number=number)
        self.salary = salary
        




# boy = BoyStudent(age=10, name="Jack", number=1)
# print(boy.name)
# boy.test()

# girl = GirlStudent(age=10, name="rose", number=2, grade_800="A")
# girl.show()
# print(isinstance(d, A))
# print(isinstance(d, B))
# print(isinstance(d, C))

print(Professor.mro())
r""" 
此处的r为转译
注意:
super().func(): 
    1.单线继承(只有两层)的时候是查找上一个父类。
    2.对于多层的继承按照mro()内的顺序继承;c3算法,菱形继承;d多条线。
                st
          /            \
       boyst             girlst
          \            /
             professor

# [<class '__main__.Professor'>, <class '__main__.BoyStudent'>, <class '__main__.GirlStudent'>, <class '__main__.Student'>, <class 'object'>]
 """
p = Professor(age=40, name="Tom", number = None, grade_800=None, salary=10000000)
p.test()

""" 
this is Student test
this is GirlStudent test
this is BoyStudent test 
"""