# -*- encoding: gbk -*-
'''
file       :timedelta_datetime.py
Description:
Date       :2022/08/30 11:17:25
Author     :Xu Zhiwen
version    :python3.7.8
'''



import datetime


current_time = datetime.datetime.now()
time_delta = datetime.timedelta(days=7)
time_future = (current_time + time_delta).strftime("%Y-%m-%d %H-%M-%S")
print("  现在时间:{}\n  时间间隔:{}\n  将来时间:{} ".format(current_time,time_delta,time_future))