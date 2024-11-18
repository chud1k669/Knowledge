lst_num = list(map(int, input().split()))
summ = 0
for i in lst_num:
    if i % 2 == 1:
        summ += i
print(summ)
