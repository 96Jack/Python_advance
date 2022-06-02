# 函数内部调用全局变量， 函数内部含有与全局变量同名的变量
sam = "狮子"
def func():
    sam = "大象"
    print("函数内部： %s" %sam)
    print("函数外部： %s" % globals()["sam"])

func()