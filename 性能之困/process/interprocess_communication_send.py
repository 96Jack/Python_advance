# -*- encoding: utf-8 -*-
'''
file       :interprocess_communication.py
Description:  通过网络进行,进程间通信
Date       :2022/03/04 15:03:20
Author     :Xu Zhiwen
version    :python3.7.8
'''

from pickle import dumps

# p1
import socket 
cli = socket.socket()
# 元组的形式传入连接数据
cli.connect(('127.0.0.1', 8000))
# 只能发送二进制的东西
cli.send(b'hello world')

# 用dumps反序列化数据
c = {1:111, 2:222, 3:333}
dd = dumps(c)
cli.send(dd)