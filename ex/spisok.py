lst = list(map(int, input().split()))
bol = lst[-1] % 2 == 1
lst.remove(lst[-1])
lst.append(bol)

print(*lst)
