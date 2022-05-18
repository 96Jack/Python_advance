# -*- encoding: utf-8 -*-
'''
file       :插入排序.py
Description: 从第二个元素开始将右边未排序的元素向左边插入排序，依次向后遍历。
[5,   4, 6, 3, 1, 2] 
[4, 5,   6, 3, 1, 2]
[4, 5, 6,   3, 1, 2]
[3, 4, 5, 6,   1, 2]
[1, 3, 4, 5, 6,   2]
[1, 2, 3, 4, 5, 6]

Date       :2022/05/10 21:57:12
Author     :Xu Zhiwen
version    :python3.7.8
'''
import random 

def insertion_sort(sort_list):
    # 注意是从第二个位置开始向前插入元素
    for i in range(1, len(sort_list)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            print("===================i :%s"% i)
            print("j :%s"% j)
            if sort_list[j - 1] > sort_list[j]:
                sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
            print("lst : %s"% test_llst)


test_llst = [random.randint(0, 100) for _ in range(6)]
print(test_llst)
insertion_sort(test_llst)
print(test_llst)