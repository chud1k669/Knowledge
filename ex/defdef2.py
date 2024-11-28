def counter_add(n):
    x = 2
    def in_def():
        return n + x
    return in_def()

n = int(input())
print(counter_add(n))
