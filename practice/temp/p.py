from lib2to3.pytree import type_repr


layer = int(input("请输入菱形的层数"))
while layer & 1 == 0:
    layer = int(input("请输入奇数层"))

print(type(layer))

for i in range(1, layer//2 +2):
    print(' '*(layer - i -2), end='')
    print("*"*(2*i -1))

for i in range(layer//2, 0, -1):
    print(' '*(layer - i - 2), end='')
    print("*"*(2*i - 1))
