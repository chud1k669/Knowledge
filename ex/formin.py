lst_num = list(map(float, input().split()))
m = 0
for i in range(len(lst_num)):
    if lst_num[i] < lst_num[i -1]:
        m = lst_num[i]
print(m)
