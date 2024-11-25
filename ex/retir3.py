def nechetn(x):
    return x % 2 != 0

lst = list(map(int, input().split()))
lst = [x for x in lst if nechetn(x)]
print(*lst)
