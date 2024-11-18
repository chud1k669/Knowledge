names = list(map(str, input().split()))
i = 0

while i < len(names):
    if names[i][0].lower() == names[i][-1]:
        print('ДА')
        break
    i+=1
else:
    print('НЕТ')