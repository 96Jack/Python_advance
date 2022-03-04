# -*- encoding: utf-8 -*-
'''
file       :async_p.py
Description:
Date       :2022/03/04 16:34:32
Author     :Xu Zhiwen
version    :python3.7.8
'''
import random
import threading
import asyncio
from typing import AsyncIterable

def foo(n):
    x = 0
    for i in range(n):
        x += random.randint(1, 100)
    return x


async def bar(n, name):
    x = 0
    for i in range(n):
        x += random.randint(1, 100)
        print(name, x)
        await asyncio.sleep(1)
    return x

# 线程
# 线程会丢弃return的返回值（用全局变量保存）
t = threading.Thread(target=foo, args=(10, ))
t.start()
print(t.is_alive())

# 计算任务
# A   ——>  -->   ——>  -->   ——>  -->   ——>  --> 
# 定时任务
#   sleep()
# B  --->  ——>  --->  ——>  --->  ——>  --->  ——> 

# 协程
# A ---->---->----->------>
        # set event()
        # yield 让出解释器的控制权      产生一个信号（loop调度）
# B     ------>                       |----->

# 时间片的切换：由系统控制，无法改变，当cpu切换到B时,线程并未运行,cpu等待,浪费资源



# 协程：让出解释器的控制权(cpu),让其他事件先运行，提升cpu的使用效率
t1 = bar(10, 't1')
t2 = bar(15, 't2')
tasks = [asyncio.ensure_future(t1), asyncio.ensure_future(t2)]
# loop协程的调度器
loop = asyncio.get_event_loop()
print("++++++++++\n", loop.run_until_complete(asyncio.wait(tasks)))

