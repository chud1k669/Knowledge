import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for i in range(len(lst_in)):
    lst_in[i] = list(map(str, lst_in[i].split('=')))
    for j in range(len(lst_in[i])):
        try:
            lst_in[i][j] = int(lst_in[i][j])
        except:
            continue

d = {}
#d[lst_in[i][0]] = lst_in[i][1]
for i in range(len(lst_in)):
    d[lst_in[i][0]] = lst_in[i][1]
print(*sorted(d.items()))