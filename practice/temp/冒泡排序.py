import random 

l = [random.randint(1, 100) for _ in range(6)]
print(l)

def merge_sort(l):
    if len(l) <=1 :
        return l
    lt = len(l) // 2
    left = merge_sort(l[:lt])
    right = merge_sort(l[lt:])
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result 

print(merge_sort(l))
 