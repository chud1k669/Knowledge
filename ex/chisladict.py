import math

d = {}
n = int(input())
while n != 0:
    if n in d:
        print("значение из кэша:", round(d[n], 2))
    elif n not in d and n != 0:
        d[n] = math.sqrt(n)
        print(round(d[n], 2))
    if n == 0:
        break
    n = int(input())
