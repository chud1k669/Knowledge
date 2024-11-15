num = int(input())
i = 0
lst= [1,1]
if num > 2:
    while len(lst) < num:
        lst.append(lst[i]+lst[i+1])
        i+=1
    print(*lst)
else:
    print("1 "*num)