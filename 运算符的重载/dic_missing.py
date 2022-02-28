# -*- encoding: utf-8 -*-
'''
file       :dic_missing.py
Description: 定义添加原字典不存在key时对应的value形式
Date       :2022/02/28 20:51:11
Author     :Xu Zhiwen
version    :python3.7.8
'''


class Dict(dict):
    # 字典的预留接口，可以定义，当用字典的key不存在时，key对应value的添加形式
    def __missing__(self, key):
        # self[key] = []
        self[key] = None
        return self[key]

d = Dict({1:2, 2:3, 3:4, 4:5})

# d[5].append(999)
# d[5] = []
print(d)
# {1: 2, 2: 3, 3: 4, 4: 5, 5: [999]}
        
