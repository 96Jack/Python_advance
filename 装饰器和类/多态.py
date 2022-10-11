# from this import d


# -*- encoding: utf-8 -*-
'''
file       :多态.py
Description:
    重写父类方法
Date       :2022/10/10 16:17:13
Author     :Xu Zhiwen
version    :python3.7.8
'''

class Plolice:
    def work_with_dog(self, dog):
        dog.work()

class Dog_father:
    def work(self):
        print("狗爸爸")

class Drug_dog(Dog_father):
    def work(self):  # 重写父类方法
        print("缉毒犬")

class Blind_dog(Dog_father):
    def work(self):
        super().work() # 拓展父类方法
        print("导盲犬")

dog_s1 = Drug_dog()
dog_s2 = Blind_dog()

P=Plolice()
"""
子类犬继承父类
"""
P.work_with_dog(dog_s1)
P.work_with_dog(dog_s2)

print(Drug_dog.__mro__) # 用__mro__属性查看类方法的调用顺序