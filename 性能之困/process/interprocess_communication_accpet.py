# -*- encoding: utf-8 -*-
'''
file       :test.py
Description:  send(相当于write), recv(相当于read), accept : 都是阻塞
Date       :2022/03/04 15:04:11
Author     :Xu Zhiwen
version    :python3.7.8
'''
# loads接收传入序列化的数据
from pickle import  loads

import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8000))
sock.listen(1024)
# accept接收的是一个包含socket和addr的元组
cli = sock.accpet()
cli_socket, cli_addr = cli
# recv接收客户端发送的信息
dd = cli_socket.recv(1000)
data = loads(dd)
print(data)