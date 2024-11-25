lst1 = set(list(map(int, input().split())))
lst2 = set(list(map(int, input().split())))
s = lst1 - lst2
print(*sorted(s))