import time
def time_1(count):
    def wrap_1(func):
        def wrap_2(*args, **kwargs):
            t1 = time.time()
            resu = func(*args)
            t2 = time.time()
            print("Cycle: {}\nTotal Time:{}".format(count, (t2 - t1)))
            return resu
        return wrap_2
    return wrap_1

@time_1(1000000)
def foo(x, y):
    return x ** y

print(foo(2, 3))