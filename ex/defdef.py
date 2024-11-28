def counter_add(a):
    x = 5
    def func_count():
        return a+x
    return func_count()


print(counter_add(int(input())))
