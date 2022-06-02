
n = int(input("请输入数据: "))
def fb(n):
    if n <=2:
        return 1
    else:
        return(fb(n-2) + fb(n-1))
print(fb(n), end="")



