lst_num = list(map(float, input().split()))
# values
# index
for v, i in enumerate(lst_num):
    if lst_num[v] < 0:
        lst_num[v] = -1.0
print(*lst_num)
