
while True:
    num = int(input("请输入数据"))
    def fb(num):
        if num <=2:
            return 1
        else:
            return( fb(num-2) + fb(num-1))
    print(fb(num))

