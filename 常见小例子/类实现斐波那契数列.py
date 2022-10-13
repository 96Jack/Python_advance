# -*- encoding: utf-8 -*-
'''
file       :类实现斐波那契数列.py
Description: 

数列中第一个数为0,第二个数为1,其后的每一个数都可由前两个数相加得到:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Date       :2022/10/13 10:14:56
Author     :Xu Zhiwen
version    :python3.7.8
'''


# n = int(input("请输入数据"))
# def fb(n):
#     if n <= 2:
#         return 1
#     return (fb(n-2) + fb(n-1))

# print(fb(n))

class FibIterator:
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num, end=" ")