# -*- encoding: utf-8 -*-
'''
file       :迭代器_1.py
Description: 实现__iter__()  和 __next__()方法的对象就是一个迭代器
Date       :2022/10/13 09:38:12
Author     :Xu Zhiwen
version    :python3.7.8
'''

from ast import main


class  Mylist:
    """自定义一个可迭代对象"""
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)
    
    def __iter__(self):
        myIterator = MyIterator(self)
        return myIterator

class MyIterator:
    """自定义可供上面使用的迭代器"""
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item 
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
        

if  "__name__" == "__main__":
    # 可迭代对象
    mylist = Mylist()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    for i in mylist:
        print(i)
    from collections import Iterator, Iterable
    isinstance(mylist, Iterable)

    # 迭代器
    myiterator = MyIterator(mylist)
    isinstance(myiterator, Iterable)
    isinstance(myiterator, Iterator)
    next(myiterator)
    next(myiterator)
    next(myiterator)
    next(myiterator)
    next(myiterator)

    