# 修改全局变量
x = 5
def func():
    global x
    x = x + 1
    print(x)
func()
print("改变后：", x)
