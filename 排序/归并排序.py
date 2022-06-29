# -*- encoding: utf-8 -*-
'''
file       :归并排序.py
Description: 
分治的思想： 先两两拆分直至拆分成单个元素，然后依次合并两个有序数组
优点： 最好和最坏的算法复杂度都是Nlog(N)
缺点： 占用更多的存储空间用来归并
Date       :2022/05/10 23:46:34
Author     :Xu Zhiwen
version    :python3.7.8
'''


import random
 
# 递归分开 ： 二分分开
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    num = len(nums) // 2
    # 将左半个列表依次拆分成单个元素
    left = merge_sort(nums[:num])
    # 将有右半个列表依次拆分成单个元素
    right = merge_sort(nums[num:])
    return merge(left, right)

 
# 合并
def merge(left, right):
    """
    合并 将两个有序数组left 和 right 合并成一个大的有序数组
    """
    l, r = 0, 0  # left与right的下标指针 从0开始往右移动
    result = []  # 依次比较 小的放result；中间变量
    print("result: %s" % result)
    while l < len(left) and r < len(right):  # 任何一个数组遍历完结束循环
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 以下2步骤是因为可能有多余元素 直接复制到result后面

    result += left[l:]
    print("result_llll: %s" % result)
    result += right[r:]
    print("result_rrrr: %s "% result)
    return result


print(merge_sort([random.randint(0, 100) for _ in range(10)]))

