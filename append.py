lst = list(map(str, input().split()))
lst.append(lst[0]!=lst[-1])
print(*lst)