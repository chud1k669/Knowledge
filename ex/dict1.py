a = list(map(str, input().split()))
for i in range(len(a)):
    a[i] = list(map(str, a[i].split('=')))
    for j in range(len(a[i])):
        try:
            a[i][j] = int(a[i][j])
        except:
            continue

d = dict(a)
print(*sorted(d.items()))