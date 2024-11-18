c = list(map(str, input().split()))
i = 0
while i < len(c):
    if len(c[i]) > 5:
        i+=1
    else:
        print("НЕТ")
        break
    if i==len(c):
        print('ДА')
