# -*- encoding: utf-8 -*-
'''
file       :2.py
Description: quick_sort
Date       :2022/05/10 23:11:23
Author     :Xu Zhiwen
version    :python3.7.8
'''
lst = [6, 5, 4, 3, 2, 1]
def quick_sort(lst, start=0, end=len(lst)-1):
    if start > end:
        return 
    pre = start
    next = end
    mid = lst[start]

    while pre < next:
        # 左小
        while lst[next] > mid and pre < next:
            next -= 1
        lst[pre] = lst[next]

        #右大
        while lst[pre] < mid and pre < next:
            pre += 1
        lst[next] = lst[pre]
    lst[pre] = mid

    quick_sort(lst, start, pre-1) 
    quick_sort(lst, pre+1, end)

quick_sort(lst)
print(lst)



    

