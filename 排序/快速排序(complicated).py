# -*- encoding: utf-8 -*-
'''
file       :快速排序(complicated).py
Description: [ 将数列切分成两半：将小的数放在左半边, 大的数放在右半边,  -> 再将切成两半的数列再分别切成两半排序 ]: 以此类推
Date       :2022/05/09 19:05:53
Author     :Xu Zhiwen
version    :python3.7.8
'''
import random

lst = [random.randint(0, 100) for _ in range(6)]
def quick_sort(lst, start=0, end=len(lst)-1):
    if start >= end:
        return
    # 定义指针
    pre = start
    next = end
    # 定义基准元素
    mid = lst[start]
    # 若pre指针和next指针重合时跳出循环，并把mid值赋给pre或next
    while pre < next:
        # 左小 ： 右边的数据大于等于基准数的不用管，小于基准数的左边放
        while lst[next] >= mid and pre < next:
            next -= 1
            print("next: %s" % next)
        lst[pre] = lst[next]
        print("lst[pre] : lst[%s] \n ls[next] : lst[%s]" % (pre, next) )
        # 右大 ： 左边的数据，小于等于基准数的不用管，大于基准数的右边放
        while lst[pre] <= mid and pre < next:
            pre += 1
            print("pre: %s" % pre)
        lst[next] = lst[pre]
        print("lst[next] : lst[%s] \n ls[pre] : lst[%s]" % (next, pre))
    lst[pre] = mid 
    print("lst[pre] : %s"% mid)
    # 递归调用对基准值左边的数据进行排序
    quick_sort(lst, start, pre-1)
    print("left: ======================lst:%s"% lst)
    # 递归调用对基准值得右边的数据进行排序
    quick_sort(lst, pre+1, end)
    print("right:======================= lst:%s"% lst) 
quick_sort(lst)
print(lst)

