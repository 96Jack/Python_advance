from cgi import test
import random

from numpy import sort 

def insert_sort(sort_list):
    for i in range(1, len(sort_list)):
        for j in range(i, 0, -1):
            if sort_list[j - 1] > sort_list[j]:
                sort_list[j-1], sort_list[j] = sort_list[j], sort_list[j-1]

test_list = [random.randint(0, 100) for _ in range(6)]
print(test_list)
insert_sort(test_list)
print(test_list)
