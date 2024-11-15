c = list(map(str, input().split()))
print(c)
i = 0
while c:
    i+=1
    if c[i] >= 5:
        print("ДА")
    else:
        print("НЕТ")
