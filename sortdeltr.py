lst = list(input().split())
a = sorted(lst)
a.remove(a[0])
print(*a)