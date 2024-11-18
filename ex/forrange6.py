lst_name = list(map(str, input().split()))
length = []

for i in lst_name:
    length.append(len(i))

print(*length)