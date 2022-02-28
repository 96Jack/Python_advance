# -*- encoding: utf-8 -*-
'''
file       :class_muti_enherit.py
Description: Mixin :混入:开发思想;设计模式;专门用来给其他类继承使用,不会实例化出来。
Date       :2022/02/25 15:38:27
Author     :Xu Zhiwen
version    :python3.7.8
'''



from codecs import getreader


class StudentMixin(object):
    def __init__(self, *, age, name, number):
        self.age = age
        self.name = name
        self.number = number
    def test_s(self):
        print("this is StudentMixin")


class TeacherMixin(object):
    def __init__(self, *,grade) -> None:
        self.grade = grade
    def test_t(self):
        # 重载同时继承父类方法oij
        
        print("this is TeacherMixin")


class ProfessorMixin(object):
    def __init__(self,*, salary) -> None:
       self.salary = salary
    def test_p(self):
        print("this is ProfessorMixin")



# 单线多重继承（只有两层）：继承的每个类的功能独立，比较安全。拓展类的属性及功能
class School(StudentMixin, TeacherMixin, ProfessorMixin):
    # def __init__(self, *, age, name, number, grade, salary):
    #     super().__init__(age=age, name=name, grade=grade, number=number,salary=salary)
    def __init__(self, *, age, name, number, grade):
        StudentMixin.__init__(self, age=age, name=name, number=number)
        TeacherMixin.__init__(self, grade=grade)
    
    def test(self):
        print("This is school")
        





print(School.mro())
# p = School(age=40, name="Tom", number=100, grade=19 ,salary=10000000)
s = School(age=40, name="Tom", number=100, grade=18)
# Mixin设计模式，可以安全地使用继承类里面的属性及功能，Mixin类间无继承交叉。
s.test_p()
print(s.grade)
