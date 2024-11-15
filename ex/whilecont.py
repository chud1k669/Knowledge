num =  int(input())
summ = num if num >0 and num !=0 else 1
while num != 0:
    num = int(input())
    if num  > 0:
        summ*=num
    else:
        continue
else:
    print(summ)