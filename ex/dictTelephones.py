numbers = input().split()

d={}
for number in numbers:
    code = number[:-10]
    if code in d:
        d[code].append(number)
    else:
        d[code]=[]
        d[code].append(number)
print(*sorted(d.items()))