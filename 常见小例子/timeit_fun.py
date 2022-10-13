# -*- encoding: utf-8 -*-
'''
file       :2.py
Description:
Date       :2022/05/28 12:25:01
Author     :Xu Zhiwen
version    :python3.7.8
'''

import random
from timeit import timeit


# 插入排序
def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        for j in range(i, 0, -1):
            if sort_list[j - 1] > sort_list[j]:
                sort_list[j -1], sort_list[j] = sort_list[j], sort_list[j-1]

t_l = [random.randint(0, 100) for _ in range(6)]

# if __name__ == "__main__":
insertion_sort(t_l)
print(t_l)

# stmt = fun(*args) ; setup = 'import ku; *args', num = run times
# "%s" %(t, ) : %s% : 后面输出用元组包含
print("插入排序6个数字运行10000次的平均时间是: %s 秒" %(timeit(stmt='insertion_sort(t_l)', setup='import random;t_l=[random.randint(0, 100) for _ in range(6)];from __main__ import insertion_sort', number=10000)))

