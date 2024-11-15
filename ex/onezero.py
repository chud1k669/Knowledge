p = [0] * 10
i = 1
while i <= 5:
    num = int(input())
    if p[num]==1:
        continue
    else:
        p[num]=1
        i+=1
print(*p)