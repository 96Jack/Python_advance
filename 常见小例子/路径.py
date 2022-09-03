# -*- encoding: utf-8 -*-
'''
file       :路径.py
Description:
Date       :2022/09/03 10:48:04
Author     :Xu Zhiwen
version    :python3.7.8
'''

import os
from  pathlib import Path

pwdpath = os.path.abspath(__file__)
dirname = os.path.dirname(pwdpath)
print(pwdpath)
print(dirname)

print("*"*30, "等同于")

pwpath = Path(__file__).resolve()
diname = pwpath.parent
print(pwpath)
print(diname)
